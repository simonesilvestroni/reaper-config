local scriptName = "Crossfade items across tracks"

function main()
    if reaper.CountSelectedMediaItems(0) ~= 2 then
        reaper.ShowMessageBox("This script expects exactly two selected items", scriptName, 0)
        return
    end

    local function getSelectedItem(i)
        local result = {
            item = reaper.GetSelectedMediaItem(0, i),
        }
        result.start = reaper.GetMediaItemInfo_Value(result.item, "D_POSITION")
        result.length = reaper.GetMediaItemInfo_Value(result.item, "D_LENGTH")
        result.ass = result.start + result.length -- because 'end' is a reserved word
        return result
    end

    local item1 = getSelectedItem(0)
    local item2 = getSelectedItem(1)
    local left, right
    if item1.start < item2.start then
        left, right = item1, item2
    else
        left, right = item2, item1
    end
    if left.ass > right.ass then
        reaper.ShowMessageBox("One item is fully contained in the other. Can't crossfade.", scriptName, 0)
        return
    end

    local overlap = left.ass - right.start
    reaper.SetMediaItemInfo_Value(left.item, "D_FADEOUTLEN", overlap)
    reaper.SetMediaItemInfo_Value(right.item, "D_FADEINLEN", overlap)

    reaper.UpdateArrange()
end

reaper.Undo_BeginBlock()
main()
reaper.Undo_EndBlock(scriptName, 0)
