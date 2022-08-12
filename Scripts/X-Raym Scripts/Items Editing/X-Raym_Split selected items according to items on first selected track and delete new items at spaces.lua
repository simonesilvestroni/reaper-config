--[[
 * ReaScript Name: Split selected items according to items on first selected track and delete new items at spaces
 * About: A script to do multi mic based editing using one single track.
 * Screenshot: https://i.imgur.com/v507YbW.gifv
 * Author: X-Raym
 * Author URI: http://extremraym.com
 * Repository: GitHub > X-Raym > EEL Scripts for Cockos REAPER
 * Repository URI: https://github.com/X-Raym/REAPER-EEL-Scripts
 * Licence: GPL v3
 * Forum Thread: Scripts: Items Editing (various)
 * Forum Thread URI: https://forum.cockos.com/showthread.php?t=163363
 * REAPER: 5.0
 * Version: 1.0.1
--]]
 
--[[
 * Changelog:
 * v1.0.1 (2020-07-06)
  # Actually delete items at spaces
 * v1.0 (2020-07-06)
  + Initial Release
 * v0.9 (2019-10-18)
  # based on X-Raym_Split selected items according to items on first selected track and keep new items at spaces.lua
--]]

-- INIT
split_pos={}
save_item={}
save_new_item={}
split_pos_total = 0
count_new_item = 0

-- SAVE TIME IN ARRAY
function save_time(time)
  table.insert(split_pos, 1, time)
  split_pos_total = split_pos_total +1
end

function save_item_selection()
  count_selected_items = reaper.CountSelectedMediaItems(0)
  for f = 0, count_selected_items-1 do
    save_item[f] = reaper.GetSelectedMediaItem(0, f)
  end
  for e = 0, count_selected_items-1 do
    reaper.Main_OnCommand(40289, 0)
    sel_item = save_item[e]
    reaper.SetMediaItemSelected(sel_item, 1)
    main()
  end
end

-- MAIN
function main()

  -- GET FIRST SELECTED ITEMS & INFOS
  sel_item_len = reaper.GetMediaItemInfo_Value(sel_item, "D_LENGTH")
  sel_item_pos = reaper.GetMediaItemInfo_Value(sel_item, "D_POSITION")
  sel_item_end = sel_item_pos + sel_item_len

  -- GET FIRST SELECTED ITEM TRACK
  track_of_sel_item = reaper.GetMediaItemTrack(sel_item)

  -- LOOP THROUGH ITEMS ON first selected track
  selected_tracks_count = reaper.CountSelectedTracks(0)

  -- GET THE TRACK
  track = reaper.GetSelectedTrack(0, 0) -- Get selected track 0

  -- INITIALIZE loop through selected items
  item_on_tracks = reaper.CountTrackMediaItems(track)
  for j = 0, item_on_tracks-1  do
    
    -- GET ITEM
    item = reaper.GetTrackMediaItem(track, j) -- Get selected item i

    -- GET INFOS
    item_len = reaper.GetMediaItemInfo_Value(item, "D_LENGTH")
    item_pos = reaper.GetMediaItemInfo_Value(item, "D_POSITION")
    item_end = item_pos + item_len

    -- IF ITEM POS IS INSIDE OUR SELECTED ITEM
    if item_pos > sel_item_pos and item_pos < sel_item_end then

      -- IF FIRST ITEM, INSERT AUTOMATICALLY
      save_time(item_pos)
      last = false
    
    end

    -- IF ITEM END IS INSIDE OUR SELECTED ITEM
    if item_end > sel_item_pos and item_end < sel_item_end then

      -- IF LAST ITEM ON TRACK, INSERT AUTOMATICALLY
      save_time(item_end)
      last = true

    end
  
  end -- END LOOP ITEMS ON TRACK

  -- SORT THE TABLE
  table.sort(split_pos)

  -- SPLIT SELECTED ITEM
  for k = 0, split_pos_total-1 do
    reaper.SplitMediaItem(sel_item, split_pos[split_pos_total-k])
  end

  -- LOOP IN NEW CREATED ITEMS AND DELETE UNWANTED ONES
  count_selected_items = reaper.CountSelectedMediaItems(0)

  -- IF THE LAST CUT WAS A ITEM POS TIME
  if last == false then
    for t = 0, count_selected_items-1 do
      item = reaper.GetSelectedMediaItem(0, count_selected_items-1-t) -- Get selected item i
      if (t % 2 == 1) then
        --reaper.SetMediaItemSelected(item, 0)
        reaper.DeleteTrackMediaItem(track_of_sel_item, item)
      else
        --reaper.SetMediaItemSelected(item, 1)
        count_new_item = count_new_item + 1
        save_new_item[count_new_item] = item
      end
    end
  else -- ELSEIF THE LAST CUT WAS A ITEM END TIME
    for t = 0, count_selected_items-1 do
      item = reaper.GetSelectedMediaItem(0, count_selected_items-1-t) -- Get selected item i
      if (t % 2 == 1) then
        --reaper.SetMediaItemSelected(item, 1)
        count_new_item = count_new_item + 1
        save_new_item[count_new_item] = item
      else
        --reaper.SetMediaItemSelected(item, 0)
        reaper.DeleteTrackMediaItem(track_of_sel_item, item)
      end
    end
  end

  for a = 1, count_new_item do
    reaper.SetMediaItemSelected(save_new_item[a], 1)
  end

end

function runloop()
  local newtime=os.time()
  
  if (loopcount < 1) then
    if newtime-lasttime >= wait_time_in_seconds then
   lasttime=newtime
   loopcount = loopcount+1
    end
  else
    ----------------------------------------------------
    -- PUT ACTION(S) YOU WANT TO RUN AFTER WAITING HERE
    
    reaper.TrackCtl_SetToolTip( "", x, y, true )
    
    ----------------------------------------------------
    loopcount = loopcount+1
  end
  if 
    (loopcount < 2) then reaper.defer(runloop) 
  end
end

function DisplayTooltip(message)
  wait_time_in_seconds = 2
  lasttime=os.time()
  loopcount=0
  
  x, y = reaper.GetMousePosition()
  reaper.TrackCtl_SetToolTip( message, x, y, false )
  
  runloop()
end

reaper.PreventUIRefresh(1)-- Prevent UI refreshing. Uncomment it only if the script works.

count_sel_tracks = reaper.CountSelectedTracks()

if count_sel_tracks > 0 then

  count_sel_items = reaper.CountSelectedMediaItems( 0 )
  
  if count_sel_items > 0 then

    reaper.Undo_BeginBlock() -- Begining of the undo block. Leave it at the top of your main function.
  
    save_item_selection()
  
    reaper.Undo_EndBlock("Split selected items according to items on first selected track and delete new items at spaces", 0) -- End of the undo block. Leave it at the bottom of your main function.
    
  else
  
    DisplayTooltip("No item selected.")
    
  end
  
else
  DisplayTooltip("No track selected.")
end

reaper.PreventUIRefresh(-1) -- Restore UI Refresh. Uncomment it only if the script works.

reaper.UpdateArrange() -- Update the arrangement (often needed)
