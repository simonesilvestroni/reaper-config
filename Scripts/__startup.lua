
--HOVER EDITING
hover_editing = tonumber(reaper.GetExtState("LKC_TOOLS","hover_editing_state"))
if hover_editing == nil then hover_editing = 1 end
command = reaper.NamedCommandLookup("_RS8277b238cd7341ba4a3c9ff870f30876ce76160b")
reaper.SetToggleCommandState(0, command, hover_editing)