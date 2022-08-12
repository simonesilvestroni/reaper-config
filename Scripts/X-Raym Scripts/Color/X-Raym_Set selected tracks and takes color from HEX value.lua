--[[
 * ReaScript Name: Set selected tracks and takes color from HEX value
 * About: Set selected tracks and takes color from HEX value. Use # or not. If no takes (aka, if Text items selected), it will work anyway.
 * Author: X-Raym
 * Author URI: http://extremraym.com
 * Repository: GitHub > X-Raym > EEL Scripts for Cockos REAPER
 * Repository URI: https://github.com/X-Raym/REAPER-EEL-Scripts
 * Licence: GPL v3
 * Version: 1.1.1
 * Version Date: 2020-07-18
 * REAPER: 5.0 pre 15
--]]
 
--[[
 * Changelog:
 * v1.1.1 (2016-11-07)
	# Bug fix (thx Buy-One !)
	# minor optimization
 * v1.1 (2016-11-07)
	# MacOS color fixed
 * v1.0 (2015-03-12)
	+ Initial Release
--]]

function main()

	reaper.Undo_BeginBlock()

	-- YOUR CODE BELOW

	color_int =  reaper.ColorToNative( R, G, B )|0x1000000 -- doesn't display the color in the arrange without it

	countItems = reaper.CountSelectedMediaItems(0)

	-- SELECTED ITEMS LOOP
	if countItems > 0 then
		for i = 0, countItems-1 do
			item = reaper.GetSelectedMediaItem(0, i)
			take = reaper.GetActiveTake(item)
			if take ~= nil then
				reaper.SetMediaItemTakeInfo_Value(take, "I_CUSTOMCOLOR", color_int)
			else
				reaper.SetMediaItemInfo_Value(item, "I_CUSTOMCOLOR", color_int)
			end
		end
	end

	countTracks = reaper.CountSelectedTracks(0)

	-- SELECTED TRACKS LOOP
	if countTracks > 0 then
		for j = 0, countTracks-1 do
			track = reaper.GetSelectedTrack(0, j)
			reaper.SetMediaTrackInfo_Value(track, "I_CUSTOMCOLOR", color_int)
		end
	end

	reaper.Undo_EndBlock("Set color hex value for selected tracks and takes", 0)
end


defaultvals_csv = "123456"

retval, retvals_csv = reaper.GetUserInputs("Color selected Track and Takes", 1, "HEX Value", defaultvals_csv) 
			
if retval then -- if user complete the fields

	if retvals_csv ~= nil then
		hex = retvals_csv:gsub("#","")
		R = tonumber("0x"..hex:sub(1,2))
		G = tonumber("0x"..hex:sub(3,4))
		B = tonumber("0x"..hex:sub(5,6))

		if R and G and B then

			main() -- Execute your main function

		end

		reaper.UpdateArrange() -- Update the arrangement (often needed)

	end

end
