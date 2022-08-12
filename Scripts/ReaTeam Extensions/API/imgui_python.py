# Generated for ReaImGui v0.7

from reaper_python import *

def ImGui_AcceptDragDropPayload(ctx, type, flagsInOptional = None):
  if not hasattr(ImGui_AcceptDragDropPayload, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayload')
    ImGui_AcceptDragDropPayload.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(type), rpr_packs(0), c_int(4096), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_AcceptDragDropPayload.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval, rpr_unpacks(args[2])

def ImGui_AcceptDragDropPayloadFiles(ctx, flagsInOptional = None):
  if not hasattr(ImGui_AcceptDragDropPayloadFiles, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayloadFiles')
    ImGui_AcceptDragDropPayloadFiles.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_AcceptDragDropPayloadFiles.func(args[0], byref(args[1]), byref(args[2]) if args[2] != None else None)
  return rval, int(args[1].value)

def ImGui_AcceptDragDropPayloadRGB(ctx, flagsInOptional = None):
  if not hasattr(ImGui_AcceptDragDropPayloadRGB, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayloadRGB')
    ImGui_AcceptDragDropPayloadRGB.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_AcceptDragDropPayloadRGB.func(args[0], byref(args[1]), byref(args[2]) if args[2] != None else None)
  return rval, int(args[1].value)

def ImGui_AcceptDragDropPayloadRGBA(ctx, flagsInOptional = None):
  if not hasattr(ImGui_AcceptDragDropPayloadRGBA, 'func'):
    proc = rpr_getfp('ImGui_AcceptDragDropPayloadRGBA')
    ImGui_AcceptDragDropPayloadRGBA.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(0), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_AcceptDragDropPayloadRGBA.func(args[0], byref(args[1]), byref(args[2]) if args[2] != None else None)
  return rval, int(args[1].value)

def ImGui_AlignTextToFramePadding(ctx):
  if not hasattr(ImGui_AlignTextToFramePadding, 'func'):
    proc = rpr_getfp('ImGui_AlignTextToFramePadding')
    ImGui_AlignTextToFramePadding.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_AlignTextToFramePadding.func(args[0])

def ImGui_ArrowButton(ctx, str_id, dir):
  if not hasattr(ImGui_ArrowButton, 'func'):
    proc = rpr_getfp('ImGui_ArrowButton')
    ImGui_ArrowButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_int(dir))
  rval = ImGui_ArrowButton.func(args[0], args[1], args[2])
  return rval

def ImGui_AttachFont(ctx, font):
  if not hasattr(ImGui_AttachFont, 'func'):
    proc = rpr_getfp('ImGui_AttachFont')
    ImGui_AttachFont.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packp('ImGui_Font*', font))
  ImGui_AttachFont.func(args[0], args[1])

def ImGui_Begin(ctx, name, p_openInOutOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_Begin, 'func'):
    proc = rpr_getfp('ImGui_Begin')
    ImGui_Begin.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(name), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_Begin.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value) if p_openInOutOptional != None else None

def ImGui_BeginChild(ctx, str_id, size_wInOptional = None, size_hInOptional = None, borderInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_BeginChild, 'func'):
    proc = rpr_getfp('ImGui_BeginChild')
    ImGui_BeginChild.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None, c_bool(borderInOptional) if borderInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginChild.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval

def ImGui_BeginChildFrame(ctx, str_id, size_w, size_h, flagsInOptional = None):
  if not hasattr(ImGui_BeginChildFrame, 'func'):
    proc = rpr_getfp('ImGui_BeginChildFrame')
    ImGui_BeginChildFrame.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_double(size_w), c_double(size_h), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginChildFrame.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval

def ImGui_BeginCombo(ctx, label, preview_value, flagsInOptional = None):
  if not hasattr(ImGui_BeginCombo, 'func'):
    proc = rpr_getfp('ImGui_BeginCombo')
    ImGui_BeginCombo.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packsc(preview_value), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginCombo.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

def ImGui_BeginDisabled(ctx, disabledInOptional = None):
  if not hasattr(ImGui_BeginDisabled, 'func'):
    proc = rpr_getfp('ImGui_BeginDisabled')
    ImGui_BeginDisabled.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(disabledInOptional) if disabledInOptional != None else None)
  ImGui_BeginDisabled.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_BeginDragDropSource(ctx, flagsInOptional = None):
  if not hasattr(ImGui_BeginDragDropSource, 'func'):
    proc = rpr_getfp('ImGui_BeginDragDropSource')
    ImGui_BeginDragDropSource.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginDragDropSource.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

def ImGui_BeginDragDropTarget(ctx):
  if not hasattr(ImGui_BeginDragDropTarget, 'func'):
    proc = rpr_getfp('ImGui_BeginDragDropTarget')
    ImGui_BeginDragDropTarget.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_BeginDragDropTarget.func(args[0])
  return rval

def ImGui_BeginGroup(ctx):
  if not hasattr(ImGui_BeginGroup, 'func'):
    proc = rpr_getfp('ImGui_BeginGroup')
    ImGui_BeginGroup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_BeginGroup.func(args[0])

def ImGui_BeginListBox(ctx, label, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(ImGui_BeginListBox, 'func'):
    proc = rpr_getfp('ImGui_BeginListBox')
    ImGui_BeginListBox.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = ImGui_BeginListBox.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval

def ImGui_BeginMenu(ctx, label, enabledInOptional = None):
  if not hasattr(ImGui_BeginMenu, 'func'):
    proc = rpr_getfp('ImGui_BeginMenu')
    ImGui_BeginMenu.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_bool(enabledInOptional) if enabledInOptional != None else None)
  rval = ImGui_BeginMenu.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_BeginMenuBar(ctx):
  if not hasattr(ImGui_BeginMenuBar, 'func'):
    proc = rpr_getfp('ImGui_BeginMenuBar')
    ImGui_BeginMenuBar.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_BeginMenuBar.func(args[0])
  return rval

def ImGui_BeginPopup(ctx, str_id, flagsInOptional = None):
  if not hasattr(ImGui_BeginPopup, 'func'):
    proc = rpr_getfp('ImGui_BeginPopup')
    ImGui_BeginPopup.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginPopup.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_BeginPopupContextItem(ctx, str_idInOptional = None, popup_flagsInOptional = None):
  if not hasattr(ImGui_BeginPopupContextItem, 'func'):
    proc = rpr_getfp('ImGui_BeginPopupContextItem')
    ImGui_BeginPopupContextItem.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_idInOptional) if str_idInOptional != None else None, c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  rval = ImGui_BeginPopupContextItem.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_BeginPopupContextWindow(ctx, str_idInOptional = None, popup_flagsInOptional = None):
  if not hasattr(ImGui_BeginPopupContextWindow, 'func'):
    proc = rpr_getfp('ImGui_BeginPopupContextWindow')
    ImGui_BeginPopupContextWindow.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_idInOptional) if str_idInOptional != None else None, c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  rval = ImGui_BeginPopupContextWindow.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_BeginPopupModal(ctx, name, p_openInOutOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_BeginPopupModal, 'func'):
    proc = rpr_getfp('ImGui_BeginPopupModal')
    ImGui_BeginPopupModal.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(name), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginPopupModal.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value) if p_openInOutOptional != None else None

def ImGui_BeginTabBar(ctx, str_id, flagsInOptional = None):
  if not hasattr(ImGui_BeginTabBar, 'func'):
    proc = rpr_getfp('ImGui_BeginTabBar')
    ImGui_BeginTabBar.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginTabBar.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_BeginTabItem(ctx, label, p_openInOutOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_BeginTabItem, 'func'):
    proc = rpr_getfp('ImGui_BeginTabItem')
    ImGui_BeginTabItem.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_BeginTabItem.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value) if p_openInOutOptional != None else None

def ImGui_BeginTable(ctx, str_id, column, flagsInOptional = None, outer_size_wInOptional = None, outer_size_hInOptional = None, inner_widthInOptional = None):
  if not hasattr(ImGui_BeginTable, 'func'):
    proc = rpr_getfp('ImGui_BeginTable')
    ImGui_BeginTable.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_int(column), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(outer_size_wInOptional) if outer_size_wInOptional != None else None, c_double(outer_size_hInOptional) if outer_size_hInOptional != None else None, c_double(inner_widthInOptional) if inner_widthInOptional != None else None)
  rval = ImGui_BeginTable.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)
  return rval

def ImGui_BeginTooltip(ctx):
  if not hasattr(ImGui_BeginTooltip, 'func'):
    proc = rpr_getfp('ImGui_BeginTooltip')
    ImGui_BeginTooltip.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_BeginTooltip.func(args[0])

def ImGui_Bullet(ctx):
  if not hasattr(ImGui_Bullet, 'func'):
    proc = rpr_getfp('ImGui_Bullet')
    ImGui_Bullet.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_Bullet.func(args[0])

def ImGui_BulletText(ctx, text):
  if not hasattr(ImGui_BulletText, 'func'):
    proc = rpr_getfp('ImGui_BulletText')
    ImGui_BulletText.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_BulletText.func(args[0], args[1])

def ImGui_Button(ctx, label, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(ImGui_Button, 'func'):
    proc = rpr_getfp('ImGui_Button')
    ImGui_Button.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = ImGui_Button.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)
  return rval

def ImGui_ButtonFlags_MouseButtonLeft():
  if not hasattr(ImGui_ButtonFlags_MouseButtonLeft, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_MouseButtonLeft')
    ImGui_ButtonFlags_MouseButtonLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ButtonFlags_MouseButtonLeft, 'cache'):
    ImGui_ButtonFlags_MouseButtonLeft.cache = ImGui_ButtonFlags_MouseButtonLeft.func()
  return ImGui_ButtonFlags_MouseButtonLeft.cache

def ImGui_ButtonFlags_MouseButtonMiddle():
  if not hasattr(ImGui_ButtonFlags_MouseButtonMiddle, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_MouseButtonMiddle')
    ImGui_ButtonFlags_MouseButtonMiddle.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ButtonFlags_MouseButtonMiddle, 'cache'):
    ImGui_ButtonFlags_MouseButtonMiddle.cache = ImGui_ButtonFlags_MouseButtonMiddle.func()
  return ImGui_ButtonFlags_MouseButtonMiddle.cache

def ImGui_ButtonFlags_MouseButtonRight():
  if not hasattr(ImGui_ButtonFlags_MouseButtonRight, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_MouseButtonRight')
    ImGui_ButtonFlags_MouseButtonRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ButtonFlags_MouseButtonRight, 'cache'):
    ImGui_ButtonFlags_MouseButtonRight.cache = ImGui_ButtonFlags_MouseButtonRight.func()
  return ImGui_ButtonFlags_MouseButtonRight.cache

def ImGui_ButtonFlags_None():
  if not hasattr(ImGui_ButtonFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ButtonFlags_None')
    ImGui_ButtonFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ButtonFlags_None, 'cache'):
    ImGui_ButtonFlags_None.cache = ImGui_ButtonFlags_None.func()
  return ImGui_ButtonFlags_None.cache

def ImGui_CalcItemWidth(ctx):
  if not hasattr(ImGui_CalcItemWidth, 'func'):
    proc = rpr_getfp('ImGui_CalcItemWidth')
    ImGui_CalcItemWidth.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_CalcItemWidth.func(args[0])
  return rval

def ImGui_CalcTextSize(ctx, text, hide_text_after_double_hashInOptional = None, wrap_widthInOptional = None):
  if not hasattr(ImGui_CalcTextSize, 'func'):
    proc = rpr_getfp('ImGui_CalcTextSize')
    ImGui_CalcTextSize.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text), c_double(0), c_double(0), c_bool(hide_text_after_double_hashInOptional) if hide_text_after_double_hashInOptional != None else None, c_double(wrap_widthInOptional) if wrap_widthInOptional != None else None)
  ImGui_CalcTextSize.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return float(args[2].value), float(args[3].value)

def ImGui_Checkbox(ctx, label, vInOut):
  if not hasattr(ImGui_Checkbox, 'func'):
    proc = rpr_getfp('ImGui_Checkbox')
    ImGui_Checkbox.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_bool(vInOut))
  rval = ImGui_Checkbox.func(args[0], args[1], byref(args[2]))
  return rval, int(args[2].value)

def ImGui_CheckboxFlags(ctx, label, flagsInOut, flags_value):
  if not hasattr(ImGui_CheckboxFlags, 'func'):
    proc = rpr_getfp('ImGui_CheckboxFlags')
    ImGui_CheckboxFlags.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(flagsInOut), c_int(flags_value))
  rval = ImGui_CheckboxFlags.func(args[0], args[1], byref(args[2]), args[3])
  return rval, int(args[2].value)

def ImGui_CloseCurrentPopup(ctx):
  if not hasattr(ImGui_CloseCurrentPopup, 'func'):
    proc = rpr_getfp('ImGui_CloseCurrentPopup')
    ImGui_CloseCurrentPopup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_CloseCurrentPopup.func(args[0])

def ImGui_Col_Border():
  if not hasattr(ImGui_Col_Border, 'func'):
    proc = rpr_getfp('ImGui_Col_Border')
    ImGui_Col_Border.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_Border, 'cache'):
    ImGui_Col_Border.cache = ImGui_Col_Border.func()
  return ImGui_Col_Border.cache

def ImGui_Col_BorderShadow():
  if not hasattr(ImGui_Col_BorderShadow, 'func'):
    proc = rpr_getfp('ImGui_Col_BorderShadow')
    ImGui_Col_BorderShadow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_BorderShadow, 'cache'):
    ImGui_Col_BorderShadow.cache = ImGui_Col_BorderShadow.func()
  return ImGui_Col_BorderShadow.cache

def ImGui_Col_Button():
  if not hasattr(ImGui_Col_Button, 'func'):
    proc = rpr_getfp('ImGui_Col_Button')
    ImGui_Col_Button.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_Button, 'cache'):
    ImGui_Col_Button.cache = ImGui_Col_Button.func()
  return ImGui_Col_Button.cache

def ImGui_Col_ButtonActive():
  if not hasattr(ImGui_Col_ButtonActive, 'func'):
    proc = rpr_getfp('ImGui_Col_ButtonActive')
    ImGui_Col_ButtonActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ButtonActive, 'cache'):
    ImGui_Col_ButtonActive.cache = ImGui_Col_ButtonActive.func()
  return ImGui_Col_ButtonActive.cache

def ImGui_Col_ButtonHovered():
  if not hasattr(ImGui_Col_ButtonHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_ButtonHovered')
    ImGui_Col_ButtonHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ButtonHovered, 'cache'):
    ImGui_Col_ButtonHovered.cache = ImGui_Col_ButtonHovered.func()
  return ImGui_Col_ButtonHovered.cache

def ImGui_Col_CheckMark():
  if not hasattr(ImGui_Col_CheckMark, 'func'):
    proc = rpr_getfp('ImGui_Col_CheckMark')
    ImGui_Col_CheckMark.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_CheckMark, 'cache'):
    ImGui_Col_CheckMark.cache = ImGui_Col_CheckMark.func()
  return ImGui_Col_CheckMark.cache

def ImGui_Col_ChildBg():
  if not hasattr(ImGui_Col_ChildBg, 'func'):
    proc = rpr_getfp('ImGui_Col_ChildBg')
    ImGui_Col_ChildBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ChildBg, 'cache'):
    ImGui_Col_ChildBg.cache = ImGui_Col_ChildBg.func()
  return ImGui_Col_ChildBg.cache

def ImGui_Col_DockingEmptyBg():
  if not hasattr(ImGui_Col_DockingEmptyBg, 'func'):
    proc = rpr_getfp('ImGui_Col_DockingEmptyBg')
    ImGui_Col_DockingEmptyBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_DockingEmptyBg, 'cache'):
    ImGui_Col_DockingEmptyBg.cache = ImGui_Col_DockingEmptyBg.func()
  return ImGui_Col_DockingEmptyBg.cache

def ImGui_Col_DockingPreview():
  if not hasattr(ImGui_Col_DockingPreview, 'func'):
    proc = rpr_getfp('ImGui_Col_DockingPreview')
    ImGui_Col_DockingPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_DockingPreview, 'cache'):
    ImGui_Col_DockingPreview.cache = ImGui_Col_DockingPreview.func()
  return ImGui_Col_DockingPreview.cache

def ImGui_Col_DragDropTarget():
  if not hasattr(ImGui_Col_DragDropTarget, 'func'):
    proc = rpr_getfp('ImGui_Col_DragDropTarget')
    ImGui_Col_DragDropTarget.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_DragDropTarget, 'cache'):
    ImGui_Col_DragDropTarget.cache = ImGui_Col_DragDropTarget.func()
  return ImGui_Col_DragDropTarget.cache

def ImGui_Col_FrameBg():
  if not hasattr(ImGui_Col_FrameBg, 'func'):
    proc = rpr_getfp('ImGui_Col_FrameBg')
    ImGui_Col_FrameBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_FrameBg, 'cache'):
    ImGui_Col_FrameBg.cache = ImGui_Col_FrameBg.func()
  return ImGui_Col_FrameBg.cache

def ImGui_Col_FrameBgActive():
  if not hasattr(ImGui_Col_FrameBgActive, 'func'):
    proc = rpr_getfp('ImGui_Col_FrameBgActive')
    ImGui_Col_FrameBgActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_FrameBgActive, 'cache'):
    ImGui_Col_FrameBgActive.cache = ImGui_Col_FrameBgActive.func()
  return ImGui_Col_FrameBgActive.cache

def ImGui_Col_FrameBgHovered():
  if not hasattr(ImGui_Col_FrameBgHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_FrameBgHovered')
    ImGui_Col_FrameBgHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_FrameBgHovered, 'cache'):
    ImGui_Col_FrameBgHovered.cache = ImGui_Col_FrameBgHovered.func()
  return ImGui_Col_FrameBgHovered.cache

def ImGui_Col_Header():
  if not hasattr(ImGui_Col_Header, 'func'):
    proc = rpr_getfp('ImGui_Col_Header')
    ImGui_Col_Header.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_Header, 'cache'):
    ImGui_Col_Header.cache = ImGui_Col_Header.func()
  return ImGui_Col_Header.cache

def ImGui_Col_HeaderActive():
  if not hasattr(ImGui_Col_HeaderActive, 'func'):
    proc = rpr_getfp('ImGui_Col_HeaderActive')
    ImGui_Col_HeaderActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_HeaderActive, 'cache'):
    ImGui_Col_HeaderActive.cache = ImGui_Col_HeaderActive.func()
  return ImGui_Col_HeaderActive.cache

def ImGui_Col_HeaderHovered():
  if not hasattr(ImGui_Col_HeaderHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_HeaderHovered')
    ImGui_Col_HeaderHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_HeaderHovered, 'cache'):
    ImGui_Col_HeaderHovered.cache = ImGui_Col_HeaderHovered.func()
  return ImGui_Col_HeaderHovered.cache

def ImGui_Col_MenuBarBg():
  if not hasattr(ImGui_Col_MenuBarBg, 'func'):
    proc = rpr_getfp('ImGui_Col_MenuBarBg')
    ImGui_Col_MenuBarBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_MenuBarBg, 'cache'):
    ImGui_Col_MenuBarBg.cache = ImGui_Col_MenuBarBg.func()
  return ImGui_Col_MenuBarBg.cache

def ImGui_Col_ModalWindowDimBg():
  if not hasattr(ImGui_Col_ModalWindowDimBg, 'func'):
    proc = rpr_getfp('ImGui_Col_ModalWindowDimBg')
    ImGui_Col_ModalWindowDimBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ModalWindowDimBg, 'cache'):
    ImGui_Col_ModalWindowDimBg.cache = ImGui_Col_ModalWindowDimBg.func()
  return ImGui_Col_ModalWindowDimBg.cache

def ImGui_Col_NavHighlight():
  if not hasattr(ImGui_Col_NavHighlight, 'func'):
    proc = rpr_getfp('ImGui_Col_NavHighlight')
    ImGui_Col_NavHighlight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_NavHighlight, 'cache'):
    ImGui_Col_NavHighlight.cache = ImGui_Col_NavHighlight.func()
  return ImGui_Col_NavHighlight.cache

def ImGui_Col_NavWindowingDimBg():
  if not hasattr(ImGui_Col_NavWindowingDimBg, 'func'):
    proc = rpr_getfp('ImGui_Col_NavWindowingDimBg')
    ImGui_Col_NavWindowingDimBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_NavWindowingDimBg, 'cache'):
    ImGui_Col_NavWindowingDimBg.cache = ImGui_Col_NavWindowingDimBg.func()
  return ImGui_Col_NavWindowingDimBg.cache

def ImGui_Col_NavWindowingHighlight():
  if not hasattr(ImGui_Col_NavWindowingHighlight, 'func'):
    proc = rpr_getfp('ImGui_Col_NavWindowingHighlight')
    ImGui_Col_NavWindowingHighlight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_NavWindowingHighlight, 'cache'):
    ImGui_Col_NavWindowingHighlight.cache = ImGui_Col_NavWindowingHighlight.func()
  return ImGui_Col_NavWindowingHighlight.cache

def ImGui_Col_PlotHistogram():
  if not hasattr(ImGui_Col_PlotHistogram, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotHistogram')
    ImGui_Col_PlotHistogram.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_PlotHistogram, 'cache'):
    ImGui_Col_PlotHistogram.cache = ImGui_Col_PlotHistogram.func()
  return ImGui_Col_PlotHistogram.cache

def ImGui_Col_PlotHistogramHovered():
  if not hasattr(ImGui_Col_PlotHistogramHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotHistogramHovered')
    ImGui_Col_PlotHistogramHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_PlotHistogramHovered, 'cache'):
    ImGui_Col_PlotHistogramHovered.cache = ImGui_Col_PlotHistogramHovered.func()
  return ImGui_Col_PlotHistogramHovered.cache

def ImGui_Col_PlotLines():
  if not hasattr(ImGui_Col_PlotLines, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotLines')
    ImGui_Col_PlotLines.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_PlotLines, 'cache'):
    ImGui_Col_PlotLines.cache = ImGui_Col_PlotLines.func()
  return ImGui_Col_PlotLines.cache

def ImGui_Col_PlotLinesHovered():
  if not hasattr(ImGui_Col_PlotLinesHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_PlotLinesHovered')
    ImGui_Col_PlotLinesHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_PlotLinesHovered, 'cache'):
    ImGui_Col_PlotLinesHovered.cache = ImGui_Col_PlotLinesHovered.func()
  return ImGui_Col_PlotLinesHovered.cache

def ImGui_Col_PopupBg():
  if not hasattr(ImGui_Col_PopupBg, 'func'):
    proc = rpr_getfp('ImGui_Col_PopupBg')
    ImGui_Col_PopupBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_PopupBg, 'cache'):
    ImGui_Col_PopupBg.cache = ImGui_Col_PopupBg.func()
  return ImGui_Col_PopupBg.cache

def ImGui_Col_ResizeGrip():
  if not hasattr(ImGui_Col_ResizeGrip, 'func'):
    proc = rpr_getfp('ImGui_Col_ResizeGrip')
    ImGui_Col_ResizeGrip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ResizeGrip, 'cache'):
    ImGui_Col_ResizeGrip.cache = ImGui_Col_ResizeGrip.func()
  return ImGui_Col_ResizeGrip.cache

def ImGui_Col_ResizeGripActive():
  if not hasattr(ImGui_Col_ResizeGripActive, 'func'):
    proc = rpr_getfp('ImGui_Col_ResizeGripActive')
    ImGui_Col_ResizeGripActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ResizeGripActive, 'cache'):
    ImGui_Col_ResizeGripActive.cache = ImGui_Col_ResizeGripActive.func()
  return ImGui_Col_ResizeGripActive.cache

def ImGui_Col_ResizeGripHovered():
  if not hasattr(ImGui_Col_ResizeGripHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_ResizeGripHovered')
    ImGui_Col_ResizeGripHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ResizeGripHovered, 'cache'):
    ImGui_Col_ResizeGripHovered.cache = ImGui_Col_ResizeGripHovered.func()
  return ImGui_Col_ResizeGripHovered.cache

def ImGui_Col_ScrollbarBg():
  if not hasattr(ImGui_Col_ScrollbarBg, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarBg')
    ImGui_Col_ScrollbarBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ScrollbarBg, 'cache'):
    ImGui_Col_ScrollbarBg.cache = ImGui_Col_ScrollbarBg.func()
  return ImGui_Col_ScrollbarBg.cache

def ImGui_Col_ScrollbarGrab():
  if not hasattr(ImGui_Col_ScrollbarGrab, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarGrab')
    ImGui_Col_ScrollbarGrab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ScrollbarGrab, 'cache'):
    ImGui_Col_ScrollbarGrab.cache = ImGui_Col_ScrollbarGrab.func()
  return ImGui_Col_ScrollbarGrab.cache

def ImGui_Col_ScrollbarGrabActive():
  if not hasattr(ImGui_Col_ScrollbarGrabActive, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarGrabActive')
    ImGui_Col_ScrollbarGrabActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ScrollbarGrabActive, 'cache'):
    ImGui_Col_ScrollbarGrabActive.cache = ImGui_Col_ScrollbarGrabActive.func()
  return ImGui_Col_ScrollbarGrabActive.cache

def ImGui_Col_ScrollbarGrabHovered():
  if not hasattr(ImGui_Col_ScrollbarGrabHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_ScrollbarGrabHovered')
    ImGui_Col_ScrollbarGrabHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_ScrollbarGrabHovered, 'cache'):
    ImGui_Col_ScrollbarGrabHovered.cache = ImGui_Col_ScrollbarGrabHovered.func()
  return ImGui_Col_ScrollbarGrabHovered.cache

def ImGui_Col_Separator():
  if not hasattr(ImGui_Col_Separator, 'func'):
    proc = rpr_getfp('ImGui_Col_Separator')
    ImGui_Col_Separator.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_Separator, 'cache'):
    ImGui_Col_Separator.cache = ImGui_Col_Separator.func()
  return ImGui_Col_Separator.cache

def ImGui_Col_SeparatorActive():
  if not hasattr(ImGui_Col_SeparatorActive, 'func'):
    proc = rpr_getfp('ImGui_Col_SeparatorActive')
    ImGui_Col_SeparatorActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_SeparatorActive, 'cache'):
    ImGui_Col_SeparatorActive.cache = ImGui_Col_SeparatorActive.func()
  return ImGui_Col_SeparatorActive.cache

def ImGui_Col_SeparatorHovered():
  if not hasattr(ImGui_Col_SeparatorHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_SeparatorHovered')
    ImGui_Col_SeparatorHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_SeparatorHovered, 'cache'):
    ImGui_Col_SeparatorHovered.cache = ImGui_Col_SeparatorHovered.func()
  return ImGui_Col_SeparatorHovered.cache

def ImGui_Col_SliderGrab():
  if not hasattr(ImGui_Col_SliderGrab, 'func'):
    proc = rpr_getfp('ImGui_Col_SliderGrab')
    ImGui_Col_SliderGrab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_SliderGrab, 'cache'):
    ImGui_Col_SliderGrab.cache = ImGui_Col_SliderGrab.func()
  return ImGui_Col_SliderGrab.cache

def ImGui_Col_SliderGrabActive():
  if not hasattr(ImGui_Col_SliderGrabActive, 'func'):
    proc = rpr_getfp('ImGui_Col_SliderGrabActive')
    ImGui_Col_SliderGrabActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_SliderGrabActive, 'cache'):
    ImGui_Col_SliderGrabActive.cache = ImGui_Col_SliderGrabActive.func()
  return ImGui_Col_SliderGrabActive.cache

def ImGui_Col_Tab():
  if not hasattr(ImGui_Col_Tab, 'func'):
    proc = rpr_getfp('ImGui_Col_Tab')
    ImGui_Col_Tab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_Tab, 'cache'):
    ImGui_Col_Tab.cache = ImGui_Col_Tab.func()
  return ImGui_Col_Tab.cache

def ImGui_Col_TabActive():
  if not hasattr(ImGui_Col_TabActive, 'func'):
    proc = rpr_getfp('ImGui_Col_TabActive')
    ImGui_Col_TabActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TabActive, 'cache'):
    ImGui_Col_TabActive.cache = ImGui_Col_TabActive.func()
  return ImGui_Col_TabActive.cache

def ImGui_Col_TabHovered():
  if not hasattr(ImGui_Col_TabHovered, 'func'):
    proc = rpr_getfp('ImGui_Col_TabHovered')
    ImGui_Col_TabHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TabHovered, 'cache'):
    ImGui_Col_TabHovered.cache = ImGui_Col_TabHovered.func()
  return ImGui_Col_TabHovered.cache

def ImGui_Col_TabUnfocused():
  if not hasattr(ImGui_Col_TabUnfocused, 'func'):
    proc = rpr_getfp('ImGui_Col_TabUnfocused')
    ImGui_Col_TabUnfocused.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TabUnfocused, 'cache'):
    ImGui_Col_TabUnfocused.cache = ImGui_Col_TabUnfocused.func()
  return ImGui_Col_TabUnfocused.cache

def ImGui_Col_TabUnfocusedActive():
  if not hasattr(ImGui_Col_TabUnfocusedActive, 'func'):
    proc = rpr_getfp('ImGui_Col_TabUnfocusedActive')
    ImGui_Col_TabUnfocusedActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TabUnfocusedActive, 'cache'):
    ImGui_Col_TabUnfocusedActive.cache = ImGui_Col_TabUnfocusedActive.func()
  return ImGui_Col_TabUnfocusedActive.cache

def ImGui_Col_TableBorderLight():
  if not hasattr(ImGui_Col_TableBorderLight, 'func'):
    proc = rpr_getfp('ImGui_Col_TableBorderLight')
    ImGui_Col_TableBorderLight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TableBorderLight, 'cache'):
    ImGui_Col_TableBorderLight.cache = ImGui_Col_TableBorderLight.func()
  return ImGui_Col_TableBorderLight.cache

def ImGui_Col_TableBorderStrong():
  if not hasattr(ImGui_Col_TableBorderStrong, 'func'):
    proc = rpr_getfp('ImGui_Col_TableBorderStrong')
    ImGui_Col_TableBorderStrong.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TableBorderStrong, 'cache'):
    ImGui_Col_TableBorderStrong.cache = ImGui_Col_TableBorderStrong.func()
  return ImGui_Col_TableBorderStrong.cache

def ImGui_Col_TableHeaderBg():
  if not hasattr(ImGui_Col_TableHeaderBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TableHeaderBg')
    ImGui_Col_TableHeaderBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TableHeaderBg, 'cache'):
    ImGui_Col_TableHeaderBg.cache = ImGui_Col_TableHeaderBg.func()
  return ImGui_Col_TableHeaderBg.cache

def ImGui_Col_TableRowBg():
  if not hasattr(ImGui_Col_TableRowBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TableRowBg')
    ImGui_Col_TableRowBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TableRowBg, 'cache'):
    ImGui_Col_TableRowBg.cache = ImGui_Col_TableRowBg.func()
  return ImGui_Col_TableRowBg.cache

def ImGui_Col_TableRowBgAlt():
  if not hasattr(ImGui_Col_TableRowBgAlt, 'func'):
    proc = rpr_getfp('ImGui_Col_TableRowBgAlt')
    ImGui_Col_TableRowBgAlt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TableRowBgAlt, 'cache'):
    ImGui_Col_TableRowBgAlt.cache = ImGui_Col_TableRowBgAlt.func()
  return ImGui_Col_TableRowBgAlt.cache

def ImGui_Col_Text():
  if not hasattr(ImGui_Col_Text, 'func'):
    proc = rpr_getfp('ImGui_Col_Text')
    ImGui_Col_Text.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_Text, 'cache'):
    ImGui_Col_Text.cache = ImGui_Col_Text.func()
  return ImGui_Col_Text.cache

def ImGui_Col_TextDisabled():
  if not hasattr(ImGui_Col_TextDisabled, 'func'):
    proc = rpr_getfp('ImGui_Col_TextDisabled')
    ImGui_Col_TextDisabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TextDisabled, 'cache'):
    ImGui_Col_TextDisabled.cache = ImGui_Col_TextDisabled.func()
  return ImGui_Col_TextDisabled.cache

def ImGui_Col_TextSelectedBg():
  if not hasattr(ImGui_Col_TextSelectedBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TextSelectedBg')
    ImGui_Col_TextSelectedBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TextSelectedBg, 'cache'):
    ImGui_Col_TextSelectedBg.cache = ImGui_Col_TextSelectedBg.func()
  return ImGui_Col_TextSelectedBg.cache

def ImGui_Col_TitleBg():
  if not hasattr(ImGui_Col_TitleBg, 'func'):
    proc = rpr_getfp('ImGui_Col_TitleBg')
    ImGui_Col_TitleBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TitleBg, 'cache'):
    ImGui_Col_TitleBg.cache = ImGui_Col_TitleBg.func()
  return ImGui_Col_TitleBg.cache

def ImGui_Col_TitleBgActive():
  if not hasattr(ImGui_Col_TitleBgActive, 'func'):
    proc = rpr_getfp('ImGui_Col_TitleBgActive')
    ImGui_Col_TitleBgActive.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TitleBgActive, 'cache'):
    ImGui_Col_TitleBgActive.cache = ImGui_Col_TitleBgActive.func()
  return ImGui_Col_TitleBgActive.cache

def ImGui_Col_TitleBgCollapsed():
  if not hasattr(ImGui_Col_TitleBgCollapsed, 'func'):
    proc = rpr_getfp('ImGui_Col_TitleBgCollapsed')
    ImGui_Col_TitleBgCollapsed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_TitleBgCollapsed, 'cache'):
    ImGui_Col_TitleBgCollapsed.cache = ImGui_Col_TitleBgCollapsed.func()
  return ImGui_Col_TitleBgCollapsed.cache

def ImGui_Col_WindowBg():
  if not hasattr(ImGui_Col_WindowBg, 'func'):
    proc = rpr_getfp('ImGui_Col_WindowBg')
    ImGui_Col_WindowBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Col_WindowBg, 'cache'):
    ImGui_Col_WindowBg.cache = ImGui_Col_WindowBg.func()
  return ImGui_Col_WindowBg.cache

def ImGui_CollapsingHeader(ctx, label, p_visibleInOut, flagsInOptional = None):
  if not hasattr(ImGui_CollapsingHeader, 'func'):
    proc = rpr_getfp('ImGui_CollapsingHeader')
    ImGui_CollapsingHeader.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_bool(p_visibleInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_CollapsingHeader.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

def ImGui_ColorButton(ctx, desc_id, col_rgba, flagsInOptional = None, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(ImGui_ColorButton, 'func'):
    proc = rpr_getfp('ImGui_ColorButton')
    ImGui_ColorButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(desc_id), c_int(col_rgba), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = ImGui_ColorButton.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval

def ImGui_ColorConvertDouble4ToU32(r, g, b, a):
  if not hasattr(ImGui_ColorConvertDouble4ToU32, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertDouble4ToU32')
    ImGui_ColorConvertDouble4ToU32.func = CFUNCTYPE(c_int, c_double, c_double, c_double, c_double)(proc)
  args = (c_double(r), c_double(g), c_double(b), c_double(a))
  rval = ImGui_ColorConvertDouble4ToU32.func(args[0], args[1], args[2], args[3])
  return rval

def ImGui_ColorConvertHSVtoRGB(h, s, v):
  if not hasattr(ImGui_ColorConvertHSVtoRGB, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertHSVtoRGB')
    ImGui_ColorConvertHSVtoRGB.func = CFUNCTYPE(None, c_double, c_double, c_double, c_void_p, c_void_p, c_void_p)(proc)
  args = (c_double(h), c_double(s), c_double(v), c_double(0), c_double(0), c_double(0))
  ImGui_ColorConvertHSVtoRGB.func(args[0], args[1], args[2], byref(args[3]), byref(args[4]), byref(args[5]))
  return float(args[3].value), float(args[4].value), float(args[5].value)

def ImGui_ColorConvertNative(rgb):
  if not hasattr(ImGui_ColorConvertNative, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertNative')
    ImGui_ColorConvertNative.func = CFUNCTYPE(c_int, c_int)(proc)
  args = (c_int(rgb),)
  rval = ImGui_ColorConvertNative.func(args[0])
  return rval

def ImGui_ColorConvertRGBtoHSV(r, g, b):
  if not hasattr(ImGui_ColorConvertRGBtoHSV, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertRGBtoHSV')
    ImGui_ColorConvertRGBtoHSV.func = CFUNCTYPE(None, c_double, c_double, c_double, c_void_p, c_void_p, c_void_p)(proc)
  args = (c_double(r), c_double(g), c_double(b), c_double(0), c_double(0), c_double(0))
  ImGui_ColorConvertRGBtoHSV.func(args[0], args[1], args[2], byref(args[3]), byref(args[4]), byref(args[5]))
  return float(args[3].value), float(args[4].value), float(args[5].value)

def ImGui_ColorConvertU32ToDouble4(rgba):
  if not hasattr(ImGui_ColorConvertU32ToDouble4, 'func'):
    proc = rpr_getfp('ImGui_ColorConvertU32ToDouble4')
    ImGui_ColorConvertU32ToDouble4.func = CFUNCTYPE(None, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (c_int(rgba), c_double(0), c_double(0), c_double(0), c_double(0))
  ImGui_ColorConvertU32ToDouble4.func(args[0], byref(args[1]), byref(args[2]), byref(args[3]), byref(args[4]))
  return float(args[1].value), float(args[2].value), float(args[3].value), float(args[4].value)

def ImGui_ColorEdit3(ctx, label, col_rgbInOut, flagsInOptional = None):
  if not hasattr(ImGui_ColorEdit3, 'func'):
    proc = rpr_getfp('ImGui_ColorEdit3')
    ImGui_ColorEdit3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(col_rgbInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_ColorEdit3.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

def ImGui_ColorEdit4(ctx, label, col_rgbaInOut, flagsInOptional = None):
  if not hasattr(ImGui_ColorEdit4, 'func'):
    proc = rpr_getfp('ImGui_ColorEdit4')
    ImGui_ColorEdit4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(col_rgbaInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_ColorEdit4.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

def ImGui_ColorEditFlags_AlphaBar():
  if not hasattr(ImGui_ColorEditFlags_AlphaBar, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_AlphaBar')
    ImGui_ColorEditFlags_AlphaBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_AlphaBar, 'cache'):
    ImGui_ColorEditFlags_AlphaBar.cache = ImGui_ColorEditFlags_AlphaBar.func()
  return ImGui_ColorEditFlags_AlphaBar.cache

def ImGui_ColorEditFlags_AlphaPreview():
  if not hasattr(ImGui_ColorEditFlags_AlphaPreview, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_AlphaPreview')
    ImGui_ColorEditFlags_AlphaPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_AlphaPreview, 'cache'):
    ImGui_ColorEditFlags_AlphaPreview.cache = ImGui_ColorEditFlags_AlphaPreview.func()
  return ImGui_ColorEditFlags_AlphaPreview.cache

def ImGui_ColorEditFlags_AlphaPreviewHalf():
  if not hasattr(ImGui_ColorEditFlags_AlphaPreviewHalf, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_AlphaPreviewHalf')
    ImGui_ColorEditFlags_AlphaPreviewHalf.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_AlphaPreviewHalf, 'cache'):
    ImGui_ColorEditFlags_AlphaPreviewHalf.cache = ImGui_ColorEditFlags_AlphaPreviewHalf.func()
  return ImGui_ColorEditFlags_AlphaPreviewHalf.cache

def ImGui_ColorEditFlags_DisplayHSV():
  if not hasattr(ImGui_ColorEditFlags_DisplayHSV, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_DisplayHSV')
    ImGui_ColorEditFlags_DisplayHSV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_DisplayHSV, 'cache'):
    ImGui_ColorEditFlags_DisplayHSV.cache = ImGui_ColorEditFlags_DisplayHSV.func()
  return ImGui_ColorEditFlags_DisplayHSV.cache

def ImGui_ColorEditFlags_DisplayHex():
  if not hasattr(ImGui_ColorEditFlags_DisplayHex, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_DisplayHex')
    ImGui_ColorEditFlags_DisplayHex.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_DisplayHex, 'cache'):
    ImGui_ColorEditFlags_DisplayHex.cache = ImGui_ColorEditFlags_DisplayHex.func()
  return ImGui_ColorEditFlags_DisplayHex.cache

def ImGui_ColorEditFlags_DisplayRGB():
  if not hasattr(ImGui_ColorEditFlags_DisplayRGB, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_DisplayRGB')
    ImGui_ColorEditFlags_DisplayRGB.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_DisplayRGB, 'cache'):
    ImGui_ColorEditFlags_DisplayRGB.cache = ImGui_ColorEditFlags_DisplayRGB.func()
  return ImGui_ColorEditFlags_DisplayRGB.cache

def ImGui_ColorEditFlags_Float():
  if not hasattr(ImGui_ColorEditFlags_Float, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_Float')
    ImGui_ColorEditFlags_Float.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_Float, 'cache'):
    ImGui_ColorEditFlags_Float.cache = ImGui_ColorEditFlags_Float.func()
  return ImGui_ColorEditFlags_Float.cache

def ImGui_ColorEditFlags_InputHSV():
  if not hasattr(ImGui_ColorEditFlags_InputHSV, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_InputHSV')
    ImGui_ColorEditFlags_InputHSV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_InputHSV, 'cache'):
    ImGui_ColorEditFlags_InputHSV.cache = ImGui_ColorEditFlags_InputHSV.func()
  return ImGui_ColorEditFlags_InputHSV.cache

def ImGui_ColorEditFlags_InputRGB():
  if not hasattr(ImGui_ColorEditFlags_InputRGB, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_InputRGB')
    ImGui_ColorEditFlags_InputRGB.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_InputRGB, 'cache'):
    ImGui_ColorEditFlags_InputRGB.cache = ImGui_ColorEditFlags_InputRGB.func()
  return ImGui_ColorEditFlags_InputRGB.cache

def ImGui_ColorEditFlags_NoAlpha():
  if not hasattr(ImGui_ColorEditFlags_NoAlpha, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoAlpha')
    ImGui_ColorEditFlags_NoAlpha.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoAlpha, 'cache'):
    ImGui_ColorEditFlags_NoAlpha.cache = ImGui_ColorEditFlags_NoAlpha.func()
  return ImGui_ColorEditFlags_NoAlpha.cache

def ImGui_ColorEditFlags_NoBorder():
  if not hasattr(ImGui_ColorEditFlags_NoBorder, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoBorder')
    ImGui_ColorEditFlags_NoBorder.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoBorder, 'cache'):
    ImGui_ColorEditFlags_NoBorder.cache = ImGui_ColorEditFlags_NoBorder.func()
  return ImGui_ColorEditFlags_NoBorder.cache

def ImGui_ColorEditFlags_NoDragDrop():
  if not hasattr(ImGui_ColorEditFlags_NoDragDrop, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoDragDrop')
    ImGui_ColorEditFlags_NoDragDrop.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoDragDrop, 'cache'):
    ImGui_ColorEditFlags_NoDragDrop.cache = ImGui_ColorEditFlags_NoDragDrop.func()
  return ImGui_ColorEditFlags_NoDragDrop.cache

def ImGui_ColorEditFlags_NoInputs():
  if not hasattr(ImGui_ColorEditFlags_NoInputs, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoInputs')
    ImGui_ColorEditFlags_NoInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoInputs, 'cache'):
    ImGui_ColorEditFlags_NoInputs.cache = ImGui_ColorEditFlags_NoInputs.func()
  return ImGui_ColorEditFlags_NoInputs.cache

def ImGui_ColorEditFlags_NoLabel():
  if not hasattr(ImGui_ColorEditFlags_NoLabel, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoLabel')
    ImGui_ColorEditFlags_NoLabel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoLabel, 'cache'):
    ImGui_ColorEditFlags_NoLabel.cache = ImGui_ColorEditFlags_NoLabel.func()
  return ImGui_ColorEditFlags_NoLabel.cache

def ImGui_ColorEditFlags_NoOptions():
  if not hasattr(ImGui_ColorEditFlags_NoOptions, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoOptions')
    ImGui_ColorEditFlags_NoOptions.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoOptions, 'cache'):
    ImGui_ColorEditFlags_NoOptions.cache = ImGui_ColorEditFlags_NoOptions.func()
  return ImGui_ColorEditFlags_NoOptions.cache

def ImGui_ColorEditFlags_NoPicker():
  if not hasattr(ImGui_ColorEditFlags_NoPicker, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoPicker')
    ImGui_ColorEditFlags_NoPicker.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoPicker, 'cache'):
    ImGui_ColorEditFlags_NoPicker.cache = ImGui_ColorEditFlags_NoPicker.func()
  return ImGui_ColorEditFlags_NoPicker.cache

def ImGui_ColorEditFlags_NoSidePreview():
  if not hasattr(ImGui_ColorEditFlags_NoSidePreview, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoSidePreview')
    ImGui_ColorEditFlags_NoSidePreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoSidePreview, 'cache'):
    ImGui_ColorEditFlags_NoSidePreview.cache = ImGui_ColorEditFlags_NoSidePreview.func()
  return ImGui_ColorEditFlags_NoSidePreview.cache

def ImGui_ColorEditFlags_NoSmallPreview():
  if not hasattr(ImGui_ColorEditFlags_NoSmallPreview, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoSmallPreview')
    ImGui_ColorEditFlags_NoSmallPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoSmallPreview, 'cache'):
    ImGui_ColorEditFlags_NoSmallPreview.cache = ImGui_ColorEditFlags_NoSmallPreview.func()
  return ImGui_ColorEditFlags_NoSmallPreview.cache

def ImGui_ColorEditFlags_NoTooltip():
  if not hasattr(ImGui_ColorEditFlags_NoTooltip, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_NoTooltip')
    ImGui_ColorEditFlags_NoTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_NoTooltip, 'cache'):
    ImGui_ColorEditFlags_NoTooltip.cache = ImGui_ColorEditFlags_NoTooltip.func()
  return ImGui_ColorEditFlags_NoTooltip.cache

def ImGui_ColorEditFlags_None():
  if not hasattr(ImGui_ColorEditFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_None')
    ImGui_ColorEditFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_None, 'cache'):
    ImGui_ColorEditFlags_None.cache = ImGui_ColorEditFlags_None.func()
  return ImGui_ColorEditFlags_None.cache

def ImGui_ColorEditFlags_PickerHueBar():
  if not hasattr(ImGui_ColorEditFlags_PickerHueBar, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_PickerHueBar')
    ImGui_ColorEditFlags_PickerHueBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_PickerHueBar, 'cache'):
    ImGui_ColorEditFlags_PickerHueBar.cache = ImGui_ColorEditFlags_PickerHueBar.func()
  return ImGui_ColorEditFlags_PickerHueBar.cache

def ImGui_ColorEditFlags_PickerHueWheel():
  if not hasattr(ImGui_ColorEditFlags_PickerHueWheel, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_PickerHueWheel')
    ImGui_ColorEditFlags_PickerHueWheel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_PickerHueWheel, 'cache'):
    ImGui_ColorEditFlags_PickerHueWheel.cache = ImGui_ColorEditFlags_PickerHueWheel.func()
  return ImGui_ColorEditFlags_PickerHueWheel.cache

def ImGui_ColorEditFlags_Uint8():
  if not hasattr(ImGui_ColorEditFlags_Uint8, 'func'):
    proc = rpr_getfp('ImGui_ColorEditFlags_Uint8')
    ImGui_ColorEditFlags_Uint8.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ColorEditFlags_Uint8, 'cache'):
    ImGui_ColorEditFlags_Uint8.cache = ImGui_ColorEditFlags_Uint8.func()
  return ImGui_ColorEditFlags_Uint8.cache

def ImGui_ColorPicker3(ctx, label, col_rgbInOut, flagsInOptional = None):
  if not hasattr(ImGui_ColorPicker3, 'func'):
    proc = rpr_getfp('ImGui_ColorPicker3')
    ImGui_ColorPicker3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(col_rgbInOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_ColorPicker3.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None)
  return rval, int(args[2].value)

def ImGui_ColorPicker4(ctx, label, col_rgbaInOut, flagsInOptional = None, ref_colInOptional = None):
  if not hasattr(ImGui_ColorPicker4, 'func'):
    proc = rpr_getfp('ImGui_ColorPicker4')
    ImGui_ColorPicker4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(col_rgbaInOut), c_int(flagsInOptional) if flagsInOptional != None else None, c_int(ref_colInOptional) if ref_colInOptional != None else None)
  rval = ImGui_ColorPicker4.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)
  return rval, int(args[2].value)

def ImGui_Combo(ctx, label, current_itemInOut, items, popup_max_height_in_itemsInOptional = None):
  if not hasattr(ImGui_Combo, 'func'):
    proc = rpr_getfp('ImGui_Combo')
    ImGui_Combo.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(current_itemInOut), rpr_packsc(items), c_int(len(items)+1), c_int(popup_max_height_in_itemsInOptional) if popup_max_height_in_itemsInOptional != None else None)
  rval = ImGui_Combo.func(args[0], args[1], byref(args[2]), args[3], args[4], byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value)

def ImGui_ComboFlags_HeightLarge():
  if not hasattr(ImGui_ComboFlags_HeightLarge, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightLarge')
    ImGui_ComboFlags_HeightLarge.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_HeightLarge, 'cache'):
    ImGui_ComboFlags_HeightLarge.cache = ImGui_ComboFlags_HeightLarge.func()
  return ImGui_ComboFlags_HeightLarge.cache

def ImGui_ComboFlags_HeightLargest():
  if not hasattr(ImGui_ComboFlags_HeightLargest, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightLargest')
    ImGui_ComboFlags_HeightLargest.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_HeightLargest, 'cache'):
    ImGui_ComboFlags_HeightLargest.cache = ImGui_ComboFlags_HeightLargest.func()
  return ImGui_ComboFlags_HeightLargest.cache

def ImGui_ComboFlags_HeightRegular():
  if not hasattr(ImGui_ComboFlags_HeightRegular, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightRegular')
    ImGui_ComboFlags_HeightRegular.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_HeightRegular, 'cache'):
    ImGui_ComboFlags_HeightRegular.cache = ImGui_ComboFlags_HeightRegular.func()
  return ImGui_ComboFlags_HeightRegular.cache

def ImGui_ComboFlags_HeightSmall():
  if not hasattr(ImGui_ComboFlags_HeightSmall, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_HeightSmall')
    ImGui_ComboFlags_HeightSmall.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_HeightSmall, 'cache'):
    ImGui_ComboFlags_HeightSmall.cache = ImGui_ComboFlags_HeightSmall.func()
  return ImGui_ComboFlags_HeightSmall.cache

def ImGui_ComboFlags_NoArrowButton():
  if not hasattr(ImGui_ComboFlags_NoArrowButton, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_NoArrowButton')
    ImGui_ComboFlags_NoArrowButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_NoArrowButton, 'cache'):
    ImGui_ComboFlags_NoArrowButton.cache = ImGui_ComboFlags_NoArrowButton.func()
  return ImGui_ComboFlags_NoArrowButton.cache

def ImGui_ComboFlags_NoPreview():
  if not hasattr(ImGui_ComboFlags_NoPreview, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_NoPreview')
    ImGui_ComboFlags_NoPreview.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_NoPreview, 'cache'):
    ImGui_ComboFlags_NoPreview.cache = ImGui_ComboFlags_NoPreview.func()
  return ImGui_ComboFlags_NoPreview.cache

def ImGui_ComboFlags_None():
  if not hasattr(ImGui_ComboFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_None')
    ImGui_ComboFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_None, 'cache'):
    ImGui_ComboFlags_None.cache = ImGui_ComboFlags_None.func()
  return ImGui_ComboFlags_None.cache

def ImGui_ComboFlags_PopupAlignLeft():
  if not hasattr(ImGui_ComboFlags_PopupAlignLeft, 'func'):
    proc = rpr_getfp('ImGui_ComboFlags_PopupAlignLeft')
    ImGui_ComboFlags_PopupAlignLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ComboFlags_PopupAlignLeft, 'cache'):
    ImGui_ComboFlags_PopupAlignLeft.cache = ImGui_ComboFlags_PopupAlignLeft.func()
  return ImGui_ComboFlags_PopupAlignLeft.cache

def ImGui_Cond_Always():
  if not hasattr(ImGui_Cond_Always, 'func'):
    proc = rpr_getfp('ImGui_Cond_Always')
    ImGui_Cond_Always.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Cond_Always, 'cache'):
    ImGui_Cond_Always.cache = ImGui_Cond_Always.func()
  return ImGui_Cond_Always.cache

def ImGui_Cond_Appearing():
  if not hasattr(ImGui_Cond_Appearing, 'func'):
    proc = rpr_getfp('ImGui_Cond_Appearing')
    ImGui_Cond_Appearing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Cond_Appearing, 'cache'):
    ImGui_Cond_Appearing.cache = ImGui_Cond_Appearing.func()
  return ImGui_Cond_Appearing.cache

def ImGui_Cond_FirstUseEver():
  if not hasattr(ImGui_Cond_FirstUseEver, 'func'):
    proc = rpr_getfp('ImGui_Cond_FirstUseEver')
    ImGui_Cond_FirstUseEver.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Cond_FirstUseEver, 'cache'):
    ImGui_Cond_FirstUseEver.cache = ImGui_Cond_FirstUseEver.func()
  return ImGui_Cond_FirstUseEver.cache

def ImGui_Cond_Once():
  if not hasattr(ImGui_Cond_Once, 'func'):
    proc = rpr_getfp('ImGui_Cond_Once')
    ImGui_Cond_Once.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Cond_Once, 'cache'):
    ImGui_Cond_Once.cache = ImGui_Cond_Once.func()
  return ImGui_Cond_Once.cache

def ImGui_ConfigFlags_DockingEnable():
  if not hasattr(ImGui_ConfigFlags_DockingEnable, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_DockingEnable')
    ImGui_ConfigFlags_DockingEnable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_DockingEnable, 'cache'):
    ImGui_ConfigFlags_DockingEnable.cache = ImGui_ConfigFlags_DockingEnable.func()
  return ImGui_ConfigFlags_DockingEnable.cache

def ImGui_ConfigFlags_NavEnableKeyboard():
  if not hasattr(ImGui_ConfigFlags_NavEnableKeyboard, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NavEnableKeyboard')
    ImGui_ConfigFlags_NavEnableKeyboard.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_NavEnableKeyboard, 'cache'):
    ImGui_ConfigFlags_NavEnableKeyboard.cache = ImGui_ConfigFlags_NavEnableKeyboard.func()
  return ImGui_ConfigFlags_NavEnableKeyboard.cache

def ImGui_ConfigFlags_NavEnableSetMousePos():
  if not hasattr(ImGui_ConfigFlags_NavEnableSetMousePos, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NavEnableSetMousePos')
    ImGui_ConfigFlags_NavEnableSetMousePos.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_NavEnableSetMousePos, 'cache'):
    ImGui_ConfigFlags_NavEnableSetMousePos.cache = ImGui_ConfigFlags_NavEnableSetMousePos.func()
  return ImGui_ConfigFlags_NavEnableSetMousePos.cache

def ImGui_ConfigFlags_NoMouse():
  if not hasattr(ImGui_ConfigFlags_NoMouse, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NoMouse')
    ImGui_ConfigFlags_NoMouse.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_NoMouse, 'cache'):
    ImGui_ConfigFlags_NoMouse.cache = ImGui_ConfigFlags_NoMouse.func()
  return ImGui_ConfigFlags_NoMouse.cache

def ImGui_ConfigFlags_NoMouseCursorChange():
  if not hasattr(ImGui_ConfigFlags_NoMouseCursorChange, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NoMouseCursorChange')
    ImGui_ConfigFlags_NoMouseCursorChange.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_NoMouseCursorChange, 'cache'):
    ImGui_ConfigFlags_NoMouseCursorChange.cache = ImGui_ConfigFlags_NoMouseCursorChange.func()
  return ImGui_ConfigFlags_NoMouseCursorChange.cache

def ImGui_ConfigFlags_NoSavedSettings():
  if not hasattr(ImGui_ConfigFlags_NoSavedSettings, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_NoSavedSettings')
    ImGui_ConfigFlags_NoSavedSettings.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_NoSavedSettings, 'cache'):
    ImGui_ConfigFlags_NoSavedSettings.cache = ImGui_ConfigFlags_NoSavedSettings.func()
  return ImGui_ConfigFlags_NoSavedSettings.cache

def ImGui_ConfigFlags_None():
  if not hasattr(ImGui_ConfigFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ConfigFlags_None')
    ImGui_ConfigFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigFlags_None, 'cache'):
    ImGui_ConfigFlags_None.cache = ImGui_ConfigFlags_None.func()
  return ImGui_ConfigFlags_None.cache

def ImGui_ConfigVar_DockingNoSplit():
  if not hasattr(ImGui_ConfigVar_DockingNoSplit, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_DockingNoSplit')
    ImGui_ConfigVar_DockingNoSplit.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_DockingNoSplit, 'cache'):
    ImGui_ConfigVar_DockingNoSplit.cache = ImGui_ConfigVar_DockingNoSplit.func()
  return ImGui_ConfigVar_DockingNoSplit.cache

def ImGui_ConfigVar_DockingTransparentPayload():
  if not hasattr(ImGui_ConfigVar_DockingTransparentPayload, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_DockingTransparentPayload')
    ImGui_ConfigVar_DockingTransparentPayload.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_DockingTransparentPayload, 'cache'):
    ImGui_ConfigVar_DockingTransparentPayload.cache = ImGui_ConfigVar_DockingTransparentPayload.func()
  return ImGui_ConfigVar_DockingTransparentPayload.cache

def ImGui_ConfigVar_DockingWithShift():
  if not hasattr(ImGui_ConfigVar_DockingWithShift, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_DockingWithShift')
    ImGui_ConfigVar_DockingWithShift.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_DockingWithShift, 'cache'):
    ImGui_ConfigVar_DockingWithShift.cache = ImGui_ConfigVar_DockingWithShift.func()
  return ImGui_ConfigVar_DockingWithShift.cache

def ImGui_ConfigVar_DragClickToInputText():
  if not hasattr(ImGui_ConfigVar_DragClickToInputText, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_DragClickToInputText')
    ImGui_ConfigVar_DragClickToInputText.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_DragClickToInputText, 'cache'):
    ImGui_ConfigVar_DragClickToInputText.cache = ImGui_ConfigVar_DragClickToInputText.func()
  return ImGui_ConfigVar_DragClickToInputText.cache

def ImGui_ConfigVar_Flags():
  if not hasattr(ImGui_ConfigVar_Flags, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_Flags')
    ImGui_ConfigVar_Flags.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_Flags, 'cache'):
    ImGui_ConfigVar_Flags.cache = ImGui_ConfigVar_Flags.func()
  return ImGui_ConfigVar_Flags.cache

def ImGui_ConfigVar_InputTextCursorBlink():
  if not hasattr(ImGui_ConfigVar_InputTextCursorBlink, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_InputTextCursorBlink')
    ImGui_ConfigVar_InputTextCursorBlink.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_InputTextCursorBlink, 'cache'):
    ImGui_ConfigVar_InputTextCursorBlink.cache = ImGui_ConfigVar_InputTextCursorBlink.func()
  return ImGui_ConfigVar_InputTextCursorBlink.cache

def ImGui_ConfigVar_InputTrickleEventQueue():
  if not hasattr(ImGui_ConfigVar_InputTrickleEventQueue, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_InputTrickleEventQueue')
    ImGui_ConfigVar_InputTrickleEventQueue.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_InputTrickleEventQueue, 'cache'):
    ImGui_ConfigVar_InputTrickleEventQueue.cache = ImGui_ConfigVar_InputTrickleEventQueue.func()
  return ImGui_ConfigVar_InputTrickleEventQueue.cache

def ImGui_ConfigVar_KeyRepeatDelay():
  if not hasattr(ImGui_ConfigVar_KeyRepeatDelay, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_KeyRepeatDelay')
    ImGui_ConfigVar_KeyRepeatDelay.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_KeyRepeatDelay, 'cache'):
    ImGui_ConfigVar_KeyRepeatDelay.cache = ImGui_ConfigVar_KeyRepeatDelay.func()
  return ImGui_ConfigVar_KeyRepeatDelay.cache

def ImGui_ConfigVar_KeyRepeatRate():
  if not hasattr(ImGui_ConfigVar_KeyRepeatRate, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_KeyRepeatRate')
    ImGui_ConfigVar_KeyRepeatRate.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_KeyRepeatRate, 'cache'):
    ImGui_ConfigVar_KeyRepeatRate.cache = ImGui_ConfigVar_KeyRepeatRate.func()
  return ImGui_ConfigVar_KeyRepeatRate.cache

def ImGui_ConfigVar_MacOSXBehaviors():
  if not hasattr(ImGui_ConfigVar_MacOSXBehaviors, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_MacOSXBehaviors')
    ImGui_ConfigVar_MacOSXBehaviors.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_MacOSXBehaviors, 'cache'):
    ImGui_ConfigVar_MacOSXBehaviors.cache = ImGui_ConfigVar_MacOSXBehaviors.func()
  return ImGui_ConfigVar_MacOSXBehaviors.cache

def ImGui_ConfigVar_MouseDoubleClickMaxDist():
  if not hasattr(ImGui_ConfigVar_MouseDoubleClickMaxDist, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_MouseDoubleClickMaxDist')
    ImGui_ConfigVar_MouseDoubleClickMaxDist.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_MouseDoubleClickMaxDist, 'cache'):
    ImGui_ConfigVar_MouseDoubleClickMaxDist.cache = ImGui_ConfigVar_MouseDoubleClickMaxDist.func()
  return ImGui_ConfigVar_MouseDoubleClickMaxDist.cache

def ImGui_ConfigVar_MouseDoubleClickTime():
  if not hasattr(ImGui_ConfigVar_MouseDoubleClickTime, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_MouseDoubleClickTime')
    ImGui_ConfigVar_MouseDoubleClickTime.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_MouseDoubleClickTime, 'cache'):
    ImGui_ConfigVar_MouseDoubleClickTime.cache = ImGui_ConfigVar_MouseDoubleClickTime.func()
  return ImGui_ConfigVar_MouseDoubleClickTime.cache

def ImGui_ConfigVar_MouseDragThreshold():
  if not hasattr(ImGui_ConfigVar_MouseDragThreshold, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_MouseDragThreshold')
    ImGui_ConfigVar_MouseDragThreshold.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_MouseDragThreshold, 'cache'):
    ImGui_ConfigVar_MouseDragThreshold.cache = ImGui_ConfigVar_MouseDragThreshold.func()
  return ImGui_ConfigVar_MouseDragThreshold.cache

def ImGui_ConfigVar_ViewportsNoDecoration():
  if not hasattr(ImGui_ConfigVar_ViewportsNoDecoration, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_ViewportsNoDecoration')
    ImGui_ConfigVar_ViewportsNoDecoration.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_ViewportsNoDecoration, 'cache'):
    ImGui_ConfigVar_ViewportsNoDecoration.cache = ImGui_ConfigVar_ViewportsNoDecoration.func()
  return ImGui_ConfigVar_ViewportsNoDecoration.cache

def ImGui_ConfigVar_WindowsMoveFromTitleBarOnly():
  if not hasattr(ImGui_ConfigVar_WindowsMoveFromTitleBarOnly, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_WindowsMoveFromTitleBarOnly')
    ImGui_ConfigVar_WindowsMoveFromTitleBarOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_WindowsMoveFromTitleBarOnly, 'cache'):
    ImGui_ConfigVar_WindowsMoveFromTitleBarOnly.cache = ImGui_ConfigVar_WindowsMoveFromTitleBarOnly.func()
  return ImGui_ConfigVar_WindowsMoveFromTitleBarOnly.cache

def ImGui_ConfigVar_WindowsResizeFromEdges():
  if not hasattr(ImGui_ConfigVar_WindowsResizeFromEdges, 'func'):
    proc = rpr_getfp('ImGui_ConfigVar_WindowsResizeFromEdges')
    ImGui_ConfigVar_WindowsResizeFromEdges.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ConfigVar_WindowsResizeFromEdges, 'cache'):
    ImGui_ConfigVar_WindowsResizeFromEdges.cache = ImGui_ConfigVar_WindowsResizeFromEdges.func()
  return ImGui_ConfigVar_WindowsResizeFromEdges.cache

def ImGui_CreateContext(label, config_flagsInOptional = None):
  if not hasattr(ImGui_CreateContext, 'func'):
    proc = rpr_getfp('ImGui_CreateContext')
    ImGui_CreateContext.func = CFUNCTYPE(c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packsc(label), c_int(config_flagsInOptional) if config_flagsInOptional != None else None)
  rval = ImGui_CreateContext.func(args[0], byref(args[1]) if args[1] != None else None)
  return rpr_unpackp('ImGui_Context*', rval)

def ImGui_CreateFont(family_or_file, size, flagsInOptional = None):
  if not hasattr(ImGui_CreateFont, 'func'):
    proc = rpr_getfp('ImGui_CreateFont')
    ImGui_CreateFont.func = CFUNCTYPE(c_void_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packsc(family_or_file), c_int(size), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_CreateFont.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rpr_unpackp('ImGui_Font*', rval)

def ImGui_CreateListClipper(ctx):
  if not hasattr(ImGui_CreateListClipper, 'func'):
    proc = rpr_getfp('ImGui_CreateListClipper')
    ImGui_CreateListClipper.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_CreateListClipper.func(args[0])
  return rpr_unpackp('ImGui_ListClipper*', rval)

def ImGui_CreateTextFilter(default_filterInOptional = None):
  if not hasattr(ImGui_CreateTextFilter, 'func'):
    proc = rpr_getfp('ImGui_CreateTextFilter')
    ImGui_CreateTextFilter.func = CFUNCTYPE(c_void_p, c_char_p)(proc)
  args = (rpr_packsc(default_filterInOptional) if default_filterInOptional != None else None,)
  rval = ImGui_CreateTextFilter.func(args[0])
  return rpr_unpackp('ImGui_TextFilter*', rval)

def ImGui_DebugTextEncoding(ctx, text):
  if not hasattr(ImGui_DebugTextEncoding, 'func'):
    proc = rpr_getfp('ImGui_DebugTextEncoding')
    ImGui_DebugTextEncoding.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_DebugTextEncoding.func(args[0], args[1])

def ImGui_DestroyContext(ctx):
  if not hasattr(ImGui_DestroyContext, 'func'):
    proc = rpr_getfp('ImGui_DestroyContext')
    ImGui_DestroyContext.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_DestroyContext.func(args[0])

def ImGui_DetachFont(ctx, font):
  if not hasattr(ImGui_DetachFont, 'func'):
    proc = rpr_getfp('ImGui_DetachFont')
    ImGui_DetachFont.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packp('ImGui_Font*', font))
  ImGui_DetachFont.func(args[0], args[1])

def ImGui_Dir_Down():
  if not hasattr(ImGui_Dir_Down, 'func'):
    proc = rpr_getfp('ImGui_Dir_Down')
    ImGui_Dir_Down.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Dir_Down, 'cache'):
    ImGui_Dir_Down.cache = ImGui_Dir_Down.func()
  return ImGui_Dir_Down.cache

def ImGui_Dir_Left():
  if not hasattr(ImGui_Dir_Left, 'func'):
    proc = rpr_getfp('ImGui_Dir_Left')
    ImGui_Dir_Left.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Dir_Left, 'cache'):
    ImGui_Dir_Left.cache = ImGui_Dir_Left.func()
  return ImGui_Dir_Left.cache

def ImGui_Dir_None():
  if not hasattr(ImGui_Dir_None, 'func'):
    proc = rpr_getfp('ImGui_Dir_None')
    ImGui_Dir_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Dir_None, 'cache'):
    ImGui_Dir_None.cache = ImGui_Dir_None.func()
  return ImGui_Dir_None.cache

def ImGui_Dir_Right():
  if not hasattr(ImGui_Dir_Right, 'func'):
    proc = rpr_getfp('ImGui_Dir_Right')
    ImGui_Dir_Right.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Dir_Right, 'cache'):
    ImGui_Dir_Right.cache = ImGui_Dir_Right.func()
  return ImGui_Dir_Right.cache

def ImGui_Dir_Up():
  if not hasattr(ImGui_Dir_Up, 'func'):
    proc = rpr_getfp('ImGui_Dir_Up')
    ImGui_Dir_Up.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Dir_Up, 'cache'):
    ImGui_Dir_Up.cache = ImGui_Dir_Up.func()
  return ImGui_Dir_Up.cache

def ImGui_DragDouble(ctx, label, vInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragDouble, 'func'):
    proc = rpr_getfp('ImGui_DragDouble')
    ImGui_DragDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(vInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragDouble.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, args[6], byref(args[7]) if args[7] != None else None)
  return rval, float(args[2].value)

def ImGui_DragDouble2(ctx, label, v1InOut, v2InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragDouble2, 'func'):
    proc = rpr_getfp('ImGui_DragDouble2')
    ImGui_DragDouble2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragDouble2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], byref(args[8]) if args[8] != None else None)
  return rval, float(args[2].value), float(args[3].value)

def ImGui_DragDouble3(ctx, label, v1InOut, v2InOut, v3InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragDouble3, 'func'):
    proc = rpr_getfp('ImGui_DragDouble3')
    ImGui_DragDouble3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragDouble3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, args[8], byref(args[9]) if args[9] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value)

def ImGui_DragDouble4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragDouble4, 'func'):
    proc = rpr_getfp('ImGui_DragDouble4')
    ImGui_DragDouble4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v4InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragDouble4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None, args[9], byref(args[10]) if args[10] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value), float(args[5].value)

def ImGui_DragDoubleN(ctx, label, values, speedInOptional = None, minInOptional = None, maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragDoubleN, 'func'):
    proc = rpr_getfp('ImGui_DragDoubleN')
    ImGui_DragDoubleN.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_double(speedInOptional) if speedInOptional != None else None, c_double(minInOptional) if minInOptional != None else None, c_double(maxInOptional) if maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragDoubleN.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, args[6], byref(args[7]) if args[7] != None else None)
  return rval

def ImGui_DragDropFlags_AcceptBeforeDelivery():
  if not hasattr(ImGui_DragDropFlags_AcceptBeforeDelivery, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptBeforeDelivery')
    ImGui_DragDropFlags_AcceptBeforeDelivery.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_AcceptBeforeDelivery, 'cache'):
    ImGui_DragDropFlags_AcceptBeforeDelivery.cache = ImGui_DragDropFlags_AcceptBeforeDelivery.func()
  return ImGui_DragDropFlags_AcceptBeforeDelivery.cache

def ImGui_DragDropFlags_AcceptNoDrawDefaultRect():
  if not hasattr(ImGui_DragDropFlags_AcceptNoDrawDefaultRect, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptNoDrawDefaultRect')
    ImGui_DragDropFlags_AcceptNoDrawDefaultRect.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_AcceptNoDrawDefaultRect, 'cache'):
    ImGui_DragDropFlags_AcceptNoDrawDefaultRect.cache = ImGui_DragDropFlags_AcceptNoDrawDefaultRect.func()
  return ImGui_DragDropFlags_AcceptNoDrawDefaultRect.cache

def ImGui_DragDropFlags_AcceptNoPreviewTooltip():
  if not hasattr(ImGui_DragDropFlags_AcceptNoPreviewTooltip, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptNoPreviewTooltip')
    ImGui_DragDropFlags_AcceptNoPreviewTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_AcceptNoPreviewTooltip, 'cache'):
    ImGui_DragDropFlags_AcceptNoPreviewTooltip.cache = ImGui_DragDropFlags_AcceptNoPreviewTooltip.func()
  return ImGui_DragDropFlags_AcceptNoPreviewTooltip.cache

def ImGui_DragDropFlags_AcceptPeekOnly():
  if not hasattr(ImGui_DragDropFlags_AcceptPeekOnly, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_AcceptPeekOnly')
    ImGui_DragDropFlags_AcceptPeekOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_AcceptPeekOnly, 'cache'):
    ImGui_DragDropFlags_AcceptPeekOnly.cache = ImGui_DragDropFlags_AcceptPeekOnly.func()
  return ImGui_DragDropFlags_AcceptPeekOnly.cache

def ImGui_DragDropFlags_None():
  if not hasattr(ImGui_DragDropFlags_None, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_None')
    ImGui_DragDropFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_None, 'cache'):
    ImGui_DragDropFlags_None.cache = ImGui_DragDropFlags_None.func()
  return ImGui_DragDropFlags_None.cache

def ImGui_DragDropFlags_SourceAllowNullID():
  if not hasattr(ImGui_DragDropFlags_SourceAllowNullID, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceAllowNullID')
    ImGui_DragDropFlags_SourceAllowNullID.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_SourceAllowNullID, 'cache'):
    ImGui_DragDropFlags_SourceAllowNullID.cache = ImGui_DragDropFlags_SourceAllowNullID.func()
  return ImGui_DragDropFlags_SourceAllowNullID.cache

def ImGui_DragDropFlags_SourceAutoExpirePayload():
  if not hasattr(ImGui_DragDropFlags_SourceAutoExpirePayload, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceAutoExpirePayload')
    ImGui_DragDropFlags_SourceAutoExpirePayload.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_SourceAutoExpirePayload, 'cache'):
    ImGui_DragDropFlags_SourceAutoExpirePayload.cache = ImGui_DragDropFlags_SourceAutoExpirePayload.func()
  return ImGui_DragDropFlags_SourceAutoExpirePayload.cache

def ImGui_DragDropFlags_SourceExtern():
  if not hasattr(ImGui_DragDropFlags_SourceExtern, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceExtern')
    ImGui_DragDropFlags_SourceExtern.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_SourceExtern, 'cache'):
    ImGui_DragDropFlags_SourceExtern.cache = ImGui_DragDropFlags_SourceExtern.func()
  return ImGui_DragDropFlags_SourceExtern.cache

def ImGui_DragDropFlags_SourceNoDisableHover():
  if not hasattr(ImGui_DragDropFlags_SourceNoDisableHover, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceNoDisableHover')
    ImGui_DragDropFlags_SourceNoDisableHover.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_SourceNoDisableHover, 'cache'):
    ImGui_DragDropFlags_SourceNoDisableHover.cache = ImGui_DragDropFlags_SourceNoDisableHover.func()
  return ImGui_DragDropFlags_SourceNoDisableHover.cache

def ImGui_DragDropFlags_SourceNoHoldToOpenOthers():
  if not hasattr(ImGui_DragDropFlags_SourceNoHoldToOpenOthers, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceNoHoldToOpenOthers')
    ImGui_DragDropFlags_SourceNoHoldToOpenOthers.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_SourceNoHoldToOpenOthers, 'cache'):
    ImGui_DragDropFlags_SourceNoHoldToOpenOthers.cache = ImGui_DragDropFlags_SourceNoHoldToOpenOthers.func()
  return ImGui_DragDropFlags_SourceNoHoldToOpenOthers.cache

def ImGui_DragDropFlags_SourceNoPreviewTooltip():
  if not hasattr(ImGui_DragDropFlags_SourceNoPreviewTooltip, 'func'):
    proc = rpr_getfp('ImGui_DragDropFlags_SourceNoPreviewTooltip')
    ImGui_DragDropFlags_SourceNoPreviewTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DragDropFlags_SourceNoPreviewTooltip, 'cache'):
    ImGui_DragDropFlags_SourceNoPreviewTooltip.cache = ImGui_DragDropFlags_SourceNoPreviewTooltip.func()
  return ImGui_DragDropFlags_SourceNoPreviewTooltip.cache

def ImGui_DragFloatRange2(ctx, label, v_current_minInOut, v_current_maxInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, format_maxInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragFloatRange2, 'func'):
    proc = rpr_getfp('ImGui_DragFloatRange2')
    ImGui_DragFloatRange2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v_current_minInOut), c_double(v_current_maxInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_double(v_minInOptional) if v_minInOptional != None else None, c_double(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, rpr_packsc(format_maxInOptional) if format_maxInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragFloatRange2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, float(args[2].value), float(args[3].value)

def ImGui_DragInt(ctx, label, vInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragInt, 'func'):
    proc = rpr_getfp('ImGui_DragInt')
    ImGui_DragInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(vInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragInt.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, args[6], byref(args[7]) if args[7] != None else None)
  return rval, int(args[2].value)

def ImGui_DragInt2(ctx, label, v1InOut, v2InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragInt2, 'func'):
    proc = rpr_getfp('ImGui_DragInt2')
    ImGui_DragInt2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragInt2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], byref(args[8]) if args[8] != None else None)
  return rval, int(args[2].value), int(args[3].value)

def ImGui_DragInt3(ctx, label, v1InOut, v2InOut, v3InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragInt3, 'func'):
    proc = rpr_getfp('ImGui_DragInt3')
    ImGui_DragInt3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragInt3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, args[8], byref(args[9]) if args[9] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value)

def ImGui_DragInt4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragInt4, 'func'):
    proc = rpr_getfp('ImGui_DragInt4')
    ImGui_DragInt4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v4InOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragInt4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None, args[9], byref(args[10]) if args[10] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

def ImGui_DragIntRange2(ctx, label, v_current_minInOut, v_current_maxInOut, v_speedInOptional = None, v_minInOptional = None, v_maxInOptional = None, formatInOptional = None, format_maxInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DragIntRange2, 'func'):
    proc = rpr_getfp('ImGui_DragIntRange2')
    ImGui_DragIntRange2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v_current_minInOut), c_int(v_current_maxInOut), c_double(v_speedInOptional) if v_speedInOptional != None else None, c_int(v_minInOptional) if v_minInOptional != None else None, c_int(v_maxInOptional) if v_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, rpr_packsc(format_maxInOptional) if format_maxInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_DragIntRange2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, int(args[2].value), int(args[3].value)

def ImGui_DrawFlags_Closed():
  if not hasattr(ImGui_DrawFlags_Closed, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_Closed')
    ImGui_DrawFlags_Closed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_Closed, 'cache'):
    ImGui_DrawFlags_Closed.cache = ImGui_DrawFlags_Closed.func()
  return ImGui_DrawFlags_Closed.cache

def ImGui_DrawFlags_None():
  if not hasattr(ImGui_DrawFlags_None, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_None')
    ImGui_DrawFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_None, 'cache'):
    ImGui_DrawFlags_None.cache = ImGui_DrawFlags_None.func()
  return ImGui_DrawFlags_None.cache

def ImGui_DrawFlags_RoundCornersAll():
  if not hasattr(ImGui_DrawFlags_RoundCornersAll, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersAll')
    ImGui_DrawFlags_RoundCornersAll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersAll, 'cache'):
    ImGui_DrawFlags_RoundCornersAll.cache = ImGui_DrawFlags_RoundCornersAll.func()
  return ImGui_DrawFlags_RoundCornersAll.cache

def ImGui_DrawFlags_RoundCornersBottom():
  if not hasattr(ImGui_DrawFlags_RoundCornersBottom, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersBottom')
    ImGui_DrawFlags_RoundCornersBottom.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersBottom, 'cache'):
    ImGui_DrawFlags_RoundCornersBottom.cache = ImGui_DrawFlags_RoundCornersBottom.func()
  return ImGui_DrawFlags_RoundCornersBottom.cache

def ImGui_DrawFlags_RoundCornersBottomLeft():
  if not hasattr(ImGui_DrawFlags_RoundCornersBottomLeft, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersBottomLeft')
    ImGui_DrawFlags_RoundCornersBottomLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersBottomLeft, 'cache'):
    ImGui_DrawFlags_RoundCornersBottomLeft.cache = ImGui_DrawFlags_RoundCornersBottomLeft.func()
  return ImGui_DrawFlags_RoundCornersBottomLeft.cache

def ImGui_DrawFlags_RoundCornersBottomRight():
  if not hasattr(ImGui_DrawFlags_RoundCornersBottomRight, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersBottomRight')
    ImGui_DrawFlags_RoundCornersBottomRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersBottomRight, 'cache'):
    ImGui_DrawFlags_RoundCornersBottomRight.cache = ImGui_DrawFlags_RoundCornersBottomRight.func()
  return ImGui_DrawFlags_RoundCornersBottomRight.cache

def ImGui_DrawFlags_RoundCornersLeft():
  if not hasattr(ImGui_DrawFlags_RoundCornersLeft, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersLeft')
    ImGui_DrawFlags_RoundCornersLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersLeft, 'cache'):
    ImGui_DrawFlags_RoundCornersLeft.cache = ImGui_DrawFlags_RoundCornersLeft.func()
  return ImGui_DrawFlags_RoundCornersLeft.cache

def ImGui_DrawFlags_RoundCornersNone():
  if not hasattr(ImGui_DrawFlags_RoundCornersNone, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersNone')
    ImGui_DrawFlags_RoundCornersNone.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersNone, 'cache'):
    ImGui_DrawFlags_RoundCornersNone.cache = ImGui_DrawFlags_RoundCornersNone.func()
  return ImGui_DrawFlags_RoundCornersNone.cache

def ImGui_DrawFlags_RoundCornersRight():
  if not hasattr(ImGui_DrawFlags_RoundCornersRight, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersRight')
    ImGui_DrawFlags_RoundCornersRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersRight, 'cache'):
    ImGui_DrawFlags_RoundCornersRight.cache = ImGui_DrawFlags_RoundCornersRight.func()
  return ImGui_DrawFlags_RoundCornersRight.cache

def ImGui_DrawFlags_RoundCornersTop():
  if not hasattr(ImGui_DrawFlags_RoundCornersTop, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersTop')
    ImGui_DrawFlags_RoundCornersTop.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersTop, 'cache'):
    ImGui_DrawFlags_RoundCornersTop.cache = ImGui_DrawFlags_RoundCornersTop.func()
  return ImGui_DrawFlags_RoundCornersTop.cache

def ImGui_DrawFlags_RoundCornersTopLeft():
  if not hasattr(ImGui_DrawFlags_RoundCornersTopLeft, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersTopLeft')
    ImGui_DrawFlags_RoundCornersTopLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersTopLeft, 'cache'):
    ImGui_DrawFlags_RoundCornersTopLeft.cache = ImGui_DrawFlags_RoundCornersTopLeft.func()
  return ImGui_DrawFlags_RoundCornersTopLeft.cache

def ImGui_DrawFlags_RoundCornersTopRight():
  if not hasattr(ImGui_DrawFlags_RoundCornersTopRight, 'func'):
    proc = rpr_getfp('ImGui_DrawFlags_RoundCornersTopRight')
    ImGui_DrawFlags_RoundCornersTopRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_DrawFlags_RoundCornersTopRight, 'cache'):
    ImGui_DrawFlags_RoundCornersTopRight.cache = ImGui_DrawFlags_RoundCornersTopRight.func()
  return ImGui_DrawFlags_RoundCornersTopRight.cache

def ImGui_DrawList_AddBezierCubic(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, col_rgba, thickness, num_segmentsInOptional = None):
  if not hasattr(ImGui_DrawList_AddBezierCubic, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddBezierCubic')
    ImGui_DrawList_AddBezierCubic.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(col_rgba), c_double(thickness), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  ImGui_DrawList_AddBezierCubic.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10], byref(args[11]) if args[11] != None else None)

def ImGui_DrawList_AddBezierQuadratic(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, col_rgba, thickness, num_segmentsInOptional = None):
  if not hasattr(ImGui_DrawList_AddBezierQuadratic, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddBezierQuadratic')
    ImGui_DrawList_AddBezierQuadratic.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(col_rgba), c_double(thickness), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  ImGui_DrawList_AddBezierQuadratic.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], byref(args[9]) if args[9] != None else None)

def ImGui_DrawList_AddCircle(draw_list, center_x, center_y, radius, col_rgba, num_segmentsInOptional = None, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_AddCircle, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddCircle')
    ImGui_DrawList_AddCircle.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None, c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_AddCircle.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)

def ImGui_DrawList_AddCircleFilled(draw_list, center_x, center_y, radius, col_rgba, num_segmentsInOptional = None):
  if not hasattr(ImGui_DrawList_AddCircleFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddCircleFilled')
    ImGui_DrawList_AddCircleFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  ImGui_DrawList_AddCircleFilled.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)

def ImGui_DrawList_AddConvexPolyFilled(draw_list, points, col_rgba):
  if not hasattr(ImGui_DrawList_AddConvexPolyFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddConvexPolyFilled')
    ImGui_DrawList_AddConvexPolyFilled.func = CFUNCTYPE(None, c_void_p, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), rpr_packp('reaper_array*', points), c_int(col_rgba))
  ImGui_DrawList_AddConvexPolyFilled.func(args[0], args[1], args[2])

def ImGui_DrawList_AddLine(draw_list, p1_x, p1_y, p2_x, p2_y, col_rgba, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_AddLine, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddLine')
    ImGui_DrawList_AddLine.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_int(col_rgba), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_AddLine.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)

def ImGui_DrawList_AddNgon(draw_list, center_x, center_y, radius, col_rgba, num_segments, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_AddNgon, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddNgon')
    ImGui_DrawList_AddNgon.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segments), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_AddNgon.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)

def ImGui_DrawList_AddNgonFilled(draw_list, center_x, center_y, radius, col_rgba, num_segments):
  if not hasattr(ImGui_DrawList_AddNgonFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddNgonFilled')
    ImGui_DrawList_AddNgonFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(col_rgba), c_int(num_segments))
  ImGui_DrawList_AddNgonFilled.func(args[0], args[1], args[2], args[3], args[4], args[5])

def ImGui_DrawList_AddPolyline(draw_list, points, col_rgba, flags, thickness):
  if not hasattr(ImGui_DrawList_AddPolyline, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddPolyline')
    ImGui_DrawList_AddPolyline.func = CFUNCTYPE(None, c_void_p, c_void_p, c_int, c_int, c_double)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), rpr_packp('reaper_array*', points), c_int(col_rgba), c_int(flags), c_double(thickness))
  ImGui_DrawList_AddPolyline.func(args[0], args[1], args[2], args[3], args[4])

def ImGui_DrawList_AddQuad(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, col_rgba, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_AddQuad, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddQuad')
    ImGui_DrawList_AddQuad.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(col_rgba), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_AddQuad.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], byref(args[10]) if args[10] != None else None)

def ImGui_DrawList_AddQuadFilled(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, col_rgba):
  if not hasattr(ImGui_DrawList_AddQuadFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddQuadFilled')
    ImGui_DrawList_AddQuadFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(col_rgba))
  ImGui_DrawList_AddQuadFilled.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9])

def ImGui_DrawList_AddRect(draw_list, p_min_x, p_min_y, p_max_x, p_max_y, col_rgba, roundingInOptional = None, flagsInOptional = None, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_AddRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddRect')
    ImGui_DrawList_AddRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p_min_x), c_double(p_min_y), c_double(p_max_x), c_double(p_max_y), c_int(col_rgba), c_double(roundingInOptional) if roundingInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None, c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_AddRect.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None)

def ImGui_DrawList_AddRectFilled(draw_list, p_min_x, p_min_y, p_max_x, p_max_y, col_rgba, roundingInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DrawList_AddRectFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddRectFilled')
    ImGui_DrawList_AddRectFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p_min_x), c_double(p_min_y), c_double(p_max_x), c_double(p_max_y), c_int(col_rgba), c_double(roundingInOptional) if roundingInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  ImGui_DrawList_AddRectFilled.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None)

def ImGui_DrawList_AddRectFilledMultiColor(draw_list, p_min_x, p_min_y, p_max_x, p_max_y, col_upr_left, col_upr_right, col_bot_right, col_bot_left):
  if not hasattr(ImGui_DrawList_AddRectFilledMultiColor, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddRectFilledMultiColor')
    ImGui_DrawList_AddRectFilledMultiColor.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p_min_x), c_double(p_min_y), c_double(p_max_x), c_double(p_max_y), c_int(col_upr_left), c_int(col_upr_right), c_int(col_bot_right), c_int(col_bot_left))
  ImGui_DrawList_AddRectFilledMultiColor.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])

def ImGui_DrawList_AddText(draw_list, x, y, col_rgba, text):
  if not hasattr(ImGui_DrawList_AddText, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddText')
    ImGui_DrawList_AddText.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_int, c_char_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(x), c_double(y), c_int(col_rgba), rpr_packsc(text))
  ImGui_DrawList_AddText.func(args[0], args[1], args[2], args[3], args[4])

def ImGui_DrawList_AddTextEx(draw_list, font, font_size, pos_x, pos_y, col_rgba, text, wrap_widthInOptional = None, cpu_fine_clip_rect_xInOptional = None, cpu_fine_clip_rect_yInOptional = None, cpu_fine_clip_rect_wInOptional = None, cpu_fine_clip_rect_hInOptional = None):
  if not hasattr(ImGui_DrawList_AddTextEx, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddTextEx')
    ImGui_DrawList_AddTextEx.func = CFUNCTYPE(None, c_void_p, c_void_p, c_double, c_double, c_double, c_int, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), rpr_packp('ImGui_Font*', font), c_double(font_size), c_double(pos_x), c_double(pos_y), c_int(col_rgba), rpr_packsc(text), c_double(wrap_widthInOptional) if wrap_widthInOptional != None else None, c_double(cpu_fine_clip_rect_xInOptional) if cpu_fine_clip_rect_xInOptional != None else None, c_double(cpu_fine_clip_rect_yInOptional) if cpu_fine_clip_rect_yInOptional != None else None, c_double(cpu_fine_clip_rect_wInOptional) if cpu_fine_clip_rect_wInOptional != None else None, c_double(cpu_fine_clip_rect_hInOptional) if cpu_fine_clip_rect_hInOptional != None else None)
  ImGui_DrawList_AddTextEx.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None, byref(args[9]) if args[9] != None else None, byref(args[10]) if args[10] != None else None, byref(args[11]) if args[11] != None else None)

def ImGui_DrawList_AddTriangle(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, col_rgba, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_AddTriangle, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddTriangle')
    ImGui_DrawList_AddTriangle.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(col_rgba), c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_AddTriangle.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)

def ImGui_DrawList_AddTriangleFilled(draw_list, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, col_rgba):
  if not hasattr(ImGui_DrawList_AddTriangleFilled, 'func'):
    proc = rpr_getfp('ImGui_DrawList_AddTriangleFilled')
    ImGui_DrawList_AddTriangleFilled.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p1_x), c_double(p1_y), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(col_rgba))
  ImGui_DrawList_AddTriangleFilled.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

def ImGui_DrawList_PathArcTo(draw_list, center_x, center_y, radius, a_min, a_max, num_segmentsInOptional = None):
  if not hasattr(ImGui_DrawList_PathArcTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathArcTo')
    ImGui_DrawList_PathArcTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_double(a_min), c_double(a_max), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  ImGui_DrawList_PathArcTo.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)

def ImGui_DrawList_PathArcToFast(draw_list, center_x, center_y, radius, a_min_of_12, a_max_of_12):
  if not hasattr(ImGui_DrawList_PathArcToFast, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathArcToFast')
    ImGui_DrawList_PathArcToFast.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_int, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(center_x), c_double(center_y), c_double(radius), c_int(a_min_of_12), c_int(a_max_of_12))
  ImGui_DrawList_PathArcToFast.func(args[0], args[1], args[2], args[3], args[4], args[5])

def ImGui_DrawList_PathBezierCubicCurveTo(draw_list, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, num_segmentsInOptional = None):
  if not hasattr(ImGui_DrawList_PathBezierCubicCurveTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathBezierCubicCurveTo')
    ImGui_DrawList_PathBezierCubicCurveTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_double(p4_x), c_double(p4_y), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  ImGui_DrawList_PathBezierCubicCurveTo.func(args[0], args[1], args[2], args[3], args[4], args[5], args[6], byref(args[7]) if args[7] != None else None)

def ImGui_DrawList_PathBezierQuadraticCurveTo(draw_list, p2_x, p2_y, p3_x, p3_y, num_segmentsInOptional = None):
  if not hasattr(ImGui_DrawList_PathBezierQuadraticCurveTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathBezierQuadraticCurveTo')
    ImGui_DrawList_PathBezierQuadraticCurveTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(p2_x), c_double(p2_y), c_double(p3_x), c_double(p3_y), c_int(num_segmentsInOptional) if num_segmentsInOptional != None else None)
  ImGui_DrawList_PathBezierQuadraticCurveTo.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)

def ImGui_DrawList_PathClear(draw_list):
  if not hasattr(ImGui_DrawList_PathClear, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathClear')
    ImGui_DrawList_PathClear.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list),)
  ImGui_DrawList_PathClear.func(args[0])

def ImGui_DrawList_PathFillConvex(draw_list, col_rgba):
  if not hasattr(ImGui_DrawList_PathFillConvex, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathFillConvex')
    ImGui_DrawList_PathFillConvex.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_int(col_rgba))
  ImGui_DrawList_PathFillConvex.func(args[0], args[1])

def ImGui_DrawList_PathLineTo(draw_list, pos_x, pos_y):
  if not hasattr(ImGui_DrawList_PathLineTo, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathLineTo')
    ImGui_DrawList_PathLineTo.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(pos_x), c_double(pos_y))
  ImGui_DrawList_PathLineTo.func(args[0], args[1], args[2])

def ImGui_DrawList_PathRect(draw_list, rect_min_x, rect_min_y, rect_max_x, rect_max_y, roundingInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_DrawList_PathRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathRect')
    ImGui_DrawList_PathRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(rect_min_x), c_double(rect_min_y), c_double(rect_max_x), c_double(rect_max_y), c_double(roundingInOptional) if roundingInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  ImGui_DrawList_PathRect.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)

def ImGui_DrawList_PathStroke(draw_list, col_rgba, flagsInOptional = None, thicknessInOptional = None):
  if not hasattr(ImGui_DrawList_PathStroke, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PathStroke')
    ImGui_DrawList_PathStroke.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_int(col_rgba), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(thicknessInOptional) if thicknessInOptional != None else None)
  ImGui_DrawList_PathStroke.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None)

def ImGui_DrawList_PopClipRect(draw_list):
  if not hasattr(ImGui_DrawList_PopClipRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PopClipRect')
    ImGui_DrawList_PopClipRect.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list),)
  ImGui_DrawList_PopClipRect.func(args[0])

def ImGui_DrawList_PushClipRect(draw_list, clip_rect_min_x, clip_rect_min_y, clip_rect_max_x, clip_rect_max_y, intersect_with_current_clip_rectInOptional = None):
  if not hasattr(ImGui_DrawList_PushClipRect, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PushClipRect')
    ImGui_DrawList_PushClipRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list), c_double(clip_rect_min_x), c_double(clip_rect_min_y), c_double(clip_rect_max_x), c_double(clip_rect_max_y), c_bool(intersect_with_current_clip_rectInOptional) if intersect_with_current_clip_rectInOptional != None else None)
  ImGui_DrawList_PushClipRect.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)

def ImGui_DrawList_PushClipRectFullScreen(draw_list):
  if not hasattr(ImGui_DrawList_PushClipRectFullScreen, 'func'):
    proc = rpr_getfp('ImGui_DrawList_PushClipRectFullScreen')
    ImGui_DrawList_PushClipRectFullScreen.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_DrawList*', draw_list),)
  ImGui_DrawList_PushClipRectFullScreen.func(args[0])

def ImGui_Dummy(ctx, size_w, size_h):
  if not hasattr(ImGui_Dummy, 'func'):
    proc = rpr_getfp('ImGui_Dummy')
    ImGui_Dummy.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(size_w), c_double(size_h))
  ImGui_Dummy.func(args[0], args[1], args[2])

def ImGui_End(ctx):
  if not hasattr(ImGui_End, 'func'):
    proc = rpr_getfp('ImGui_End')
    ImGui_End.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_End.func(args[0])

def ImGui_EndChild(ctx):
  if not hasattr(ImGui_EndChild, 'func'):
    proc = rpr_getfp('ImGui_EndChild')
    ImGui_EndChild.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndChild.func(args[0])

def ImGui_EndChildFrame(ctx):
  if not hasattr(ImGui_EndChildFrame, 'func'):
    proc = rpr_getfp('ImGui_EndChildFrame')
    ImGui_EndChildFrame.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndChildFrame.func(args[0])

def ImGui_EndCombo(ctx):
  if not hasattr(ImGui_EndCombo, 'func'):
    proc = rpr_getfp('ImGui_EndCombo')
    ImGui_EndCombo.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndCombo.func(args[0])

def ImGui_EndDisabled(ctx):
  if not hasattr(ImGui_EndDisabled, 'func'):
    proc = rpr_getfp('ImGui_EndDisabled')
    ImGui_EndDisabled.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndDisabled.func(args[0])

def ImGui_EndDragDropSource(ctx):
  if not hasattr(ImGui_EndDragDropSource, 'func'):
    proc = rpr_getfp('ImGui_EndDragDropSource')
    ImGui_EndDragDropSource.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndDragDropSource.func(args[0])

def ImGui_EndDragDropTarget(ctx):
  if not hasattr(ImGui_EndDragDropTarget, 'func'):
    proc = rpr_getfp('ImGui_EndDragDropTarget')
    ImGui_EndDragDropTarget.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndDragDropTarget.func(args[0])

def ImGui_EndGroup(ctx):
  if not hasattr(ImGui_EndGroup, 'func'):
    proc = rpr_getfp('ImGui_EndGroup')
    ImGui_EndGroup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndGroup.func(args[0])

def ImGui_EndListBox(ctx):
  if not hasattr(ImGui_EndListBox, 'func'):
    proc = rpr_getfp('ImGui_EndListBox')
    ImGui_EndListBox.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndListBox.func(args[0])

def ImGui_EndMenu(ctx):
  if not hasattr(ImGui_EndMenu, 'func'):
    proc = rpr_getfp('ImGui_EndMenu')
    ImGui_EndMenu.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndMenu.func(args[0])

def ImGui_EndMenuBar(ctx):
  if not hasattr(ImGui_EndMenuBar, 'func'):
    proc = rpr_getfp('ImGui_EndMenuBar')
    ImGui_EndMenuBar.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndMenuBar.func(args[0])

def ImGui_EndPopup(ctx):
  if not hasattr(ImGui_EndPopup, 'func'):
    proc = rpr_getfp('ImGui_EndPopup')
    ImGui_EndPopup.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndPopup.func(args[0])

def ImGui_EndTabBar(ctx):
  if not hasattr(ImGui_EndTabBar, 'func'):
    proc = rpr_getfp('ImGui_EndTabBar')
    ImGui_EndTabBar.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndTabBar.func(args[0])

def ImGui_EndTabItem(ctx):
  if not hasattr(ImGui_EndTabItem, 'func'):
    proc = rpr_getfp('ImGui_EndTabItem')
    ImGui_EndTabItem.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndTabItem.func(args[0])

def ImGui_EndTable(ctx):
  if not hasattr(ImGui_EndTable, 'func'):
    proc = rpr_getfp('ImGui_EndTable')
    ImGui_EndTable.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndTable.func(args[0])

def ImGui_EndTooltip(ctx):
  if not hasattr(ImGui_EndTooltip, 'func'):
    proc = rpr_getfp('ImGui_EndTooltip')
    ImGui_EndTooltip.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_EndTooltip.func(args[0])

def ImGui_FocusedFlags_AnyWindow():
  if not hasattr(ImGui_FocusedFlags_AnyWindow, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_AnyWindow')
    ImGui_FocusedFlags_AnyWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_AnyWindow, 'cache'):
    ImGui_FocusedFlags_AnyWindow.cache = ImGui_FocusedFlags_AnyWindow.func()
  return ImGui_FocusedFlags_AnyWindow.cache

def ImGui_FocusedFlags_ChildWindows():
  if not hasattr(ImGui_FocusedFlags_ChildWindows, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_ChildWindows')
    ImGui_FocusedFlags_ChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_ChildWindows, 'cache'):
    ImGui_FocusedFlags_ChildWindows.cache = ImGui_FocusedFlags_ChildWindows.func()
  return ImGui_FocusedFlags_ChildWindows.cache

def ImGui_FocusedFlags_DockHierarchy():
  if not hasattr(ImGui_FocusedFlags_DockHierarchy, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_DockHierarchy')
    ImGui_FocusedFlags_DockHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_DockHierarchy, 'cache'):
    ImGui_FocusedFlags_DockHierarchy.cache = ImGui_FocusedFlags_DockHierarchy.func()
  return ImGui_FocusedFlags_DockHierarchy.cache

def ImGui_FocusedFlags_NoPopupHierarchy():
  if not hasattr(ImGui_FocusedFlags_NoPopupHierarchy, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_NoPopupHierarchy')
    ImGui_FocusedFlags_NoPopupHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_NoPopupHierarchy, 'cache'):
    ImGui_FocusedFlags_NoPopupHierarchy.cache = ImGui_FocusedFlags_NoPopupHierarchy.func()
  return ImGui_FocusedFlags_NoPopupHierarchy.cache

def ImGui_FocusedFlags_None():
  if not hasattr(ImGui_FocusedFlags_None, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_None')
    ImGui_FocusedFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_None, 'cache'):
    ImGui_FocusedFlags_None.cache = ImGui_FocusedFlags_None.func()
  return ImGui_FocusedFlags_None.cache

def ImGui_FocusedFlags_RootAndChildWindows():
  if not hasattr(ImGui_FocusedFlags_RootAndChildWindows, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_RootAndChildWindows')
    ImGui_FocusedFlags_RootAndChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_RootAndChildWindows, 'cache'):
    ImGui_FocusedFlags_RootAndChildWindows.cache = ImGui_FocusedFlags_RootAndChildWindows.func()
  return ImGui_FocusedFlags_RootAndChildWindows.cache

def ImGui_FocusedFlags_RootWindow():
  if not hasattr(ImGui_FocusedFlags_RootWindow, 'func'):
    proc = rpr_getfp('ImGui_FocusedFlags_RootWindow')
    ImGui_FocusedFlags_RootWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FocusedFlags_RootWindow, 'cache'):
    ImGui_FocusedFlags_RootWindow.cache = ImGui_FocusedFlags_RootWindow.func()
  return ImGui_FocusedFlags_RootWindow.cache

def ImGui_FontFlags_Bold():
  if not hasattr(ImGui_FontFlags_Bold, 'func'):
    proc = rpr_getfp('ImGui_FontFlags_Bold')
    ImGui_FontFlags_Bold.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FontFlags_Bold, 'cache'):
    ImGui_FontFlags_Bold.cache = ImGui_FontFlags_Bold.func()
  return ImGui_FontFlags_Bold.cache

def ImGui_FontFlags_Italic():
  if not hasattr(ImGui_FontFlags_Italic, 'func'):
    proc = rpr_getfp('ImGui_FontFlags_Italic')
    ImGui_FontFlags_Italic.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FontFlags_Italic, 'cache'):
    ImGui_FontFlags_Italic.cache = ImGui_FontFlags_Italic.func()
  return ImGui_FontFlags_Italic.cache

def ImGui_FontFlags_None():
  if not hasattr(ImGui_FontFlags_None, 'func'):
    proc = rpr_getfp('ImGui_FontFlags_None')
    ImGui_FontFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_FontFlags_None, 'cache'):
    ImGui_FontFlags_None.cache = ImGui_FontFlags_None.func()
  return ImGui_FontFlags_None.cache

def ImGui_GetBackgroundDrawList(ctx):
  if not hasattr(ImGui_GetBackgroundDrawList, 'func'):
    proc = rpr_getfp('ImGui_GetBackgroundDrawList')
    ImGui_GetBackgroundDrawList.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetBackgroundDrawList.func(args[0])
  return rpr_unpackp('ImGui_DrawList*', rval)

def ImGui_GetClipboardText(ctx):
  if not hasattr(ImGui_GetClipboardText, 'func'):
    proc = rpr_getfp('ImGui_GetClipboardText')
    ImGui_GetClipboardText.func = CFUNCTYPE(c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetClipboardText.func(args[0])
  return str(rval.decode())

def ImGui_GetColor(ctx, idx, alpha_mulInOptional = None):
  if not hasattr(ImGui_GetColor, 'func'):
    proc = rpr_getfp('ImGui_GetColor')
    ImGui_GetColor.func = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(idx), c_double(alpha_mulInOptional) if alpha_mulInOptional != None else None)
  rval = ImGui_GetColor.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_GetColorEx(ctx, col_rgba):
  if not hasattr(ImGui_GetColorEx, 'func'):
    proc = rpr_getfp('ImGui_GetColorEx')
    ImGui_GetColorEx.func = CFUNCTYPE(c_int, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(col_rgba))
  rval = ImGui_GetColorEx.func(args[0], args[1])
  return rval

def ImGui_GetConfigVar(ctx, var_idx):
  if not hasattr(ImGui_GetConfigVar, 'func'):
    proc = rpr_getfp('ImGui_GetConfigVar')
    ImGui_GetConfigVar.func = CFUNCTYPE(c_double, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(var_idx))
  rval = ImGui_GetConfigVar.func(args[0], args[1])
  return rval

def ImGui_GetContentRegionAvail(ctx):
  if not hasattr(ImGui_GetContentRegionAvail, 'func'):
    proc = rpr_getfp('ImGui_GetContentRegionAvail')
    ImGui_GetContentRegionAvail.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetContentRegionAvail.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetContentRegionMax(ctx):
  if not hasattr(ImGui_GetContentRegionMax, 'func'):
    proc = rpr_getfp('ImGui_GetContentRegionMax')
    ImGui_GetContentRegionMax.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetContentRegionMax.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetCursorPos(ctx):
  if not hasattr(ImGui_GetCursorPos, 'func'):
    proc = rpr_getfp('ImGui_GetCursorPos')
    ImGui_GetCursorPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetCursorPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetCursorPosX(ctx):
  if not hasattr(ImGui_GetCursorPosX, 'func'):
    proc = rpr_getfp('ImGui_GetCursorPosX')
    ImGui_GetCursorPosX.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetCursorPosX.func(args[0])
  return rval

def ImGui_GetCursorPosY(ctx):
  if not hasattr(ImGui_GetCursorPosY, 'func'):
    proc = rpr_getfp('ImGui_GetCursorPosY')
    ImGui_GetCursorPosY.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetCursorPosY.func(args[0])
  return rval

def ImGui_GetCursorScreenPos(ctx):
  if not hasattr(ImGui_GetCursorScreenPos, 'func'):
    proc = rpr_getfp('ImGui_GetCursorScreenPos')
    ImGui_GetCursorScreenPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetCursorScreenPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetCursorStartPos(ctx):
  if not hasattr(ImGui_GetCursorStartPos, 'func'):
    proc = rpr_getfp('ImGui_GetCursorStartPos')
    ImGui_GetCursorStartPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetCursorStartPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetDeltaTime(ctx):
  if not hasattr(ImGui_GetDeltaTime, 'func'):
    proc = rpr_getfp('ImGui_GetDeltaTime')
    ImGui_GetDeltaTime.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetDeltaTime.func(args[0])
  return rval

def ImGui_GetDragDropPayload(ctx):
  if not hasattr(ImGui_GetDragDropPayload, 'func'):
    proc = rpr_getfp('ImGui_GetDragDropPayload')
    ImGui_GetDragDropPayload.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_int, c_char_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packs(0), c_int(1024), rpr_packs(0), c_int(4096), c_bool(0), c_bool(0))
  rval = ImGui_GetDragDropPayload.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]), byref(args[6]))
  return rval, rpr_unpacks(args[1]), rpr_unpacks(args[3]), int(args[5].value), int(args[6].value)

def ImGui_GetDragDropPayloadFile(ctx, index):
  if not hasattr(ImGui_GetDragDropPayloadFile, 'func'):
    proc = rpr_getfp('ImGui_GetDragDropPayloadFile')
    ImGui_GetDragDropPayloadFile.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_char_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(index), rpr_packs(0), c_int(1024))
  rval = ImGui_GetDragDropPayloadFile.func(args[0], args[1], args[2], args[3])
  return rval, rpr_unpacks(args[2])

def ImGui_GetFont(ctx):
  if not hasattr(ImGui_GetFont, 'func'):
    proc = rpr_getfp('ImGui_GetFont')
    ImGui_GetFont.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetFont.func(args[0])
  return rpr_unpackp('ImGui_Font*', rval)

def ImGui_GetFontSize(ctx):
  if not hasattr(ImGui_GetFontSize, 'func'):
    proc = rpr_getfp('ImGui_GetFontSize')
    ImGui_GetFontSize.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetFontSize.func(args[0])
  return rval

def ImGui_GetForegroundDrawList(ctx):
  if not hasattr(ImGui_GetForegroundDrawList, 'func'):
    proc = rpr_getfp('ImGui_GetForegroundDrawList')
    ImGui_GetForegroundDrawList.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetForegroundDrawList.func(args[0])
  return rpr_unpackp('ImGui_DrawList*', rval)

def ImGui_GetFrameCount(ctx):
  if not hasattr(ImGui_GetFrameCount, 'func'):
    proc = rpr_getfp('ImGui_GetFrameCount')
    ImGui_GetFrameCount.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetFrameCount.func(args[0])
  return rval

def ImGui_GetFrameHeight(ctx):
  if not hasattr(ImGui_GetFrameHeight, 'func'):
    proc = rpr_getfp('ImGui_GetFrameHeight')
    ImGui_GetFrameHeight.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetFrameHeight.func(args[0])
  return rval

def ImGui_GetFrameHeightWithSpacing(ctx):
  if not hasattr(ImGui_GetFrameHeightWithSpacing, 'func'):
    proc = rpr_getfp('ImGui_GetFrameHeightWithSpacing')
    ImGui_GetFrameHeightWithSpacing.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetFrameHeightWithSpacing.func(args[0])
  return rval

def ImGui_GetInputQueueCharacter(ctx, idx):
  if not hasattr(ImGui_GetInputQueueCharacter, 'func'):
    proc = rpr_getfp('ImGui_GetInputQueueCharacter')
    ImGui_GetInputQueueCharacter.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(idx), c_int(0))
  rval = ImGui_GetInputQueueCharacter.func(args[0], args[1], byref(args[2]))
  return rval, int(args[2].value)

def ImGui_GetItemRectMax(ctx):
  if not hasattr(ImGui_GetItemRectMax, 'func'):
    proc = rpr_getfp('ImGui_GetItemRectMax')
    ImGui_GetItemRectMax.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetItemRectMax.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetItemRectMin(ctx):
  if not hasattr(ImGui_GetItemRectMin, 'func'):
    proc = rpr_getfp('ImGui_GetItemRectMin')
    ImGui_GetItemRectMin.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetItemRectMin.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetItemRectSize(ctx):
  if not hasattr(ImGui_GetItemRectSize, 'func'):
    proc = rpr_getfp('ImGui_GetItemRectSize')
    ImGui_GetItemRectSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetItemRectSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetKeyDownDuration(ctx, key):
  if not hasattr(ImGui_GetKeyDownDuration, 'func'):
    proc = rpr_getfp('ImGui_GetKeyDownDuration')
    ImGui_GetKeyDownDuration.func = CFUNCTYPE(c_double, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(key))
  rval = ImGui_GetKeyDownDuration.func(args[0], args[1])
  return rval

def ImGui_GetKeyMods(ctx):
  if not hasattr(ImGui_GetKeyMods, 'func'):
    proc = rpr_getfp('ImGui_GetKeyMods')
    ImGui_GetKeyMods.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetKeyMods.func(args[0])
  return rval

def ImGui_GetKeyPressedAmount(ctx, key, repeat_delay, rate):
  if not hasattr(ImGui_GetKeyPressedAmount, 'func'):
    proc = rpr_getfp('ImGui_GetKeyPressedAmount')
    ImGui_GetKeyPressedAmount.func = CFUNCTYPE(c_int, c_void_p, c_int, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(key), c_double(repeat_delay), c_double(rate))
  rval = ImGui_GetKeyPressedAmount.func(args[0], args[1], args[2], args[3])
  return rval

def ImGui_GetMainViewport(ctx):
  if not hasattr(ImGui_GetMainViewport, 'func'):
    proc = rpr_getfp('ImGui_GetMainViewport')
    ImGui_GetMainViewport.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetMainViewport.func(args[0])
  return rpr_unpackp('ImGui_Viewport*', rval)

def ImGui_GetMouseClickedCount(ctx, button):
  if not hasattr(ImGui_GetMouseClickedCount, 'func'):
    proc = rpr_getfp('ImGui_GetMouseClickedCount')
    ImGui_GetMouseClickedCount.func = CFUNCTYPE(c_int, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button))
  rval = ImGui_GetMouseClickedCount.func(args[0], args[1])
  return rval

def ImGui_GetMouseClickedPos(ctx, button):
  if not hasattr(ImGui_GetMouseClickedPos, 'func'):
    proc = rpr_getfp('ImGui_GetMouseClickedPos')
    ImGui_GetMouseClickedPos.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button), c_double(0), c_double(0))
  ImGui_GetMouseClickedPos.func(args[0], args[1], byref(args[2]), byref(args[3]))
  return float(args[2].value), float(args[3].value)

def ImGui_GetMouseCursor(ctx):
  if not hasattr(ImGui_GetMouseCursor, 'func'):
    proc = rpr_getfp('ImGui_GetMouseCursor')
    ImGui_GetMouseCursor.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetMouseCursor.func(args[0])
  return rval

def ImGui_GetMouseDelta(ctx):
  if not hasattr(ImGui_GetMouseDelta, 'func'):
    proc = rpr_getfp('ImGui_GetMouseDelta')
    ImGui_GetMouseDelta.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetMouseDelta.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetMouseDownDuration(ctx, button):
  if not hasattr(ImGui_GetMouseDownDuration, 'func'):
    proc = rpr_getfp('ImGui_GetMouseDownDuration')
    ImGui_GetMouseDownDuration.func = CFUNCTYPE(c_double, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button))
  rval = ImGui_GetMouseDownDuration.func(args[0], args[1])
  return rval

def ImGui_GetMouseDragDelta(ctx, buttonInOptional = None, lock_thresholdInOptional = None):
  if not hasattr(ImGui_GetMouseDragDelta, 'func'):
    proc = rpr_getfp('ImGui_GetMouseDragDelta')
    ImGui_GetMouseDragDelta.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0), c_int(buttonInOptional) if buttonInOptional != None else None, c_double(lock_thresholdInOptional) if lock_thresholdInOptional != None else None)
  ImGui_GetMouseDragDelta.func(args[0], byref(args[1]), byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)
  return float(args[1].value), float(args[2].value)

def ImGui_GetMousePos(ctx):
  if not hasattr(ImGui_GetMousePos, 'func'):
    proc = rpr_getfp('ImGui_GetMousePos')
    ImGui_GetMousePos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetMousePos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetMousePosOnOpeningCurrentPopup(ctx):
  if not hasattr(ImGui_GetMousePosOnOpeningCurrentPopup, 'func'):
    proc = rpr_getfp('ImGui_GetMousePosOnOpeningCurrentPopup')
    ImGui_GetMousePosOnOpeningCurrentPopup.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetMousePosOnOpeningCurrentPopup.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetMouseWheel(ctx):
  if not hasattr(ImGui_GetMouseWheel, 'func'):
    proc = rpr_getfp('ImGui_GetMouseWheel')
    ImGui_GetMouseWheel.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetMouseWheel.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetScrollMaxX(ctx):
  if not hasattr(ImGui_GetScrollMaxX, 'func'):
    proc = rpr_getfp('ImGui_GetScrollMaxX')
    ImGui_GetScrollMaxX.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetScrollMaxX.func(args[0])
  return rval

def ImGui_GetScrollMaxY(ctx):
  if not hasattr(ImGui_GetScrollMaxY, 'func'):
    proc = rpr_getfp('ImGui_GetScrollMaxY')
    ImGui_GetScrollMaxY.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetScrollMaxY.func(args[0])
  return rval

def ImGui_GetScrollX(ctx):
  if not hasattr(ImGui_GetScrollX, 'func'):
    proc = rpr_getfp('ImGui_GetScrollX')
    ImGui_GetScrollX.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetScrollX.func(args[0])
  return rval

def ImGui_GetScrollY(ctx):
  if not hasattr(ImGui_GetScrollY, 'func'):
    proc = rpr_getfp('ImGui_GetScrollY')
    ImGui_GetScrollY.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetScrollY.func(args[0])
  return rval

def ImGui_GetStyleColor(ctx, idx):
  if not hasattr(ImGui_GetStyleColor, 'func'):
    proc = rpr_getfp('ImGui_GetStyleColor')
    ImGui_GetStyleColor.func = CFUNCTYPE(c_int, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(idx))
  rval = ImGui_GetStyleColor.func(args[0], args[1])
  return rval

def ImGui_GetStyleVar(ctx, var_idx):
  if not hasattr(ImGui_GetStyleVar, 'func'):
    proc = rpr_getfp('ImGui_GetStyleVar')
    ImGui_GetStyleVar.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(var_idx), c_double(0), c_double(0))
  ImGui_GetStyleVar.func(args[0], args[1], byref(args[2]), byref(args[3]))
  return float(args[2].value), float(args[3].value)

def ImGui_GetTextLineHeight(ctx):
  if not hasattr(ImGui_GetTextLineHeight, 'func'):
    proc = rpr_getfp('ImGui_GetTextLineHeight')
    ImGui_GetTextLineHeight.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetTextLineHeight.func(args[0])
  return rval

def ImGui_GetTextLineHeightWithSpacing(ctx):
  if not hasattr(ImGui_GetTextLineHeightWithSpacing, 'func'):
    proc = rpr_getfp('ImGui_GetTextLineHeightWithSpacing')
    ImGui_GetTextLineHeightWithSpacing.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetTextLineHeightWithSpacing.func(args[0])
  return rval

def ImGui_GetTime(ctx):
  if not hasattr(ImGui_GetTime, 'func'):
    proc = rpr_getfp('ImGui_GetTime')
    ImGui_GetTime.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetTime.func(args[0])
  return rval

def ImGui_GetTreeNodeToLabelSpacing(ctx):
  if not hasattr(ImGui_GetTreeNodeToLabelSpacing, 'func'):
    proc = rpr_getfp('ImGui_GetTreeNodeToLabelSpacing')
    ImGui_GetTreeNodeToLabelSpacing.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetTreeNodeToLabelSpacing.func(args[0])
  return rval

def ImGui_GetVersion():
  if not hasattr(ImGui_GetVersion, 'func'):
    proc = rpr_getfp('ImGui_GetVersion')
    ImGui_GetVersion.func = CFUNCTYPE(None, c_char_p, c_int, c_void_p, c_char_p, c_int)(proc)
  args = (rpr_packs(0), c_int(1024), c_int(0), rpr_packs(0), c_int(1024))
  ImGui_GetVersion.func(args[0], args[1], byref(args[2]), args[3], args[4])
  return rpr_unpacks(args[0]), int(args[2].value), rpr_unpacks(args[3])

def ImGui_GetWindowContentRegionMax(ctx):
  if not hasattr(ImGui_GetWindowContentRegionMax, 'func'):
    proc = rpr_getfp('ImGui_GetWindowContentRegionMax')
    ImGui_GetWindowContentRegionMax.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetWindowContentRegionMax.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetWindowContentRegionMin(ctx):
  if not hasattr(ImGui_GetWindowContentRegionMin, 'func'):
    proc = rpr_getfp('ImGui_GetWindowContentRegionMin')
    ImGui_GetWindowContentRegionMin.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetWindowContentRegionMin.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetWindowDockID(ctx):
  if not hasattr(ImGui_GetWindowDockID, 'func'):
    proc = rpr_getfp('ImGui_GetWindowDockID')
    ImGui_GetWindowDockID.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetWindowDockID.func(args[0])
  return rval

def ImGui_GetWindowDrawList(ctx):
  if not hasattr(ImGui_GetWindowDrawList, 'func'):
    proc = rpr_getfp('ImGui_GetWindowDrawList')
    ImGui_GetWindowDrawList.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetWindowDrawList.func(args[0])
  return rpr_unpackp('ImGui_DrawList*', rval)

def ImGui_GetWindowHeight(ctx):
  if not hasattr(ImGui_GetWindowHeight, 'func'):
    proc = rpr_getfp('ImGui_GetWindowHeight')
    ImGui_GetWindowHeight.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetWindowHeight.func(args[0])
  return rval

def ImGui_GetWindowPos(ctx):
  if not hasattr(ImGui_GetWindowPos, 'func'):
    proc = rpr_getfp('ImGui_GetWindowPos')
    ImGui_GetWindowPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetWindowPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetWindowSize(ctx):
  if not hasattr(ImGui_GetWindowSize, 'func'):
    proc = rpr_getfp('ImGui_GetWindowSize')
    ImGui_GetWindowSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(0), c_double(0))
  ImGui_GetWindowSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_GetWindowViewport(ctx):
  if not hasattr(ImGui_GetWindowViewport, 'func'):
    proc = rpr_getfp('ImGui_GetWindowViewport')
    ImGui_GetWindowViewport.func = CFUNCTYPE(c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetWindowViewport.func(args[0])
  return rpr_unpackp('ImGui_Viewport*', rval)

def ImGui_GetWindowWidth(ctx):
  if not hasattr(ImGui_GetWindowWidth, 'func'):
    proc = rpr_getfp('ImGui_GetWindowWidth')
    ImGui_GetWindowWidth.func = CFUNCTYPE(c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_GetWindowWidth.func(args[0])
  return rval

def ImGui_HoveredFlags_AllowWhenBlockedByActiveItem():
  if not hasattr(ImGui_HoveredFlags_AllowWhenBlockedByActiveItem, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenBlockedByActiveItem')
    ImGui_HoveredFlags_AllowWhenBlockedByActiveItem.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_AllowWhenBlockedByActiveItem, 'cache'):
    ImGui_HoveredFlags_AllowWhenBlockedByActiveItem.cache = ImGui_HoveredFlags_AllowWhenBlockedByActiveItem.func()
  return ImGui_HoveredFlags_AllowWhenBlockedByActiveItem.cache

def ImGui_HoveredFlags_AllowWhenBlockedByPopup():
  if not hasattr(ImGui_HoveredFlags_AllowWhenBlockedByPopup, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenBlockedByPopup')
    ImGui_HoveredFlags_AllowWhenBlockedByPopup.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_AllowWhenBlockedByPopup, 'cache'):
    ImGui_HoveredFlags_AllowWhenBlockedByPopup.cache = ImGui_HoveredFlags_AllowWhenBlockedByPopup.func()
  return ImGui_HoveredFlags_AllowWhenBlockedByPopup.cache

def ImGui_HoveredFlags_AllowWhenDisabled():
  if not hasattr(ImGui_HoveredFlags_AllowWhenDisabled, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenDisabled')
    ImGui_HoveredFlags_AllowWhenDisabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_AllowWhenDisabled, 'cache'):
    ImGui_HoveredFlags_AllowWhenDisabled.cache = ImGui_HoveredFlags_AllowWhenDisabled.func()
  return ImGui_HoveredFlags_AllowWhenDisabled.cache

def ImGui_HoveredFlags_AllowWhenOverlapped():
  if not hasattr(ImGui_HoveredFlags_AllowWhenOverlapped, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AllowWhenOverlapped')
    ImGui_HoveredFlags_AllowWhenOverlapped.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_AllowWhenOverlapped, 'cache'):
    ImGui_HoveredFlags_AllowWhenOverlapped.cache = ImGui_HoveredFlags_AllowWhenOverlapped.func()
  return ImGui_HoveredFlags_AllowWhenOverlapped.cache

def ImGui_HoveredFlags_AnyWindow():
  if not hasattr(ImGui_HoveredFlags_AnyWindow, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_AnyWindow')
    ImGui_HoveredFlags_AnyWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_AnyWindow, 'cache'):
    ImGui_HoveredFlags_AnyWindow.cache = ImGui_HoveredFlags_AnyWindow.func()
  return ImGui_HoveredFlags_AnyWindow.cache

def ImGui_HoveredFlags_ChildWindows():
  if not hasattr(ImGui_HoveredFlags_ChildWindows, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_ChildWindows')
    ImGui_HoveredFlags_ChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_ChildWindows, 'cache'):
    ImGui_HoveredFlags_ChildWindows.cache = ImGui_HoveredFlags_ChildWindows.func()
  return ImGui_HoveredFlags_ChildWindows.cache

def ImGui_HoveredFlags_DockHierarchy():
  if not hasattr(ImGui_HoveredFlags_DockHierarchy, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_DockHierarchy')
    ImGui_HoveredFlags_DockHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_DockHierarchy, 'cache'):
    ImGui_HoveredFlags_DockHierarchy.cache = ImGui_HoveredFlags_DockHierarchy.func()
  return ImGui_HoveredFlags_DockHierarchy.cache

def ImGui_HoveredFlags_NoNavOverride():
  if not hasattr(ImGui_HoveredFlags_NoNavOverride, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_NoNavOverride')
    ImGui_HoveredFlags_NoNavOverride.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_NoNavOverride, 'cache'):
    ImGui_HoveredFlags_NoNavOverride.cache = ImGui_HoveredFlags_NoNavOverride.func()
  return ImGui_HoveredFlags_NoNavOverride.cache

def ImGui_HoveredFlags_NoPopupHierarchy():
  if not hasattr(ImGui_HoveredFlags_NoPopupHierarchy, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_NoPopupHierarchy')
    ImGui_HoveredFlags_NoPopupHierarchy.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_NoPopupHierarchy, 'cache'):
    ImGui_HoveredFlags_NoPopupHierarchy.cache = ImGui_HoveredFlags_NoPopupHierarchy.func()
  return ImGui_HoveredFlags_NoPopupHierarchy.cache

def ImGui_HoveredFlags_None():
  if not hasattr(ImGui_HoveredFlags_None, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_None')
    ImGui_HoveredFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_None, 'cache'):
    ImGui_HoveredFlags_None.cache = ImGui_HoveredFlags_None.func()
  return ImGui_HoveredFlags_None.cache

def ImGui_HoveredFlags_RectOnly():
  if not hasattr(ImGui_HoveredFlags_RectOnly, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_RectOnly')
    ImGui_HoveredFlags_RectOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_RectOnly, 'cache'):
    ImGui_HoveredFlags_RectOnly.cache = ImGui_HoveredFlags_RectOnly.func()
  return ImGui_HoveredFlags_RectOnly.cache

def ImGui_HoveredFlags_RootAndChildWindows():
  if not hasattr(ImGui_HoveredFlags_RootAndChildWindows, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_RootAndChildWindows')
    ImGui_HoveredFlags_RootAndChildWindows.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_RootAndChildWindows, 'cache'):
    ImGui_HoveredFlags_RootAndChildWindows.cache = ImGui_HoveredFlags_RootAndChildWindows.func()
  return ImGui_HoveredFlags_RootAndChildWindows.cache

def ImGui_HoveredFlags_RootWindow():
  if not hasattr(ImGui_HoveredFlags_RootWindow, 'func'):
    proc = rpr_getfp('ImGui_HoveredFlags_RootWindow')
    ImGui_HoveredFlags_RootWindow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_HoveredFlags_RootWindow, 'cache'):
    ImGui_HoveredFlags_RootWindow.cache = ImGui_HoveredFlags_RootWindow.func()
  return ImGui_HoveredFlags_RootWindow.cache

def ImGui_Indent(ctx, indent_wInOptional = None):
  if not hasattr(ImGui_Indent, 'func'):
    proc = rpr_getfp('ImGui_Indent')
    ImGui_Indent.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(indent_wInOptional) if indent_wInOptional != None else None)
  ImGui_Indent.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_InputDouble(ctx, label, vInOut, stepInOptional = None, step_fastInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputDouble, 'func'):
    proc = rpr_getfp('ImGui_InputDouble')
    ImGui_InputDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(vInOut), c_double(stepInOptional) if stepInOptional != None else None, c_double(step_fastInOptional) if step_fastInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputDouble.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value)

def ImGui_InputDouble2(ctx, label, v1InOut, v2InOut, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputDouble2, 'func'):
    proc = rpr_getfp('ImGui_InputDouble2')
    ImGui_InputDouble2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputDouble2.func(args[0], args[1], byref(args[2]), byref(args[3]), args[4], byref(args[5]) if args[5] != None else None)
  return rval, float(args[2].value), float(args[3].value)

def ImGui_InputDouble3(ctx, label, v1InOut, v2InOut, v3InOut, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputDouble3, 'func'):
    proc = rpr_getfp('ImGui_InputDouble3')
    ImGui_InputDouble3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputDouble3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value)

def ImGui_InputDouble4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputDouble4, 'func'):
    proc = rpr_getfp('ImGui_InputDouble4')
    ImGui_InputDouble4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v4InOut), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputDouble4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), args[6], byref(args[7]) if args[7] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value), float(args[5].value)

def ImGui_InputDoubleN(ctx, label, values, stepInOptional = None, step_fastInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputDoubleN, 'func'):
    proc = rpr_getfp('ImGui_InputDoubleN')
    ImGui_InputDoubleN.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_double(stepInOptional) if stepInOptional != None else None, c_double(step_fastInOptional) if step_fastInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputDoubleN.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, args[5], byref(args[6]) if args[6] != None else None)
  return rval

def ImGui_InputInt(ctx, label, vInOut, stepInOptional = None, step_fastInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputInt, 'func'):
    proc = rpr_getfp('ImGui_InputInt')
    ImGui_InputInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(vInOut), c_int(stepInOptional) if stepInOptional != None else None, c_int(step_fastInOptional) if step_fastInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputInt.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value)

def ImGui_InputInt2(ctx, label, v1InOut, v2InOut, flagsInOptional = None):
  if not hasattr(ImGui_InputInt2, 'func'):
    proc = rpr_getfp('ImGui_InputInt2')
    ImGui_InputInt2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputInt2.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]) if args[4] != None else None)
  return rval, int(args[2].value), int(args[3].value)

def ImGui_InputInt3(ctx, label, v1InOut, v2InOut, v3InOut, flagsInOptional = None):
  if not hasattr(ImGui_InputInt3, 'func'):
    proc = rpr_getfp('ImGui_InputInt3')
    ImGui_InputInt3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputInt3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value)

def ImGui_InputInt4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, flagsInOptional = None):
  if not hasattr(ImGui_InputInt4, 'func'):
    proc = rpr_getfp('ImGui_InputInt4')
    ImGui_InputInt4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v4InOut), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputInt4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), byref(args[6]) if args[6] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

def ImGui_InputText(ctx, label, bufInOutNeedBig, flagsInOptional = None):
  if not hasattr(ImGui_InputText, 'func'):
    proc = rpr_getfp('ImGui_InputText')
    ImGui_InputText.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packs(bufInOutNeedBig), c_int(4096), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputText.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval, rpr_unpacks(args[2])

def ImGui_InputTextFlags_AllowTabInput():
  if not hasattr(ImGui_InputTextFlags_AllowTabInput, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_AllowTabInput')
    ImGui_InputTextFlags_AllowTabInput.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_AllowTabInput, 'cache'):
    ImGui_InputTextFlags_AllowTabInput.cache = ImGui_InputTextFlags_AllowTabInput.func()
  return ImGui_InputTextFlags_AllowTabInput.cache

def ImGui_InputTextFlags_AlwaysOverwrite():
  if not hasattr(ImGui_InputTextFlags_AlwaysOverwrite, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_AlwaysOverwrite')
    ImGui_InputTextFlags_AlwaysOverwrite.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_AlwaysOverwrite, 'cache'):
    ImGui_InputTextFlags_AlwaysOverwrite.cache = ImGui_InputTextFlags_AlwaysOverwrite.func()
  return ImGui_InputTextFlags_AlwaysOverwrite.cache

def ImGui_InputTextFlags_AutoSelectAll():
  if not hasattr(ImGui_InputTextFlags_AutoSelectAll, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_AutoSelectAll')
    ImGui_InputTextFlags_AutoSelectAll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_AutoSelectAll, 'cache'):
    ImGui_InputTextFlags_AutoSelectAll.cache = ImGui_InputTextFlags_AutoSelectAll.func()
  return ImGui_InputTextFlags_AutoSelectAll.cache

def ImGui_InputTextFlags_CharsDecimal():
  if not hasattr(ImGui_InputTextFlags_CharsDecimal, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsDecimal')
    ImGui_InputTextFlags_CharsDecimal.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_CharsDecimal, 'cache'):
    ImGui_InputTextFlags_CharsDecimal.cache = ImGui_InputTextFlags_CharsDecimal.func()
  return ImGui_InputTextFlags_CharsDecimal.cache

def ImGui_InputTextFlags_CharsHexadecimal():
  if not hasattr(ImGui_InputTextFlags_CharsHexadecimal, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsHexadecimal')
    ImGui_InputTextFlags_CharsHexadecimal.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_CharsHexadecimal, 'cache'):
    ImGui_InputTextFlags_CharsHexadecimal.cache = ImGui_InputTextFlags_CharsHexadecimal.func()
  return ImGui_InputTextFlags_CharsHexadecimal.cache

def ImGui_InputTextFlags_CharsNoBlank():
  if not hasattr(ImGui_InputTextFlags_CharsNoBlank, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsNoBlank')
    ImGui_InputTextFlags_CharsNoBlank.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_CharsNoBlank, 'cache'):
    ImGui_InputTextFlags_CharsNoBlank.cache = ImGui_InputTextFlags_CharsNoBlank.func()
  return ImGui_InputTextFlags_CharsNoBlank.cache

def ImGui_InputTextFlags_CharsScientific():
  if not hasattr(ImGui_InputTextFlags_CharsScientific, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsScientific')
    ImGui_InputTextFlags_CharsScientific.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_CharsScientific, 'cache'):
    ImGui_InputTextFlags_CharsScientific.cache = ImGui_InputTextFlags_CharsScientific.func()
  return ImGui_InputTextFlags_CharsScientific.cache

def ImGui_InputTextFlags_CharsUppercase():
  if not hasattr(ImGui_InputTextFlags_CharsUppercase, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CharsUppercase')
    ImGui_InputTextFlags_CharsUppercase.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_CharsUppercase, 'cache'):
    ImGui_InputTextFlags_CharsUppercase.cache = ImGui_InputTextFlags_CharsUppercase.func()
  return ImGui_InputTextFlags_CharsUppercase.cache

def ImGui_InputTextFlags_CtrlEnterForNewLine():
  if not hasattr(ImGui_InputTextFlags_CtrlEnterForNewLine, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_CtrlEnterForNewLine')
    ImGui_InputTextFlags_CtrlEnterForNewLine.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_CtrlEnterForNewLine, 'cache'):
    ImGui_InputTextFlags_CtrlEnterForNewLine.cache = ImGui_InputTextFlags_CtrlEnterForNewLine.func()
  return ImGui_InputTextFlags_CtrlEnterForNewLine.cache

def ImGui_InputTextFlags_EnterReturnsTrue():
  if not hasattr(ImGui_InputTextFlags_EnterReturnsTrue, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_EnterReturnsTrue')
    ImGui_InputTextFlags_EnterReturnsTrue.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_EnterReturnsTrue, 'cache'):
    ImGui_InputTextFlags_EnterReturnsTrue.cache = ImGui_InputTextFlags_EnterReturnsTrue.func()
  return ImGui_InputTextFlags_EnterReturnsTrue.cache

def ImGui_InputTextFlags_NoHorizontalScroll():
  if not hasattr(ImGui_InputTextFlags_NoHorizontalScroll, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_NoHorizontalScroll')
    ImGui_InputTextFlags_NoHorizontalScroll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_NoHorizontalScroll, 'cache'):
    ImGui_InputTextFlags_NoHorizontalScroll.cache = ImGui_InputTextFlags_NoHorizontalScroll.func()
  return ImGui_InputTextFlags_NoHorizontalScroll.cache

def ImGui_InputTextFlags_NoUndoRedo():
  if not hasattr(ImGui_InputTextFlags_NoUndoRedo, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_NoUndoRedo')
    ImGui_InputTextFlags_NoUndoRedo.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_NoUndoRedo, 'cache'):
    ImGui_InputTextFlags_NoUndoRedo.cache = ImGui_InputTextFlags_NoUndoRedo.func()
  return ImGui_InputTextFlags_NoUndoRedo.cache

def ImGui_InputTextFlags_None():
  if not hasattr(ImGui_InputTextFlags_None, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_None')
    ImGui_InputTextFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_None, 'cache'):
    ImGui_InputTextFlags_None.cache = ImGui_InputTextFlags_None.func()
  return ImGui_InputTextFlags_None.cache

def ImGui_InputTextFlags_Password():
  if not hasattr(ImGui_InputTextFlags_Password, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_Password')
    ImGui_InputTextFlags_Password.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_Password, 'cache'):
    ImGui_InputTextFlags_Password.cache = ImGui_InputTextFlags_Password.func()
  return ImGui_InputTextFlags_Password.cache

def ImGui_InputTextFlags_ReadOnly():
  if not hasattr(ImGui_InputTextFlags_ReadOnly, 'func'):
    proc = rpr_getfp('ImGui_InputTextFlags_ReadOnly')
    ImGui_InputTextFlags_ReadOnly.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_InputTextFlags_ReadOnly, 'cache'):
    ImGui_InputTextFlags_ReadOnly.cache = ImGui_InputTextFlags_ReadOnly.func()
  return ImGui_InputTextFlags_ReadOnly.cache

def ImGui_InputTextMultiline(ctx, label, bufInOutNeedBig, size_wInOptional = None, size_hInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_InputTextMultiline, 'func'):
    proc = rpr_getfp('ImGui_InputTextMultiline')
    ImGui_InputTextMultiline.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_int, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packs(bufInOutNeedBig), c_int(4096), c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputTextMultiline.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None)
  return rval, rpr_unpacks(args[2])

def ImGui_InputTextWithHint(ctx, label, hint, bufInOutNeedBig, flagsInOptional = None):
  if not hasattr(ImGui_InputTextWithHint, 'func'):
    proc = rpr_getfp('ImGui_InputTextWithHint')
    ImGui_InputTextWithHint.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packsc(hint), rpr_packs(bufInOutNeedBig), c_int(4096), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InputTextWithHint.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)
  return rval, rpr_unpacks(args[3])

def ImGui_InvisibleButton(ctx, str_id, size_w, size_h, flagsInOptional = None):
  if not hasattr(ImGui_InvisibleButton, 'func'):
    proc = rpr_getfp('ImGui_InvisibleButton')
    ImGui_InvisibleButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_double(size_w), c_double(size_h), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_InvisibleButton.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)
  return rval

def ImGui_IsAnyItemActive(ctx):
  if not hasattr(ImGui_IsAnyItemActive, 'func'):
    proc = rpr_getfp('ImGui_IsAnyItemActive')
    ImGui_IsAnyItemActive.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsAnyItemActive.func(args[0])
  return rval

def ImGui_IsAnyItemFocused(ctx):
  if not hasattr(ImGui_IsAnyItemFocused, 'func'):
    proc = rpr_getfp('ImGui_IsAnyItemFocused')
    ImGui_IsAnyItemFocused.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsAnyItemFocused.func(args[0])
  return rval

def ImGui_IsAnyItemHovered(ctx):
  if not hasattr(ImGui_IsAnyItemHovered, 'func'):
    proc = rpr_getfp('ImGui_IsAnyItemHovered')
    ImGui_IsAnyItemHovered.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsAnyItemHovered.func(args[0])
  return rval

def ImGui_IsAnyMouseDown(ctx):
  if not hasattr(ImGui_IsAnyMouseDown, 'func'):
    proc = rpr_getfp('ImGui_IsAnyMouseDown')
    ImGui_IsAnyMouseDown.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsAnyMouseDown.func(args[0])
  return rval

def ImGui_IsItemActivated(ctx):
  if not hasattr(ImGui_IsItemActivated, 'func'):
    proc = rpr_getfp('ImGui_IsItemActivated')
    ImGui_IsItemActivated.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemActivated.func(args[0])
  return rval

def ImGui_IsItemActive(ctx):
  if not hasattr(ImGui_IsItemActive, 'func'):
    proc = rpr_getfp('ImGui_IsItemActive')
    ImGui_IsItemActive.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemActive.func(args[0])
  return rval

def ImGui_IsItemClicked(ctx, mouse_buttonInOptional = None):
  if not hasattr(ImGui_IsItemClicked, 'func'):
    proc = rpr_getfp('ImGui_IsItemClicked')
    ImGui_IsItemClicked.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(mouse_buttonInOptional) if mouse_buttonInOptional != None else None)
  rval = ImGui_IsItemClicked.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

def ImGui_IsItemDeactivated(ctx):
  if not hasattr(ImGui_IsItemDeactivated, 'func'):
    proc = rpr_getfp('ImGui_IsItemDeactivated')
    ImGui_IsItemDeactivated.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemDeactivated.func(args[0])
  return rval

def ImGui_IsItemDeactivatedAfterEdit(ctx):
  if not hasattr(ImGui_IsItemDeactivatedAfterEdit, 'func'):
    proc = rpr_getfp('ImGui_IsItemDeactivatedAfterEdit')
    ImGui_IsItemDeactivatedAfterEdit.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemDeactivatedAfterEdit.func(args[0])
  return rval

def ImGui_IsItemEdited(ctx):
  if not hasattr(ImGui_IsItemEdited, 'func'):
    proc = rpr_getfp('ImGui_IsItemEdited')
    ImGui_IsItemEdited.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemEdited.func(args[0])
  return rval

def ImGui_IsItemFocused(ctx):
  if not hasattr(ImGui_IsItemFocused, 'func'):
    proc = rpr_getfp('ImGui_IsItemFocused')
    ImGui_IsItemFocused.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemFocused.func(args[0])
  return rval

def ImGui_IsItemHovered(ctx, flagsInOptional = None):
  if not hasattr(ImGui_IsItemHovered, 'func'):
    proc = rpr_getfp('ImGui_IsItemHovered')
    ImGui_IsItemHovered.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_IsItemHovered.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

def ImGui_IsItemToggledOpen(ctx):
  if not hasattr(ImGui_IsItemToggledOpen, 'func'):
    proc = rpr_getfp('ImGui_IsItemToggledOpen')
    ImGui_IsItemToggledOpen.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemToggledOpen.func(args[0])
  return rval

def ImGui_IsItemVisible(ctx):
  if not hasattr(ImGui_IsItemVisible, 'func'):
    proc = rpr_getfp('ImGui_IsItemVisible')
    ImGui_IsItemVisible.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsItemVisible.func(args[0])
  return rval

def ImGui_IsKeyDown(ctx, key):
  if not hasattr(ImGui_IsKeyDown, 'func'):
    proc = rpr_getfp('ImGui_IsKeyDown')
    ImGui_IsKeyDown.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(key))
  rval = ImGui_IsKeyDown.func(args[0], args[1])
  return rval

def ImGui_IsKeyPressed(ctx, key, repeatInOptional = None):
  if not hasattr(ImGui_IsKeyPressed, 'func'):
    proc = rpr_getfp('ImGui_IsKeyPressed')
    ImGui_IsKeyPressed.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(key), c_bool(repeatInOptional) if repeatInOptional != None else None)
  rval = ImGui_IsKeyPressed.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_IsKeyReleased(ctx, key):
  if not hasattr(ImGui_IsKeyReleased, 'func'):
    proc = rpr_getfp('ImGui_IsKeyReleased')
    ImGui_IsKeyReleased.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(key))
  rval = ImGui_IsKeyReleased.func(args[0], args[1])
  return rval

def ImGui_IsMouseClicked(ctx, button, repeatInOptional = None):
  if not hasattr(ImGui_IsMouseClicked, 'func'):
    proc = rpr_getfp('ImGui_IsMouseClicked')
    ImGui_IsMouseClicked.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button), c_bool(repeatInOptional) if repeatInOptional != None else None)
  rval = ImGui_IsMouseClicked.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_IsMouseDoubleClicked(ctx, button):
  if not hasattr(ImGui_IsMouseDoubleClicked, 'func'):
    proc = rpr_getfp('ImGui_IsMouseDoubleClicked')
    ImGui_IsMouseDoubleClicked.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button))
  rval = ImGui_IsMouseDoubleClicked.func(args[0], args[1])
  return rval

def ImGui_IsMouseDown(ctx, button):
  if not hasattr(ImGui_IsMouseDown, 'func'):
    proc = rpr_getfp('ImGui_IsMouseDown')
    ImGui_IsMouseDown.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button))
  rval = ImGui_IsMouseDown.func(args[0], args[1])
  return rval

def ImGui_IsMouseDragging(ctx, button, lock_thresholdInOptional = None):
  if not hasattr(ImGui_IsMouseDragging, 'func'):
    proc = rpr_getfp('ImGui_IsMouseDragging')
    ImGui_IsMouseDragging.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button), c_double(lock_thresholdInOptional) if lock_thresholdInOptional != None else None)
  rval = ImGui_IsMouseDragging.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_IsMouseHoveringRect(ctx, r_min_x, r_min_y, r_max_x, r_max_y, clipInOptional = None):
  if not hasattr(ImGui_IsMouseHoveringRect, 'func'):
    proc = rpr_getfp('ImGui_IsMouseHoveringRect')
    ImGui_IsMouseHoveringRect.func = CFUNCTYPE(c_bool, c_void_p, c_double, c_double, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(r_min_x), c_double(r_min_y), c_double(r_max_x), c_double(r_max_y), c_bool(clipInOptional) if clipInOptional != None else None)
  rval = ImGui_IsMouseHoveringRect.func(args[0], args[1], args[2], args[3], args[4], byref(args[5]) if args[5] != None else None)
  return rval

def ImGui_IsMousePosValid(ctx, mouse_pos_xInOptional = None, mouse_pos_yInOptional = None):
  if not hasattr(ImGui_IsMousePosValid, 'func'):
    proc = rpr_getfp('ImGui_IsMousePosValid')
    ImGui_IsMousePosValid.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(mouse_pos_xInOptional) if mouse_pos_xInOptional != None else None, c_double(mouse_pos_yInOptional) if mouse_pos_yInOptional != None else None)
  rval = ImGui_IsMousePosValid.func(args[0], byref(args[1]) if args[1] != None else None, byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_IsMouseReleased(ctx, button):
  if not hasattr(ImGui_IsMouseReleased, 'func'):
    proc = rpr_getfp('ImGui_IsMouseReleased')
    ImGui_IsMouseReleased.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(button))
  rval = ImGui_IsMouseReleased.func(args[0], args[1])
  return rval

def ImGui_IsPopupOpen(ctx, str_id, flagsInOptional = None):
  if not hasattr(ImGui_IsPopupOpen, 'func'):
    proc = rpr_getfp('ImGui_IsPopupOpen')
    ImGui_IsPopupOpen.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_IsPopupOpen.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_IsRectVisible(ctx, size_w, size_h):
  if not hasattr(ImGui_IsRectVisible, 'func'):
    proc = rpr_getfp('ImGui_IsRectVisible')
    ImGui_IsRectVisible.func = CFUNCTYPE(c_bool, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(size_w), c_double(size_h))
  rval = ImGui_IsRectVisible.func(args[0], args[1], args[2])
  return rval

def ImGui_IsRectVisibleEx(ctx, rect_min_x, rect_min_y, rect_max_x, rect_max_y):
  if not hasattr(ImGui_IsRectVisibleEx, 'func'):
    proc = rpr_getfp('ImGui_IsRectVisibleEx')
    ImGui_IsRectVisibleEx.func = CFUNCTYPE(c_bool, c_void_p, c_double, c_double, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(rect_min_x), c_double(rect_min_y), c_double(rect_max_x), c_double(rect_max_y))
  rval = ImGui_IsRectVisibleEx.func(args[0], args[1], args[2], args[3], args[4])
  return rval

def ImGui_IsWindowAppearing(ctx):
  if not hasattr(ImGui_IsWindowAppearing, 'func'):
    proc = rpr_getfp('ImGui_IsWindowAppearing')
    ImGui_IsWindowAppearing.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsWindowAppearing.func(args[0])
  return rval

def ImGui_IsWindowCollapsed(ctx):
  if not hasattr(ImGui_IsWindowCollapsed, 'func'):
    proc = rpr_getfp('ImGui_IsWindowCollapsed')
    ImGui_IsWindowCollapsed.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsWindowCollapsed.func(args[0])
  return rval

def ImGui_IsWindowDocked(ctx):
  if not hasattr(ImGui_IsWindowDocked, 'func'):
    proc = rpr_getfp('ImGui_IsWindowDocked')
    ImGui_IsWindowDocked.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_IsWindowDocked.func(args[0])
  return rval

def ImGui_IsWindowFocused(ctx, flagsInOptional = None):
  if not hasattr(ImGui_IsWindowFocused, 'func'):
    proc = rpr_getfp('ImGui_IsWindowFocused')
    ImGui_IsWindowFocused.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_IsWindowFocused.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

def ImGui_IsWindowHovered(ctx, flagsInOptional = None):
  if not hasattr(ImGui_IsWindowHovered, 'func'):
    proc = rpr_getfp('ImGui_IsWindowHovered')
    ImGui_IsWindowHovered.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_IsWindowHovered.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

def ImGui_Key_0():
  if not hasattr(ImGui_Key_0, 'func'):
    proc = rpr_getfp('ImGui_Key_0')
    ImGui_Key_0.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_0, 'cache'):
    ImGui_Key_0.cache = ImGui_Key_0.func()
  return ImGui_Key_0.cache

def ImGui_Key_1():
  if not hasattr(ImGui_Key_1, 'func'):
    proc = rpr_getfp('ImGui_Key_1')
    ImGui_Key_1.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_1, 'cache'):
    ImGui_Key_1.cache = ImGui_Key_1.func()
  return ImGui_Key_1.cache

def ImGui_Key_2():
  if not hasattr(ImGui_Key_2, 'func'):
    proc = rpr_getfp('ImGui_Key_2')
    ImGui_Key_2.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_2, 'cache'):
    ImGui_Key_2.cache = ImGui_Key_2.func()
  return ImGui_Key_2.cache

def ImGui_Key_3():
  if not hasattr(ImGui_Key_3, 'func'):
    proc = rpr_getfp('ImGui_Key_3')
    ImGui_Key_3.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_3, 'cache'):
    ImGui_Key_3.cache = ImGui_Key_3.func()
  return ImGui_Key_3.cache

def ImGui_Key_4():
  if not hasattr(ImGui_Key_4, 'func'):
    proc = rpr_getfp('ImGui_Key_4')
    ImGui_Key_4.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_4, 'cache'):
    ImGui_Key_4.cache = ImGui_Key_4.func()
  return ImGui_Key_4.cache

def ImGui_Key_5():
  if not hasattr(ImGui_Key_5, 'func'):
    proc = rpr_getfp('ImGui_Key_5')
    ImGui_Key_5.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_5, 'cache'):
    ImGui_Key_5.cache = ImGui_Key_5.func()
  return ImGui_Key_5.cache

def ImGui_Key_6():
  if not hasattr(ImGui_Key_6, 'func'):
    proc = rpr_getfp('ImGui_Key_6')
    ImGui_Key_6.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_6, 'cache'):
    ImGui_Key_6.cache = ImGui_Key_6.func()
  return ImGui_Key_6.cache

def ImGui_Key_7():
  if not hasattr(ImGui_Key_7, 'func'):
    proc = rpr_getfp('ImGui_Key_7')
    ImGui_Key_7.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_7, 'cache'):
    ImGui_Key_7.cache = ImGui_Key_7.func()
  return ImGui_Key_7.cache

def ImGui_Key_8():
  if not hasattr(ImGui_Key_8, 'func'):
    proc = rpr_getfp('ImGui_Key_8')
    ImGui_Key_8.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_8, 'cache'):
    ImGui_Key_8.cache = ImGui_Key_8.func()
  return ImGui_Key_8.cache

def ImGui_Key_9():
  if not hasattr(ImGui_Key_9, 'func'):
    proc = rpr_getfp('ImGui_Key_9')
    ImGui_Key_9.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_9, 'cache'):
    ImGui_Key_9.cache = ImGui_Key_9.func()
  return ImGui_Key_9.cache

def ImGui_Key_A():
  if not hasattr(ImGui_Key_A, 'func'):
    proc = rpr_getfp('ImGui_Key_A')
    ImGui_Key_A.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_A, 'cache'):
    ImGui_Key_A.cache = ImGui_Key_A.func()
  return ImGui_Key_A.cache

def ImGui_Key_Apostrophe():
  if not hasattr(ImGui_Key_Apostrophe, 'func'):
    proc = rpr_getfp('ImGui_Key_Apostrophe')
    ImGui_Key_Apostrophe.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Apostrophe, 'cache'):
    ImGui_Key_Apostrophe.cache = ImGui_Key_Apostrophe.func()
  return ImGui_Key_Apostrophe.cache

def ImGui_Key_B():
  if not hasattr(ImGui_Key_B, 'func'):
    proc = rpr_getfp('ImGui_Key_B')
    ImGui_Key_B.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_B, 'cache'):
    ImGui_Key_B.cache = ImGui_Key_B.func()
  return ImGui_Key_B.cache

def ImGui_Key_Backslash():
  if not hasattr(ImGui_Key_Backslash, 'func'):
    proc = rpr_getfp('ImGui_Key_Backslash')
    ImGui_Key_Backslash.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Backslash, 'cache'):
    ImGui_Key_Backslash.cache = ImGui_Key_Backslash.func()
  return ImGui_Key_Backslash.cache

def ImGui_Key_Backspace():
  if not hasattr(ImGui_Key_Backspace, 'func'):
    proc = rpr_getfp('ImGui_Key_Backspace')
    ImGui_Key_Backspace.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Backspace, 'cache'):
    ImGui_Key_Backspace.cache = ImGui_Key_Backspace.func()
  return ImGui_Key_Backspace.cache

def ImGui_Key_C():
  if not hasattr(ImGui_Key_C, 'func'):
    proc = rpr_getfp('ImGui_Key_C')
    ImGui_Key_C.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_C, 'cache'):
    ImGui_Key_C.cache = ImGui_Key_C.func()
  return ImGui_Key_C.cache

def ImGui_Key_CapsLock():
  if not hasattr(ImGui_Key_CapsLock, 'func'):
    proc = rpr_getfp('ImGui_Key_CapsLock')
    ImGui_Key_CapsLock.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_CapsLock, 'cache'):
    ImGui_Key_CapsLock.cache = ImGui_Key_CapsLock.func()
  return ImGui_Key_CapsLock.cache

def ImGui_Key_Comma():
  if not hasattr(ImGui_Key_Comma, 'func'):
    proc = rpr_getfp('ImGui_Key_Comma')
    ImGui_Key_Comma.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Comma, 'cache'):
    ImGui_Key_Comma.cache = ImGui_Key_Comma.func()
  return ImGui_Key_Comma.cache

def ImGui_Key_D():
  if not hasattr(ImGui_Key_D, 'func'):
    proc = rpr_getfp('ImGui_Key_D')
    ImGui_Key_D.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_D, 'cache'):
    ImGui_Key_D.cache = ImGui_Key_D.func()
  return ImGui_Key_D.cache

def ImGui_Key_Delete():
  if not hasattr(ImGui_Key_Delete, 'func'):
    proc = rpr_getfp('ImGui_Key_Delete')
    ImGui_Key_Delete.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Delete, 'cache'):
    ImGui_Key_Delete.cache = ImGui_Key_Delete.func()
  return ImGui_Key_Delete.cache

def ImGui_Key_DownArrow():
  if not hasattr(ImGui_Key_DownArrow, 'func'):
    proc = rpr_getfp('ImGui_Key_DownArrow')
    ImGui_Key_DownArrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_DownArrow, 'cache'):
    ImGui_Key_DownArrow.cache = ImGui_Key_DownArrow.func()
  return ImGui_Key_DownArrow.cache

def ImGui_Key_E():
  if not hasattr(ImGui_Key_E, 'func'):
    proc = rpr_getfp('ImGui_Key_E')
    ImGui_Key_E.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_E, 'cache'):
    ImGui_Key_E.cache = ImGui_Key_E.func()
  return ImGui_Key_E.cache

def ImGui_Key_End():
  if not hasattr(ImGui_Key_End, 'func'):
    proc = rpr_getfp('ImGui_Key_End')
    ImGui_Key_End.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_End, 'cache'):
    ImGui_Key_End.cache = ImGui_Key_End.func()
  return ImGui_Key_End.cache

def ImGui_Key_Enter():
  if not hasattr(ImGui_Key_Enter, 'func'):
    proc = rpr_getfp('ImGui_Key_Enter')
    ImGui_Key_Enter.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Enter, 'cache'):
    ImGui_Key_Enter.cache = ImGui_Key_Enter.func()
  return ImGui_Key_Enter.cache

def ImGui_Key_Equal():
  if not hasattr(ImGui_Key_Equal, 'func'):
    proc = rpr_getfp('ImGui_Key_Equal')
    ImGui_Key_Equal.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Equal, 'cache'):
    ImGui_Key_Equal.cache = ImGui_Key_Equal.func()
  return ImGui_Key_Equal.cache

def ImGui_Key_Escape():
  if not hasattr(ImGui_Key_Escape, 'func'):
    proc = rpr_getfp('ImGui_Key_Escape')
    ImGui_Key_Escape.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Escape, 'cache'):
    ImGui_Key_Escape.cache = ImGui_Key_Escape.func()
  return ImGui_Key_Escape.cache

def ImGui_Key_F():
  if not hasattr(ImGui_Key_F, 'func'):
    proc = rpr_getfp('ImGui_Key_F')
    ImGui_Key_F.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F, 'cache'):
    ImGui_Key_F.cache = ImGui_Key_F.func()
  return ImGui_Key_F.cache

def ImGui_Key_F1():
  if not hasattr(ImGui_Key_F1, 'func'):
    proc = rpr_getfp('ImGui_Key_F1')
    ImGui_Key_F1.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F1, 'cache'):
    ImGui_Key_F1.cache = ImGui_Key_F1.func()
  return ImGui_Key_F1.cache

def ImGui_Key_F10():
  if not hasattr(ImGui_Key_F10, 'func'):
    proc = rpr_getfp('ImGui_Key_F10')
    ImGui_Key_F10.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F10, 'cache'):
    ImGui_Key_F10.cache = ImGui_Key_F10.func()
  return ImGui_Key_F10.cache

def ImGui_Key_F11():
  if not hasattr(ImGui_Key_F11, 'func'):
    proc = rpr_getfp('ImGui_Key_F11')
    ImGui_Key_F11.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F11, 'cache'):
    ImGui_Key_F11.cache = ImGui_Key_F11.func()
  return ImGui_Key_F11.cache

def ImGui_Key_F12():
  if not hasattr(ImGui_Key_F12, 'func'):
    proc = rpr_getfp('ImGui_Key_F12')
    ImGui_Key_F12.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F12, 'cache'):
    ImGui_Key_F12.cache = ImGui_Key_F12.func()
  return ImGui_Key_F12.cache

def ImGui_Key_F2():
  if not hasattr(ImGui_Key_F2, 'func'):
    proc = rpr_getfp('ImGui_Key_F2')
    ImGui_Key_F2.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F2, 'cache'):
    ImGui_Key_F2.cache = ImGui_Key_F2.func()
  return ImGui_Key_F2.cache

def ImGui_Key_F3():
  if not hasattr(ImGui_Key_F3, 'func'):
    proc = rpr_getfp('ImGui_Key_F3')
    ImGui_Key_F3.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F3, 'cache'):
    ImGui_Key_F3.cache = ImGui_Key_F3.func()
  return ImGui_Key_F3.cache

def ImGui_Key_F4():
  if not hasattr(ImGui_Key_F4, 'func'):
    proc = rpr_getfp('ImGui_Key_F4')
    ImGui_Key_F4.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F4, 'cache'):
    ImGui_Key_F4.cache = ImGui_Key_F4.func()
  return ImGui_Key_F4.cache

def ImGui_Key_F5():
  if not hasattr(ImGui_Key_F5, 'func'):
    proc = rpr_getfp('ImGui_Key_F5')
    ImGui_Key_F5.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F5, 'cache'):
    ImGui_Key_F5.cache = ImGui_Key_F5.func()
  return ImGui_Key_F5.cache

def ImGui_Key_F6():
  if not hasattr(ImGui_Key_F6, 'func'):
    proc = rpr_getfp('ImGui_Key_F6')
    ImGui_Key_F6.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F6, 'cache'):
    ImGui_Key_F6.cache = ImGui_Key_F6.func()
  return ImGui_Key_F6.cache

def ImGui_Key_F7():
  if not hasattr(ImGui_Key_F7, 'func'):
    proc = rpr_getfp('ImGui_Key_F7')
    ImGui_Key_F7.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F7, 'cache'):
    ImGui_Key_F7.cache = ImGui_Key_F7.func()
  return ImGui_Key_F7.cache

def ImGui_Key_F8():
  if not hasattr(ImGui_Key_F8, 'func'):
    proc = rpr_getfp('ImGui_Key_F8')
    ImGui_Key_F8.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F8, 'cache'):
    ImGui_Key_F8.cache = ImGui_Key_F8.func()
  return ImGui_Key_F8.cache

def ImGui_Key_F9():
  if not hasattr(ImGui_Key_F9, 'func'):
    proc = rpr_getfp('ImGui_Key_F9')
    ImGui_Key_F9.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_F9, 'cache'):
    ImGui_Key_F9.cache = ImGui_Key_F9.func()
  return ImGui_Key_F9.cache

def ImGui_Key_G():
  if not hasattr(ImGui_Key_G, 'func'):
    proc = rpr_getfp('ImGui_Key_G')
    ImGui_Key_G.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_G, 'cache'):
    ImGui_Key_G.cache = ImGui_Key_G.func()
  return ImGui_Key_G.cache

def ImGui_Key_GraveAccent():
  if not hasattr(ImGui_Key_GraveAccent, 'func'):
    proc = rpr_getfp('ImGui_Key_GraveAccent')
    ImGui_Key_GraveAccent.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_GraveAccent, 'cache'):
    ImGui_Key_GraveAccent.cache = ImGui_Key_GraveAccent.func()
  return ImGui_Key_GraveAccent.cache

def ImGui_Key_H():
  if not hasattr(ImGui_Key_H, 'func'):
    proc = rpr_getfp('ImGui_Key_H')
    ImGui_Key_H.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_H, 'cache'):
    ImGui_Key_H.cache = ImGui_Key_H.func()
  return ImGui_Key_H.cache

def ImGui_Key_Home():
  if not hasattr(ImGui_Key_Home, 'func'):
    proc = rpr_getfp('ImGui_Key_Home')
    ImGui_Key_Home.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Home, 'cache'):
    ImGui_Key_Home.cache = ImGui_Key_Home.func()
  return ImGui_Key_Home.cache

def ImGui_Key_I():
  if not hasattr(ImGui_Key_I, 'func'):
    proc = rpr_getfp('ImGui_Key_I')
    ImGui_Key_I.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_I, 'cache'):
    ImGui_Key_I.cache = ImGui_Key_I.func()
  return ImGui_Key_I.cache

def ImGui_Key_Insert():
  if not hasattr(ImGui_Key_Insert, 'func'):
    proc = rpr_getfp('ImGui_Key_Insert')
    ImGui_Key_Insert.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Insert, 'cache'):
    ImGui_Key_Insert.cache = ImGui_Key_Insert.func()
  return ImGui_Key_Insert.cache

def ImGui_Key_J():
  if not hasattr(ImGui_Key_J, 'func'):
    proc = rpr_getfp('ImGui_Key_J')
    ImGui_Key_J.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_J, 'cache'):
    ImGui_Key_J.cache = ImGui_Key_J.func()
  return ImGui_Key_J.cache

def ImGui_Key_K():
  if not hasattr(ImGui_Key_K, 'func'):
    proc = rpr_getfp('ImGui_Key_K')
    ImGui_Key_K.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_K, 'cache'):
    ImGui_Key_K.cache = ImGui_Key_K.func()
  return ImGui_Key_K.cache

def ImGui_Key_Keypad0():
  if not hasattr(ImGui_Key_Keypad0, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad0')
    ImGui_Key_Keypad0.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad0, 'cache'):
    ImGui_Key_Keypad0.cache = ImGui_Key_Keypad0.func()
  return ImGui_Key_Keypad0.cache

def ImGui_Key_Keypad1():
  if not hasattr(ImGui_Key_Keypad1, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad1')
    ImGui_Key_Keypad1.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad1, 'cache'):
    ImGui_Key_Keypad1.cache = ImGui_Key_Keypad1.func()
  return ImGui_Key_Keypad1.cache

def ImGui_Key_Keypad2():
  if not hasattr(ImGui_Key_Keypad2, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad2')
    ImGui_Key_Keypad2.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad2, 'cache'):
    ImGui_Key_Keypad2.cache = ImGui_Key_Keypad2.func()
  return ImGui_Key_Keypad2.cache

def ImGui_Key_Keypad3():
  if not hasattr(ImGui_Key_Keypad3, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad3')
    ImGui_Key_Keypad3.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad3, 'cache'):
    ImGui_Key_Keypad3.cache = ImGui_Key_Keypad3.func()
  return ImGui_Key_Keypad3.cache

def ImGui_Key_Keypad4():
  if not hasattr(ImGui_Key_Keypad4, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad4')
    ImGui_Key_Keypad4.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad4, 'cache'):
    ImGui_Key_Keypad4.cache = ImGui_Key_Keypad4.func()
  return ImGui_Key_Keypad4.cache

def ImGui_Key_Keypad5():
  if not hasattr(ImGui_Key_Keypad5, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad5')
    ImGui_Key_Keypad5.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad5, 'cache'):
    ImGui_Key_Keypad5.cache = ImGui_Key_Keypad5.func()
  return ImGui_Key_Keypad5.cache

def ImGui_Key_Keypad6():
  if not hasattr(ImGui_Key_Keypad6, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad6')
    ImGui_Key_Keypad6.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad6, 'cache'):
    ImGui_Key_Keypad6.cache = ImGui_Key_Keypad6.func()
  return ImGui_Key_Keypad6.cache

def ImGui_Key_Keypad7():
  if not hasattr(ImGui_Key_Keypad7, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad7')
    ImGui_Key_Keypad7.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad7, 'cache'):
    ImGui_Key_Keypad7.cache = ImGui_Key_Keypad7.func()
  return ImGui_Key_Keypad7.cache

def ImGui_Key_Keypad8():
  if not hasattr(ImGui_Key_Keypad8, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad8')
    ImGui_Key_Keypad8.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad8, 'cache'):
    ImGui_Key_Keypad8.cache = ImGui_Key_Keypad8.func()
  return ImGui_Key_Keypad8.cache

def ImGui_Key_Keypad9():
  if not hasattr(ImGui_Key_Keypad9, 'func'):
    proc = rpr_getfp('ImGui_Key_Keypad9')
    ImGui_Key_Keypad9.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Keypad9, 'cache'):
    ImGui_Key_Keypad9.cache = ImGui_Key_Keypad9.func()
  return ImGui_Key_Keypad9.cache

def ImGui_Key_KeypadAdd():
  if not hasattr(ImGui_Key_KeypadAdd, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadAdd')
    ImGui_Key_KeypadAdd.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadAdd, 'cache'):
    ImGui_Key_KeypadAdd.cache = ImGui_Key_KeypadAdd.func()
  return ImGui_Key_KeypadAdd.cache

def ImGui_Key_KeypadDecimal():
  if not hasattr(ImGui_Key_KeypadDecimal, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadDecimal')
    ImGui_Key_KeypadDecimal.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadDecimal, 'cache'):
    ImGui_Key_KeypadDecimal.cache = ImGui_Key_KeypadDecimal.func()
  return ImGui_Key_KeypadDecimal.cache

def ImGui_Key_KeypadDivide():
  if not hasattr(ImGui_Key_KeypadDivide, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadDivide')
    ImGui_Key_KeypadDivide.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadDivide, 'cache'):
    ImGui_Key_KeypadDivide.cache = ImGui_Key_KeypadDivide.func()
  return ImGui_Key_KeypadDivide.cache

def ImGui_Key_KeypadEnter():
  if not hasattr(ImGui_Key_KeypadEnter, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadEnter')
    ImGui_Key_KeypadEnter.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadEnter, 'cache'):
    ImGui_Key_KeypadEnter.cache = ImGui_Key_KeypadEnter.func()
  return ImGui_Key_KeypadEnter.cache

def ImGui_Key_KeypadEqual():
  if not hasattr(ImGui_Key_KeypadEqual, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadEqual')
    ImGui_Key_KeypadEqual.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadEqual, 'cache'):
    ImGui_Key_KeypadEqual.cache = ImGui_Key_KeypadEqual.func()
  return ImGui_Key_KeypadEqual.cache

def ImGui_Key_KeypadMultiply():
  if not hasattr(ImGui_Key_KeypadMultiply, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadMultiply')
    ImGui_Key_KeypadMultiply.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadMultiply, 'cache'):
    ImGui_Key_KeypadMultiply.cache = ImGui_Key_KeypadMultiply.func()
  return ImGui_Key_KeypadMultiply.cache

def ImGui_Key_KeypadSubtract():
  if not hasattr(ImGui_Key_KeypadSubtract, 'func'):
    proc = rpr_getfp('ImGui_Key_KeypadSubtract')
    ImGui_Key_KeypadSubtract.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_KeypadSubtract, 'cache'):
    ImGui_Key_KeypadSubtract.cache = ImGui_Key_KeypadSubtract.func()
  return ImGui_Key_KeypadSubtract.cache

def ImGui_Key_L():
  if not hasattr(ImGui_Key_L, 'func'):
    proc = rpr_getfp('ImGui_Key_L')
    ImGui_Key_L.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_L, 'cache'):
    ImGui_Key_L.cache = ImGui_Key_L.func()
  return ImGui_Key_L.cache

def ImGui_Key_LeftAlt():
  if not hasattr(ImGui_Key_LeftAlt, 'func'):
    proc = rpr_getfp('ImGui_Key_LeftAlt')
    ImGui_Key_LeftAlt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_LeftAlt, 'cache'):
    ImGui_Key_LeftAlt.cache = ImGui_Key_LeftAlt.func()
  return ImGui_Key_LeftAlt.cache

def ImGui_Key_LeftArrow():
  if not hasattr(ImGui_Key_LeftArrow, 'func'):
    proc = rpr_getfp('ImGui_Key_LeftArrow')
    ImGui_Key_LeftArrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_LeftArrow, 'cache'):
    ImGui_Key_LeftArrow.cache = ImGui_Key_LeftArrow.func()
  return ImGui_Key_LeftArrow.cache

def ImGui_Key_LeftBracket():
  if not hasattr(ImGui_Key_LeftBracket, 'func'):
    proc = rpr_getfp('ImGui_Key_LeftBracket')
    ImGui_Key_LeftBracket.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_LeftBracket, 'cache'):
    ImGui_Key_LeftBracket.cache = ImGui_Key_LeftBracket.func()
  return ImGui_Key_LeftBracket.cache

def ImGui_Key_LeftCtrl():
  if not hasattr(ImGui_Key_LeftCtrl, 'func'):
    proc = rpr_getfp('ImGui_Key_LeftCtrl')
    ImGui_Key_LeftCtrl.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_LeftCtrl, 'cache'):
    ImGui_Key_LeftCtrl.cache = ImGui_Key_LeftCtrl.func()
  return ImGui_Key_LeftCtrl.cache

def ImGui_Key_LeftShift():
  if not hasattr(ImGui_Key_LeftShift, 'func'):
    proc = rpr_getfp('ImGui_Key_LeftShift')
    ImGui_Key_LeftShift.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_LeftShift, 'cache'):
    ImGui_Key_LeftShift.cache = ImGui_Key_LeftShift.func()
  return ImGui_Key_LeftShift.cache

def ImGui_Key_LeftSuper():
  if not hasattr(ImGui_Key_LeftSuper, 'func'):
    proc = rpr_getfp('ImGui_Key_LeftSuper')
    ImGui_Key_LeftSuper.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_LeftSuper, 'cache'):
    ImGui_Key_LeftSuper.cache = ImGui_Key_LeftSuper.func()
  return ImGui_Key_LeftSuper.cache

def ImGui_Key_M():
  if not hasattr(ImGui_Key_M, 'func'):
    proc = rpr_getfp('ImGui_Key_M')
    ImGui_Key_M.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_M, 'cache'):
    ImGui_Key_M.cache = ImGui_Key_M.func()
  return ImGui_Key_M.cache

def ImGui_Key_Menu():
  if not hasattr(ImGui_Key_Menu, 'func'):
    proc = rpr_getfp('ImGui_Key_Menu')
    ImGui_Key_Menu.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Menu, 'cache'):
    ImGui_Key_Menu.cache = ImGui_Key_Menu.func()
  return ImGui_Key_Menu.cache

def ImGui_Key_Minus():
  if not hasattr(ImGui_Key_Minus, 'func'):
    proc = rpr_getfp('ImGui_Key_Minus')
    ImGui_Key_Minus.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Minus, 'cache'):
    ImGui_Key_Minus.cache = ImGui_Key_Minus.func()
  return ImGui_Key_Minus.cache

def ImGui_Key_ModAlt():
  if not hasattr(ImGui_Key_ModAlt, 'func'):
    proc = rpr_getfp('ImGui_Key_ModAlt')
    ImGui_Key_ModAlt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_ModAlt, 'cache'):
    ImGui_Key_ModAlt.cache = ImGui_Key_ModAlt.func()
  return ImGui_Key_ModAlt.cache

def ImGui_Key_ModCtrl():
  if not hasattr(ImGui_Key_ModCtrl, 'func'):
    proc = rpr_getfp('ImGui_Key_ModCtrl')
    ImGui_Key_ModCtrl.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_ModCtrl, 'cache'):
    ImGui_Key_ModCtrl.cache = ImGui_Key_ModCtrl.func()
  return ImGui_Key_ModCtrl.cache

def ImGui_Key_ModShift():
  if not hasattr(ImGui_Key_ModShift, 'func'):
    proc = rpr_getfp('ImGui_Key_ModShift')
    ImGui_Key_ModShift.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_ModShift, 'cache'):
    ImGui_Key_ModShift.cache = ImGui_Key_ModShift.func()
  return ImGui_Key_ModShift.cache

def ImGui_Key_ModSuper():
  if not hasattr(ImGui_Key_ModSuper, 'func'):
    proc = rpr_getfp('ImGui_Key_ModSuper')
    ImGui_Key_ModSuper.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_ModSuper, 'cache'):
    ImGui_Key_ModSuper.cache = ImGui_Key_ModSuper.func()
  return ImGui_Key_ModSuper.cache

def ImGui_Key_N():
  if not hasattr(ImGui_Key_N, 'func'):
    proc = rpr_getfp('ImGui_Key_N')
    ImGui_Key_N.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_N, 'cache'):
    ImGui_Key_N.cache = ImGui_Key_N.func()
  return ImGui_Key_N.cache

def ImGui_Key_NumLock():
  if not hasattr(ImGui_Key_NumLock, 'func'):
    proc = rpr_getfp('ImGui_Key_NumLock')
    ImGui_Key_NumLock.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_NumLock, 'cache'):
    ImGui_Key_NumLock.cache = ImGui_Key_NumLock.func()
  return ImGui_Key_NumLock.cache

def ImGui_Key_O():
  if not hasattr(ImGui_Key_O, 'func'):
    proc = rpr_getfp('ImGui_Key_O')
    ImGui_Key_O.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_O, 'cache'):
    ImGui_Key_O.cache = ImGui_Key_O.func()
  return ImGui_Key_O.cache

def ImGui_Key_P():
  if not hasattr(ImGui_Key_P, 'func'):
    proc = rpr_getfp('ImGui_Key_P')
    ImGui_Key_P.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_P, 'cache'):
    ImGui_Key_P.cache = ImGui_Key_P.func()
  return ImGui_Key_P.cache

def ImGui_Key_PageDown():
  if not hasattr(ImGui_Key_PageDown, 'func'):
    proc = rpr_getfp('ImGui_Key_PageDown')
    ImGui_Key_PageDown.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_PageDown, 'cache'):
    ImGui_Key_PageDown.cache = ImGui_Key_PageDown.func()
  return ImGui_Key_PageDown.cache

def ImGui_Key_PageUp():
  if not hasattr(ImGui_Key_PageUp, 'func'):
    proc = rpr_getfp('ImGui_Key_PageUp')
    ImGui_Key_PageUp.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_PageUp, 'cache'):
    ImGui_Key_PageUp.cache = ImGui_Key_PageUp.func()
  return ImGui_Key_PageUp.cache

def ImGui_Key_Pause():
  if not hasattr(ImGui_Key_Pause, 'func'):
    proc = rpr_getfp('ImGui_Key_Pause')
    ImGui_Key_Pause.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Pause, 'cache'):
    ImGui_Key_Pause.cache = ImGui_Key_Pause.func()
  return ImGui_Key_Pause.cache

def ImGui_Key_Period():
  if not hasattr(ImGui_Key_Period, 'func'):
    proc = rpr_getfp('ImGui_Key_Period')
    ImGui_Key_Period.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Period, 'cache'):
    ImGui_Key_Period.cache = ImGui_Key_Period.func()
  return ImGui_Key_Period.cache

def ImGui_Key_PrintScreen():
  if not hasattr(ImGui_Key_PrintScreen, 'func'):
    proc = rpr_getfp('ImGui_Key_PrintScreen')
    ImGui_Key_PrintScreen.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_PrintScreen, 'cache'):
    ImGui_Key_PrintScreen.cache = ImGui_Key_PrintScreen.func()
  return ImGui_Key_PrintScreen.cache

def ImGui_Key_Q():
  if not hasattr(ImGui_Key_Q, 'func'):
    proc = rpr_getfp('ImGui_Key_Q')
    ImGui_Key_Q.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Q, 'cache'):
    ImGui_Key_Q.cache = ImGui_Key_Q.func()
  return ImGui_Key_Q.cache

def ImGui_Key_R():
  if not hasattr(ImGui_Key_R, 'func'):
    proc = rpr_getfp('ImGui_Key_R')
    ImGui_Key_R.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_R, 'cache'):
    ImGui_Key_R.cache = ImGui_Key_R.func()
  return ImGui_Key_R.cache

def ImGui_Key_RightAlt():
  if not hasattr(ImGui_Key_RightAlt, 'func'):
    proc = rpr_getfp('ImGui_Key_RightAlt')
    ImGui_Key_RightAlt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_RightAlt, 'cache'):
    ImGui_Key_RightAlt.cache = ImGui_Key_RightAlt.func()
  return ImGui_Key_RightAlt.cache

def ImGui_Key_RightArrow():
  if not hasattr(ImGui_Key_RightArrow, 'func'):
    proc = rpr_getfp('ImGui_Key_RightArrow')
    ImGui_Key_RightArrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_RightArrow, 'cache'):
    ImGui_Key_RightArrow.cache = ImGui_Key_RightArrow.func()
  return ImGui_Key_RightArrow.cache

def ImGui_Key_RightBracket():
  if not hasattr(ImGui_Key_RightBracket, 'func'):
    proc = rpr_getfp('ImGui_Key_RightBracket')
    ImGui_Key_RightBracket.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_RightBracket, 'cache'):
    ImGui_Key_RightBracket.cache = ImGui_Key_RightBracket.func()
  return ImGui_Key_RightBracket.cache

def ImGui_Key_RightCtrl():
  if not hasattr(ImGui_Key_RightCtrl, 'func'):
    proc = rpr_getfp('ImGui_Key_RightCtrl')
    ImGui_Key_RightCtrl.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_RightCtrl, 'cache'):
    ImGui_Key_RightCtrl.cache = ImGui_Key_RightCtrl.func()
  return ImGui_Key_RightCtrl.cache

def ImGui_Key_RightShift():
  if not hasattr(ImGui_Key_RightShift, 'func'):
    proc = rpr_getfp('ImGui_Key_RightShift')
    ImGui_Key_RightShift.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_RightShift, 'cache'):
    ImGui_Key_RightShift.cache = ImGui_Key_RightShift.func()
  return ImGui_Key_RightShift.cache

def ImGui_Key_RightSuper():
  if not hasattr(ImGui_Key_RightSuper, 'func'):
    proc = rpr_getfp('ImGui_Key_RightSuper')
    ImGui_Key_RightSuper.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_RightSuper, 'cache'):
    ImGui_Key_RightSuper.cache = ImGui_Key_RightSuper.func()
  return ImGui_Key_RightSuper.cache

def ImGui_Key_S():
  if not hasattr(ImGui_Key_S, 'func'):
    proc = rpr_getfp('ImGui_Key_S')
    ImGui_Key_S.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_S, 'cache'):
    ImGui_Key_S.cache = ImGui_Key_S.func()
  return ImGui_Key_S.cache

def ImGui_Key_ScrollLock():
  if not hasattr(ImGui_Key_ScrollLock, 'func'):
    proc = rpr_getfp('ImGui_Key_ScrollLock')
    ImGui_Key_ScrollLock.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_ScrollLock, 'cache'):
    ImGui_Key_ScrollLock.cache = ImGui_Key_ScrollLock.func()
  return ImGui_Key_ScrollLock.cache

def ImGui_Key_Semicolon():
  if not hasattr(ImGui_Key_Semicolon, 'func'):
    proc = rpr_getfp('ImGui_Key_Semicolon')
    ImGui_Key_Semicolon.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Semicolon, 'cache'):
    ImGui_Key_Semicolon.cache = ImGui_Key_Semicolon.func()
  return ImGui_Key_Semicolon.cache

def ImGui_Key_Slash():
  if not hasattr(ImGui_Key_Slash, 'func'):
    proc = rpr_getfp('ImGui_Key_Slash')
    ImGui_Key_Slash.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Slash, 'cache'):
    ImGui_Key_Slash.cache = ImGui_Key_Slash.func()
  return ImGui_Key_Slash.cache

def ImGui_Key_Space():
  if not hasattr(ImGui_Key_Space, 'func'):
    proc = rpr_getfp('ImGui_Key_Space')
    ImGui_Key_Space.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Space, 'cache'):
    ImGui_Key_Space.cache = ImGui_Key_Space.func()
  return ImGui_Key_Space.cache

def ImGui_Key_T():
  if not hasattr(ImGui_Key_T, 'func'):
    proc = rpr_getfp('ImGui_Key_T')
    ImGui_Key_T.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_T, 'cache'):
    ImGui_Key_T.cache = ImGui_Key_T.func()
  return ImGui_Key_T.cache

def ImGui_Key_Tab():
  if not hasattr(ImGui_Key_Tab, 'func'):
    proc = rpr_getfp('ImGui_Key_Tab')
    ImGui_Key_Tab.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Tab, 'cache'):
    ImGui_Key_Tab.cache = ImGui_Key_Tab.func()
  return ImGui_Key_Tab.cache

def ImGui_Key_U():
  if not hasattr(ImGui_Key_U, 'func'):
    proc = rpr_getfp('ImGui_Key_U')
    ImGui_Key_U.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_U, 'cache'):
    ImGui_Key_U.cache = ImGui_Key_U.func()
  return ImGui_Key_U.cache

def ImGui_Key_UpArrow():
  if not hasattr(ImGui_Key_UpArrow, 'func'):
    proc = rpr_getfp('ImGui_Key_UpArrow')
    ImGui_Key_UpArrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_UpArrow, 'cache'):
    ImGui_Key_UpArrow.cache = ImGui_Key_UpArrow.func()
  return ImGui_Key_UpArrow.cache

def ImGui_Key_V():
  if not hasattr(ImGui_Key_V, 'func'):
    proc = rpr_getfp('ImGui_Key_V')
    ImGui_Key_V.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_V, 'cache'):
    ImGui_Key_V.cache = ImGui_Key_V.func()
  return ImGui_Key_V.cache

def ImGui_Key_W():
  if not hasattr(ImGui_Key_W, 'func'):
    proc = rpr_getfp('ImGui_Key_W')
    ImGui_Key_W.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_W, 'cache'):
    ImGui_Key_W.cache = ImGui_Key_W.func()
  return ImGui_Key_W.cache

def ImGui_Key_X():
  if not hasattr(ImGui_Key_X, 'func'):
    proc = rpr_getfp('ImGui_Key_X')
    ImGui_Key_X.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_X, 'cache'):
    ImGui_Key_X.cache = ImGui_Key_X.func()
  return ImGui_Key_X.cache

def ImGui_Key_Y():
  if not hasattr(ImGui_Key_Y, 'func'):
    proc = rpr_getfp('ImGui_Key_Y')
    ImGui_Key_Y.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Y, 'cache'):
    ImGui_Key_Y.cache = ImGui_Key_Y.func()
  return ImGui_Key_Y.cache

def ImGui_Key_Z():
  if not hasattr(ImGui_Key_Z, 'func'):
    proc = rpr_getfp('ImGui_Key_Z')
    ImGui_Key_Z.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_Key_Z, 'cache'):
    ImGui_Key_Z.cache = ImGui_Key_Z.func()
  return ImGui_Key_Z.cache

def ImGui_LabelText(ctx, label, text):
  if not hasattr(ImGui_LabelText, 'func'):
    proc = rpr_getfp('ImGui_LabelText')
    ImGui_LabelText.func = CFUNCTYPE(None, c_void_p, c_char_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packsc(text))
  ImGui_LabelText.func(args[0], args[1], args[2])

def ImGui_ListBox(ctx, label, current_itemInOut, items, height_in_itemsInOptional = None):
  if not hasattr(ImGui_ListBox, 'func'):
    proc = rpr_getfp('ImGui_ListBox')
    ImGui_ListBox.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_char_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(current_itemInOut), rpr_packsc(items), c_int(len(items)+1), c_int(height_in_itemsInOptional) if height_in_itemsInOptional != None else None)
  rval = ImGui_ListBox.func(args[0], args[1], byref(args[2]), args[3], args[4], byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value)

def ImGui_ListClipper_Begin(clipper, items_count, items_heightInOptional = None):
  if not hasattr(ImGui_ListClipper_Begin, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_Begin')
    ImGui_ListClipper_Begin.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_ListClipper*', clipper), c_int(items_count), c_double(items_heightInOptional) if items_heightInOptional != None else None)
  ImGui_ListClipper_Begin.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_ListClipper_End(clipper):
  if not hasattr(ImGui_ListClipper_End, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_End')
    ImGui_ListClipper_End.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_ListClipper*', clipper),)
  ImGui_ListClipper_End.func(args[0])

def ImGui_ListClipper_ForceDisplayRangeByIndices(clipper, item_min, item_max):
  if not hasattr(ImGui_ListClipper_ForceDisplayRangeByIndices, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_ForceDisplayRangeByIndices')
    ImGui_ListClipper_ForceDisplayRangeByIndices.func = CFUNCTYPE(None, c_void_p, c_int, c_int)(proc)
  args = (rpr_packp('ImGui_ListClipper*', clipper), c_int(item_min), c_int(item_max))
  ImGui_ListClipper_ForceDisplayRangeByIndices.func(args[0], args[1], args[2])

def ImGui_ListClipper_GetDisplayRange(clipper):
  if not hasattr(ImGui_ListClipper_GetDisplayRange, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_GetDisplayRange')
    ImGui_ListClipper_GetDisplayRange.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_ListClipper*', clipper), c_int(0), c_int(0))
  ImGui_ListClipper_GetDisplayRange.func(args[0], byref(args[1]), byref(args[2]))
  return int(args[1].value), int(args[2].value)

def ImGui_ListClipper_Step(clipper):
  if not hasattr(ImGui_ListClipper_Step, 'func'):
    proc = rpr_getfp('ImGui_ListClipper_Step')
    ImGui_ListClipper_Step.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_ListClipper*', clipper),)
  rval = ImGui_ListClipper_Step.func(args[0])
  return rval

def ImGui_LogFinish(ctx):
  if not hasattr(ImGui_LogFinish, 'func'):
    proc = rpr_getfp('ImGui_LogFinish')
    ImGui_LogFinish.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_LogFinish.func(args[0])

def ImGui_LogText(ctx, text):
  if not hasattr(ImGui_LogText, 'func'):
    proc = rpr_getfp('ImGui_LogText')
    ImGui_LogText.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_LogText.func(args[0], args[1])

def ImGui_LogToClipboard(ctx, auto_open_depthInOptional = None):
  if not hasattr(ImGui_LogToClipboard, 'func'):
    proc = rpr_getfp('ImGui_LogToClipboard')
    ImGui_LogToClipboard.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(auto_open_depthInOptional) if auto_open_depthInOptional != None else None)
  ImGui_LogToClipboard.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_LogToFile(ctx, auto_open_depthInOptional = None, filenameInOptional = None):
  if not hasattr(ImGui_LogToFile, 'func'):
    proc = rpr_getfp('ImGui_LogToFile')
    ImGui_LogToFile.func = CFUNCTYPE(None, c_void_p, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(auto_open_depthInOptional) if auto_open_depthInOptional != None else None, rpr_packsc(filenameInOptional) if filenameInOptional != None else None)
  ImGui_LogToFile.func(args[0], byref(args[1]) if args[1] != None else None, args[2])

def ImGui_LogToTTY(ctx, auto_open_depthInOptional = None):
  if not hasattr(ImGui_LogToTTY, 'func'):
    proc = rpr_getfp('ImGui_LogToTTY')
    ImGui_LogToTTY.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(auto_open_depthInOptional) if auto_open_depthInOptional != None else None)
  ImGui_LogToTTY.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_MenuItem(ctx, label, shortcutInOptional = None, p_selectedInOutOptional = None, enabledInOptional = None):
  if not hasattr(ImGui_MenuItem, 'func'):
    proc = rpr_getfp('ImGui_MenuItem')
    ImGui_MenuItem.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packsc(shortcutInOptional) if shortcutInOptional != None else None, c_bool(p_selectedInOutOptional) if p_selectedInOutOptional != None else None, c_bool(enabledInOptional) if enabledInOptional != None else None)
  rval = ImGui_MenuItem.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)
  return rval, int(args[3].value) if p_selectedInOutOptional != None else None

def ImGui_ModFlags_Alt():
  if not hasattr(ImGui_ModFlags_Alt, 'func'):
    proc = rpr_getfp('ImGui_ModFlags_Alt')
    ImGui_ModFlags_Alt.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ModFlags_Alt, 'cache'):
    ImGui_ModFlags_Alt.cache = ImGui_ModFlags_Alt.func()
  return ImGui_ModFlags_Alt.cache

def ImGui_ModFlags_Ctrl():
  if not hasattr(ImGui_ModFlags_Ctrl, 'func'):
    proc = rpr_getfp('ImGui_ModFlags_Ctrl')
    ImGui_ModFlags_Ctrl.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ModFlags_Ctrl, 'cache'):
    ImGui_ModFlags_Ctrl.cache = ImGui_ModFlags_Ctrl.func()
  return ImGui_ModFlags_Ctrl.cache

def ImGui_ModFlags_None():
  if not hasattr(ImGui_ModFlags_None, 'func'):
    proc = rpr_getfp('ImGui_ModFlags_None')
    ImGui_ModFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ModFlags_None, 'cache'):
    ImGui_ModFlags_None.cache = ImGui_ModFlags_None.func()
  return ImGui_ModFlags_None.cache

def ImGui_ModFlags_Shift():
  if not hasattr(ImGui_ModFlags_Shift, 'func'):
    proc = rpr_getfp('ImGui_ModFlags_Shift')
    ImGui_ModFlags_Shift.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ModFlags_Shift, 'cache'):
    ImGui_ModFlags_Shift.cache = ImGui_ModFlags_Shift.func()
  return ImGui_ModFlags_Shift.cache

def ImGui_ModFlags_Super():
  if not hasattr(ImGui_ModFlags_Super, 'func'):
    proc = rpr_getfp('ImGui_ModFlags_Super')
    ImGui_ModFlags_Super.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_ModFlags_Super, 'cache'):
    ImGui_ModFlags_Super.cache = ImGui_ModFlags_Super.func()
  return ImGui_ModFlags_Super.cache

def ImGui_MouseButton_Left():
  if not hasattr(ImGui_MouseButton_Left, 'func'):
    proc = rpr_getfp('ImGui_MouseButton_Left')
    ImGui_MouseButton_Left.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseButton_Left, 'cache'):
    ImGui_MouseButton_Left.cache = ImGui_MouseButton_Left.func()
  return ImGui_MouseButton_Left.cache

def ImGui_MouseButton_Middle():
  if not hasattr(ImGui_MouseButton_Middle, 'func'):
    proc = rpr_getfp('ImGui_MouseButton_Middle')
    ImGui_MouseButton_Middle.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseButton_Middle, 'cache'):
    ImGui_MouseButton_Middle.cache = ImGui_MouseButton_Middle.func()
  return ImGui_MouseButton_Middle.cache

def ImGui_MouseButton_Right():
  if not hasattr(ImGui_MouseButton_Right, 'func'):
    proc = rpr_getfp('ImGui_MouseButton_Right')
    ImGui_MouseButton_Right.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseButton_Right, 'cache'):
    ImGui_MouseButton_Right.cache = ImGui_MouseButton_Right.func()
  return ImGui_MouseButton_Right.cache

def ImGui_MouseCursor_Arrow():
  if not hasattr(ImGui_MouseCursor_Arrow, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_Arrow')
    ImGui_MouseCursor_Arrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_Arrow, 'cache'):
    ImGui_MouseCursor_Arrow.cache = ImGui_MouseCursor_Arrow.func()
  return ImGui_MouseCursor_Arrow.cache

def ImGui_MouseCursor_Hand():
  if not hasattr(ImGui_MouseCursor_Hand, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_Hand')
    ImGui_MouseCursor_Hand.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_Hand, 'cache'):
    ImGui_MouseCursor_Hand.cache = ImGui_MouseCursor_Hand.func()
  return ImGui_MouseCursor_Hand.cache

def ImGui_MouseCursor_NotAllowed():
  if not hasattr(ImGui_MouseCursor_NotAllowed, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_NotAllowed')
    ImGui_MouseCursor_NotAllowed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_NotAllowed, 'cache'):
    ImGui_MouseCursor_NotAllowed.cache = ImGui_MouseCursor_NotAllowed.func()
  return ImGui_MouseCursor_NotAllowed.cache

def ImGui_MouseCursor_ResizeAll():
  if not hasattr(ImGui_MouseCursor_ResizeAll, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeAll')
    ImGui_MouseCursor_ResizeAll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_ResizeAll, 'cache'):
    ImGui_MouseCursor_ResizeAll.cache = ImGui_MouseCursor_ResizeAll.func()
  return ImGui_MouseCursor_ResizeAll.cache

def ImGui_MouseCursor_ResizeEW():
  if not hasattr(ImGui_MouseCursor_ResizeEW, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeEW')
    ImGui_MouseCursor_ResizeEW.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_ResizeEW, 'cache'):
    ImGui_MouseCursor_ResizeEW.cache = ImGui_MouseCursor_ResizeEW.func()
  return ImGui_MouseCursor_ResizeEW.cache

def ImGui_MouseCursor_ResizeNESW():
  if not hasattr(ImGui_MouseCursor_ResizeNESW, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeNESW')
    ImGui_MouseCursor_ResizeNESW.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_ResizeNESW, 'cache'):
    ImGui_MouseCursor_ResizeNESW.cache = ImGui_MouseCursor_ResizeNESW.func()
  return ImGui_MouseCursor_ResizeNESW.cache

def ImGui_MouseCursor_ResizeNS():
  if not hasattr(ImGui_MouseCursor_ResizeNS, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeNS')
    ImGui_MouseCursor_ResizeNS.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_ResizeNS, 'cache'):
    ImGui_MouseCursor_ResizeNS.cache = ImGui_MouseCursor_ResizeNS.func()
  return ImGui_MouseCursor_ResizeNS.cache

def ImGui_MouseCursor_ResizeNWSE():
  if not hasattr(ImGui_MouseCursor_ResizeNWSE, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_ResizeNWSE')
    ImGui_MouseCursor_ResizeNWSE.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_ResizeNWSE, 'cache'):
    ImGui_MouseCursor_ResizeNWSE.cache = ImGui_MouseCursor_ResizeNWSE.func()
  return ImGui_MouseCursor_ResizeNWSE.cache

def ImGui_MouseCursor_TextInput():
  if not hasattr(ImGui_MouseCursor_TextInput, 'func'):
    proc = rpr_getfp('ImGui_MouseCursor_TextInput')
    ImGui_MouseCursor_TextInput.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_MouseCursor_TextInput, 'cache'):
    ImGui_MouseCursor_TextInput.cache = ImGui_MouseCursor_TextInput.func()
  return ImGui_MouseCursor_TextInput.cache

def ImGui_NewLine(ctx):
  if not hasattr(ImGui_NewLine, 'func'):
    proc = rpr_getfp('ImGui_NewLine')
    ImGui_NewLine.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_NewLine.func(args[0])

def ImGui_NumericLimits_Float():
  if not hasattr(ImGui_NumericLimits_Float, 'func'):
    proc = rpr_getfp('ImGui_NumericLimits_Float')
    ImGui_NumericLimits_Float.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (c_double(0), c_double(0))
  ImGui_NumericLimits_Float.func(byref(args[0]), byref(args[1]))
  return float(args[0].value), float(args[1].value)

def ImGui_OpenPopup(ctx, str_id, popup_flagsInOptional = None):
  if not hasattr(ImGui_OpenPopup, 'func'):
    proc = rpr_getfp('ImGui_OpenPopup')
    ImGui_OpenPopup.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  ImGui_OpenPopup.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_OpenPopupOnItemClick(ctx, str_idInOptional = None, popup_flagsInOptional = None):
  if not hasattr(ImGui_OpenPopupOnItemClick, 'func'):
    proc = rpr_getfp('ImGui_OpenPopupOnItemClick')
    ImGui_OpenPopupOnItemClick.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_idInOptional) if str_idInOptional != None else None, c_int(popup_flagsInOptional) if popup_flagsInOptional != None else None)
  ImGui_OpenPopupOnItemClick.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_PlotHistogram(ctx, label, values, values_offsetInOptional = None, overlay_textInOptional = None, scale_minInOptional = None, scale_maxInOptional = None, graph_size_wInOptional = None, graph_size_hInOptional = None):
  if not hasattr(ImGui_PlotHistogram, 'func'):
    proc = rpr_getfp('ImGui_PlotHistogram')
    ImGui_PlotHistogram.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_int(values_offsetInOptional) if values_offsetInOptional != None else None, rpr_packsc(overlay_textInOptional) if overlay_textInOptional != None else None, c_double(scale_minInOptional) if scale_minInOptional != None else None, c_double(scale_maxInOptional) if scale_maxInOptional != None else None, c_double(graph_size_wInOptional) if graph_size_wInOptional != None else None, c_double(graph_size_hInOptional) if graph_size_hInOptional != None else None)
  ImGui_PlotHistogram.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None)

def ImGui_PlotLines(ctx, label, values, values_offsetInOptional = None, overlay_textInOptional = None, scale_minInOptional = None, scale_maxInOptional = None, graph_size_wInOptional = None, graph_size_hInOptional = None):
  if not hasattr(ImGui_PlotLines, 'func'):
    proc = rpr_getfp('ImGui_PlotLines')
    ImGui_PlotLines.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_int(values_offsetInOptional) if values_offsetInOptional != None else None, rpr_packsc(overlay_textInOptional) if overlay_textInOptional != None else None, c_double(scale_minInOptional) if scale_minInOptional != None else None, c_double(scale_maxInOptional) if scale_maxInOptional != None else None, c_double(graph_size_wInOptional) if graph_size_wInOptional != None else None, c_double(graph_size_hInOptional) if graph_size_hInOptional != None else None)
  ImGui_PlotLines.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, args[4], byref(args[5]) if args[5] != None else None, byref(args[6]) if args[6] != None else None, byref(args[7]) if args[7] != None else None, byref(args[8]) if args[8] != None else None)

def ImGui_PointConvertNative(ctx, xInOut, yInOut, to_nativeInOptional = None):
  if not hasattr(ImGui_PointConvertNative, 'func'):
    proc = rpr_getfp('ImGui_PointConvertNative')
    ImGui_PointConvertNative.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(xInOut), c_double(yInOut), c_bool(to_nativeInOptional) if to_nativeInOptional != None else None)
  ImGui_PointConvertNative.func(args[0], byref(args[1]), byref(args[2]), byref(args[3]) if args[3] != None else None)
  return float(args[1].value), float(args[2].value)

def ImGui_PopAllowKeyboardFocus(ctx):
  if not hasattr(ImGui_PopAllowKeyboardFocus, 'func'):
    proc = rpr_getfp('ImGui_PopAllowKeyboardFocus')
    ImGui_PopAllowKeyboardFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopAllowKeyboardFocus.func(args[0])

def ImGui_PopButtonRepeat(ctx):
  if not hasattr(ImGui_PopButtonRepeat, 'func'):
    proc = rpr_getfp('ImGui_PopButtonRepeat')
    ImGui_PopButtonRepeat.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopButtonRepeat.func(args[0])

def ImGui_PopClipRect(ctx):
  if not hasattr(ImGui_PopClipRect, 'func'):
    proc = rpr_getfp('ImGui_PopClipRect')
    ImGui_PopClipRect.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopClipRect.func(args[0])

def ImGui_PopFont(ctx):
  if not hasattr(ImGui_PopFont, 'func'):
    proc = rpr_getfp('ImGui_PopFont')
    ImGui_PopFont.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopFont.func(args[0])

def ImGui_PopID(ctx):
  if not hasattr(ImGui_PopID, 'func'):
    proc = rpr_getfp('ImGui_PopID')
    ImGui_PopID.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopID.func(args[0])

def ImGui_PopItemWidth(ctx):
  if not hasattr(ImGui_PopItemWidth, 'func'):
    proc = rpr_getfp('ImGui_PopItemWidth')
    ImGui_PopItemWidth.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopItemWidth.func(args[0])

def ImGui_PopStyleColor(ctx, countInOptional = None):
  if not hasattr(ImGui_PopStyleColor, 'func'):
    proc = rpr_getfp('ImGui_PopStyleColor')
    ImGui_PopStyleColor.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(countInOptional) if countInOptional != None else None)
  ImGui_PopStyleColor.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_PopStyleVar(ctx, countInOptional = None):
  if not hasattr(ImGui_PopStyleVar, 'func'):
    proc = rpr_getfp('ImGui_PopStyleVar')
    ImGui_PopStyleVar.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(countInOptional) if countInOptional != None else None)
  ImGui_PopStyleVar.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_PopTextWrapPos(ctx):
  if not hasattr(ImGui_PopTextWrapPos, 'func'):
    proc = rpr_getfp('ImGui_PopTextWrapPos')
    ImGui_PopTextWrapPos.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_PopTextWrapPos.func(args[0])

def ImGui_PopupFlags_AnyPopup():
  if not hasattr(ImGui_PopupFlags_AnyPopup, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_AnyPopup')
    ImGui_PopupFlags_AnyPopup.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_AnyPopup, 'cache'):
    ImGui_PopupFlags_AnyPopup.cache = ImGui_PopupFlags_AnyPopup.func()
  return ImGui_PopupFlags_AnyPopup.cache

def ImGui_PopupFlags_AnyPopupId():
  if not hasattr(ImGui_PopupFlags_AnyPopupId, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_AnyPopupId')
    ImGui_PopupFlags_AnyPopupId.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_AnyPopupId, 'cache'):
    ImGui_PopupFlags_AnyPopupId.cache = ImGui_PopupFlags_AnyPopupId.func()
  return ImGui_PopupFlags_AnyPopupId.cache

def ImGui_PopupFlags_AnyPopupLevel():
  if not hasattr(ImGui_PopupFlags_AnyPopupLevel, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_AnyPopupLevel')
    ImGui_PopupFlags_AnyPopupLevel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_AnyPopupLevel, 'cache'):
    ImGui_PopupFlags_AnyPopupLevel.cache = ImGui_PopupFlags_AnyPopupLevel.func()
  return ImGui_PopupFlags_AnyPopupLevel.cache

def ImGui_PopupFlags_MouseButtonLeft():
  if not hasattr(ImGui_PopupFlags_MouseButtonLeft, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_MouseButtonLeft')
    ImGui_PopupFlags_MouseButtonLeft.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_MouseButtonLeft, 'cache'):
    ImGui_PopupFlags_MouseButtonLeft.cache = ImGui_PopupFlags_MouseButtonLeft.func()
  return ImGui_PopupFlags_MouseButtonLeft.cache

def ImGui_PopupFlags_MouseButtonMiddle():
  if not hasattr(ImGui_PopupFlags_MouseButtonMiddle, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_MouseButtonMiddle')
    ImGui_PopupFlags_MouseButtonMiddle.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_MouseButtonMiddle, 'cache'):
    ImGui_PopupFlags_MouseButtonMiddle.cache = ImGui_PopupFlags_MouseButtonMiddle.func()
  return ImGui_PopupFlags_MouseButtonMiddle.cache

def ImGui_PopupFlags_MouseButtonRight():
  if not hasattr(ImGui_PopupFlags_MouseButtonRight, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_MouseButtonRight')
    ImGui_PopupFlags_MouseButtonRight.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_MouseButtonRight, 'cache'):
    ImGui_PopupFlags_MouseButtonRight.cache = ImGui_PopupFlags_MouseButtonRight.func()
  return ImGui_PopupFlags_MouseButtonRight.cache

def ImGui_PopupFlags_NoOpenOverExistingPopup():
  if not hasattr(ImGui_PopupFlags_NoOpenOverExistingPopup, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_NoOpenOverExistingPopup')
    ImGui_PopupFlags_NoOpenOverExistingPopup.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_NoOpenOverExistingPopup, 'cache'):
    ImGui_PopupFlags_NoOpenOverExistingPopup.cache = ImGui_PopupFlags_NoOpenOverExistingPopup.func()
  return ImGui_PopupFlags_NoOpenOverExistingPopup.cache

def ImGui_PopupFlags_NoOpenOverItems():
  if not hasattr(ImGui_PopupFlags_NoOpenOverItems, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_NoOpenOverItems')
    ImGui_PopupFlags_NoOpenOverItems.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_NoOpenOverItems, 'cache'):
    ImGui_PopupFlags_NoOpenOverItems.cache = ImGui_PopupFlags_NoOpenOverItems.func()
  return ImGui_PopupFlags_NoOpenOverItems.cache

def ImGui_PopupFlags_None():
  if not hasattr(ImGui_PopupFlags_None, 'func'):
    proc = rpr_getfp('ImGui_PopupFlags_None')
    ImGui_PopupFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_PopupFlags_None, 'cache'):
    ImGui_PopupFlags_None.cache = ImGui_PopupFlags_None.func()
  return ImGui_PopupFlags_None.cache

def ImGui_ProgressBar(ctx, fraction, size_arg_wInOptional = None, size_arg_hInOptional = None, overlayInOptional = None):
  if not hasattr(ImGui_ProgressBar, 'func'):
    proc = rpr_getfp('ImGui_ProgressBar')
    ImGui_ProgressBar.func = CFUNCTYPE(None, c_void_p, c_double, c_void_p, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(fraction), c_double(size_arg_wInOptional) if size_arg_wInOptional != None else None, c_double(size_arg_hInOptional) if size_arg_hInOptional != None else None, rpr_packsc(overlayInOptional) if overlayInOptional != None else None)
  ImGui_ProgressBar.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None, args[4])

def ImGui_PushAllowKeyboardFocus(ctx, allow_keyboard_focus):
  if not hasattr(ImGui_PushAllowKeyboardFocus, 'func'):
    proc = rpr_getfp('ImGui_PushAllowKeyboardFocus')
    ImGui_PushAllowKeyboardFocus.func = CFUNCTYPE(None, c_void_p, c_bool)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(allow_keyboard_focus))
  ImGui_PushAllowKeyboardFocus.func(args[0], args[1])

def ImGui_PushButtonRepeat(ctx, repeat):
  if not hasattr(ImGui_PushButtonRepeat, 'func'):
    proc = rpr_getfp('ImGui_PushButtonRepeat')
    ImGui_PushButtonRepeat.func = CFUNCTYPE(None, c_void_p, c_bool)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(repeat))
  ImGui_PushButtonRepeat.func(args[0], args[1])

def ImGui_PushClipRect(ctx, clip_rect_min_x, clip_rect_min_y, clip_rect_max_x, clip_rect_max_y, intersect_with_current_clip_rect):
  if not hasattr(ImGui_PushClipRect, 'func'):
    proc = rpr_getfp('ImGui_PushClipRect')
    ImGui_PushClipRect.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double, c_bool)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(clip_rect_min_x), c_double(clip_rect_min_y), c_double(clip_rect_max_x), c_double(clip_rect_max_y), c_bool(intersect_with_current_clip_rect))
  ImGui_PushClipRect.func(args[0], args[1], args[2], args[3], args[4], args[5])

def ImGui_PushFont(ctx, font):
  if not hasattr(ImGui_PushFont, 'func'):
    proc = rpr_getfp('ImGui_PushFont')
    ImGui_PushFont.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packp('ImGui_Font*', font))
  ImGui_PushFont.func(args[0], args[1])

def ImGui_PushID(ctx, str_id):
  if not hasattr(ImGui_PushID, 'func'):
    proc = rpr_getfp('ImGui_PushID')
    ImGui_PushID.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id))
  ImGui_PushID.func(args[0], args[1])

def ImGui_PushItemWidth(ctx, item_width):
  if not hasattr(ImGui_PushItemWidth, 'func'):
    proc = rpr_getfp('ImGui_PushItemWidth')
    ImGui_PushItemWidth.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(item_width))
  ImGui_PushItemWidth.func(args[0], args[1])

def ImGui_PushStyleColor(ctx, idx, col_rgba):
  if not hasattr(ImGui_PushStyleColor, 'func'):
    proc = rpr_getfp('ImGui_PushStyleColor')
    ImGui_PushStyleColor.func = CFUNCTYPE(None, c_void_p, c_int, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(idx), c_int(col_rgba))
  ImGui_PushStyleColor.func(args[0], args[1], args[2])

def ImGui_PushStyleVar(ctx, var_idx, val1, val2InOptional = None):
  if not hasattr(ImGui_PushStyleVar, 'func'):
    proc = rpr_getfp('ImGui_PushStyleVar')
    ImGui_PushStyleVar.func = CFUNCTYPE(None, c_void_p, c_int, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(var_idx), c_double(val1), c_double(val2InOptional) if val2InOptional != None else None)
  ImGui_PushStyleVar.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

def ImGui_PushTextWrapPos(ctx, wrap_local_pos_xInOptional = None):
  if not hasattr(ImGui_PushTextWrapPos, 'func'):
    proc = rpr_getfp('ImGui_PushTextWrapPos')
    ImGui_PushTextWrapPos.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(wrap_local_pos_xInOptional) if wrap_local_pos_xInOptional != None else None)
  ImGui_PushTextWrapPos.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_RadioButton(ctx, label, active):
  if not hasattr(ImGui_RadioButton, 'func'):
    proc = rpr_getfp('ImGui_RadioButton')
    ImGui_RadioButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_bool)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_bool(active))
  rval = ImGui_RadioButton.func(args[0], args[1], args[2])
  return rval

def ImGui_RadioButtonEx(ctx, label, vInOut, v_button):
  if not hasattr(ImGui_RadioButtonEx, 'func'):
    proc = rpr_getfp('ImGui_RadioButtonEx')
    ImGui_RadioButtonEx.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(vInOut), c_int(v_button))
  rval = ImGui_RadioButtonEx.func(args[0], args[1], byref(args[2]), args[3])
  return rval, int(args[2].value)

def ImGui_ResetMouseDragDelta(ctx, buttonInOptional = None):
  if not hasattr(ImGui_ResetMouseDragDelta, 'func'):
    proc = rpr_getfp('ImGui_ResetMouseDragDelta')
    ImGui_ResetMouseDragDelta.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(buttonInOptional) if buttonInOptional != None else None)
  ImGui_ResetMouseDragDelta.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_SameLine(ctx, offset_from_start_xInOptional = None, spacingInOptional = None):
  if not hasattr(ImGui_SameLine, 'func'):
    proc = rpr_getfp('ImGui_SameLine')
    ImGui_SameLine.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(offset_from_start_xInOptional) if offset_from_start_xInOptional != None else None, c_double(spacingInOptional) if spacingInOptional != None else None)
  ImGui_SameLine.func(args[0], byref(args[1]) if args[1] != None else None, byref(args[2]) if args[2] != None else None)

def ImGui_Selectable(ctx, label, p_selectedInOut, flagsInOptional = None, size_wInOptional = None, size_hInOptional = None):
  if not hasattr(ImGui_Selectable, 'func'):
    proc = rpr_getfp('ImGui_Selectable')
    ImGui_Selectable.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_bool(p_selectedInOut), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(size_wInOptional) if size_wInOptional != None else None, c_double(size_hInOptional) if size_hInOptional != None else None)
  rval = ImGui_Selectable.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)
  return rval, int(args[2].value)

def ImGui_SelectableFlags_AllowDoubleClick():
  if not hasattr(ImGui_SelectableFlags_AllowDoubleClick, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_AllowDoubleClick')
    ImGui_SelectableFlags_AllowDoubleClick.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SelectableFlags_AllowDoubleClick, 'cache'):
    ImGui_SelectableFlags_AllowDoubleClick.cache = ImGui_SelectableFlags_AllowDoubleClick.func()
  return ImGui_SelectableFlags_AllowDoubleClick.cache

def ImGui_SelectableFlags_AllowItemOverlap():
  if not hasattr(ImGui_SelectableFlags_AllowItemOverlap, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_AllowItemOverlap')
    ImGui_SelectableFlags_AllowItemOverlap.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SelectableFlags_AllowItemOverlap, 'cache'):
    ImGui_SelectableFlags_AllowItemOverlap.cache = ImGui_SelectableFlags_AllowItemOverlap.func()
  return ImGui_SelectableFlags_AllowItemOverlap.cache

def ImGui_SelectableFlags_Disabled():
  if not hasattr(ImGui_SelectableFlags_Disabled, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_Disabled')
    ImGui_SelectableFlags_Disabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SelectableFlags_Disabled, 'cache'):
    ImGui_SelectableFlags_Disabled.cache = ImGui_SelectableFlags_Disabled.func()
  return ImGui_SelectableFlags_Disabled.cache

def ImGui_SelectableFlags_DontClosePopups():
  if not hasattr(ImGui_SelectableFlags_DontClosePopups, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_DontClosePopups')
    ImGui_SelectableFlags_DontClosePopups.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SelectableFlags_DontClosePopups, 'cache'):
    ImGui_SelectableFlags_DontClosePopups.cache = ImGui_SelectableFlags_DontClosePopups.func()
  return ImGui_SelectableFlags_DontClosePopups.cache

def ImGui_SelectableFlags_None():
  if not hasattr(ImGui_SelectableFlags_None, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_None')
    ImGui_SelectableFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SelectableFlags_None, 'cache'):
    ImGui_SelectableFlags_None.cache = ImGui_SelectableFlags_None.func()
  return ImGui_SelectableFlags_None.cache

def ImGui_SelectableFlags_SpanAllColumns():
  if not hasattr(ImGui_SelectableFlags_SpanAllColumns, 'func'):
    proc = rpr_getfp('ImGui_SelectableFlags_SpanAllColumns')
    ImGui_SelectableFlags_SpanAllColumns.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SelectableFlags_SpanAllColumns, 'cache'):
    ImGui_SelectableFlags_SpanAllColumns.cache = ImGui_SelectableFlags_SpanAllColumns.func()
  return ImGui_SelectableFlags_SpanAllColumns.cache

def ImGui_Separator(ctx):
  if not hasattr(ImGui_Separator, 'func'):
    proc = rpr_getfp('ImGui_Separator')
    ImGui_Separator.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_Separator.func(args[0])

def ImGui_SetClipboardText(ctx, text):
  if not hasattr(ImGui_SetClipboardText, 'func'):
    proc = rpr_getfp('ImGui_SetClipboardText')
    ImGui_SetClipboardText.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_SetClipboardText.func(args[0], args[1])

def ImGui_SetColorEditOptions(ctx, flags):
  if not hasattr(ImGui_SetColorEditOptions, 'func'):
    proc = rpr_getfp('ImGui_SetColorEditOptions')
    ImGui_SetColorEditOptions.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(flags))
  ImGui_SetColorEditOptions.func(args[0], args[1])

def ImGui_SetConfigVar(ctx, var_idx, value):
  if not hasattr(ImGui_SetConfigVar, 'func'):
    proc = rpr_getfp('ImGui_SetConfigVar')
    ImGui_SetConfigVar.func = CFUNCTYPE(None, c_void_p, c_int, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(var_idx), c_double(value))
  ImGui_SetConfigVar.func(args[0], args[1], args[2])

def ImGui_SetCursorPos(ctx, local_pos_x, local_pos_y):
  if not hasattr(ImGui_SetCursorPos, 'func'):
    proc = rpr_getfp('ImGui_SetCursorPos')
    ImGui_SetCursorPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(local_pos_x), c_double(local_pos_y))
  ImGui_SetCursorPos.func(args[0], args[1], args[2])

def ImGui_SetCursorPosX(ctx, local_x):
  if not hasattr(ImGui_SetCursorPosX, 'func'):
    proc = rpr_getfp('ImGui_SetCursorPosX')
    ImGui_SetCursorPosX.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(local_x))
  ImGui_SetCursorPosX.func(args[0], args[1])

def ImGui_SetCursorPosY(ctx, local_y):
  if not hasattr(ImGui_SetCursorPosY, 'func'):
    proc = rpr_getfp('ImGui_SetCursorPosY')
    ImGui_SetCursorPosY.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(local_y))
  ImGui_SetCursorPosY.func(args[0], args[1])

def ImGui_SetCursorScreenPos(ctx, pos_x, pos_y):
  if not hasattr(ImGui_SetCursorScreenPos, 'func'):
    proc = rpr_getfp('ImGui_SetCursorScreenPos')
    ImGui_SetCursorScreenPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(pos_x), c_double(pos_y))
  ImGui_SetCursorScreenPos.func(args[0], args[1], args[2])

def ImGui_SetDragDropPayload(ctx, type, data, condInOptional = None):
  if not hasattr(ImGui_SetDragDropPayload, 'func'):
    proc = rpr_getfp('ImGui_SetDragDropPayload')
    ImGui_SetDragDropPayload.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(type), rpr_packsc(data), c_int(condInOptional) if condInOptional != None else None)
  rval = ImGui_SetDragDropPayload.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

def ImGui_SetItemAllowOverlap(ctx):
  if not hasattr(ImGui_SetItemAllowOverlap, 'func'):
    proc = rpr_getfp('ImGui_SetItemAllowOverlap')
    ImGui_SetItemAllowOverlap.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_SetItemAllowOverlap.func(args[0])

def ImGui_SetItemDefaultFocus(ctx):
  if not hasattr(ImGui_SetItemDefaultFocus, 'func'):
    proc = rpr_getfp('ImGui_SetItemDefaultFocus')
    ImGui_SetItemDefaultFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_SetItemDefaultFocus.func(args[0])

def ImGui_SetKeyboardFocusHere(ctx, offsetInOptional = None):
  if not hasattr(ImGui_SetKeyboardFocusHere, 'func'):
    proc = rpr_getfp('ImGui_SetKeyboardFocusHere')
    ImGui_SetKeyboardFocusHere.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(offsetInOptional) if offsetInOptional != None else None)
  ImGui_SetKeyboardFocusHere.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_SetMouseCursor(ctx, cursor_type):
  if not hasattr(ImGui_SetMouseCursor, 'func'):
    proc = rpr_getfp('ImGui_SetMouseCursor')
    ImGui_SetMouseCursor.func = CFUNCTYPE(None, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(cursor_type))
  ImGui_SetMouseCursor.func(args[0], args[1])

def ImGui_SetNextFrameWantCaptureKeyboard(ctx, want_capture_keyboard):
  if not hasattr(ImGui_SetNextFrameWantCaptureKeyboard, 'func'):
    proc = rpr_getfp('ImGui_SetNextFrameWantCaptureKeyboard')
    ImGui_SetNextFrameWantCaptureKeyboard.func = CFUNCTYPE(None, c_void_p, c_bool)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(want_capture_keyboard))
  ImGui_SetNextFrameWantCaptureKeyboard.func(args[0], args[1])

def ImGui_SetNextItemOpen(ctx, is_open, condInOptional = None):
  if not hasattr(ImGui_SetNextItemOpen, 'func'):
    proc = rpr_getfp('ImGui_SetNextItemOpen')
    ImGui_SetNextItemOpen.func = CFUNCTYPE(None, c_void_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(is_open), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetNextItemOpen.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_SetNextItemWidth(ctx, item_width):
  if not hasattr(ImGui_SetNextItemWidth, 'func'):
    proc = rpr_getfp('ImGui_SetNextItemWidth')
    ImGui_SetNextItemWidth.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(item_width))
  ImGui_SetNextItemWidth.func(args[0], args[1])

def ImGui_SetNextWindowBgAlpha(ctx, alpha):
  if not hasattr(ImGui_SetNextWindowBgAlpha, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowBgAlpha')
    ImGui_SetNextWindowBgAlpha.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(alpha))
  ImGui_SetNextWindowBgAlpha.func(args[0], args[1])

def ImGui_SetNextWindowCollapsed(ctx, collapsed, condInOptional = None):
  if not hasattr(ImGui_SetNextWindowCollapsed, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowCollapsed')
    ImGui_SetNextWindowCollapsed.func = CFUNCTYPE(None, c_void_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(collapsed), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetNextWindowCollapsed.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_SetNextWindowContentSize(ctx, size_w, size_h):
  if not hasattr(ImGui_SetNextWindowContentSize, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowContentSize')
    ImGui_SetNextWindowContentSize.func = CFUNCTYPE(None, c_void_p, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(size_w), c_double(size_h))
  ImGui_SetNextWindowContentSize.func(args[0], args[1], args[2])

def ImGui_SetNextWindowDockID(ctx, dock_id, condInOptional = None):
  if not hasattr(ImGui_SetNextWindowDockID, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowDockID')
    ImGui_SetNextWindowDockID.func = CFUNCTYPE(None, c_void_p, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(dock_id), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetNextWindowDockID.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_SetNextWindowFocus(ctx):
  if not hasattr(ImGui_SetNextWindowFocus, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowFocus')
    ImGui_SetNextWindowFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_SetNextWindowFocus.func(args[0])

def ImGui_SetNextWindowPos(ctx, pos_x, pos_y, condInOptional = None, pivot_xInOptional = None, pivot_yInOptional = None):
  if not hasattr(ImGui_SetNextWindowPos, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowPos')
    ImGui_SetNextWindowPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(pos_x), c_double(pos_y), c_int(condInOptional) if condInOptional != None else None, c_double(pivot_xInOptional) if pivot_xInOptional != None else None, c_double(pivot_yInOptional) if pivot_yInOptional != None else None)
  ImGui_SetNextWindowPos.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, byref(args[5]) if args[5] != None else None)

def ImGui_SetNextWindowSize(ctx, size_w, size_h, condInOptional = None):
  if not hasattr(ImGui_SetNextWindowSize, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowSize')
    ImGui_SetNextWindowSize.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(size_w), c_double(size_h), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetNextWindowSize.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

def ImGui_SetNextWindowSizeConstraints(ctx, size_min_w, size_min_h, size_max_w, size_max_h):
  if not hasattr(ImGui_SetNextWindowSizeConstraints, 'func'):
    proc = rpr_getfp('ImGui_SetNextWindowSizeConstraints')
    ImGui_SetNextWindowSizeConstraints.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_double, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(size_min_w), c_double(size_min_h), c_double(size_max_w), c_double(size_max_h))
  ImGui_SetNextWindowSizeConstraints.func(args[0], args[1], args[2], args[3], args[4])

def ImGui_SetScrollFromPosX(ctx, local_x, center_x_ratioInOptional = None):
  if not hasattr(ImGui_SetScrollFromPosX, 'func'):
    proc = rpr_getfp('ImGui_SetScrollFromPosX')
    ImGui_SetScrollFromPosX.func = CFUNCTYPE(None, c_void_p, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(local_x), c_double(center_x_ratioInOptional) if center_x_ratioInOptional != None else None)
  ImGui_SetScrollFromPosX.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_SetScrollFromPosY(ctx, local_y, center_y_ratioInOptional = None):
  if not hasattr(ImGui_SetScrollFromPosY, 'func'):
    proc = rpr_getfp('ImGui_SetScrollFromPosY')
    ImGui_SetScrollFromPosY.func = CFUNCTYPE(None, c_void_p, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(local_y), c_double(center_y_ratioInOptional) if center_y_ratioInOptional != None else None)
  ImGui_SetScrollFromPosY.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_SetScrollHereX(ctx, center_x_ratioInOptional = None):
  if not hasattr(ImGui_SetScrollHereX, 'func'):
    proc = rpr_getfp('ImGui_SetScrollHereX')
    ImGui_SetScrollHereX.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(center_x_ratioInOptional) if center_x_ratioInOptional != None else None)
  ImGui_SetScrollHereX.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_SetScrollHereY(ctx, center_y_ratioInOptional = None):
  if not hasattr(ImGui_SetScrollHereY, 'func'):
    proc = rpr_getfp('ImGui_SetScrollHereY')
    ImGui_SetScrollHereY.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(center_y_ratioInOptional) if center_y_ratioInOptional != None else None)
  ImGui_SetScrollHereY.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_SetScrollX(ctx, scroll_x):
  if not hasattr(ImGui_SetScrollX, 'func'):
    proc = rpr_getfp('ImGui_SetScrollX')
    ImGui_SetScrollX.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(scroll_x))
  ImGui_SetScrollX.func(args[0], args[1])

def ImGui_SetScrollY(ctx, scroll_y):
  if not hasattr(ImGui_SetScrollY, 'func'):
    proc = rpr_getfp('ImGui_SetScrollY')
    ImGui_SetScrollY.func = CFUNCTYPE(None, c_void_p, c_double)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(scroll_y))
  ImGui_SetScrollY.func(args[0], args[1])

def ImGui_SetTabItemClosed(ctx, tab_or_docked_window_label):
  if not hasattr(ImGui_SetTabItemClosed, 'func'):
    proc = rpr_getfp('ImGui_SetTabItemClosed')
    ImGui_SetTabItemClosed.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(tab_or_docked_window_label))
  ImGui_SetTabItemClosed.func(args[0], args[1])

def ImGui_SetTooltip(ctx, text):
  if not hasattr(ImGui_SetTooltip, 'func'):
    proc = rpr_getfp('ImGui_SetTooltip')
    ImGui_SetTooltip.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_SetTooltip.func(args[0], args[1])

def ImGui_SetWindowCollapsed(ctx, collapsed, condInOptional = None):
  if not hasattr(ImGui_SetWindowCollapsed, 'func'):
    proc = rpr_getfp('ImGui_SetWindowCollapsed')
    ImGui_SetWindowCollapsed.func = CFUNCTYPE(None, c_void_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(collapsed), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetWindowCollapsed.func(args[0], args[1], byref(args[2]) if args[2] != None else None)

def ImGui_SetWindowCollapsedEx(ctx, name, collapsed, condInOptional = None):
  if not hasattr(ImGui_SetWindowCollapsedEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowCollapsedEx')
    ImGui_SetWindowCollapsedEx.func = CFUNCTYPE(None, c_void_p, c_char_p, c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(name), c_bool(collapsed), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetWindowCollapsedEx.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

def ImGui_SetWindowFocus(ctx):
  if not hasattr(ImGui_SetWindowFocus, 'func'):
    proc = rpr_getfp('ImGui_SetWindowFocus')
    ImGui_SetWindowFocus.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_SetWindowFocus.func(args[0])

def ImGui_SetWindowFocusEx(ctx, name):
  if not hasattr(ImGui_SetWindowFocusEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowFocusEx')
    ImGui_SetWindowFocusEx.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(name))
  ImGui_SetWindowFocusEx.func(args[0], args[1])

def ImGui_SetWindowPos(ctx, pos_x, pos_y, condInOptional = None):
  if not hasattr(ImGui_SetWindowPos, 'func'):
    proc = rpr_getfp('ImGui_SetWindowPos')
    ImGui_SetWindowPos.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(pos_x), c_double(pos_y), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetWindowPos.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

def ImGui_SetWindowPosEx(ctx, name, pos_x, pos_y, condInOptional = None):
  if not hasattr(ImGui_SetWindowPosEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowPosEx')
    ImGui_SetWindowPosEx.func = CFUNCTYPE(None, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(name), c_double(pos_x), c_double(pos_y), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetWindowPosEx.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)

def ImGui_SetWindowSize(ctx, size_w, size_h, condInOptional = None):
  if not hasattr(ImGui_SetWindowSize, 'func'):
    proc = rpr_getfp('ImGui_SetWindowSize')
    ImGui_SetWindowSize.func = CFUNCTYPE(None, c_void_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(size_w), c_double(size_h), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetWindowSize.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

def ImGui_SetWindowSizeEx(ctx, name, size_w, size_h, condInOptional = None):
  if not hasattr(ImGui_SetWindowSizeEx, 'func'):
    proc = rpr_getfp('ImGui_SetWindowSizeEx')
    ImGui_SetWindowSizeEx.func = CFUNCTYPE(None, c_void_p, c_char_p, c_double, c_double, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(name), c_double(size_w), c_double(size_h), c_int(condInOptional) if condInOptional != None else None)
  ImGui_SetWindowSizeEx.func(args[0], args[1], args[2], args[3], byref(args[4]) if args[4] != None else None)

def ImGui_ShowAboutWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ImGui_ShowAboutWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowAboutWindow')
    ImGui_ShowAboutWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ImGui_ShowAboutWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

def ImGui_ShowDebugLogWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ImGui_ShowDebugLogWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowDebugLogWindow')
    ImGui_ShowDebugLogWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ImGui_ShowDebugLogWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

def ImGui_ShowMetricsWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ImGui_ShowMetricsWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowMetricsWindow')
    ImGui_ShowMetricsWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ImGui_ShowMetricsWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

def ImGui_ShowStackToolWindow(ctx, p_openInOutOptional = None):
  if not hasattr(ImGui_ShowStackToolWindow, 'func'):
    proc = rpr_getfp('ImGui_ShowStackToolWindow')
    ImGui_ShowStackToolWindow.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(p_openInOutOptional) if p_openInOutOptional != None else None)
  ImGui_ShowStackToolWindow.func(args[0], byref(args[1]) if args[1] != None else None)
  return int(args[1].value) if p_openInOutOptional != None else None

def ImGui_SliderAngle(ctx, label, v_radInOut, v_degrees_minInOptional = None, v_degrees_maxInOptional = None, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderAngle, 'func'):
    proc = rpr_getfp('ImGui_SliderAngle')
    ImGui_SliderAngle.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v_radInOut), c_double(v_degrees_minInOptional) if v_degrees_minInOptional != None else None, c_double(v_degrees_maxInOptional) if v_degrees_maxInOptional != None else None, rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderAngle.func(args[0], args[1], byref(args[2]), byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None, args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value)

def ImGui_SliderDouble(ctx, label, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderDouble, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble')
    ImGui_SliderDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(vInOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderDouble.func(args[0], args[1], byref(args[2]), args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)
  return rval, float(args[2].value)

def ImGui_SliderDouble2(ctx, label, v1InOut, v2InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderDouble2, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble2')
    ImGui_SliderDouble2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderDouble2.func(args[0], args[1], byref(args[2]), byref(args[3]), args[4], args[5], args[6], byref(args[7]) if args[7] != None else None)
  return rval, float(args[2].value), float(args[3].value)

def ImGui_SliderDouble3(ctx, label, v1InOut, v2InOut, v3InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderDouble3, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble3')
    ImGui_SliderDouble3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderDouble3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value)

def ImGui_SliderDouble4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderDouble4, 'func'):
    proc = rpr_getfp('ImGui_SliderDouble4')
    ImGui_SliderDouble4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(v1InOut), c_double(v2InOut), c_double(v3InOut), c_double(v4InOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderDouble4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), args[6], args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, float(args[2].value), float(args[3].value), float(args[4].value), float(args[5].value)

def ImGui_SliderDoubleN(ctx, label, values, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderDoubleN, 'func'):
    proc = rpr_getfp('ImGui_SliderDoubleN')
    ImGui_SliderDoubleN.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), rpr_packp('reaper_array*', values), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderDoubleN.func(args[0], args[1], args[2], args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)
  return rval

def ImGui_SliderFlags_AlwaysClamp():
  if not hasattr(ImGui_SliderFlags_AlwaysClamp, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_AlwaysClamp')
    ImGui_SliderFlags_AlwaysClamp.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SliderFlags_AlwaysClamp, 'cache'):
    ImGui_SliderFlags_AlwaysClamp.cache = ImGui_SliderFlags_AlwaysClamp.func()
  return ImGui_SliderFlags_AlwaysClamp.cache

def ImGui_SliderFlags_Logarithmic():
  if not hasattr(ImGui_SliderFlags_Logarithmic, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_Logarithmic')
    ImGui_SliderFlags_Logarithmic.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SliderFlags_Logarithmic, 'cache'):
    ImGui_SliderFlags_Logarithmic.cache = ImGui_SliderFlags_Logarithmic.func()
  return ImGui_SliderFlags_Logarithmic.cache

def ImGui_SliderFlags_NoInput():
  if not hasattr(ImGui_SliderFlags_NoInput, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_NoInput')
    ImGui_SliderFlags_NoInput.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SliderFlags_NoInput, 'cache'):
    ImGui_SliderFlags_NoInput.cache = ImGui_SliderFlags_NoInput.func()
  return ImGui_SliderFlags_NoInput.cache

def ImGui_SliderFlags_NoRoundToFormat():
  if not hasattr(ImGui_SliderFlags_NoRoundToFormat, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_NoRoundToFormat')
    ImGui_SliderFlags_NoRoundToFormat.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SliderFlags_NoRoundToFormat, 'cache'):
    ImGui_SliderFlags_NoRoundToFormat.cache = ImGui_SliderFlags_NoRoundToFormat.func()
  return ImGui_SliderFlags_NoRoundToFormat.cache

def ImGui_SliderFlags_None():
  if not hasattr(ImGui_SliderFlags_None, 'func'):
    proc = rpr_getfp('ImGui_SliderFlags_None')
    ImGui_SliderFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SliderFlags_None, 'cache'):
    ImGui_SliderFlags_None.cache = ImGui_SliderFlags_None.func()
  return ImGui_SliderFlags_None.cache

def ImGui_SliderInt(ctx, label, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderInt, 'func'):
    proc = rpr_getfp('ImGui_SliderInt')
    ImGui_SliderInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(vInOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderInt.func(args[0], args[1], byref(args[2]), args[3], args[4], args[5], byref(args[6]) if args[6] != None else None)
  return rval, int(args[2].value)

def ImGui_SliderInt2(ctx, label, v1InOut, v2InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderInt2, 'func'):
    proc = rpr_getfp('ImGui_SliderInt2')
    ImGui_SliderInt2.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderInt2.func(args[0], args[1], byref(args[2]), byref(args[3]), args[4], args[5], args[6], byref(args[7]) if args[7] != None else None)
  return rval, int(args[2].value), int(args[3].value)

def ImGui_SliderInt3(ctx, label, v1InOut, v2InOut, v3InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderInt3, 'func'):
    proc = rpr_getfp('ImGui_SliderInt3')
    ImGui_SliderInt3.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderInt3.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value)

def ImGui_SliderInt4(ctx, label, v1InOut, v2InOut, v3InOut, v4InOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_SliderInt4, 'func'):
    proc = rpr_getfp('ImGui_SliderInt4')
    ImGui_SliderInt4.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(v1InOut), c_int(v2InOut), c_int(v3InOut), c_int(v4InOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_SliderInt4.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]), args[6], args[7], args[8], byref(args[9]) if args[9] != None else None)
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

def ImGui_SmallButton(ctx, label):
  if not hasattr(ImGui_SmallButton, 'func'):
    proc = rpr_getfp('ImGui_SmallButton')
    ImGui_SmallButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label))
  rval = ImGui_SmallButton.func(args[0], args[1])
  return rval

def ImGui_SortDirection_Ascending():
  if not hasattr(ImGui_SortDirection_Ascending, 'func'):
    proc = rpr_getfp('ImGui_SortDirection_Ascending')
    ImGui_SortDirection_Ascending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SortDirection_Ascending, 'cache'):
    ImGui_SortDirection_Ascending.cache = ImGui_SortDirection_Ascending.func()
  return ImGui_SortDirection_Ascending.cache

def ImGui_SortDirection_Descending():
  if not hasattr(ImGui_SortDirection_Descending, 'func'):
    proc = rpr_getfp('ImGui_SortDirection_Descending')
    ImGui_SortDirection_Descending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SortDirection_Descending, 'cache'):
    ImGui_SortDirection_Descending.cache = ImGui_SortDirection_Descending.func()
  return ImGui_SortDirection_Descending.cache

def ImGui_SortDirection_None():
  if not hasattr(ImGui_SortDirection_None, 'func'):
    proc = rpr_getfp('ImGui_SortDirection_None')
    ImGui_SortDirection_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_SortDirection_None, 'cache'):
    ImGui_SortDirection_None.cache = ImGui_SortDirection_None.func()
  return ImGui_SortDirection_None.cache

def ImGui_Spacing(ctx):
  if not hasattr(ImGui_Spacing, 'func'):
    proc = rpr_getfp('ImGui_Spacing')
    ImGui_Spacing.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_Spacing.func(args[0])

def ImGui_StyleVar_Alpha():
  if not hasattr(ImGui_StyleVar_Alpha, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_Alpha')
    ImGui_StyleVar_Alpha.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_Alpha, 'cache'):
    ImGui_StyleVar_Alpha.cache = ImGui_StyleVar_Alpha.func()
  return ImGui_StyleVar_Alpha.cache

def ImGui_StyleVar_ButtonTextAlign():
  if not hasattr(ImGui_StyleVar_ButtonTextAlign, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ButtonTextAlign')
    ImGui_StyleVar_ButtonTextAlign.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ButtonTextAlign, 'cache'):
    ImGui_StyleVar_ButtonTextAlign.cache = ImGui_StyleVar_ButtonTextAlign.func()
  return ImGui_StyleVar_ButtonTextAlign.cache

def ImGui_StyleVar_CellPadding():
  if not hasattr(ImGui_StyleVar_CellPadding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_CellPadding')
    ImGui_StyleVar_CellPadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_CellPadding, 'cache'):
    ImGui_StyleVar_CellPadding.cache = ImGui_StyleVar_CellPadding.func()
  return ImGui_StyleVar_CellPadding.cache

def ImGui_StyleVar_ChildBorderSize():
  if not hasattr(ImGui_StyleVar_ChildBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ChildBorderSize')
    ImGui_StyleVar_ChildBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ChildBorderSize, 'cache'):
    ImGui_StyleVar_ChildBorderSize.cache = ImGui_StyleVar_ChildBorderSize.func()
  return ImGui_StyleVar_ChildBorderSize.cache

def ImGui_StyleVar_ChildRounding():
  if not hasattr(ImGui_StyleVar_ChildRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ChildRounding')
    ImGui_StyleVar_ChildRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ChildRounding, 'cache'):
    ImGui_StyleVar_ChildRounding.cache = ImGui_StyleVar_ChildRounding.func()
  return ImGui_StyleVar_ChildRounding.cache

def ImGui_StyleVar_DisabledAlpha():
  if not hasattr(ImGui_StyleVar_DisabledAlpha, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_DisabledAlpha')
    ImGui_StyleVar_DisabledAlpha.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_DisabledAlpha, 'cache'):
    ImGui_StyleVar_DisabledAlpha.cache = ImGui_StyleVar_DisabledAlpha.func()
  return ImGui_StyleVar_DisabledAlpha.cache

def ImGui_StyleVar_FrameBorderSize():
  if not hasattr(ImGui_StyleVar_FrameBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_FrameBorderSize')
    ImGui_StyleVar_FrameBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_FrameBorderSize, 'cache'):
    ImGui_StyleVar_FrameBorderSize.cache = ImGui_StyleVar_FrameBorderSize.func()
  return ImGui_StyleVar_FrameBorderSize.cache

def ImGui_StyleVar_FramePadding():
  if not hasattr(ImGui_StyleVar_FramePadding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_FramePadding')
    ImGui_StyleVar_FramePadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_FramePadding, 'cache'):
    ImGui_StyleVar_FramePadding.cache = ImGui_StyleVar_FramePadding.func()
  return ImGui_StyleVar_FramePadding.cache

def ImGui_StyleVar_FrameRounding():
  if not hasattr(ImGui_StyleVar_FrameRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_FrameRounding')
    ImGui_StyleVar_FrameRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_FrameRounding, 'cache'):
    ImGui_StyleVar_FrameRounding.cache = ImGui_StyleVar_FrameRounding.func()
  return ImGui_StyleVar_FrameRounding.cache

def ImGui_StyleVar_GrabMinSize():
  if not hasattr(ImGui_StyleVar_GrabMinSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_GrabMinSize')
    ImGui_StyleVar_GrabMinSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_GrabMinSize, 'cache'):
    ImGui_StyleVar_GrabMinSize.cache = ImGui_StyleVar_GrabMinSize.func()
  return ImGui_StyleVar_GrabMinSize.cache

def ImGui_StyleVar_GrabRounding():
  if not hasattr(ImGui_StyleVar_GrabRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_GrabRounding')
    ImGui_StyleVar_GrabRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_GrabRounding, 'cache'):
    ImGui_StyleVar_GrabRounding.cache = ImGui_StyleVar_GrabRounding.func()
  return ImGui_StyleVar_GrabRounding.cache

def ImGui_StyleVar_IndentSpacing():
  if not hasattr(ImGui_StyleVar_IndentSpacing, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_IndentSpacing')
    ImGui_StyleVar_IndentSpacing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_IndentSpacing, 'cache'):
    ImGui_StyleVar_IndentSpacing.cache = ImGui_StyleVar_IndentSpacing.func()
  return ImGui_StyleVar_IndentSpacing.cache

def ImGui_StyleVar_ItemInnerSpacing():
  if not hasattr(ImGui_StyleVar_ItemInnerSpacing, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ItemInnerSpacing')
    ImGui_StyleVar_ItemInnerSpacing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ItemInnerSpacing, 'cache'):
    ImGui_StyleVar_ItemInnerSpacing.cache = ImGui_StyleVar_ItemInnerSpacing.func()
  return ImGui_StyleVar_ItemInnerSpacing.cache

def ImGui_StyleVar_ItemSpacing():
  if not hasattr(ImGui_StyleVar_ItemSpacing, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ItemSpacing')
    ImGui_StyleVar_ItemSpacing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ItemSpacing, 'cache'):
    ImGui_StyleVar_ItemSpacing.cache = ImGui_StyleVar_ItemSpacing.func()
  return ImGui_StyleVar_ItemSpacing.cache

def ImGui_StyleVar_PopupBorderSize():
  if not hasattr(ImGui_StyleVar_PopupBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_PopupBorderSize')
    ImGui_StyleVar_PopupBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_PopupBorderSize, 'cache'):
    ImGui_StyleVar_PopupBorderSize.cache = ImGui_StyleVar_PopupBorderSize.func()
  return ImGui_StyleVar_PopupBorderSize.cache

def ImGui_StyleVar_PopupRounding():
  if not hasattr(ImGui_StyleVar_PopupRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_PopupRounding')
    ImGui_StyleVar_PopupRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_PopupRounding, 'cache'):
    ImGui_StyleVar_PopupRounding.cache = ImGui_StyleVar_PopupRounding.func()
  return ImGui_StyleVar_PopupRounding.cache

def ImGui_StyleVar_ScrollbarRounding():
  if not hasattr(ImGui_StyleVar_ScrollbarRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ScrollbarRounding')
    ImGui_StyleVar_ScrollbarRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ScrollbarRounding, 'cache'):
    ImGui_StyleVar_ScrollbarRounding.cache = ImGui_StyleVar_ScrollbarRounding.func()
  return ImGui_StyleVar_ScrollbarRounding.cache

def ImGui_StyleVar_ScrollbarSize():
  if not hasattr(ImGui_StyleVar_ScrollbarSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_ScrollbarSize')
    ImGui_StyleVar_ScrollbarSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_ScrollbarSize, 'cache'):
    ImGui_StyleVar_ScrollbarSize.cache = ImGui_StyleVar_ScrollbarSize.func()
  return ImGui_StyleVar_ScrollbarSize.cache

def ImGui_StyleVar_SelectableTextAlign():
  if not hasattr(ImGui_StyleVar_SelectableTextAlign, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_SelectableTextAlign')
    ImGui_StyleVar_SelectableTextAlign.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_SelectableTextAlign, 'cache'):
    ImGui_StyleVar_SelectableTextAlign.cache = ImGui_StyleVar_SelectableTextAlign.func()
  return ImGui_StyleVar_SelectableTextAlign.cache

def ImGui_StyleVar_TabRounding():
  if not hasattr(ImGui_StyleVar_TabRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_TabRounding')
    ImGui_StyleVar_TabRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_TabRounding, 'cache'):
    ImGui_StyleVar_TabRounding.cache = ImGui_StyleVar_TabRounding.func()
  return ImGui_StyleVar_TabRounding.cache

def ImGui_StyleVar_WindowBorderSize():
  if not hasattr(ImGui_StyleVar_WindowBorderSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowBorderSize')
    ImGui_StyleVar_WindowBorderSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_WindowBorderSize, 'cache'):
    ImGui_StyleVar_WindowBorderSize.cache = ImGui_StyleVar_WindowBorderSize.func()
  return ImGui_StyleVar_WindowBorderSize.cache

def ImGui_StyleVar_WindowMinSize():
  if not hasattr(ImGui_StyleVar_WindowMinSize, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowMinSize')
    ImGui_StyleVar_WindowMinSize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_WindowMinSize, 'cache'):
    ImGui_StyleVar_WindowMinSize.cache = ImGui_StyleVar_WindowMinSize.func()
  return ImGui_StyleVar_WindowMinSize.cache

def ImGui_StyleVar_WindowPadding():
  if not hasattr(ImGui_StyleVar_WindowPadding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowPadding')
    ImGui_StyleVar_WindowPadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_WindowPadding, 'cache'):
    ImGui_StyleVar_WindowPadding.cache = ImGui_StyleVar_WindowPadding.func()
  return ImGui_StyleVar_WindowPadding.cache

def ImGui_StyleVar_WindowRounding():
  if not hasattr(ImGui_StyleVar_WindowRounding, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowRounding')
    ImGui_StyleVar_WindowRounding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_WindowRounding, 'cache'):
    ImGui_StyleVar_WindowRounding.cache = ImGui_StyleVar_WindowRounding.func()
  return ImGui_StyleVar_WindowRounding.cache

def ImGui_StyleVar_WindowTitleAlign():
  if not hasattr(ImGui_StyleVar_WindowTitleAlign, 'func'):
    proc = rpr_getfp('ImGui_StyleVar_WindowTitleAlign')
    ImGui_StyleVar_WindowTitleAlign.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_StyleVar_WindowTitleAlign, 'cache'):
    ImGui_StyleVar_WindowTitleAlign.cache = ImGui_StyleVar_WindowTitleAlign.func()
  return ImGui_StyleVar_WindowTitleAlign.cache

def ImGui_TabBarFlags_AutoSelectNewTabs():
  if not hasattr(ImGui_TabBarFlags_AutoSelectNewTabs, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_AutoSelectNewTabs')
    ImGui_TabBarFlags_AutoSelectNewTabs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_AutoSelectNewTabs, 'cache'):
    ImGui_TabBarFlags_AutoSelectNewTabs.cache = ImGui_TabBarFlags_AutoSelectNewTabs.func()
  return ImGui_TabBarFlags_AutoSelectNewTabs.cache

def ImGui_TabBarFlags_FittingPolicyResizeDown():
  if not hasattr(ImGui_TabBarFlags_FittingPolicyResizeDown, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_FittingPolicyResizeDown')
    ImGui_TabBarFlags_FittingPolicyResizeDown.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_FittingPolicyResizeDown, 'cache'):
    ImGui_TabBarFlags_FittingPolicyResizeDown.cache = ImGui_TabBarFlags_FittingPolicyResizeDown.func()
  return ImGui_TabBarFlags_FittingPolicyResizeDown.cache

def ImGui_TabBarFlags_FittingPolicyScroll():
  if not hasattr(ImGui_TabBarFlags_FittingPolicyScroll, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_FittingPolicyScroll')
    ImGui_TabBarFlags_FittingPolicyScroll.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_FittingPolicyScroll, 'cache'):
    ImGui_TabBarFlags_FittingPolicyScroll.cache = ImGui_TabBarFlags_FittingPolicyScroll.func()
  return ImGui_TabBarFlags_FittingPolicyScroll.cache

def ImGui_TabBarFlags_NoCloseWithMiddleMouseButton():
  if not hasattr(ImGui_TabBarFlags_NoCloseWithMiddleMouseButton, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_NoCloseWithMiddleMouseButton')
    ImGui_TabBarFlags_NoCloseWithMiddleMouseButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_NoCloseWithMiddleMouseButton, 'cache'):
    ImGui_TabBarFlags_NoCloseWithMiddleMouseButton.cache = ImGui_TabBarFlags_NoCloseWithMiddleMouseButton.func()
  return ImGui_TabBarFlags_NoCloseWithMiddleMouseButton.cache

def ImGui_TabBarFlags_NoTabListScrollingButtons():
  if not hasattr(ImGui_TabBarFlags_NoTabListScrollingButtons, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_NoTabListScrollingButtons')
    ImGui_TabBarFlags_NoTabListScrollingButtons.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_NoTabListScrollingButtons, 'cache'):
    ImGui_TabBarFlags_NoTabListScrollingButtons.cache = ImGui_TabBarFlags_NoTabListScrollingButtons.func()
  return ImGui_TabBarFlags_NoTabListScrollingButtons.cache

def ImGui_TabBarFlags_NoTooltip():
  if not hasattr(ImGui_TabBarFlags_NoTooltip, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_NoTooltip')
    ImGui_TabBarFlags_NoTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_NoTooltip, 'cache'):
    ImGui_TabBarFlags_NoTooltip.cache = ImGui_TabBarFlags_NoTooltip.func()
  return ImGui_TabBarFlags_NoTooltip.cache

def ImGui_TabBarFlags_None():
  if not hasattr(ImGui_TabBarFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_None')
    ImGui_TabBarFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_None, 'cache'):
    ImGui_TabBarFlags_None.cache = ImGui_TabBarFlags_None.func()
  return ImGui_TabBarFlags_None.cache

def ImGui_TabBarFlags_Reorderable():
  if not hasattr(ImGui_TabBarFlags_Reorderable, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_Reorderable')
    ImGui_TabBarFlags_Reorderable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_Reorderable, 'cache'):
    ImGui_TabBarFlags_Reorderable.cache = ImGui_TabBarFlags_Reorderable.func()
  return ImGui_TabBarFlags_Reorderable.cache

def ImGui_TabBarFlags_TabListPopupButton():
  if not hasattr(ImGui_TabBarFlags_TabListPopupButton, 'func'):
    proc = rpr_getfp('ImGui_TabBarFlags_TabListPopupButton')
    ImGui_TabBarFlags_TabListPopupButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabBarFlags_TabListPopupButton, 'cache'):
    ImGui_TabBarFlags_TabListPopupButton.cache = ImGui_TabBarFlags_TabListPopupButton.func()
  return ImGui_TabBarFlags_TabListPopupButton.cache

def ImGui_TabItemButton(ctx, label, flagsInOptional = None):
  if not hasattr(ImGui_TabItemButton, 'func'):
    proc = rpr_getfp('ImGui_TabItemButton')
    ImGui_TabItemButton.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_TabItemButton.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_TabItemFlags_Leading():
  if not hasattr(ImGui_TabItemFlags_Leading, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_Leading')
    ImGui_TabItemFlags_Leading.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_Leading, 'cache'):
    ImGui_TabItemFlags_Leading.cache = ImGui_TabItemFlags_Leading.func()
  return ImGui_TabItemFlags_Leading.cache

def ImGui_TabItemFlags_NoCloseWithMiddleMouseButton():
  if not hasattr(ImGui_TabItemFlags_NoCloseWithMiddleMouseButton, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoCloseWithMiddleMouseButton')
    ImGui_TabItemFlags_NoCloseWithMiddleMouseButton.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_NoCloseWithMiddleMouseButton, 'cache'):
    ImGui_TabItemFlags_NoCloseWithMiddleMouseButton.cache = ImGui_TabItemFlags_NoCloseWithMiddleMouseButton.func()
  return ImGui_TabItemFlags_NoCloseWithMiddleMouseButton.cache

def ImGui_TabItemFlags_NoPushId():
  if not hasattr(ImGui_TabItemFlags_NoPushId, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoPushId')
    ImGui_TabItemFlags_NoPushId.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_NoPushId, 'cache'):
    ImGui_TabItemFlags_NoPushId.cache = ImGui_TabItemFlags_NoPushId.func()
  return ImGui_TabItemFlags_NoPushId.cache

def ImGui_TabItemFlags_NoReorder():
  if not hasattr(ImGui_TabItemFlags_NoReorder, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoReorder')
    ImGui_TabItemFlags_NoReorder.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_NoReorder, 'cache'):
    ImGui_TabItemFlags_NoReorder.cache = ImGui_TabItemFlags_NoReorder.func()
  return ImGui_TabItemFlags_NoReorder.cache

def ImGui_TabItemFlags_NoTooltip():
  if not hasattr(ImGui_TabItemFlags_NoTooltip, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_NoTooltip')
    ImGui_TabItemFlags_NoTooltip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_NoTooltip, 'cache'):
    ImGui_TabItemFlags_NoTooltip.cache = ImGui_TabItemFlags_NoTooltip.func()
  return ImGui_TabItemFlags_NoTooltip.cache

def ImGui_TabItemFlags_None():
  if not hasattr(ImGui_TabItemFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_None')
    ImGui_TabItemFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_None, 'cache'):
    ImGui_TabItemFlags_None.cache = ImGui_TabItemFlags_None.func()
  return ImGui_TabItemFlags_None.cache

def ImGui_TabItemFlags_SetSelected():
  if not hasattr(ImGui_TabItemFlags_SetSelected, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_SetSelected')
    ImGui_TabItemFlags_SetSelected.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_SetSelected, 'cache'):
    ImGui_TabItemFlags_SetSelected.cache = ImGui_TabItemFlags_SetSelected.func()
  return ImGui_TabItemFlags_SetSelected.cache

def ImGui_TabItemFlags_Trailing():
  if not hasattr(ImGui_TabItemFlags_Trailing, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_Trailing')
    ImGui_TabItemFlags_Trailing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_Trailing, 'cache'):
    ImGui_TabItemFlags_Trailing.cache = ImGui_TabItemFlags_Trailing.func()
  return ImGui_TabItemFlags_Trailing.cache

def ImGui_TabItemFlags_UnsavedDocument():
  if not hasattr(ImGui_TabItemFlags_UnsavedDocument, 'func'):
    proc = rpr_getfp('ImGui_TabItemFlags_UnsavedDocument')
    ImGui_TabItemFlags_UnsavedDocument.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TabItemFlags_UnsavedDocument, 'cache'):
    ImGui_TabItemFlags_UnsavedDocument.cache = ImGui_TabItemFlags_UnsavedDocument.func()
  return ImGui_TabItemFlags_UnsavedDocument.cache

def ImGui_TableBgTarget_CellBg():
  if not hasattr(ImGui_TableBgTarget_CellBg, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_CellBg')
    ImGui_TableBgTarget_CellBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableBgTarget_CellBg, 'cache'):
    ImGui_TableBgTarget_CellBg.cache = ImGui_TableBgTarget_CellBg.func()
  return ImGui_TableBgTarget_CellBg.cache

def ImGui_TableBgTarget_None():
  if not hasattr(ImGui_TableBgTarget_None, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_None')
    ImGui_TableBgTarget_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableBgTarget_None, 'cache'):
    ImGui_TableBgTarget_None.cache = ImGui_TableBgTarget_None.func()
  return ImGui_TableBgTarget_None.cache

def ImGui_TableBgTarget_RowBg0():
  if not hasattr(ImGui_TableBgTarget_RowBg0, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_RowBg0')
    ImGui_TableBgTarget_RowBg0.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableBgTarget_RowBg0, 'cache'):
    ImGui_TableBgTarget_RowBg0.cache = ImGui_TableBgTarget_RowBg0.func()
  return ImGui_TableBgTarget_RowBg0.cache

def ImGui_TableBgTarget_RowBg1():
  if not hasattr(ImGui_TableBgTarget_RowBg1, 'func'):
    proc = rpr_getfp('ImGui_TableBgTarget_RowBg1')
    ImGui_TableBgTarget_RowBg1.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableBgTarget_RowBg1, 'cache'):
    ImGui_TableBgTarget_RowBg1.cache = ImGui_TableBgTarget_RowBg1.func()
  return ImGui_TableBgTarget_RowBg1.cache

def ImGui_TableColumnFlags_DefaultHide():
  if not hasattr(ImGui_TableColumnFlags_DefaultHide, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_DefaultHide')
    ImGui_TableColumnFlags_DefaultHide.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_DefaultHide, 'cache'):
    ImGui_TableColumnFlags_DefaultHide.cache = ImGui_TableColumnFlags_DefaultHide.func()
  return ImGui_TableColumnFlags_DefaultHide.cache

def ImGui_TableColumnFlags_DefaultSort():
  if not hasattr(ImGui_TableColumnFlags_DefaultSort, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_DefaultSort')
    ImGui_TableColumnFlags_DefaultSort.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_DefaultSort, 'cache'):
    ImGui_TableColumnFlags_DefaultSort.cache = ImGui_TableColumnFlags_DefaultSort.func()
  return ImGui_TableColumnFlags_DefaultSort.cache

def ImGui_TableColumnFlags_Disabled():
  if not hasattr(ImGui_TableColumnFlags_Disabled, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_Disabled')
    ImGui_TableColumnFlags_Disabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_Disabled, 'cache'):
    ImGui_TableColumnFlags_Disabled.cache = ImGui_TableColumnFlags_Disabled.func()
  return ImGui_TableColumnFlags_Disabled.cache

def ImGui_TableColumnFlags_IndentDisable():
  if not hasattr(ImGui_TableColumnFlags_IndentDisable, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IndentDisable')
    ImGui_TableColumnFlags_IndentDisable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_IndentDisable, 'cache'):
    ImGui_TableColumnFlags_IndentDisable.cache = ImGui_TableColumnFlags_IndentDisable.func()
  return ImGui_TableColumnFlags_IndentDisable.cache

def ImGui_TableColumnFlags_IndentEnable():
  if not hasattr(ImGui_TableColumnFlags_IndentEnable, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IndentEnable')
    ImGui_TableColumnFlags_IndentEnable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_IndentEnable, 'cache'):
    ImGui_TableColumnFlags_IndentEnable.cache = ImGui_TableColumnFlags_IndentEnable.func()
  return ImGui_TableColumnFlags_IndentEnable.cache

def ImGui_TableColumnFlags_IsEnabled():
  if not hasattr(ImGui_TableColumnFlags_IsEnabled, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsEnabled')
    ImGui_TableColumnFlags_IsEnabled.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_IsEnabled, 'cache'):
    ImGui_TableColumnFlags_IsEnabled.cache = ImGui_TableColumnFlags_IsEnabled.func()
  return ImGui_TableColumnFlags_IsEnabled.cache

def ImGui_TableColumnFlags_IsHovered():
  if not hasattr(ImGui_TableColumnFlags_IsHovered, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsHovered')
    ImGui_TableColumnFlags_IsHovered.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_IsHovered, 'cache'):
    ImGui_TableColumnFlags_IsHovered.cache = ImGui_TableColumnFlags_IsHovered.func()
  return ImGui_TableColumnFlags_IsHovered.cache

def ImGui_TableColumnFlags_IsSorted():
  if not hasattr(ImGui_TableColumnFlags_IsSorted, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsSorted')
    ImGui_TableColumnFlags_IsSorted.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_IsSorted, 'cache'):
    ImGui_TableColumnFlags_IsSorted.cache = ImGui_TableColumnFlags_IsSorted.func()
  return ImGui_TableColumnFlags_IsSorted.cache

def ImGui_TableColumnFlags_IsVisible():
  if not hasattr(ImGui_TableColumnFlags_IsVisible, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_IsVisible')
    ImGui_TableColumnFlags_IsVisible.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_IsVisible, 'cache'):
    ImGui_TableColumnFlags_IsVisible.cache = ImGui_TableColumnFlags_IsVisible.func()
  return ImGui_TableColumnFlags_IsVisible.cache

def ImGui_TableColumnFlags_NoClip():
  if not hasattr(ImGui_TableColumnFlags_NoClip, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoClip')
    ImGui_TableColumnFlags_NoClip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoClip, 'cache'):
    ImGui_TableColumnFlags_NoClip.cache = ImGui_TableColumnFlags_NoClip.func()
  return ImGui_TableColumnFlags_NoClip.cache

def ImGui_TableColumnFlags_NoHeaderLabel():
  if not hasattr(ImGui_TableColumnFlags_NoHeaderLabel, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoHeaderLabel')
    ImGui_TableColumnFlags_NoHeaderLabel.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoHeaderLabel, 'cache'):
    ImGui_TableColumnFlags_NoHeaderLabel.cache = ImGui_TableColumnFlags_NoHeaderLabel.func()
  return ImGui_TableColumnFlags_NoHeaderLabel.cache

def ImGui_TableColumnFlags_NoHeaderWidth():
  if not hasattr(ImGui_TableColumnFlags_NoHeaderWidth, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoHeaderWidth')
    ImGui_TableColumnFlags_NoHeaderWidth.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoHeaderWidth, 'cache'):
    ImGui_TableColumnFlags_NoHeaderWidth.cache = ImGui_TableColumnFlags_NoHeaderWidth.func()
  return ImGui_TableColumnFlags_NoHeaderWidth.cache

def ImGui_TableColumnFlags_NoHide():
  if not hasattr(ImGui_TableColumnFlags_NoHide, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoHide')
    ImGui_TableColumnFlags_NoHide.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoHide, 'cache'):
    ImGui_TableColumnFlags_NoHide.cache = ImGui_TableColumnFlags_NoHide.func()
  return ImGui_TableColumnFlags_NoHide.cache

def ImGui_TableColumnFlags_NoReorder():
  if not hasattr(ImGui_TableColumnFlags_NoReorder, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoReorder')
    ImGui_TableColumnFlags_NoReorder.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoReorder, 'cache'):
    ImGui_TableColumnFlags_NoReorder.cache = ImGui_TableColumnFlags_NoReorder.func()
  return ImGui_TableColumnFlags_NoReorder.cache

def ImGui_TableColumnFlags_NoResize():
  if not hasattr(ImGui_TableColumnFlags_NoResize, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoResize')
    ImGui_TableColumnFlags_NoResize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoResize, 'cache'):
    ImGui_TableColumnFlags_NoResize.cache = ImGui_TableColumnFlags_NoResize.func()
  return ImGui_TableColumnFlags_NoResize.cache

def ImGui_TableColumnFlags_NoSort():
  if not hasattr(ImGui_TableColumnFlags_NoSort, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoSort')
    ImGui_TableColumnFlags_NoSort.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoSort, 'cache'):
    ImGui_TableColumnFlags_NoSort.cache = ImGui_TableColumnFlags_NoSort.func()
  return ImGui_TableColumnFlags_NoSort.cache

def ImGui_TableColumnFlags_NoSortAscending():
  if not hasattr(ImGui_TableColumnFlags_NoSortAscending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoSortAscending')
    ImGui_TableColumnFlags_NoSortAscending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoSortAscending, 'cache'):
    ImGui_TableColumnFlags_NoSortAscending.cache = ImGui_TableColumnFlags_NoSortAscending.func()
  return ImGui_TableColumnFlags_NoSortAscending.cache

def ImGui_TableColumnFlags_NoSortDescending():
  if not hasattr(ImGui_TableColumnFlags_NoSortDescending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_NoSortDescending')
    ImGui_TableColumnFlags_NoSortDescending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_NoSortDescending, 'cache'):
    ImGui_TableColumnFlags_NoSortDescending.cache = ImGui_TableColumnFlags_NoSortDescending.func()
  return ImGui_TableColumnFlags_NoSortDescending.cache

def ImGui_TableColumnFlags_None():
  if not hasattr(ImGui_TableColumnFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_None')
    ImGui_TableColumnFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_None, 'cache'):
    ImGui_TableColumnFlags_None.cache = ImGui_TableColumnFlags_None.func()
  return ImGui_TableColumnFlags_None.cache

def ImGui_TableColumnFlags_PreferSortAscending():
  if not hasattr(ImGui_TableColumnFlags_PreferSortAscending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_PreferSortAscending')
    ImGui_TableColumnFlags_PreferSortAscending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_PreferSortAscending, 'cache'):
    ImGui_TableColumnFlags_PreferSortAscending.cache = ImGui_TableColumnFlags_PreferSortAscending.func()
  return ImGui_TableColumnFlags_PreferSortAscending.cache

def ImGui_TableColumnFlags_PreferSortDescending():
  if not hasattr(ImGui_TableColumnFlags_PreferSortDescending, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_PreferSortDescending')
    ImGui_TableColumnFlags_PreferSortDescending.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_PreferSortDescending, 'cache'):
    ImGui_TableColumnFlags_PreferSortDescending.cache = ImGui_TableColumnFlags_PreferSortDescending.func()
  return ImGui_TableColumnFlags_PreferSortDescending.cache

def ImGui_TableColumnFlags_WidthFixed():
  if not hasattr(ImGui_TableColumnFlags_WidthFixed, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_WidthFixed')
    ImGui_TableColumnFlags_WidthFixed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_WidthFixed, 'cache'):
    ImGui_TableColumnFlags_WidthFixed.cache = ImGui_TableColumnFlags_WidthFixed.func()
  return ImGui_TableColumnFlags_WidthFixed.cache

def ImGui_TableColumnFlags_WidthStretch():
  if not hasattr(ImGui_TableColumnFlags_WidthStretch, 'func'):
    proc = rpr_getfp('ImGui_TableColumnFlags_WidthStretch')
    ImGui_TableColumnFlags_WidthStretch.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableColumnFlags_WidthStretch, 'cache'):
    ImGui_TableColumnFlags_WidthStretch.cache = ImGui_TableColumnFlags_WidthStretch.func()
  return ImGui_TableColumnFlags_WidthStretch.cache

def ImGui_TableFlags_Borders():
  if not hasattr(ImGui_TableFlags_Borders, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Borders')
    ImGui_TableFlags_Borders.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_Borders, 'cache'):
    ImGui_TableFlags_Borders.cache = ImGui_TableFlags_Borders.func()
  return ImGui_TableFlags_Borders.cache

def ImGui_TableFlags_BordersH():
  if not hasattr(ImGui_TableFlags_BordersH, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersH')
    ImGui_TableFlags_BordersH.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersH, 'cache'):
    ImGui_TableFlags_BordersH.cache = ImGui_TableFlags_BordersH.func()
  return ImGui_TableFlags_BordersH.cache

def ImGui_TableFlags_BordersInner():
  if not hasattr(ImGui_TableFlags_BordersInner, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersInner')
    ImGui_TableFlags_BordersInner.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersInner, 'cache'):
    ImGui_TableFlags_BordersInner.cache = ImGui_TableFlags_BordersInner.func()
  return ImGui_TableFlags_BordersInner.cache

def ImGui_TableFlags_BordersInnerH():
  if not hasattr(ImGui_TableFlags_BordersInnerH, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersInnerH')
    ImGui_TableFlags_BordersInnerH.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersInnerH, 'cache'):
    ImGui_TableFlags_BordersInnerH.cache = ImGui_TableFlags_BordersInnerH.func()
  return ImGui_TableFlags_BordersInnerH.cache

def ImGui_TableFlags_BordersInnerV():
  if not hasattr(ImGui_TableFlags_BordersInnerV, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersInnerV')
    ImGui_TableFlags_BordersInnerV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersInnerV, 'cache'):
    ImGui_TableFlags_BordersInnerV.cache = ImGui_TableFlags_BordersInnerV.func()
  return ImGui_TableFlags_BordersInnerV.cache

def ImGui_TableFlags_BordersOuter():
  if not hasattr(ImGui_TableFlags_BordersOuter, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersOuter')
    ImGui_TableFlags_BordersOuter.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersOuter, 'cache'):
    ImGui_TableFlags_BordersOuter.cache = ImGui_TableFlags_BordersOuter.func()
  return ImGui_TableFlags_BordersOuter.cache

def ImGui_TableFlags_BordersOuterH():
  if not hasattr(ImGui_TableFlags_BordersOuterH, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersOuterH')
    ImGui_TableFlags_BordersOuterH.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersOuterH, 'cache'):
    ImGui_TableFlags_BordersOuterH.cache = ImGui_TableFlags_BordersOuterH.func()
  return ImGui_TableFlags_BordersOuterH.cache

def ImGui_TableFlags_BordersOuterV():
  if not hasattr(ImGui_TableFlags_BordersOuterV, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersOuterV')
    ImGui_TableFlags_BordersOuterV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersOuterV, 'cache'):
    ImGui_TableFlags_BordersOuterV.cache = ImGui_TableFlags_BordersOuterV.func()
  return ImGui_TableFlags_BordersOuterV.cache

def ImGui_TableFlags_BordersV():
  if not hasattr(ImGui_TableFlags_BordersV, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_BordersV')
    ImGui_TableFlags_BordersV.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_BordersV, 'cache'):
    ImGui_TableFlags_BordersV.cache = ImGui_TableFlags_BordersV.func()
  return ImGui_TableFlags_BordersV.cache

def ImGui_TableFlags_ContextMenuInBody():
  if not hasattr(ImGui_TableFlags_ContextMenuInBody, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_ContextMenuInBody')
    ImGui_TableFlags_ContextMenuInBody.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_ContextMenuInBody, 'cache'):
    ImGui_TableFlags_ContextMenuInBody.cache = ImGui_TableFlags_ContextMenuInBody.func()
  return ImGui_TableFlags_ContextMenuInBody.cache

def ImGui_TableFlags_Hideable():
  if not hasattr(ImGui_TableFlags_Hideable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Hideable')
    ImGui_TableFlags_Hideable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_Hideable, 'cache'):
    ImGui_TableFlags_Hideable.cache = ImGui_TableFlags_Hideable.func()
  return ImGui_TableFlags_Hideable.cache

def ImGui_TableFlags_NoClip():
  if not hasattr(ImGui_TableFlags_NoClip, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoClip')
    ImGui_TableFlags_NoClip.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoClip, 'cache'):
    ImGui_TableFlags_NoClip.cache = ImGui_TableFlags_NoClip.func()
  return ImGui_TableFlags_NoClip.cache

def ImGui_TableFlags_NoHostExtendX():
  if not hasattr(ImGui_TableFlags_NoHostExtendX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoHostExtendX')
    ImGui_TableFlags_NoHostExtendX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoHostExtendX, 'cache'):
    ImGui_TableFlags_NoHostExtendX.cache = ImGui_TableFlags_NoHostExtendX.func()
  return ImGui_TableFlags_NoHostExtendX.cache

def ImGui_TableFlags_NoHostExtendY():
  if not hasattr(ImGui_TableFlags_NoHostExtendY, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoHostExtendY')
    ImGui_TableFlags_NoHostExtendY.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoHostExtendY, 'cache'):
    ImGui_TableFlags_NoHostExtendY.cache = ImGui_TableFlags_NoHostExtendY.func()
  return ImGui_TableFlags_NoHostExtendY.cache

def ImGui_TableFlags_NoKeepColumnsVisible():
  if not hasattr(ImGui_TableFlags_NoKeepColumnsVisible, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoKeepColumnsVisible')
    ImGui_TableFlags_NoKeepColumnsVisible.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoKeepColumnsVisible, 'cache'):
    ImGui_TableFlags_NoKeepColumnsVisible.cache = ImGui_TableFlags_NoKeepColumnsVisible.func()
  return ImGui_TableFlags_NoKeepColumnsVisible.cache

def ImGui_TableFlags_NoPadInnerX():
  if not hasattr(ImGui_TableFlags_NoPadInnerX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoPadInnerX')
    ImGui_TableFlags_NoPadInnerX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoPadInnerX, 'cache'):
    ImGui_TableFlags_NoPadInnerX.cache = ImGui_TableFlags_NoPadInnerX.func()
  return ImGui_TableFlags_NoPadInnerX.cache

def ImGui_TableFlags_NoPadOuterX():
  if not hasattr(ImGui_TableFlags_NoPadOuterX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoPadOuterX')
    ImGui_TableFlags_NoPadOuterX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoPadOuterX, 'cache'):
    ImGui_TableFlags_NoPadOuterX.cache = ImGui_TableFlags_NoPadOuterX.func()
  return ImGui_TableFlags_NoPadOuterX.cache

def ImGui_TableFlags_NoSavedSettings():
  if not hasattr(ImGui_TableFlags_NoSavedSettings, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_NoSavedSettings')
    ImGui_TableFlags_NoSavedSettings.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_NoSavedSettings, 'cache'):
    ImGui_TableFlags_NoSavedSettings.cache = ImGui_TableFlags_NoSavedSettings.func()
  return ImGui_TableFlags_NoSavedSettings.cache

def ImGui_TableFlags_None():
  if not hasattr(ImGui_TableFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_None')
    ImGui_TableFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_None, 'cache'):
    ImGui_TableFlags_None.cache = ImGui_TableFlags_None.func()
  return ImGui_TableFlags_None.cache

def ImGui_TableFlags_PadOuterX():
  if not hasattr(ImGui_TableFlags_PadOuterX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_PadOuterX')
    ImGui_TableFlags_PadOuterX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_PadOuterX, 'cache'):
    ImGui_TableFlags_PadOuterX.cache = ImGui_TableFlags_PadOuterX.func()
  return ImGui_TableFlags_PadOuterX.cache

def ImGui_TableFlags_PreciseWidths():
  if not hasattr(ImGui_TableFlags_PreciseWidths, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_PreciseWidths')
    ImGui_TableFlags_PreciseWidths.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_PreciseWidths, 'cache'):
    ImGui_TableFlags_PreciseWidths.cache = ImGui_TableFlags_PreciseWidths.func()
  return ImGui_TableFlags_PreciseWidths.cache

def ImGui_TableFlags_Reorderable():
  if not hasattr(ImGui_TableFlags_Reorderable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Reorderable')
    ImGui_TableFlags_Reorderable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_Reorderable, 'cache'):
    ImGui_TableFlags_Reorderable.cache = ImGui_TableFlags_Reorderable.func()
  return ImGui_TableFlags_Reorderable.cache

def ImGui_TableFlags_Resizable():
  if not hasattr(ImGui_TableFlags_Resizable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Resizable')
    ImGui_TableFlags_Resizable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_Resizable, 'cache'):
    ImGui_TableFlags_Resizable.cache = ImGui_TableFlags_Resizable.func()
  return ImGui_TableFlags_Resizable.cache

def ImGui_TableFlags_RowBg():
  if not hasattr(ImGui_TableFlags_RowBg, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_RowBg')
    ImGui_TableFlags_RowBg.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_RowBg, 'cache'):
    ImGui_TableFlags_RowBg.cache = ImGui_TableFlags_RowBg.func()
  return ImGui_TableFlags_RowBg.cache

def ImGui_TableFlags_ScrollX():
  if not hasattr(ImGui_TableFlags_ScrollX, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_ScrollX')
    ImGui_TableFlags_ScrollX.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_ScrollX, 'cache'):
    ImGui_TableFlags_ScrollX.cache = ImGui_TableFlags_ScrollX.func()
  return ImGui_TableFlags_ScrollX.cache

def ImGui_TableFlags_ScrollY():
  if not hasattr(ImGui_TableFlags_ScrollY, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_ScrollY')
    ImGui_TableFlags_ScrollY.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_ScrollY, 'cache'):
    ImGui_TableFlags_ScrollY.cache = ImGui_TableFlags_ScrollY.func()
  return ImGui_TableFlags_ScrollY.cache

def ImGui_TableFlags_SizingFixedFit():
  if not hasattr(ImGui_TableFlags_SizingFixedFit, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingFixedFit')
    ImGui_TableFlags_SizingFixedFit.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_SizingFixedFit, 'cache'):
    ImGui_TableFlags_SizingFixedFit.cache = ImGui_TableFlags_SizingFixedFit.func()
  return ImGui_TableFlags_SizingFixedFit.cache

def ImGui_TableFlags_SizingFixedSame():
  if not hasattr(ImGui_TableFlags_SizingFixedSame, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingFixedSame')
    ImGui_TableFlags_SizingFixedSame.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_SizingFixedSame, 'cache'):
    ImGui_TableFlags_SizingFixedSame.cache = ImGui_TableFlags_SizingFixedSame.func()
  return ImGui_TableFlags_SizingFixedSame.cache

def ImGui_TableFlags_SizingStretchProp():
  if not hasattr(ImGui_TableFlags_SizingStretchProp, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingStretchProp')
    ImGui_TableFlags_SizingStretchProp.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_SizingStretchProp, 'cache'):
    ImGui_TableFlags_SizingStretchProp.cache = ImGui_TableFlags_SizingStretchProp.func()
  return ImGui_TableFlags_SizingStretchProp.cache

def ImGui_TableFlags_SizingStretchSame():
  if not hasattr(ImGui_TableFlags_SizingStretchSame, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SizingStretchSame')
    ImGui_TableFlags_SizingStretchSame.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_SizingStretchSame, 'cache'):
    ImGui_TableFlags_SizingStretchSame.cache = ImGui_TableFlags_SizingStretchSame.func()
  return ImGui_TableFlags_SizingStretchSame.cache

def ImGui_TableFlags_SortMulti():
  if not hasattr(ImGui_TableFlags_SortMulti, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SortMulti')
    ImGui_TableFlags_SortMulti.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_SortMulti, 'cache'):
    ImGui_TableFlags_SortMulti.cache = ImGui_TableFlags_SortMulti.func()
  return ImGui_TableFlags_SortMulti.cache

def ImGui_TableFlags_SortTristate():
  if not hasattr(ImGui_TableFlags_SortTristate, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_SortTristate')
    ImGui_TableFlags_SortTristate.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_SortTristate, 'cache'):
    ImGui_TableFlags_SortTristate.cache = ImGui_TableFlags_SortTristate.func()
  return ImGui_TableFlags_SortTristate.cache

def ImGui_TableFlags_Sortable():
  if not hasattr(ImGui_TableFlags_Sortable, 'func'):
    proc = rpr_getfp('ImGui_TableFlags_Sortable')
    ImGui_TableFlags_Sortable.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableFlags_Sortable, 'cache'):
    ImGui_TableFlags_Sortable.cache = ImGui_TableFlags_Sortable.func()
  return ImGui_TableFlags_Sortable.cache

def ImGui_TableGetColumnCount(ctx):
  if not hasattr(ImGui_TableGetColumnCount, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnCount')
    ImGui_TableGetColumnCount.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_TableGetColumnCount.func(args[0])
  return rval

def ImGui_TableGetColumnFlags(ctx, column_nInOptional = None):
  if not hasattr(ImGui_TableGetColumnFlags, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnFlags')
    ImGui_TableGetColumnFlags.func = CFUNCTYPE(c_int, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(column_nInOptional) if column_nInOptional != None else None)
  rval = ImGui_TableGetColumnFlags.func(args[0], byref(args[1]) if args[1] != None else None)
  return rval

def ImGui_TableGetColumnIndex(ctx):
  if not hasattr(ImGui_TableGetColumnIndex, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnIndex')
    ImGui_TableGetColumnIndex.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_TableGetColumnIndex.func(args[0])
  return rval

def ImGui_TableGetColumnName(ctx, column_nInOptional = None):
  if not hasattr(ImGui_TableGetColumnName, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnName')
    ImGui_TableGetColumnName.func = CFUNCTYPE(c_char_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(column_nInOptional) if column_nInOptional != None else None)
  rval = ImGui_TableGetColumnName.func(args[0], byref(args[1]) if args[1] != None else None)
  return str(rval.decode())

def ImGui_TableGetColumnSortSpecs(ctx):
  if not hasattr(ImGui_TableGetColumnSortSpecs, 'func'):
    proc = rpr_getfp('ImGui_TableGetColumnSortSpecs')
    ImGui_TableGetColumnSortSpecs.func = CFUNCTYPE(c_bool, c_void_p, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(len(id)+1), c_int(0), c_int(0), c_int(0), c_int(0))
  rval = ImGui_TableGetColumnSortSpecs.func(args[0], args[1], byref(args[2]), byref(args[3]), byref(args[4]), byref(args[5]))
  return rval, int(args[2].value), int(args[3].value), int(args[4].value), int(args[5].value)

def ImGui_TableGetRowIndex(ctx):
  if not hasattr(ImGui_TableGetRowIndex, 'func'):
    proc = rpr_getfp('ImGui_TableGetRowIndex')
    ImGui_TableGetRowIndex.func = CFUNCTYPE(c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_TableGetRowIndex.func(args[0])
  return rval

def ImGui_TableHeader(ctx, label):
  if not hasattr(ImGui_TableHeader, 'func'):
    proc = rpr_getfp('ImGui_TableHeader')
    ImGui_TableHeader.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label))
  ImGui_TableHeader.func(args[0], args[1])

def ImGui_TableHeadersRow(ctx):
  if not hasattr(ImGui_TableHeadersRow, 'func'):
    proc = rpr_getfp('ImGui_TableHeadersRow')
    ImGui_TableHeadersRow.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_TableHeadersRow.func(args[0])

def ImGui_TableNeedSort(ctx):
  if not hasattr(ImGui_TableNeedSort, 'func'):
    proc = rpr_getfp('ImGui_TableNeedSort')
    ImGui_TableNeedSort.func = CFUNCTYPE(c_bool, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_bool(0))
  rval = ImGui_TableNeedSort.func(args[0], byref(args[1]))
  return rval, int(args[1].value)

def ImGui_TableNextColumn(ctx):
  if not hasattr(ImGui_TableNextColumn, 'func'):
    proc = rpr_getfp('ImGui_TableNextColumn')
    ImGui_TableNextColumn.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  rval = ImGui_TableNextColumn.func(args[0])
  return rval

def ImGui_TableNextRow(ctx, row_flagsInOptional = None, min_row_heightInOptional = None):
  if not hasattr(ImGui_TableNextRow, 'func'):
    proc = rpr_getfp('ImGui_TableNextRow')
    ImGui_TableNextRow.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(row_flagsInOptional) if row_flagsInOptional != None else None, c_double(min_row_heightInOptional) if min_row_heightInOptional != None else None)
  ImGui_TableNextRow.func(args[0], byref(args[1]) if args[1] != None else None, byref(args[2]) if args[2] != None else None)

def ImGui_TableRowFlags_Headers():
  if not hasattr(ImGui_TableRowFlags_Headers, 'func'):
    proc = rpr_getfp('ImGui_TableRowFlags_Headers')
    ImGui_TableRowFlags_Headers.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableRowFlags_Headers, 'cache'):
    ImGui_TableRowFlags_Headers.cache = ImGui_TableRowFlags_Headers.func()
  return ImGui_TableRowFlags_Headers.cache

def ImGui_TableRowFlags_None():
  if not hasattr(ImGui_TableRowFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TableRowFlags_None')
    ImGui_TableRowFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TableRowFlags_None, 'cache'):
    ImGui_TableRowFlags_None.cache = ImGui_TableRowFlags_None.func()
  return ImGui_TableRowFlags_None.cache

def ImGui_TableSetBgColor(ctx, target, color_rgba, column_nInOptional = None):
  if not hasattr(ImGui_TableSetBgColor, 'func'):
    proc = rpr_getfp('ImGui_TableSetBgColor')
    ImGui_TableSetBgColor.func = CFUNCTYPE(None, c_void_p, c_int, c_int, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(target), c_int(color_rgba), c_int(column_nInOptional) if column_nInOptional != None else None)
  ImGui_TableSetBgColor.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)

def ImGui_TableSetColumnEnabled(ctx, column_n, v):
  if not hasattr(ImGui_TableSetColumnEnabled, 'func'):
    proc = rpr_getfp('ImGui_TableSetColumnEnabled')
    ImGui_TableSetColumnEnabled.func = CFUNCTYPE(None, c_void_p, c_int, c_bool)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(column_n), c_bool(v))
  ImGui_TableSetColumnEnabled.func(args[0], args[1], args[2])

def ImGui_TableSetColumnIndex(ctx, column_n):
  if not hasattr(ImGui_TableSetColumnIndex, 'func'):
    proc = rpr_getfp('ImGui_TableSetColumnIndex')
    ImGui_TableSetColumnIndex.func = CFUNCTYPE(c_bool, c_void_p, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(column_n))
  rval = ImGui_TableSetColumnIndex.func(args[0], args[1])
  return rval

def ImGui_TableSetupColumn(ctx, label, flagsInOptional = None, init_width_or_weightInOptional = None, user_idInOptional = None):
  if not hasattr(ImGui_TableSetupColumn, 'func'):
    proc = rpr_getfp('ImGui_TableSetupColumn')
    ImGui_TableSetupColumn.func = CFUNCTYPE(None, c_void_p, c_char_p, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None, c_double(init_width_or_weightInOptional) if init_width_or_weightInOptional != None else None, c_int(user_idInOptional) if user_idInOptional != None else None)
  ImGui_TableSetupColumn.func(args[0], args[1], byref(args[2]) if args[2] != None else None, byref(args[3]) if args[3] != None else None, byref(args[4]) if args[4] != None else None)

def ImGui_TableSetupScrollFreeze(ctx, cols, rows):
  if not hasattr(ImGui_TableSetupScrollFreeze, 'func'):
    proc = rpr_getfp('ImGui_TableSetupScrollFreeze')
    ImGui_TableSetupScrollFreeze.func = CFUNCTYPE(None, c_void_p, c_int, c_int)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(cols), c_int(rows))
  ImGui_TableSetupScrollFreeze.func(args[0], args[1], args[2])

def ImGui_Text(ctx, text):
  if not hasattr(ImGui_Text, 'func'):
    proc = rpr_getfp('ImGui_Text')
    ImGui_Text.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_Text.func(args[0], args[1])

def ImGui_TextColored(ctx, col_rgba, text):
  if not hasattr(ImGui_TextColored, 'func'):
    proc = rpr_getfp('ImGui_TextColored')
    ImGui_TextColored.func = CFUNCTYPE(None, c_void_p, c_int, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_int(col_rgba), rpr_packsc(text))
  ImGui_TextColored.func(args[0], args[1], args[2])

def ImGui_TextDisabled(ctx, text):
  if not hasattr(ImGui_TextDisabled, 'func'):
    proc = rpr_getfp('ImGui_TextDisabled')
    ImGui_TextDisabled.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_TextDisabled.func(args[0], args[1])

def ImGui_TextFilter_Clear(filter):
  if not hasattr(ImGui_TextFilter_Clear, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Clear')
    ImGui_TextFilter_Clear.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_TextFilter*', filter),)
  ImGui_TextFilter_Clear.func(args[0])

def ImGui_TextFilter_Draw(filter, ctx, labelInOptional = None, widthInOptional = None):
  if not hasattr(ImGui_TextFilter_Draw, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Draw')
    ImGui_TextFilter_Draw.func = CFUNCTYPE(c_bool, c_void_p, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_TextFilter*', filter), rpr_packp('ImGui_Context*', ctx), rpr_packsc(labelInOptional) if labelInOptional != None else None, c_double(widthInOptional) if widthInOptional != None else None)
  rval = ImGui_TextFilter_Draw.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

def ImGui_TextFilter_Get(filter):
  if not hasattr(ImGui_TextFilter_Get, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Get')
    ImGui_TextFilter_Get.func = CFUNCTYPE(c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_TextFilter*', filter),)
  rval = ImGui_TextFilter_Get.func(args[0])
  return str(rval.decode())

def ImGui_TextFilter_IsActive(filter):
  if not hasattr(ImGui_TextFilter_IsActive, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_IsActive')
    ImGui_TextFilter_IsActive.func = CFUNCTYPE(c_bool, c_void_p)(proc)
  args = (rpr_packp('ImGui_TextFilter*', filter),)
  rval = ImGui_TextFilter_IsActive.func(args[0])
  return rval

def ImGui_TextFilter_PassFilter(filter, text):
  if not hasattr(ImGui_TextFilter_PassFilter, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_PassFilter')
    ImGui_TextFilter_PassFilter.func = CFUNCTYPE(c_bool, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_TextFilter*', filter), rpr_packsc(text))
  rval = ImGui_TextFilter_PassFilter.func(args[0], args[1])
  return rval

def ImGui_TextFilter_Set(filter, filter_text):
  if not hasattr(ImGui_TextFilter_Set, 'func'):
    proc = rpr_getfp('ImGui_TextFilter_Set')
    ImGui_TextFilter_Set.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_TextFilter*', filter), rpr_packsc(filter_text))
  ImGui_TextFilter_Set.func(args[0], args[1])

def ImGui_TextWrapped(ctx, text):
  if not hasattr(ImGui_TextWrapped, 'func'):
    proc = rpr_getfp('ImGui_TextWrapped')
    ImGui_TextWrapped.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(text))
  ImGui_TextWrapped.func(args[0], args[1])

def ImGui_TreeNode(ctx, label, flagsInOptional = None):
  if not hasattr(ImGui_TreeNode, 'func'):
    proc = rpr_getfp('ImGui_TreeNode')
    ImGui_TreeNode.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_TreeNode.func(args[0], args[1], byref(args[2]) if args[2] != None else None)
  return rval

def ImGui_TreeNodeEx(ctx, str_id, label, flagsInOptional = None):
  if not hasattr(ImGui_TreeNodeEx, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeEx')
    ImGui_TreeNodeEx.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id), rpr_packsc(label), c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_TreeNodeEx.func(args[0], args[1], args[2], byref(args[3]) if args[3] != None else None)
  return rval

def ImGui_TreeNodeFlags_AllowItemOverlap():
  if not hasattr(ImGui_TreeNodeFlags_AllowItemOverlap, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_AllowItemOverlap')
    ImGui_TreeNodeFlags_AllowItemOverlap.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_AllowItemOverlap, 'cache'):
    ImGui_TreeNodeFlags_AllowItemOverlap.cache = ImGui_TreeNodeFlags_AllowItemOverlap.func()
  return ImGui_TreeNodeFlags_AllowItemOverlap.cache

def ImGui_TreeNodeFlags_Bullet():
  if not hasattr(ImGui_TreeNodeFlags_Bullet, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Bullet')
    ImGui_TreeNodeFlags_Bullet.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_Bullet, 'cache'):
    ImGui_TreeNodeFlags_Bullet.cache = ImGui_TreeNodeFlags_Bullet.func()
  return ImGui_TreeNodeFlags_Bullet.cache

def ImGui_TreeNodeFlags_CollapsingHeader():
  if not hasattr(ImGui_TreeNodeFlags_CollapsingHeader, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_CollapsingHeader')
    ImGui_TreeNodeFlags_CollapsingHeader.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_CollapsingHeader, 'cache'):
    ImGui_TreeNodeFlags_CollapsingHeader.cache = ImGui_TreeNodeFlags_CollapsingHeader.func()
  return ImGui_TreeNodeFlags_CollapsingHeader.cache

def ImGui_TreeNodeFlags_DefaultOpen():
  if not hasattr(ImGui_TreeNodeFlags_DefaultOpen, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_DefaultOpen')
    ImGui_TreeNodeFlags_DefaultOpen.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_DefaultOpen, 'cache'):
    ImGui_TreeNodeFlags_DefaultOpen.cache = ImGui_TreeNodeFlags_DefaultOpen.func()
  return ImGui_TreeNodeFlags_DefaultOpen.cache

def ImGui_TreeNodeFlags_FramePadding():
  if not hasattr(ImGui_TreeNodeFlags_FramePadding, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_FramePadding')
    ImGui_TreeNodeFlags_FramePadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_FramePadding, 'cache'):
    ImGui_TreeNodeFlags_FramePadding.cache = ImGui_TreeNodeFlags_FramePadding.func()
  return ImGui_TreeNodeFlags_FramePadding.cache

def ImGui_TreeNodeFlags_Framed():
  if not hasattr(ImGui_TreeNodeFlags_Framed, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Framed')
    ImGui_TreeNodeFlags_Framed.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_Framed, 'cache'):
    ImGui_TreeNodeFlags_Framed.cache = ImGui_TreeNodeFlags_Framed.func()
  return ImGui_TreeNodeFlags_Framed.cache

def ImGui_TreeNodeFlags_Leaf():
  if not hasattr(ImGui_TreeNodeFlags_Leaf, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Leaf')
    ImGui_TreeNodeFlags_Leaf.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_Leaf, 'cache'):
    ImGui_TreeNodeFlags_Leaf.cache = ImGui_TreeNodeFlags_Leaf.func()
  return ImGui_TreeNodeFlags_Leaf.cache

def ImGui_TreeNodeFlags_NoAutoOpenOnLog():
  if not hasattr(ImGui_TreeNodeFlags_NoAutoOpenOnLog, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_NoAutoOpenOnLog')
    ImGui_TreeNodeFlags_NoAutoOpenOnLog.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_NoAutoOpenOnLog, 'cache'):
    ImGui_TreeNodeFlags_NoAutoOpenOnLog.cache = ImGui_TreeNodeFlags_NoAutoOpenOnLog.func()
  return ImGui_TreeNodeFlags_NoAutoOpenOnLog.cache

def ImGui_TreeNodeFlags_NoTreePushOnOpen():
  if not hasattr(ImGui_TreeNodeFlags_NoTreePushOnOpen, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_NoTreePushOnOpen')
    ImGui_TreeNodeFlags_NoTreePushOnOpen.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_NoTreePushOnOpen, 'cache'):
    ImGui_TreeNodeFlags_NoTreePushOnOpen.cache = ImGui_TreeNodeFlags_NoTreePushOnOpen.func()
  return ImGui_TreeNodeFlags_NoTreePushOnOpen.cache

def ImGui_TreeNodeFlags_None():
  if not hasattr(ImGui_TreeNodeFlags_None, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_None')
    ImGui_TreeNodeFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_None, 'cache'):
    ImGui_TreeNodeFlags_None.cache = ImGui_TreeNodeFlags_None.func()
  return ImGui_TreeNodeFlags_None.cache

def ImGui_TreeNodeFlags_OpenOnArrow():
  if not hasattr(ImGui_TreeNodeFlags_OpenOnArrow, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_OpenOnArrow')
    ImGui_TreeNodeFlags_OpenOnArrow.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_OpenOnArrow, 'cache'):
    ImGui_TreeNodeFlags_OpenOnArrow.cache = ImGui_TreeNodeFlags_OpenOnArrow.func()
  return ImGui_TreeNodeFlags_OpenOnArrow.cache

def ImGui_TreeNodeFlags_OpenOnDoubleClick():
  if not hasattr(ImGui_TreeNodeFlags_OpenOnDoubleClick, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_OpenOnDoubleClick')
    ImGui_TreeNodeFlags_OpenOnDoubleClick.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_OpenOnDoubleClick, 'cache'):
    ImGui_TreeNodeFlags_OpenOnDoubleClick.cache = ImGui_TreeNodeFlags_OpenOnDoubleClick.func()
  return ImGui_TreeNodeFlags_OpenOnDoubleClick.cache

def ImGui_TreeNodeFlags_Selected():
  if not hasattr(ImGui_TreeNodeFlags_Selected, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_Selected')
    ImGui_TreeNodeFlags_Selected.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_Selected, 'cache'):
    ImGui_TreeNodeFlags_Selected.cache = ImGui_TreeNodeFlags_Selected.func()
  return ImGui_TreeNodeFlags_Selected.cache

def ImGui_TreeNodeFlags_SpanAvailWidth():
  if not hasattr(ImGui_TreeNodeFlags_SpanAvailWidth, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_SpanAvailWidth')
    ImGui_TreeNodeFlags_SpanAvailWidth.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_SpanAvailWidth, 'cache'):
    ImGui_TreeNodeFlags_SpanAvailWidth.cache = ImGui_TreeNodeFlags_SpanAvailWidth.func()
  return ImGui_TreeNodeFlags_SpanAvailWidth.cache

def ImGui_TreeNodeFlags_SpanFullWidth():
  if not hasattr(ImGui_TreeNodeFlags_SpanFullWidth, 'func'):
    proc = rpr_getfp('ImGui_TreeNodeFlags_SpanFullWidth')
    ImGui_TreeNodeFlags_SpanFullWidth.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_TreeNodeFlags_SpanFullWidth, 'cache'):
    ImGui_TreeNodeFlags_SpanFullWidth.cache = ImGui_TreeNodeFlags_SpanFullWidth.func()
  return ImGui_TreeNodeFlags_SpanFullWidth.cache

def ImGui_TreePop(ctx):
  if not hasattr(ImGui_TreePop, 'func'):
    proc = rpr_getfp('ImGui_TreePop')
    ImGui_TreePop.func = CFUNCTYPE(None, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx),)
  ImGui_TreePop.func(args[0])

def ImGui_TreePush(ctx, str_id):
  if not hasattr(ImGui_TreePush, 'func'):
    proc = rpr_getfp('ImGui_TreePush')
    ImGui_TreePush.func = CFUNCTYPE(None, c_void_p, c_char_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(str_id))
  ImGui_TreePush.func(args[0], args[1])

def ImGui_Unindent(ctx, indent_wInOptional = None):
  if not hasattr(ImGui_Unindent, 'func'):
    proc = rpr_getfp('ImGui_Unindent')
    ImGui_Unindent.func = CFUNCTYPE(None, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), c_double(indent_wInOptional) if indent_wInOptional != None else None)
  ImGui_Unindent.func(args[0], byref(args[1]) if args[1] != None else None)

def ImGui_VSliderDouble(ctx, label, size_w, size_h, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_VSliderDouble, 'func'):
    proc = rpr_getfp('ImGui_VSliderDouble')
    ImGui_VSliderDouble.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p, c_double, c_double, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(size_w), c_double(size_h), c_double(vInOut), c_double(v_min), c_double(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_VSliderDouble.func(args[0], args[1], args[2], args[3], byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, float(args[4].value)

def ImGui_VSliderInt(ctx, label, size_w, size_h, vInOut, v_min, v_max, formatInOptional = None, flagsInOptional = None):
  if not hasattr(ImGui_VSliderInt, 'func'):
    proc = rpr_getfp('ImGui_VSliderInt')
    ImGui_VSliderInt.func = CFUNCTYPE(c_bool, c_void_p, c_char_p, c_double, c_double, c_void_p, c_int, c_int, c_char_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Context*', ctx), rpr_packsc(label), c_double(size_w), c_double(size_h), c_int(vInOut), c_int(v_min), c_int(v_max), rpr_packsc(formatInOptional) if formatInOptional != None else None, c_int(flagsInOptional) if flagsInOptional != None else None)
  rval = ImGui_VSliderInt.func(args[0], args[1], args[2], args[3], byref(args[4]), args[5], args[6], args[7], byref(args[8]) if args[8] != None else None)
  return rval, int(args[4].value)

def ImGui_ValidatePtr(pointer, type):
  if not hasattr(ImGui_ValidatePtr, 'func'):
    proc = rpr_getfp('ImGui_ValidatePtr')
    ImGui_ValidatePtr.func = CFUNCTYPE(c_bool, c_void_p, c_char_p)(proc)
  args = (rpr_packp('void*', pointer), rpr_packsc(type))
  rval = ImGui_ValidatePtr.func(args[0], args[1])
  return rval

def ImGui_Viewport_GetCenter(viewport):
  if not hasattr(ImGui_Viewport_GetCenter, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetCenter')
    ImGui_Viewport_GetCenter.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Viewport*', viewport), c_double(0), c_double(0))
  ImGui_Viewport_GetCenter.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_Viewport_GetPos(viewport):
  if not hasattr(ImGui_Viewport_GetPos, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetPos')
    ImGui_Viewport_GetPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Viewport*', viewport), c_double(0), c_double(0))
  ImGui_Viewport_GetPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_Viewport_GetSize(viewport):
  if not hasattr(ImGui_Viewport_GetSize, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetSize')
    ImGui_Viewport_GetSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Viewport*', viewport), c_double(0), c_double(0))
  ImGui_Viewport_GetSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_Viewport_GetWorkCenter(viewport):
  if not hasattr(ImGui_Viewport_GetWorkCenter, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetWorkCenter')
    ImGui_Viewport_GetWorkCenter.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Viewport*', viewport), c_double(0), c_double(0))
  ImGui_Viewport_GetWorkCenter.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_Viewport_GetWorkPos(viewport):
  if not hasattr(ImGui_Viewport_GetWorkPos, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetWorkPos')
    ImGui_Viewport_GetWorkPos.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Viewport*', viewport), c_double(0), c_double(0))
  ImGui_Viewport_GetWorkPos.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_Viewport_GetWorkSize(viewport):
  if not hasattr(ImGui_Viewport_GetWorkSize, 'func'):
    proc = rpr_getfp('ImGui_Viewport_GetWorkSize')
    ImGui_Viewport_GetWorkSize.func = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)(proc)
  args = (rpr_packp('ImGui_Viewport*', viewport), c_double(0), c_double(0))
  ImGui_Viewport_GetWorkSize.func(args[0], byref(args[1]), byref(args[2]))
  return float(args[1].value), float(args[2].value)

def ImGui_WindowFlags_AlwaysAutoResize():
  if not hasattr(ImGui_WindowFlags_AlwaysAutoResize, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysAutoResize')
    ImGui_WindowFlags_AlwaysAutoResize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_AlwaysAutoResize, 'cache'):
    ImGui_WindowFlags_AlwaysAutoResize.cache = ImGui_WindowFlags_AlwaysAutoResize.func()
  return ImGui_WindowFlags_AlwaysAutoResize.cache

def ImGui_WindowFlags_AlwaysHorizontalScrollbar():
  if not hasattr(ImGui_WindowFlags_AlwaysHorizontalScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysHorizontalScrollbar')
    ImGui_WindowFlags_AlwaysHorizontalScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_AlwaysHorizontalScrollbar, 'cache'):
    ImGui_WindowFlags_AlwaysHorizontalScrollbar.cache = ImGui_WindowFlags_AlwaysHorizontalScrollbar.func()
  return ImGui_WindowFlags_AlwaysHorizontalScrollbar.cache

def ImGui_WindowFlags_AlwaysUseWindowPadding():
  if not hasattr(ImGui_WindowFlags_AlwaysUseWindowPadding, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysUseWindowPadding')
    ImGui_WindowFlags_AlwaysUseWindowPadding.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_AlwaysUseWindowPadding, 'cache'):
    ImGui_WindowFlags_AlwaysUseWindowPadding.cache = ImGui_WindowFlags_AlwaysUseWindowPadding.func()
  return ImGui_WindowFlags_AlwaysUseWindowPadding.cache

def ImGui_WindowFlags_AlwaysVerticalScrollbar():
  if not hasattr(ImGui_WindowFlags_AlwaysVerticalScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_AlwaysVerticalScrollbar')
    ImGui_WindowFlags_AlwaysVerticalScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_AlwaysVerticalScrollbar, 'cache'):
    ImGui_WindowFlags_AlwaysVerticalScrollbar.cache = ImGui_WindowFlags_AlwaysVerticalScrollbar.func()
  return ImGui_WindowFlags_AlwaysVerticalScrollbar.cache

def ImGui_WindowFlags_HorizontalScrollbar():
  if not hasattr(ImGui_WindowFlags_HorizontalScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_HorizontalScrollbar')
    ImGui_WindowFlags_HorizontalScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_HorizontalScrollbar, 'cache'):
    ImGui_WindowFlags_HorizontalScrollbar.cache = ImGui_WindowFlags_HorizontalScrollbar.func()
  return ImGui_WindowFlags_HorizontalScrollbar.cache

def ImGui_WindowFlags_MenuBar():
  if not hasattr(ImGui_WindowFlags_MenuBar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_MenuBar')
    ImGui_WindowFlags_MenuBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_MenuBar, 'cache'):
    ImGui_WindowFlags_MenuBar.cache = ImGui_WindowFlags_MenuBar.func()
  return ImGui_WindowFlags_MenuBar.cache

def ImGui_WindowFlags_NoBackground():
  if not hasattr(ImGui_WindowFlags_NoBackground, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoBackground')
    ImGui_WindowFlags_NoBackground.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoBackground, 'cache'):
    ImGui_WindowFlags_NoBackground.cache = ImGui_WindowFlags_NoBackground.func()
  return ImGui_WindowFlags_NoBackground.cache

def ImGui_WindowFlags_NoCollapse():
  if not hasattr(ImGui_WindowFlags_NoCollapse, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoCollapse')
    ImGui_WindowFlags_NoCollapse.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoCollapse, 'cache'):
    ImGui_WindowFlags_NoCollapse.cache = ImGui_WindowFlags_NoCollapse.func()
  return ImGui_WindowFlags_NoCollapse.cache

def ImGui_WindowFlags_NoDecoration():
  if not hasattr(ImGui_WindowFlags_NoDecoration, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoDecoration')
    ImGui_WindowFlags_NoDecoration.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoDecoration, 'cache'):
    ImGui_WindowFlags_NoDecoration.cache = ImGui_WindowFlags_NoDecoration.func()
  return ImGui_WindowFlags_NoDecoration.cache

def ImGui_WindowFlags_NoDocking():
  if not hasattr(ImGui_WindowFlags_NoDocking, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoDocking')
    ImGui_WindowFlags_NoDocking.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoDocking, 'cache'):
    ImGui_WindowFlags_NoDocking.cache = ImGui_WindowFlags_NoDocking.func()
  return ImGui_WindowFlags_NoDocking.cache

def ImGui_WindowFlags_NoFocusOnAppearing():
  if not hasattr(ImGui_WindowFlags_NoFocusOnAppearing, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoFocusOnAppearing')
    ImGui_WindowFlags_NoFocusOnAppearing.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoFocusOnAppearing, 'cache'):
    ImGui_WindowFlags_NoFocusOnAppearing.cache = ImGui_WindowFlags_NoFocusOnAppearing.func()
  return ImGui_WindowFlags_NoFocusOnAppearing.cache

def ImGui_WindowFlags_NoInputs():
  if not hasattr(ImGui_WindowFlags_NoInputs, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoInputs')
    ImGui_WindowFlags_NoInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoInputs, 'cache'):
    ImGui_WindowFlags_NoInputs.cache = ImGui_WindowFlags_NoInputs.func()
  return ImGui_WindowFlags_NoInputs.cache

def ImGui_WindowFlags_NoMouseInputs():
  if not hasattr(ImGui_WindowFlags_NoMouseInputs, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoMouseInputs')
    ImGui_WindowFlags_NoMouseInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoMouseInputs, 'cache'):
    ImGui_WindowFlags_NoMouseInputs.cache = ImGui_WindowFlags_NoMouseInputs.func()
  return ImGui_WindowFlags_NoMouseInputs.cache

def ImGui_WindowFlags_NoMove():
  if not hasattr(ImGui_WindowFlags_NoMove, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoMove')
    ImGui_WindowFlags_NoMove.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoMove, 'cache'):
    ImGui_WindowFlags_NoMove.cache = ImGui_WindowFlags_NoMove.func()
  return ImGui_WindowFlags_NoMove.cache

def ImGui_WindowFlags_NoNav():
  if not hasattr(ImGui_WindowFlags_NoNav, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoNav')
    ImGui_WindowFlags_NoNav.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoNav, 'cache'):
    ImGui_WindowFlags_NoNav.cache = ImGui_WindowFlags_NoNav.func()
  return ImGui_WindowFlags_NoNav.cache

def ImGui_WindowFlags_NoNavFocus():
  if not hasattr(ImGui_WindowFlags_NoNavFocus, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoNavFocus')
    ImGui_WindowFlags_NoNavFocus.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoNavFocus, 'cache'):
    ImGui_WindowFlags_NoNavFocus.cache = ImGui_WindowFlags_NoNavFocus.func()
  return ImGui_WindowFlags_NoNavFocus.cache

def ImGui_WindowFlags_NoNavInputs():
  if not hasattr(ImGui_WindowFlags_NoNavInputs, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoNavInputs')
    ImGui_WindowFlags_NoNavInputs.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoNavInputs, 'cache'):
    ImGui_WindowFlags_NoNavInputs.cache = ImGui_WindowFlags_NoNavInputs.func()
  return ImGui_WindowFlags_NoNavInputs.cache

def ImGui_WindowFlags_NoResize():
  if not hasattr(ImGui_WindowFlags_NoResize, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoResize')
    ImGui_WindowFlags_NoResize.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoResize, 'cache'):
    ImGui_WindowFlags_NoResize.cache = ImGui_WindowFlags_NoResize.func()
  return ImGui_WindowFlags_NoResize.cache

def ImGui_WindowFlags_NoSavedSettings():
  if not hasattr(ImGui_WindowFlags_NoSavedSettings, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoSavedSettings')
    ImGui_WindowFlags_NoSavedSettings.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoSavedSettings, 'cache'):
    ImGui_WindowFlags_NoSavedSettings.cache = ImGui_WindowFlags_NoSavedSettings.func()
  return ImGui_WindowFlags_NoSavedSettings.cache

def ImGui_WindowFlags_NoScrollWithMouse():
  if not hasattr(ImGui_WindowFlags_NoScrollWithMouse, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoScrollWithMouse')
    ImGui_WindowFlags_NoScrollWithMouse.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoScrollWithMouse, 'cache'):
    ImGui_WindowFlags_NoScrollWithMouse.cache = ImGui_WindowFlags_NoScrollWithMouse.func()
  return ImGui_WindowFlags_NoScrollWithMouse.cache

def ImGui_WindowFlags_NoScrollbar():
  if not hasattr(ImGui_WindowFlags_NoScrollbar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoScrollbar')
    ImGui_WindowFlags_NoScrollbar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoScrollbar, 'cache'):
    ImGui_WindowFlags_NoScrollbar.cache = ImGui_WindowFlags_NoScrollbar.func()
  return ImGui_WindowFlags_NoScrollbar.cache

def ImGui_WindowFlags_NoTitleBar():
  if not hasattr(ImGui_WindowFlags_NoTitleBar, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_NoTitleBar')
    ImGui_WindowFlags_NoTitleBar.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_NoTitleBar, 'cache'):
    ImGui_WindowFlags_NoTitleBar.cache = ImGui_WindowFlags_NoTitleBar.func()
  return ImGui_WindowFlags_NoTitleBar.cache

def ImGui_WindowFlags_None():
  if not hasattr(ImGui_WindowFlags_None, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_None')
    ImGui_WindowFlags_None.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_None, 'cache'):
    ImGui_WindowFlags_None.cache = ImGui_WindowFlags_None.func()
  return ImGui_WindowFlags_None.cache

def ImGui_WindowFlags_TopMost():
  if not hasattr(ImGui_WindowFlags_TopMost, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_TopMost')
    ImGui_WindowFlags_TopMost.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_TopMost, 'cache'):
    ImGui_WindowFlags_TopMost.cache = ImGui_WindowFlags_TopMost.func()
  return ImGui_WindowFlags_TopMost.cache

def ImGui_WindowFlags_UnsavedDocument():
  if not hasattr(ImGui_WindowFlags_UnsavedDocument, 'func'):
    proc = rpr_getfp('ImGui_WindowFlags_UnsavedDocument')
    ImGui_WindowFlags_UnsavedDocument.func = CFUNCTYPE(c_int)(proc)
  if not hasattr(ImGui_WindowFlags_UnsavedDocument, 'cache'):
    ImGui_WindowFlags_UnsavedDocument.cache = ImGui_WindowFlags_UnsavedDocument.func()
  return ImGui_WindowFlags_UnsavedDocument.cache
