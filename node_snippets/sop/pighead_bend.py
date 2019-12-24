created_snippets_node_list = list()
# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj/geo1")

# Code for /obj/geo1/bend1
hou_node = hou_parent.createNode("bend", "bend1", run_init_scripts=False, load_contents=True, exact_type_name=True)

# -- mark for connection -- 
created_snippets_node_list.append(hou_node)
snippets_node_bend1 = hou_node

hou_node.move(hou.Vector2(-4.44682, 2.05515))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(True)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/bend1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/mask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("mask")
hou_parm.lock(False)
hou_parm.set("bend_attrib")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/maskmode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("maskmode")
hou_parm.lock(False)
hou_parm.set("maskoff")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/folder11 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("folder11")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/dodeform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("dodeform")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/limit_deformation parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("limit_deformation")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/bendfolder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("bendfolder")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/enablebend parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("enablebend")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/bendmode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("bendmode")
hou_parm.lock(False)
hou_parm.set("angle")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/bend parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("bend")
hou_parm.lock(False)
hou_parm.set(93.973302837754673)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/bendscalemode_angle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("bendscalemode_angle")
hou_parm.lock(False)
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/goaldir parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm_tuple = hou_node.parmTuple("goaldir")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/bend1/bendscalemode_dir parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("bendscalemode_dir")
hou_parm.lock(False)
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/bend_attrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("bend_attrib")
hou_parm.lock(False)
hou_parm.set("bend_attrib")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/upvectorcontrol parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("upvectorcontrol")
hou_parm.lock(False)
hou_parm.set("yaxis")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/up parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm_tuple = hou_node.parmTuple("up")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/bend1/upangle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("upangle")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/twistfolder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("twistfolder")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/enabletwist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("enabletwist")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/twist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("twist")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/twistscalemode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("twistscalemode")
hou_parm.lock(False)
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/twist_attrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("twist_attrib")
hou_parm.lock(False)
hou_parm.set("twist_attrib")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/lengthscalefolder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("lengthscalefolder")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/enablelengthscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("enablelengthscale")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/preservevolume parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("preservevolume")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/lengthscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("lengthscale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/lengthscalescalemode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("lengthscalescalemode")
hou_parm.lock(False)
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/lengthscale_attrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("lengthscale_attrib")
hou_parm.lock(False)
hou_parm.set("lengthscale_attrib")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taperfolder parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taperfolder")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/enabletaper parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("enabletaper")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/tapermode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("tapermode")
hou_parm.lock(False)
hou_parm.set("linear")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taper parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taper")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taperscalemode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taperscalemode")
hou_parm.lock(False)
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taper_attrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taper_attrib")
hou_parm.lock(False)
hou_parm.set("taper_attrib")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/squish parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("squish")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/squishscalemode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("squishscalemode")
hou_parm.lock(False)
hou_parm.set("none")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/squishpivot parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("squishpivot")
hou_parm.lock(False)
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/squish_attrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("squish_attrib")
hou_parm.lock(False)
hou_parm.set("squish_attrib")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/enableramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("enableramp")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taperprofile parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taperprofile")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/folder0 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/setcaptureregion parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("setcaptureregion")
hou_parm.lock(False)
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/origin parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm_tuple = hou_node.parmTuple("origin")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/bend1/dir parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm_tuple = hou_node.parmTuple("dir")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/bend1/length parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("length")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/enableoutattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("enableoutattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/outattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("outattrib")
hou_parm.lock(False)
hou_parm.set("capture")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/userest parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("userest")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/attribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("attribs")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/updateaffectednmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("updateaffectednmls")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/vlength parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("vlength")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/derivative_stepsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("derivative_stepsize")
hou_parm.lock(False)
hou_parm.set(0.01)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taperprofile1pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taperprofile1pos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taperprofile1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taperprofile1value")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/bend1/taperprofile1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bend1")
hou_parm = hou_node.parm("taperprofile1interp")
hou_parm.lock(False)
hou_parm.set("linear")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

# Code to establish connections for /obj/geo1/bend1
hou_node = hou_parent.node("bend1")
if hou_parent.node("testgeometry_pighead1") is not None:
    hou_node.setInput(0, hou_parent.node("testgeometry_pighead1"), 0)
hou_node.setUserData("___toolid___", "geometry_lineartaper")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("___toolcount___", "4")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj/geo1")

# Code for /obj/geo1/testgeometry_pighead1
hou_node = hou_parent.createNode("testgeometry_pighead", "testgeometry_pighead1", run_init_scripts=False, load_contents=True, exact_type_name=True)

# -- mark for connection -- 
created_snippets_node_list.append(hou_node)
snippets_node_testgeometry_pighead1 = hou_node

hou_node.move(hou.Vector2(-4.44682, 3.08167))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(True)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/testgeometry_pighead1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/testgeometry_pighead1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/testgeometry_pighead1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/testgeometry_pighead1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/testgeometry_pighead1/uniformscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/testgeometry_pighead1")
hou_parm = hou_node.parm("uniformscale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/testgeometry_pighead1/difficulty parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/testgeometry_pighead1")
hou_parm = hou_node.parm("difficulty")
hou_parm.lock(False)
hou_parm.set("medium")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/testgeometry_pighead1/addshader parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/testgeometry_pighead1")
hou_parm = hou_node.parm("addshader")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "sop_testgeometry_pighead")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("___toolcount___", "1")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# -- construct connection -- 
snippets_node_bend1.setInput(0, snippets_node_testgeometry_pighead1, 0)