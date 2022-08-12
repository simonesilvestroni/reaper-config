-- Generated for ReaImGui v0.7

local shims = {
  { version=0x00070000, apply=function() -- v0.7
    -- KeyModFlags to ModFlags rename
    reaper.ImGui_KeyModFlags_None  = reaper.ImGui_ModFlags_None
    reaper.ImGui_KeyModFlags_Ctrl  = reaper.ImGui_ModFlags_Ctrl
    reaper.ImGui_KeyModFlags_Shift = reaper.ImGui_ModFlags_Shift
    reaper.ImGui_KeyModFlags_Alt   = reaper.ImGui_ModFlags_Alt
    reaper.ImGui_KeyModFlags_Super = reaper.ImGui_ModFlags_Super
    
    -- Capture*FromApp to SetNextFrameWantCapture* rename
    reaper.ImGui_CaptureKeyboardFromApp = reaper.SetNextFrameWantCaptureKeyboard
    
    -- non-vanilla HSVtoRGB/RGBtoHSV packing and optional alpha parameter
    local function shimColConv(convFunc)
      return function(x, y, z, a)
        local x, y, z = convFunc(x, y, z)
        local rgba = reaper.ImGui_ColorConvertDouble4ToU32(x, y, z, a or 1.0)
        return (rgba & 0xffffffff) >> (a and 0 or 8), a, x, y, z
      end
    end
    reaper.ImGui_ColorConvertHSVtoRGB = shimColConv(reaper.ImGui_ColorConvertHSVtoRGB)
    reaper.ImGui_ColorConvertRGBtoHSV = shimColConv(reaper.ImGui_ColorConvertRGBtoHSV)
    
    -- ConfigVar API
    function reaper.ImGui_GetConfigFlags(ctx)
      return reaper.ImGui_GetConfigVar(ctx, reaper.ImGui_ConfigVar_Flags())
    end
    function reaper.ImGui_SetConfigFlags(ctx, flags)
      return reaper.ImGui_SetConfigVar(ctx, reaper.ImGui_ConfigVar_Flags(), flags)
    end
    
    -- null-terminated combo and list box items
    local Combo, ListBox = reaper.ImGui_Combo, reaper.ImGui_ListBox
    function reaper.ImGui_Combo(ctx, label, current_item, items, popup_max_height_in_items)
      return Combo(ctx, label, current_item, items:gsub('\31', '\0'), popup_max_height_in_items)
    end
    function reaper.ImGui_ListBox(ctx, label, current_item, items, height_in_items)
      return ListBox(ctx, label, current_item, items:gsub('\31', '\0'), height_in_items)
    end
    
    -- Addition of IMGUI_VERSION_NUM to GetVersion
    local GetVersion = reaper.ImGui_GetVersion
    function reaper.ImGui_GetVersion()
      local imgui_version, imgui_version_num, reaimgui_version = GetVersion()
      return imgui_version, reaimgui_version
    end
  end },
}

local function parseVersion(ver)
  local segs, pos, packed = 4, 1, 0
  ver = tostring(ver)
  for i = 1, segs do
    local sep_pos = ver:find('.', pos, true)
    local seg = tonumber(ver:sub(pos, sep_pos and sep_pos - 1 or nil))
    if not seg or (seg & ~0xff) ~= 0 then break end -- invalid
    packed = packed | (seg << 8 * (segs - i))
    if not sep_pos then return packed end
    pos = sep_pos + 1
  end
  error(('invalid version string "%s"'):format(ver))
end

return function(compat_version)
  local version = parseVersion(compat_version)
  assert(version <= 0x00070000,
    ('reaimgui 0.7 is too old (script requires %s)'):format(compat_version))
  for _, shim in ipairs(shims) do
    if shim.version <= version then break end
    shim.apply()
  end
end
