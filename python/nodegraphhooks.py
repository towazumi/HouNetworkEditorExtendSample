#coding:utf-8 

from canvaseventtypes import *
from custom_tabmenu_handler import CustomTabMenuHandler

def createEventHandler(uievent, pending_actions):
    """ ネットワークエディタからのイベントをフックする """

    if isinstance(uievent, KeyboardEvent):
        if uievent.eventtype == 'keyhit' and uievent.key=='Shift+Tab':
            # カスタムタブメニュー用のイベントハンドラを返す 
            return CustomTabMenuHandler(uievent), True
    
    return None, False