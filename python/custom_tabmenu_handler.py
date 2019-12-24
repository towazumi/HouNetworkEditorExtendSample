#coding:utf-8 

import os
import hou
import nodegraphbase as base
from hutil.Qt import QtGui
from hutil.Qt import QtWidgets


# ノードをスクリプトとして保存するディレクトリ
NODE_SNIPPPETS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'node_snippets'))


class CustomTabMenuHandler(base.EventHandler):
    """ Shift+Tabで開くカスタムタブメニュー処理 """

    def __init__(self, uievent):
        """ 初期化処理 """
        base.EventHandler.__init__(self, uievent)

        # 現在どのカテゴリのオペレーターにいるか文字列で取得
        category = self.start_uievent.editor.pwd().childTypeCategory().name().lower()
        self.category = category

        # Menuの作成 
        self.menu = hou.qt.Menu()
        # アクションの登録 
        if category=='sop':
            self.addAction(self.menu, 'Create OUT Null', self.createOUTNullNode)

        self.addAction(self.menu, 'Add Script Block', self.addScriptBlock)
        
        self.menu.addSeparator()

        self.addAction(self.menu, 'Save Node As Python', self.saveNodesAsPython)

        node_snippets_menu = hou.qt.Menu()
        node_snippets_menu.setTitle('Load Node From Python ({0})'.format(category))
        for root, dirs, files in os.walk(os.path.join(NODE_SNIPPPETS_DIR, category)):
            for name in files:
                self.addAction(node_snippets_menu, name, lambda f=self.loadNodesFromPython,arg=(name):f(arg))
        self.menu.addMenu(node_snippets_menu)

        # Menuの表示
        cursor_pos = QtGui.QCursor.pos()
        self.menu.move(cursor_pos)
        self.menu.show()

    def handleEvent(self, uievent, pending_actions):
        """ イベント処理 """
        # イベント処理を継続する場合はイベントハンドラを返す 
        if self.menu.isVisible():
            return self
        # メニューが消えたらイベント処理を終了する 
        return None

    def addAction(self, menu, name, func):
        """ アクション登録用のヘルパー関数 """
        act = QtWidgets.QAction(name, menu)
        act.triggered.connect(func)
        menu.addAction(act)

    def createOUTNullNode(self):
        """ OUTという名前のNullノードを追加する """
        # NetworkEditorの取得
        editor = self.start_uievent.editor
        # Nullノードの作成
        node = editor.pwd().createNode('null', 'OUT')
        # 黒色を割り当てる
        node.setColor(hou.Color((0,0,0)))
        # マウス位置にノードを移動
        mousepos = editor.posFromScreen(self.start_uievent.mousepos)
        node.setPosition(mousepos)

    def addScriptBlock(self):
        """ ノードにスクリプトのテキストブロックと実行ボタンを追加する """
        
        script_block_prefix = 'scriptblock_'
        script_folder_label = 'Scripts'

        for node in hou.selectedNodes():
            group = node.parmTemplateGroup()

            # find 'Scripts' folder 
            folder = group.findFolder(script_folder_label)

            if not folder:
                folder = hou.FolderParmTemplate( script_block_prefix + 'folder', script_folder_label) 
                group.addParmTemplate(folder)

            # add snipet 
            index = 0
            while group.find( script_block_prefix + 'snipet_' + str(index) ):
                index += 1

            snipet = hou.StringParmTemplate(script_block_prefix + 'snipet_' + str(index) , 'Python Script', 1)
            snipet.setTags( dict(editor='1',editorlang='python') )
            snipet.setDefaultValue( ("# node = kwargs['node']",) )  
            group.appendToFolder(script_folder_label, snipet)

            # add execute button 
            button = hou.ButtonParmTemplate(script_block_prefix + 'button_' + str(index), 'Exec')
            button.setScriptCallback( "exec(kwargs['node'].parm('{}').eval())".format(snipet.name()))
            button.setScriptCallbackLanguage(hou.scriptLanguage.Python)
            group.appendToFolder(script_folder_label, button)

            node.setParmTemplateGroup(group)

    def saveNodesAsPython(self):
        """ 選択しているノードをPythonとして保存 """

        nodes = hou.selectedNodes()

        if len(nodes)==0:
            return

        # 保存ディレクトリ 
        save_directory = os.path.join(NODE_SNIPPPETS_DIR, self.category).replace(os.sep, '/')
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # ファイルダイアログを表示 
        filepath = hou.ui.selectFile(
            save_directory, 
            'Save Nodes As Python Script',
            pattern='*.py')

        # ファイルパスが有効なら 
        if filepath is not None:
            lines = list()

            lines.append('created_snippets_node_list = list()')

            for node in nodes:
                code_lines = node.asCode(recurse=True).splitlines()

                insert_pos = -1
                for i, line in enumerate(code_lines):
                    if line.startswith('hou_node = hou_parent.createNode'):
                        insert_pos = i + 1
                        break

                if insert_pos>=0:
                    lines.extend(code_lines[0:insert_pos])
                else:
                    lines.extend(code_lines)

                lines.append('')
                lines.append('# -- mark for connection -- ')
                lines.append('created_snippets_node_list.append(hou_node)')
                lines.append('snippets_node_{} = hou_node'.format(node.name()))
                lines.append('')

                if insert_pos>=0:
                    lines.extend(code_lines[insert_pos:])

            # ノードを接続するコードを挿入
            if len(nodes)>1:
                lines.append('# -- construct connection -- ')

                for node in nodes:
                    for connection in node.inputConnections():
                        if connection is None:
                            continue
                        
                        inpuNode = connection.inputNode()
                        if inpuNode in nodes:
                            lines.append('snippets_node_{}.setInput({}, snippets_node_{}, {})'.format(node.name(), connection.inputIndex(), inpuNode.name(), connection.outputIndex()))
            
            # ファイルを保存
            with open(filepath, 'w') as f:
                f.write('\n'.join(lines))

    def loadNodesFromPython(self, filename):
        """ Pythonスクリプトからノードを復元 """
        hou_parent = self.start_uievent.editor.pwd()
        d=dict( hou=hou, hou_parent=hou_parent )
        execfile( os.path.join(NODE_SNIPPPETS_DIR, self.category, filename ), d, d)

        # Pythonスクリプトにはノードの位置も記録されているのでマウス位置付近にレイアウトする 
        editor = self.start_uievent.editor
        mousepos = editor.posFromScreen(self.start_uievent.mousepos)
        if 'created_snippets_node_list' in d:
            for node in d['created_snippets_node_list']:
                node.setPosition(mousepos)
            hou_parent.layoutChildren(d['created_snippets_node_list'])



    