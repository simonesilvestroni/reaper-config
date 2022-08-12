--[[
Description: Trim items to specified length
Version: 1.10
Author: Lokasenna
Donation: https://paypal.me/Lokasenna
Changelog:
    New: Uses the current version of my GUI library
    Fix: Expand error message when the library is missing
Links:
	Lokasenna's Website http://forum.cockos.com/member.php?u=10417
About:
    Trims all selected items to a given length
--]]

-- Licensed under the GNU GPL v3

-- Script UI generated by Lokasenna's GUI Builder


local lib_path = reaper.GetExtState("Lokasenna_GUI", "lib_path_v2")
if not lib_path or lib_path == "" then
    reaper.MB("Couldn't load the Lokasenna_GUI library. Please install 'Lokasenna's GUI library v2 for Lua', available on ReaPack, then run the 'Set Lokasenna_GUI v2 library path.lua' script in your Action List.", "Whoops!", 0)
    return
end
loadfile(lib_path .. "Core.lua")()

GUI.req("Classes/Class - Menubox.lua")()
GUI.req("Classes/Class - Button.lua")()
GUI.req("Classes/Class - Textbox.lua")()
-- If any of the requested libraries weren't found, abort the script.
if missing_lib then return 0 end


local function parse_settings()

    -- Valid the textbox
    local length = tonumber( GUI.Val("Textbox1") )
    if not length then return end

    -- Get a time multiplier for the specified unit
    local _, units = GUI.Val("Menubox1")

    -- Get settings
    if     units    == "milliseconds" then
        length = length / 1000
    elseif units    == "minutes" then
        length = length * 60
    elseif units    == "beats" then
        length = length * (60 / reaper.Master_GetTempo() )
    elseif units    == "measures" then
        length = length * 4 * (60 / reaper.Master_GetTempo() )
    elseif units    == "frames" then
        length = get_frames(length)
    elseif units    == "gridlines" then
        local _, divisionIn, _, _ = reaper.GetSetProjectGrid(0, false)
        length =    length * divisionIn * 4 * (60 / reaper.Master_GetTempo() )
    elseif units    == "visible gridlines" then

        local pos = reaper.GetCursorPosition()
        local cur = 0.001

        while true do

            local cur_pos = reaper.SnapToGrid(0, pos + cur)

            if cur_pos ~= pos then
                length = length * (cur_pos - pos)
                break
            else
                cur = cur * 2
            end

        end

    end

    return length

end



local function go()

    local num_items = reaper.CountSelectedMediaItems()
    if num_items == 0 then
        reaper.MB("No items selected.", "Whoops!", 0)
        return
    end

    reaper.PreventUIRefresh(1)
    reaper.Undo_BeginBlock()

    -- Parse the user settings to get a length
    local l = parse_settings()
    if not l then return end

    -- For each selected item
    for i = 0, num_items - 1 do

        local item = reaper.GetSelectedMediaItem(0, i)

        reaper.SetMediaItemInfo_Value(item, "D_LENGTH", l)

    end

    reaper.Undo_EndBlock("Trim items to specified length", -1)
    reaper.PreventUIRefresh(-1)
    reaper.UpdateArrange()

end









GUI.name = "Trim items to..."
GUI.x, GUI.y, GUI.w, GUI.h = 0, 0, 280, 96
GUI.anchor, GUI.corner = "mouse", "C"



GUI.New("Button1", "Button", {
    z = 11,
    x = 116.0,
    y = 48,
    w = 48,
    h = 24,
    caption = "Go!",
    font = 3,
    col_txt = "txt",
    col_fill = "elm_frame",
    func = go,
})

GUI.New("Menubox1", "Menubox", {
    z = 11,
    x = 132,
    y = 16.0,
    w = 112,
    h = 20,
    caption = "",
    optarray = {"beats", "measures", "milliseconds", "seconds", "minutes", "gridlines", "visible gridlines", "frames"},
    retval = 5.0,
    font_a = 3,
    font_b = 4,
    col_txt = "txt",
    col_cap = "txt",
    bg = "wnd_bg",
    pad = 4,
    noarrow = false,
    align = 0
})

GUI.New("Textbox1", "Textbox", {
    z = 11,
    x = 64.0,
    y = 16.0,
    w = 64,
    h = 20,
    caption = "Length:",
    cap_pos = "left",
    font_a = 3,
    font_b = 4,
    color = "txt",
    bg = "wnd_bg",
    shadow = true,
    pad = 4,
    undo_limit = 20
})


GUI.Init()
GUI.Main()
