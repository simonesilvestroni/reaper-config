sTitle = 'Theme Assembler'
reaper.ClearConsole()

OS = reaper.GetOS()
script_path = ({reaper.get_action_context()})[2]:match('^.*[/\\]'):sub(1,-2)
themes_path = reaper.GetResourcePath() .. "/ColorThemes"

if not reaper.file_exists(script_path..'/theme_assembler/initial/Assembled_Theme.ReaperTheme') then
  reaper.MB("theme_assembler path does not exist alongside script file in "..script_path,
            "Theme Assembler Installation Error",0);
else


gfx.init(sTitle,
tonumber(reaper.GetExtState(sTitle,"wndw")) or 800,
tonumber(reaper.GetExtState(sTitle,"wndh")) or 600,
tonumber(reaper.GetExtState(sTitle,"dock")) or 0,
tonumber(reaper.GetExtState(sTitle,"wndx")) or 100,
tonumber(reaper.GetExtState(sTitle,"wndy")) or 50)

gfx.ext_retina = 1







  ---------- COLOURS -----------
  
function setCol(col)
  if col[1] and col[2] and col[3] then
    local r = col[1] / 255
    local g = col[2] / 255
    local b = col[3] / 255
    local a = 1
    if col[4] ~= nil then a = col[4] / 255 end
    gfx.set(r,g,b,a)
    gfx.a2=gfx.a
  end
end

function getProjectCustCols()
  projectCustCols = {}
  for i=0, reaper.CountTracks(0)-1 do
    local c = reaper.GetTrackColor(reaper.GetTrack(0, i))
    if c ~= 0 then
      local r,g,b = reaper.ColorFromNative(c)
      table.insert(projectCustCols,{r,g,b})
    end
  end
end

representCustCol = {70,90,90}

  ---------- TEXT -----------

textPadding = 6

if OS:find("Win") ~= nil then

  gfx.setfont(1, "Calibri", 13)
  gfx.setfont(2, "Calibri", 15)
  gfx.setfont(3, "Calibri", 22)
  gfx.setfont(4, "Calibri Bold", 50)
  
  gfx.setfont(11, "Calibri", 19)
  gfx.setfont(12, "Calibri", 22)
  gfx.setfont(13, "Calibri", 33)
  gfx.setfont(14, "Calibri Bold", 75)
  
  gfx.setfont(21, "Calibri", 26)
  gfx.setfont(22, "Calibri", 30)
  gfx.setfont(23, "Calibri", 44)
  gfx.setfont(24, "Calibri Bold", 100)

elseif OS == 'Other' then
  gfx.setfont(1, "Open Sans", 9)
  gfx.setfont(2, "Open Sans", 11)
  gfx.setfont(3, "Open Sans", 20)
  gfx.setfont(4, "Open Sans Bold", 40)
  
  gfx.setfont(11, "Open Sans", 13)
  gfx.setfont(12, "Open Sans", 15)
  gfx.setfont(13, "Open Sans", 30)
  gfx.setfont(14, "Open Sans Bold", 60)
  
  gfx.setfont(21, "Open Sans", 18)
  gfx.setfont(22, "Open Sans", 22)
  gfx.setfont(23, "Open Sans", 40)
  gfx.setfont(24, "Open Sans Bold", 80)

else

  gfx.setfont(1, "Helvetica", 9)
  gfx.setfont(2, "Helvetica", 11)
  gfx.setfont(3, "Helvetica", 19)
  gfx.setfont(4, "Helvetica Bold", 40)
  
  gfx.setfont(11, "Helvetica", 13)
  gfx.setfont(12, "Helvetica", 15)
  gfx.setfont(13, "Helvetica", 30)
  gfx.setfont(14, "Helvetica Bold", 75)
  
  gfx.setfont(21, "Helvetica", 18)
  gfx.setfont(22, "Helvetica", 22)
  gfx.setfont(23, "Helvetica", 38)
  gfx.setfont(24, "Helvetica Bold", 92)
end

function text(str,x,y,w,h,align,col,style,lineSpacing,vCenter,wrap)
  local lineSpace = lineSpacing or (11*scaleMult)
  setCol(col or {255,255,255})
  gfx.setfont(style or 1)

  local lines = nil
  if wrap == true then lines = textWrap(str,w)
  else
    lines = {}
    for s in string.gmatch(str, "([^#]+)") do
      table.insert(lines, s)
    end
  end
  if vCenter ~= false and #lines > 1 then y = y - lineSpace/2 end
  for k,v in ipairs(lines) do
    gfx.x, gfx.y = x,y
    gfx.drawstr(v,align or 0,x+(w or 0),y+(h or 0))
    y = y + lineSpace
  end
end

function textWrap(str,w) -- returns array of lines
  local lines,curlen,curline,last_sspace = {}, 0, "", false
  -- enumerate words
  for s in str:gmatch("([^%s-/]*[-/]* ?)") do
    local sspace = false -- set if space was the delimiter
    if s:match(' $') then
      sspace = true
      s = s:sub(1,-2)
    end
    local measure_s = s
    if curlen ~= 0 and last_sspace == true then
      measure_s = " " .. measure_s
    end
    last_sspace = sspace

    local length = gfx.measurestr(measure_s)
    if length > w then
      if curline ~= "" then
        table.insert(lines,curline)
        curline = ""
      end
      curlen = 0
      while length > w do -- split up a long word, decimating measure_s as we go
        local wlen = string.len(measure_s) - 1
        while wlen > 0 do
          local sstr = string.format("%s%s",measure_s:sub(1,wlen), wlen>1 and "-" or "")
          local slen = gfx.measurestr(sstr)
          if slen <= w or wlen == 1 then
            table.insert(lines,sstr)
            measure_s = measure_s:sub(wlen+1)
            length = gfx.measurestr(measure_s)
            break
          end
          wlen = wlen - 1
        end
      end
    end
    if measure_s ~= "" then
      if curlen == 0 or curlen + length <= w then
        curline = curline .. measure_s
        curlen = curlen + length
      else -- word would not fit, add without leading space and remeasure
        table.insert(lines,curline)
        curline = s
        curlen = gfx.measurestr(s)
      end
    end
  end
  if curline ~= "" then
    table.insert(lines,curline)
  end
  return lines
end



  --------- IMAGES ----------
  
imgBufferOffset = 500  

function loadImage(idx, name, location, noIScales)

  local i = idx
  if i then
    if location then
      str = script_path..'/theme_assembler/'..location.."/"..name..".png"
      if OS:find("Win") ~= nil then str = str:gsub("/","\\") end --to stop it being reported as a bug
      if gfx.loadimg(i, str) == -1 then reaper.ShowConsoleMsg("script image "..name.." not found\n") end
    else
      local scaleFolder = ''
      if noIScales ~= true and scaleMult == 1.5 then scaleFolder = '/150' end
      if noIScales ~= true and scaleMult == 2 then scaleFolder = '/200' end
      local str = themes_path..'/'..themeFolder..scaleFolder.."/"..name..".png"
      if OS:find("Win") ~= nil then str = str:gsub("/","\\") end
      if gfx.loadimg(i, str) == -1 then reaper.ShowConsoleMsg("theme image "..name.." not found\n") end
    end
  end
  
  -- look for pink
    gfx.dest = idx
    gfx.x,gfx.y = 0,0
    if isPixelPink(gfx.getpixel()) then --top left is pink
      local bufW,bufH = gfx.getimgdim(idx)
      gfx.x,gfx.y = bufW-1,bufH-1
      if isPixelPink(gfx.getpixel()) then --bottom right also pink
        local tx, ly, bx, ry = 0,0,0,0
        
        gfx.x,gfx.y = 0,0 
        while isPixelPink(gfx.getpixel()) do
          tx = math.floor(gfx.x+1)
          gfx.x = gfx.x+1
        end
        
        gfx.x,gfx.y = 0,0
        while isPixelPink(gfx.getpixel()) do
          ly = math.floor(gfx.y+1)
          gfx.y = gfx.y+1
        end
        
        gfx.x,gfx.y = bufW-1,bufH-1 
        while isPixelPink(gfx.getpixel()) do
          bx = math.floor(bufW - gfx.x)
          gfx.x = gfx.x-1
        end
        
        gfx.x,gfx.y = bufW-1,bufH-1 
        while isPixelPink(gfx.getpixel()) do
          ry = math.floor(bufH - gfx.y)
          gfx.y = gfx.y-1
        end
        
        --reaper.ShowConsoleMsg('top x pink = '..tx..', left y pink = '..ly..', bottom x pink = '..bx..', right y pink = '..ry..'\n')
        bufferPinkValues[idx] = {tx=tx, ly=ly, bx=bx, ry=ry} -- apparently lua understands this, nice
        
      end
    end
  
end

function isPixelPink(r,g,b) 
  if (r==1 and g==0 and b==1) or (r==1 and g==1 and b==0) then -- yellow is also pink. The world's a weird place.
    return true 
  else return false 
  end 
end

function getImage(img, location, noIScales)
  local buf = nil
  local i = imgBufferOffset
  while buf == nil do -- find the next empty buffer and assign
    local h,w = gfx.getimgdim(i)
    if h==0 then buf=i end
    i = i+1
  end
  --reaper.ShowConsoleMsg('image to '..buf..'\n')
  loadImage(buf, img, location, noIScales)  
  return buf
end

function pinkBlit(img, srcx, srcy, destx, desty, tx, ly, bx, ry, unstretchedC2W, unstretchedR2H, stretchedC2W, stretchedR2H)
  --gfx.blit(source, scale, rotation, srcx, srcy, srcw, srch, destx, desty, destw, desth)
  --reaper.ShowConsoleMsg(img..' unstretchedC2W, unstretchedR2H = '..unstretchedC2W..', '..unstretchedR2H..',  stretchedC2W, stretchedR2H = '..stretchedC2W..', '..stretchedR2H..'\n')
  gfx.blit(img, 1, 0, srcx +1, srcy +1, tx-1, ly-1, destx, desty, tx-1, ly-1)
  gfx.blit(img, 1, 0, srcx +tx, srcy +1, unstretchedC2W, ly-1, destx+tx-1, desty, stretchedC2W, ly-1)
  gfx.blit(img, 1, 0, srcx +tx +unstretchedC2W, srcy +1, bx-1, ly-1, destx+tx-1+stretchedC2W, desty, bx-1, ly-1)
  
  gfx.blit(img, 1, 0, srcx+1, ly, tx-1, unstretchedR2H, destx, desty+ly-1, tx-1, stretchedR2H)
  gfx.blit(img, 1, 0, srcx +tx, ly, unstretchedC2W, unstretchedR2H, destx+tx-1, desty+ly-1, stretchedC2W, stretchedR2H)
  gfx.blit(img, 1, 0, srcx +tx +unstretchedC2W, ly, bx-1, unstretchedR2H, destx+tx-1+stretchedC2W, desty+ly-1, bx-1, stretchedR2H)
  
  gfx.blit(img, 1, 0, srcx+1, ly +unstretchedR2H, tx-1, ry-1, destx, desty+ly-1+stretchedR2H, tx-1, ry-1)
  gfx.blit(img, 1, 0, srcx +tx, ly +unstretchedR2H, unstretchedC2W, ry-1, destx+tx-1, desty+ly-1+stretchedR2H, stretchedC2W, ry-1)
  gfx.blit(img, 1, 0, srcx +tx +unstretchedC2W, ly +unstretchedR2H, bx-1, ry-1, destx+tx-1+stretchedC2W, desty+ly-1+stretchedR2H, bx-1, ry-1)
end



function copyImg(el) 
  for i,v in ipairs(el.states) do 
  local scales = {{'',''},{'_150','/150'},{'_200','/200'}}
    if el.iType == 'meterV' or el.iType == 'meterH' then scales = {{'',''}} end
    for p,q in ipairs(scales)do
      --reaper.ShowConsoleMsg('src is '..path.."Scripts\\theme_assembler\\"..v[1]..'\\'..el.img..q[1]..'.png\n')
      --reaper.ShowConsoleMsg('dest is '..path.."ColorThemes\\"..themeFolder..q[2]..'\\'..v[1]..'.png\n')
      src = script_path.."/theme_assembler/"..v[1]..'/'..el.img..q[1]..'.png'
      dest = themes_path.."/"..themeFolder..q[2]..'/'..v[1]..'.png'
      osCopy(src, dest)
    end
  end
  refreshTheme()
  reloadImgs()
end

function reloadImgs()
  for b in ipairs(els) do -- iterate blocks 
    for z in ipairs(els[b]) do -- iterate z
      if els[b][z] ~= nil then
        for j,k in pairs(els[b][z]) do
          k:reloadImg()
        end
      end
    end
  end
  doArrange = true
end

  --------- OBJECTS ----------

els = {}
function AddEl(o)
  if o.x == nil and o.y == nil and o.updateOn == nil and o.action == nil then --just a proto
  else
    if o.parent then  adoptChild(o.parent, o) end
    if o.block == nil then if o.parent and o.parent.block then o.block = o.parent.block  end end-- no block specified, inherit from parent
    if o.z == nil then if o.parent and o.parent.z then o.z = o.parent.z  end end -- no z specified, inherit from parent
    if els[o.block] == nil then els[o.block] = {} end
    if els[o.block][o.z] == nil then els[o.block][o.z] = {o}
    else els[o.block][o.z][#els[o.block][o.z]+1] = o
    end
  end
end

El = {}
function El:new(o)
  local o = o or {}
  if o.interactive == nil then o.interactive = true end
  self.__index = self
  AddEl(o)
  setmetatable(o, self)
  return o
end

Block = {}
function Block:new(o)
  local o = o or {}
  if els == nil then els = {} end
  els[#els+1] = o
  self.__index = self
  setmetatable(o, self)
  return o
end

Button = El:new{} 
function Button:new(o)
  self.__index = self
  AddEl(o)
  setmetatable(o, self)
  return o
end

funcText = El:new{} 
function funcText:new(o)
  self.__index = self
  AddEl(o)
  o.onArrange = function() self.w = fitText(o)+16 end
  setmetatable(o, self)
  return o
end

TargetButton = El:new{} 
function TargetButton:new(o)
  self.__index = self
  AddEl(o)
  o.z = o.z or 2
  o.iType = o.iType or 3
  if o.iType == 'stack' then o.iFrameH, o.iFrame = o.iFrameH or 20, o.iFrame or 1 end
  if o.iType == ('meterV' or 'meterH') then o.mValue = 0 end
  o.img = o.title or nil
  if o.onClick == nil then
    o.onClick = function() setTarget(o) end
  end
  if o.iType == 'themeFile' then
      o.children = {
      El:new({parent=o, x=0, y=0, w=110, h=50, onClick=o.onClick}),
      El:new({parent=o.children[1], x=1, y=1, w=48, h=48, img="reaper_theme_icon", iLocation='scriptImages', iType='scriptImage', onClick=o.onClick, toolTip='Code Colors & Font Assignments'}),
      El:new({parent=o.children[1], x=44, y=14, w=60, h=38, onClick=o.onClick, text={str='Theme Colors & Fonts File', style=1,align=3,wrap=true, col={200,200,200}}})
      }
  end
  if o.iType == 'idxbgColorHack' then o.w, o.h = 16,70 end
  setmetatable(o, self)
  return o
end

ChoiceBox = El:new{} 
function ChoiceBox:new(ch) 
  self.__index = self
  local title = ch.img or ch.title
  o = El:new({parent=ch.parent, flow=ch.flow or false,  resizeParent='v', text={str=string.gsub(title, "_", " "),style=1,align=9,col={255,255,255}},
        x=0, y=0, border=10, w=ch.w or 88, h=ch.h or 50, col={70,70,70}, mouseOverCol={80,80,80},
        onClick = ch.onClick or function() copyImg(ch) end})
  AddEl(o)
  o.children = {}
  local ChoiceImgW, ChoiceImgH = nil, nil
  if ch.iType == 'stack' then ch.iFrameH, ch.iFrame = ch.iFrameH or ch.w, ch.iFrame or 1 
  elseif ch.iType == 'meterV' then ChoiceImgW, ChoiceImgH = 20, 140
  elseif ch.iType == 'meterH' then ChoiceImgW, ChoiceImgH = 140, 12
  elseif ch.iType == 'idxbgColorHack' then o.col, ChoiceImgW, ChoiceImgH = representCustCol, 74, 30
  end
  ch.iType = ch.iType or 3
  o.children.img = El:new({parent=o, x=0, y=-7, iFrameH = 20, iFrame = ch.iFrame,
                elAlign={x={'parent','centre'},y={'parent','centre'}}, w=ChoiceImgW, h=ChoiceImgH, img=ch.img, iType=ch.iType, noIScales=ch.noIScales, onFps=ch.onFps or nil, 
                iLocation=ch.iLocation, states=ch.states, meterColumn=ch.meterColumn, onClick = o.onClick})
  if ch.iType == 'themeFile' then
    o.children.img = nil
    o.onClick = function() copyThemeFile(ch) end
    El:new({parent=o, x=0, y=0, w=100, h=36, col=ch.proxyCols[1], onClick=o.onClick})
    El:new({parent=o, x=4, y=4, w=24, h=28, col=ch.proxyCols[2], onClick=o.onClick})
    El:new({parent=o, x=28, y=4, w=24, h=14, col=ch.proxyCols[3], onClick=o.onClick})
    El:new({parent=o, x=28, y=18, w=24, h=14, col=ch.proxyCols[4], onClick=o.onClick})
  end
  setmetatable(o, self)
  return o
end

OrderField = El:new{} 
function OrderField:new(o)
  self.__index = self
  o.parent = orderThing
  o.x, o.y, o.w, o.h = 8, 8, o.w or 120, 30
  --o.col={60,60,60} 
  AddEl(o)
  o.children = {}
  
  if o.rButton then 
    local r = Button:new({parent=o, z=2, x=13, elAlign={x={'parent','right'}}, y=4, w=18, h=24, img='swap', iType=3, iLocation='scriptImages', toolTip='Swap Locations',
      onClick=function() 
        swapFields(o.index,o.index+1)
      end})
    table.insert(o.children, r)
  end
  
  setmetatable(o, self)
  return o
end



  --------- FUNCS ----------
  
  
function El:purge()
  --reaper.ShowConsoleMsg('purging\n')
  for b in ipairs(els) do -- iterate block
    for z in ipairs(els[b]) do
      if els[b][z] ~= nil and #els[b][z] ~= 0 then
        for j,k in pairs(els[b][z]) do
          if k == self then
            if self.children ~= nil then 
              for l,m in pairs(self.children) do
                m:purge() 
              end 
            end
            if self:addToDirtyZone(b,z) == true then
              if self.imgIdx then
                gfx.setimgdim(self.imgIdx,0,0)
              end
              table.remove(els[b][z],j)
              doDraw = true
            end
          end
        end
      end
    end
  end -- end iterating blocks
end

function colCycle(self) -- for debugging / inducing headaches
  if colDebug ~= true then self.col = {0,255,0,150}
  else self.col = {math.random(255),math.random(255),math.random(255),255}
    self:addToDirtyZone()
  end
end  

function osCopy(src, dest)

  if src:sub(-4) == ".png" or  src:sub(-12) == ".ReaperTheme" then
    local srcf = io.open(src,"rb")
    if srcf then
      local dstf = io.open(dest,"wb")
      if dstf then
        while true do
          local b = srcf:read(32768)
          if not b then break end
          dstf:write(b)
        end
      end
      srcf:close()
      if dstf then dstf:close() return true end
    end
  end
  -- paths should have forward slashes for everything here
  if OS:find("Win") ~= nil then
    src = src:gsub("/","\\") -- xcopy wants backslashes
    dest = dest:gsub("/","\\")
    --reaper.ShowConsoleMsg('xcopy /e/f/y "'..src..'" "'..dest..'" \n')
    os.execute('xcopy /e/f/i/y "'..src..'" "'..dest..'"')
  else
    assert(src:match("\\")==nil, "src for filecopy has backslash")
    assert(dest:match("\\")==nil, "dest for filecopy has backslash")
    os.execute('cp -fR "'..src..'" "'..dest .. '"')
  end
  return true
end

--[[function tableOfDir(folder)
  local filelist=io.popen('dir "' .. folder .. '" /b')
  local t ={}
  for filename in filelist:lines() do
    table.insert(t, filename)
  end
  return t
end]]

function getReaperThemeVar(var) -- or use reaper.GetThemeColor()
  local var = var:gsub("%[","%%[") -- some vars have square brackets in their name
  local str = themes_path..'/'..'Assembled_Theme.ReaperTheme'
  if OS:find("Win") ~= nil then str = str:gsub("/","\\") end
  for line in io.lines(str) do
    if string.find(line, var) then
      return string.match(line, "=(.*)")
    end
  end
end

function getRtconfigVar(var)
  local str = themes_path..'/'..themeFolder..'/'..'rtconfig.txt'
  if OS:find("Win") ~= nil then str = str:gsub("/","\\") end
  for line in io.lines(str) do
    if string.find(line, 'set '..var) then
      return string.match(line, '[+-]?%d+')
    end
  end
end

function setRtconfigVar(var, val)
  local str = themes_path..'/'..themeFolder..'/'..'rtconfig.txt'
  if OS:find("Win") ~= nil then str = str:gsub("/","\\") end
  local rtConfigTable = {}
  
  for line in io.lines(str) do
    if string.find(line, 'set '..var) then
      table.insert(rtConfigTable, 'set '..var..' '..val)
    else
      table.insert(rtConfigTable,line)
    end
  end
  
  local file = io.open(str, "w")
  io.output(file)
  for i,v in ipairs(rtConfigTable) do
    io.write(v..'\n')
  end
  io.close(file)
  refreshTheme()
  
end

function setReaperThemeVar(var, val, newThemeName)
  local themeFileTable = {}
  for line in io.lines(themes_path..'/Assembled_Theme.ReaperTheme') do
    if string.find(line, var) then
      --reaper.ShowConsoleMsg('found '..var..'\n')
      table.insert(themeFileTable, var..val)
    else
      table.insert(themeFileTable,line)
    end
  end
  
  local themeName = (newThemeName or 'Assembled_Theme')..'.ReaperTheme'
  local file = io.open(themes_path..'/'..themeName, "w")
  io.output(file)
  for i,v in ipairs(themeFileTable) do
    io.write(v..'\n')
  end
  io.close(file)
  return true
end

function swapFields(f1,f2)
  local str = themes_path..'/'..themeFolder..'/'..'rtconfig.txt'
  if OS:find("Win") ~= nil then str = str:gsub("/","\\") end
  local rtConfigTable = {}
  for line in io.lines(str) do table.insert(rtConfigTable,line) end
  
  local file = io.open(str, "w")
  io.output(file)
  local fl = 0
  for i,v in ipairs(rtConfigTable) do
    if string.find(v, 'then tcp') then
      fl = fl + 1
      if fl >= 11 then fl = 1 end
      if fl == f1 then io.write(rtConfigTable[i+1]..'\n')
        elseif fl == f2 then io.write(rtConfigTable[i-1]..'\n')
        else io.write(v..'\n')
      end 
    else
      io.write(v..'\n') -- unchanged line
    end
  end  
  io.close(file)
  refreshTheme()
  doArrange = true
end


function math.Clamp(val, min, max)
  return math.min(math.max(val, min), max)
end


function copyThemeFile(el) 
  src = script_path.."/theme_assembler/ReaperTheme/"..el.title..'.ReaperTheme'
  --reaper.ShowConsoleMsg('src is '..src..'\n')
  dest = themes_path..'/Assembled_Theme.ReaperTheme'
  --reaper.ShowConsoleMsg('dest is '..dest..'\n')
  osCopy(src, dest)
  refreshTheme()
end

function getCurrentTheme()
  local reaperLastTheme = reaper.GetLastColorThemeFile()
  if(reaper.file_exists(reaperLastTheme)==true) then return reaperLastTheme
  else return nil
  end
end

function themeCheck() 
  if themeTitle ~= oldthemeTitle or themeTitle == nil then
    last_theme_filename = getCurrentTheme()
    last_theme_filename_check = reaper.time_precise()
    themeTitle = string.match(string.match(last_theme_filename or 'Assembled_Theme', '[^\\/]*$'),'(.*)%..*$') 
    switchTheme(themeTitle)
    oldthemeTitle = themeTitle
  else 
    local now = reaper.time_precise()
    if now > last_theme_filename_check+1 and suspendSwitchTheme ~= true  then -- once per second see if the theme filename changed
      last_theme_filename_check = now
      local tfn = reaper.GetLastColorThemeFile()
      if tfn ~= last_theme_filename then
        themeTitle = string.match(string.match(tfn, '[^\\/]*$'),'(.*)%..*$')
        switchTheme(themeTitle)
        last_theme_filename = tfn
      end
    end
  end
end

function switchTheme(thisTheme)
  if thisTheme ~= 'Assembled_Theme' and script_path and themes_path then
    if(reaper.file_exists(themes_path..'/Assembled_Theme.ReaperTheme')==true) then
      local v = reaper.ShowMessageBox('switch to Assembled Theme?', 'Wrong theme in use', 1)
      if v == 1 then reaper.OpenColorThemeFile(themes_path..'/Assembled_Theme.ReaperTheme') end
      if v == 2 then gfx.quit() end
    else
      local v = reaper.ShowMessageBox('Create theme?', 'Assembled Theme not found', 1)
      if v == 1 then 
        if OS:find("Win") ~= nil then
          if osCopy(script_path..'/theme_assembler/initial/', themes_path..'/') == true 
             then reaper.OpenColorThemeFile(themes_path..'/Assembled_Theme.ReaperTheme') end
        else
          if osCopy(script_path..'/theme_assembler/initial/Assembled_Theme.ReaperTheme', themes_path..'/Assembled_Theme.ReaperTheme') == true and
             osCopy(script_path..'/theme_assembler/initial/Assembled_Theme_Resources', themes_path..'/Assembled_Theme_Resources') == true
            then reaper.OpenColorThemeFile(themes_path..'/Assembled_Theme.ReaperTheme') end
        end
      end
      if v == 2 then gfx.quit() end
    end
  end
end

function setTarget(n) 
  target = n.title
  populateTarget(n)
end

function adoptChild(parent, child)
  if parent.children then parent.children[#parent.children + 1] = child
  else parent.children = {child}
  end
end

function populateTarget(t)

  local combinedStyles = {}
  for i,v in ipairs(buttonStyles) do table.insert(combinedStyles,v) end
  if t.buttonStyles then for i,v in ipairs(t.buttonStyles) do table.insert(combinedStyles,v) end end

  if chooserBox then chooserBox:purge() end -- kill a previous one
  chooserBox = El:new({parent=thinBox, x=0, y=0, flow=mcpBox, w=-10, h=100, r={toEdge, thinBox, 'right'}, children={}})
  if t.states then
 
    if t.chosenState==nil then t.chosenState = {} end
    for i,v in pairs(t.states) do -- i is button states

      chooserBox.children[i] = El:new({parent=chooserBox, flow=true,  x=0, y=0, border=10, w=0, r={toEdge, chooserBox, 'right'}, h=40, col={30,30,30}})
      titleBox = El:new({parent=chooserBox.children[i], x=0, y=0, w=0, h=16, r={toEdge, chooserBox, 'right'}, col={50,50,50}})

      if t.iType == 'meterV' or t.iType == 'meterH' then
        for q,r in ipairs({'Normal','Normal Clipped','Armed','Armed Clipped'}) do
          funcText:new({parent=titleBox, x=0, y=0, h=16, flow=true, resizeParent='v', mouseOverCol={255,255,255,50}, 
            text={str=r, style=2, align=1, col={200,200,200}},
            onClick = function() 
              t.meterColumn = q
              populateTarget(t)
            end}) -- the text that chooses from the different meter columns
         end
      
      else
        for q,r in pairs(v) do -- r[1] is image file name, r[2] is image title
          funcText:new({parent=titleBox, x=0, y=0, h=16, flow=true, resizeParent='v', mouseOverCol={255,255,255,50}, 
            text={str=string.gsub(r[2], "_", " "), style=2, align=1, col={200,200,200}},
            onClick = function() 
              t.chosenState[i] = q
              populateTarget(t)
            end}) -- the text that chooses from the different styles
        end
      end
      
      local stateIType = t.iType or nil
      if t.iTypeStates then stateIType = t.iTypeStates[i] end
      local varState = t.chosenState[i] or 1 -- meters don't have chosenState
      local p = script_path.."/theme_assembler/"..v[varState][1].."/"

      if t.iType == 'themeFile' then --not images, so can't pass the image exists check for the combinedStyles thing, so special case
        for l,m in ipairs(t.buttonStyles) do
          ChoiceBox:new({parent=chooserBox.children[i],x=0,y=0,w=100,h=50, flow=true, col={255,0,0}, title=m, iType='themeFile',
                          states=v, proxyCols=t.styleProxyCols[l]})
        end

      else for l,m in ipairs(combinedStyles) do
          local scaleString = ''
          if scaleFactor>100 then scaleString = '_'..scaleFactor end
          --if t.iType == 'themeFile' or reaper.file_exists(p..m..scaleString..'.png') then
          if reaper.file_exists(p..m..scaleString..'.png') then
            if t.iType == 'meterV' then
              ChoiceBox:new({parent=chooserBox.children[i],x=0,y=0,h=t.buttonH or nil,flow=true, img=m, noIScales=t.noIScales, iType=stateIType, onFps=t.onFps or nil, 
                              iLocation=v[1][1], meterColumn=(t.meterColumn or 1), states=v})
            elseif t.iType == 'meterH' then
              ChoiceBox:new({parent=chooserBox.children[i],x=0,y=0,w=t.buttonW or nil,flow=true, img=m, noIScales=t.noIScales, iType=stateIType, onFps=t.onFps or nil, 
                              iLocation=v[1][1], meterColumn=(t.meterColumn or 1), states=v})
            elseif t.iType == 'idxbgColorHack' then
              ChoiceBox:new({parent=chooserBox.children[i],x=0,y=0,w=80,h=50, flow=true, col={255,0,0}, img=m, iType='idxbgColorHack',
                              iLocation=v[varState][1], states=v})
            else
              ChoiceBox:new({parent=chooserBox.children[i],x=0,y=0,h=t.buttonH or nil,flow=true, img=m, iType=stateIType, onFps=t.onFps or nil, 
                            iLocation=v[varState][1], states=v})
            end
          
          end
        end
      end
    end
  end
  
  doArrange = true
end

function addTimer(self,index,time) 
  if Timers == nil then Timers = {} end
  if Timers[index] == nil then
    if self.Timers == nil then self.Timers = {} end
    self.Timers[index] = nowTime + time
    Timers[index] = self 
    return true
  end
end

function removeTimer(self,index)
  if self.Timers and self.Timers[index] and Timers[index] and self.onTimerComplete[index] then
    self.Timers[index], Timers[index], self.onTimerComplete[index] = nil, nil, nil
  end
end

function cycleBitmapStack(self)
  if self.iFrameC then
    self.iFrameDirection = self.iFrameDirection or 1
    if self.iFrame == self.iFrameC-1 and self.iFrameDirection == 1 then self.iFrameDirection = -1 end
    if self.iFrame == 0 then self.iFrameDirection = 1 end
    self.iFrame = self.iFrame + self.iFrameDirection
    self:addToDirtyZone()
  end
end

function fakeMeterVals(self)
  local newRnd, newVal = math.random(), (self.mValue or 1) * 0.85
  if newRnd > 0.8 then newVal = newRnd end
  self.mValue = newVal
  self:addToDirtyZone()
end

function refreshTheme()
  local thisTheme = reaper.GetLastColorThemeFile()
  reaper.OpenColorThemeFile(thisTheme)
end

function El:reloadImg()
  if self.img then
    if self.imgIdx then
      local i = scaleToDrawImg(self) 
      loadImage(self.imgIdx, i, self.iLocation or nil, self.noIScales)
    end
    self:addToDirtyZone()
  end
end

function scaleToDrawImg(self)
  local i = self.img
  local doScale = true
  if self.noIScales and self.noIScales == true then doScale = false end
  if self.iLocation and doScale == true then -- image lives in script resources
    if scaleMult == 1.5 then i = self.img..'_150' end
    if scaleMult == 2 then i = self.img..'_200' end 
  end
  return i
end

function setScale(scale)
  scaleMult = scale
  if scaleMult == 1 then textScaleOffs = 0 end
  if scaleMult == 1.5 then textScaleOffs = 10 end
  if scaleMult == 2 then textScaleOffs = 20 end
  reloadImgs()
  doArrange = true
  doOnGfxResize()
end

function fitText(self)
  gfx.setfont(self.text.style or 1)
 return gfx.measurestr(self.text.str)
end

function getPreviousEl(self) -- returns the previous child of this element's parent
  if self.parent then
    for i=1, #self.parent.children do
      if self.parent.children[i] == self and i>1 then
        return self.parent.children[i-1] 
      end
    end
  end
end

  --------- ARRANGE ----------

function El:dirtyXywhCheck(b,z)
  if self.drawX == nil then -- then you've never been arranged
    if self:arrange(self) == true then 
      self:addToDirtyZone(b, z, false) 
    end
  else
    self.ox,self.oy,self.ow,self.oh = self.drawX, self.drawY, self.drawW, self.drawH
    if self:arrange(self) == true then
      if self.drawX ~= self.ox or self.drawY ~= self.oy or self.drawW ~= self.ow or self.drawH ~= self.oh then 
        self:addToDirtyZone(b, z, true)
      end
    end
  end
end

function El:addToDirtyZone(b, z, newXywh)
  b = b or self.block or 1
  z = z or self.z or 1 
  local kx,ky,kw,kh = self.drawX or self.x, self.drawY or self.y, self.drawW or self.w or 0, self.drawH or self.h or 0 
  --reaper.ShowConsoleMsg((self.img or 'el')..' addToDirtyZone '..' kx:'..kx..' ky:'..ky..' kw:'..kw..' kh:'..kh..'\n')
  if dirtyZones[b] == nil then dirtyZones[b] = {} end
  if dirtyZones[b][z] == nil then dirtyZones[b][z] = {x1={},y1={},x2={},y2={}} end
  if kw ~= nil then
    dirtyZones[b][z].x1[#dirtyZones[b][z].x1+1] = kx
    dirtyZones[b][z].y1[#dirtyZones[b][z].y1+1] = ky
    dirtyZones[b][z].x2[#dirtyZones[b][z].x2+1] = kx + kw
    dirtyZones[b][z].y2[#dirtyZones[b][z].y2+1] = ky + kh
    --reaper.ShowConsoleMsg('b='..b..',z='..z..' x y w h = '..kx..' '..ky..' '..kw..' '..kh..'\n')
  end
  if newXywh == true then -- element has moved, so also dirtyZone its old location
    dirtyZones[b][z].x1[#dirtyZones[b][z].x1+1] = self.ox
    dirtyZones[b][z].y1[#dirtyZones[b][z].y1+1] = self.oy
    dirtyZones[b][z].x2[#dirtyZones[b][z].x2+1] = self.ox + self.ow
    dirtyZones[b][z].y2[#dirtyZones[b][z].y2+1] = self.oy + self.oh
  end
  doDraw = true
  return true
end

function El:drawToBuffer(buffer,dx,dy,dw,dh)
  local kx,ky,kw,kh = self.drawX or self.x, self.drawY or self.y, self.drawW or self.w or 0, self.drawH or self.h or 0 
  if hasOverlap(kx,ky,kw,kh,dx,dy,dw,dh) == true then
    self:draw(buffer,dx,dy) --draw the element to the buffer
  end
end

function hasOverlap(x1,y1,w1,h1,x2,y2,w2,h2)
  if x1+w1 > x2 and x1 < x2 + w2 and y1+h1 > y2 and y1 < y2 + h2 then return true end
end

function resizeParent(self)
  if self.resizeParent and self.resizeParent=='v' and (self.drawY + self.drawH) > (self.parent.drawY + self.parent.drawH) then
    self.parent.ox, self.parent.oy, self.parent.ow, self.parent.oh = self.parent.drawX, self.parent.drawY, self.parent.drawW, self.parent.drawH
    self.parent.drawH = self.drawY + self.drawH - self.parent.drawY + (self.border or 0)
    self.parent:addToDirtyZone(self.parent.block or 1, self.parent.z or 1, true)
    if self.parent.parent then resizeParent(self.parent) end
  end
end

function doOnGfxResize()
  for b in ipairs(els) do -- iterate blocks 
    for z in ipairs(els[b]) do -- iterate z
      if els[b][z] ~= nil then
        for j,k in pairs(els[b][z]) do
          if k.onGfxResize then k.onGfxResize(k) end
          doArrange = true
        end
      end
    end
  end
end

function toEdge(self,edge) -- sets an edge to another element's edge. Called by el:arrange()
 if edge == 'left' then -- my left edge
    if self.l[3] == 'left' then reaper.ShowConsoleMsg('left toEdge left not done yet\n') end
    if self.l[3] == 'right' then return self.l[2].drawX + self.l[2].drawW + self.x end
  end
  if edge == 'top' then -- my top edge
    if self.t[3] == 'top' then return self.t[2].drawY + self.y end
    if self.t[3] == 'bottom' then return self.t[2].drawY + self.t[2].drawH + self.y end
  end
  if edge == 'right' then -- my right edge
    if self.r[3] == 'left' then reaper.ShowConsoleMsg('right toEdge left not done yet\n') end
    if self.r[3] == 'right' then return self.r[2].drawX + self.r[2].drawW - (self.drawX or self.x) + self.w end
  end
  if edge == 'bottom' then -- my bottom edge
    if self.b[3] == 'top' then reaper.ShowConsoleMsg('bottom toEdge top not done yet\n') end
    if self.b[3] == 'bottom' then return self.b[2].drawY + self.b[2].drawH - self.drawY + self.h end
  end
end

function El:arrange()
  local px, py, pw, ph, pCOffx, pCOffy = 0, 0, 0, 0, 0, 0 -- pCOff are the parent's clipping offsets
  if self.parent ~= nil then 
    px, py, pw, ph = self.parent.drawX or 0, self.parent.drawY or 0, self.parent.drawW or 0, self.parent.drawH or 0 
  end
  
  if self.fieldParent ~= nil then -- attach elements to reordering tcp box fields
    for i,v in ipairs(orderFields) do
      if v.field == self.fieldParent then
        px, py, pw, ph = v.drawX or v.x or 0, v.drawY or v.y or 0, v.drawW or 0, v.drawH or 0
        v.w = self.fieldW or 120
      end
    end
  end
 
  if self.onArrange then self.onArrange(self) end
  
  self.drawX, self.drawY = px+((self.x or 0)+(self.border or 0)-pCOffx)*scaleMult, py+((self.y or 0)+(self.border or 0)-pCOffy)*scaleMult 
  self.drawW, self.drawH = (self.w or 0)*scaleMult, (self.h or 0)*scaleMult
      
  if self.l ~= nil then self.drawX = self.l[1](self,'left') end
  if self.t ~= nil then self.drawY = self.t[1](self,'top') end
  if self.r ~= nil then self.drawW = self.r[1](self,'right') end
  if self.b ~= nil then self.drawH = self.b[1](self,'bottom') end
  if self.minW ~= nil and self.drawW < self.minW then self.drawW = self.minW end
  if self.minH ~= nil and self.drawH < self.minH then self.drawH = self.minH end

  if self.img then 
    self.drawImg = scaleToDrawImg(self) -- adds _150 or _200 to name
    if self.imgIdx == nil then self.imgIdx = getImage(self.drawImg, self.iLocation, self.noIScales) end
    --self.imgIdx = getImage(self.drawImg, self.iLocation, self.noIScales)
    self.measuredImgW, self.measuredImgH = gfx.getimgdim(self.imgIdx)
    local pinkAdjustedImgW, pinkAdjustedImgH = self.measuredImgW, self.measuredImgH
    if bufferPinkValues[self.imgIdx] then pinkAdjustedImgW, pinkAdjustedImgH = self.measuredImgW-2, self.measuredImgH-2 end

    if self.iType ~= nil then
      if self.iType == 3 then 
        if self.w==nil then self.drawW = pinkAdjustedImgW/3 end
        if self.h==nil then self.drawH = pinkAdjustedImgH end
      elseif self.iType == 'stack' then 
        self.drawW, self.drawH = self.measuredImgW, self.measuredImgW
      else -- any other iType
        if self.w==nil then self.drawW = pinkAdjustedImgW end
        if self.h==nil then self.drawH = pinkAdjustedImgH end 
      end
    end

  end 
  
  local b = self.border or 0
  if self.flow then
    if self.flow == true then self.flow = getPreviousEl(self) or nil end -- auto set previous child as flow element
    if type(self.flow) == 'table' then
    
      local fx, fy = self.flow.drawX + self.flow.drawW + (self.x*scaleMult or 0) + b, self.flow.drawY
      if fx + b + self.drawW > px+pw then -- then flow to next row
        fx = (self.x*scaleMult or 0) + px + b
        fy = self.flow.drawY + self.flow.drawH + (self.y*scaleMult or 0) + b
      end
      self.drawX, self.drawY = fx, fy
      
    end 
  end
 
  resizeParent(self) -- checks if el has a resizeParent set, and if so does that
  
  if self.elAlign then
  
    if self.elAlign.x then
      local target = self.elAlign.x[1]
      if self.elAlign.x[1]=='parent' then target = self.parent end
      tx,tw = target.drawX or target.x, target.drawW or target.w
      if self.elAlign.x[2]=='centre' then self.drawX = tx+(tw/2)-(self.drawW/2)+ (self.x*scaleMult) end 
      if self.elAlign.x[2]=='right' then self.drawX = tx + tw - self.drawW + (self.x*scaleMult) end
    end
    
    if self.elAlign.y then
      local target = self.elAlign.y[1]
      if self.elAlign.y[1]=='parent' then target = self.parent end
      ty,th = target.drawY or target.y, target.drawH or target.h
      if self.elAlign.y[2]=='centre' then self.drawY = ty+(th/2)-(self.drawH/2)+self.y end
      if self.elAlign.y[2]=='bottom' then reaper.ShowConsoleMsg('element align bottom not done yet\n') end
    end

  end
  
  if self.clip==true then
    if (self.drawX + self.drawW +b > px+pw) or (self.drawY + self.drawH +b > py+ph) then 
      self.drawW = 0 
    end
  end
  
  --check final position, cull if outside parent
  if self.drawX > px+pw then -- fully to the right of parent
    self.drawW = 0 -- using zero width (instead of some kind of 'don't draw' state) so that dirtyCheck notices
  end

  return true
end




  --------- DRAW ----------
  
function El:draw(z,offsX,offsY)
  gfx.dest = (z or 1)
  local x,y,w,h = self.drawX or self.x or 0, self.drawY or self.y or 0, self.drawW or self.w or 0, self.drawH or self.h or 0
  x, y = x-offsX, y-offsY
  local col = self.drawCol or self.col or nil
  if col ~= nil then -- fill
    setCol(col)
    if self.shape ~= nil then
      if self.shape == 'circle' then gfx.circle(x+w/2,y+w/2,w/2,1,1) end
    else gfx.rect(x,y,w,h)
    end
  end
  if self.strokeCol ~= nil then -- stroke
    local c = fromRgbCol(self.strokeCol)
      gfx.set(c[1],c[2],c[3],c[4])
      if self.shape ~= nil then reaper.ShowConsoleMsg('non-rectangular strokes not done yet in El:draw\n') 
      else 
        gfx.line(x,y+h,x,y,0)
        gfx.line(x+1,y,x+w,y,0)
        gfx.line(x+w,y+1,x+w,y+h)
        gfx.line(x+1,y+h,x+w-1,y+h)
      end
  end
  if self.text ~= nil then
    if self.text.val ~=nil then self.text.str = self.text.val() end
    local tx,tw = x + textPadding, w - 2*textPadding
    text(self.text.str,tx,y,tw,h,self.text.align,self.text.col,((self.text.style + textScaleOffs) or 1),self.text.lineSpacing,self.text.vCenter,self.text.wrap)
  end
 
  if self.drawImg ~= nil then
 
    local pinkXY, pinkWH, imgW, imgH = 0,0,self.measuredImgW, self.measuredImgH
    if bufferPinkValues[self.imgIdx] then 
      pinkXY, pinkWH, imgW, imgH = 1, 2, self.measuredImgW-2, self.measuredImgH-2
    end

    gfx.a = (self.img.a or 255) / 255
    if self.iType == 'stack' then 
      local iFrameHScaled = self.iFrameH * scaleMult  
      if self.iFrameC == nil then self.iFrameC = self.measuredImgH / iFrameHScaled end
      local frame = (self.iFrame or 0) * self.measuredImgW --iFrameHScaled
      --reaper.ShowConsoleMsg('blit imgIdx '..self.imgIdx..' bitmap stack '..self.img..' frame '..frame..' at '..x..'  '..y..'  iFrameHScaled: '..iFrameHScaled..'  self.measuredImgW: '..self.measuredImgW..'\n')
      --gfx.blit(source, scale, rotation, srcx, srcy, srcw, srch, destx, desty, destw, desth
      gfx.blit(self.imgIdx, 1, 0, 0, frame, self.measuredImgW, self.measuredImgW, x, y, w, self.measuredImgW)
      
    elseif self.iType == 'meterV' then
      local mColm = (self.meterColumn  or 1)*2 
      local stripW, displayVal = self.measuredImgW / 8, self.mValue or 0
      gfx.blit(self.imgIdx, 1, 0, stripW*(mColm-2), 0, stripW, self.measuredImgH, x, y, w, h)
      gfx.blit(self.imgIdx, 1, 0, stripW*(mColm-1), self.measuredImgH*(1-displayVal), stripW, self.measuredImgH*displayVal, x, y+(h*(1-displayVal)), w, h*displayVal)
    
    elseif self.iType == 'meterH' then
      local mRow = (self.meterColumn  or 1)*2 
      --reaper.ShowConsoleMsg('blit meter value '..self.mValue..' at '..x..'  '..y..', w: '..w..', h: '..h..', iDw: '..iDw..'\n')
      local stripH, displayVal = self.measuredImgH / 8, self.mValue or 0
      gfx.blit(self.imgIdx, 1, 0, 0, stripH*(mRow-2), self.measuredImgW, stripH, x, y, w, h)
      gfx.blit(self.imgIdx, 1, 0, 0, stripH*(mRow-1), self.measuredImgW*displayVal, stripH, x, y, w*displayVal, h)
      
    elseif self.iType == 'idxbgColorHack' then
      gfx.blit(self.imgIdx, 1, 0, 1000, 4, 1, 1, x+16, y, w-(16*scaleMult), h)
      
    elseif self.iType == 'tcpIdxBg' then
      local tx, ly, bx,ry = bufferPinkValues[self.imgIdx].tx, bufferPinkValues[self.imgIdx].ly, bufferPinkValues[self.imgIdx].bx, bufferPinkValues[self.imgIdx].ry
      local stretchedC2W, stretchedR2H = w -tx -bx +2, h -ly -ry +2
      local idxColumnW = 18*scaleMult
      
      --gfx.blit(source, scale, rotation, srcx, srcy, srcw, srch, destx, desty, destw, desth)
      gfx.blit(self.imgIdx, 1, 0, tx-2, 1, 1, ly-1, x, y, 1, ly-1)
      gfx.blit(self.imgIdx, 1, 0, 1+tx, 1, self.measuredImgW-tx-bx-1, ly-1, x+1, y, idxColumnW, ly-1)
      gfx.blit(self.imgIdx, 1, 0, self.measuredImgW-bx, 1, w-1-idxColumnW, ly-1, x +1 +idxColumnW, y, w-1-idxColumnW, ly-1)
      
      gfx.blit(self.imgIdx, 1, 0, tx-2, ly, 1, self.measuredImgH-ly-ry, x, y+ly-1, 1, stretchedR2H)
      gfx.blit(self.imgIdx, 1, 0, tx, ly, self.measuredImgW-tx-bx, self.measuredImgH-ly-ry, x+1, y+ly-1, idxColumnW, stretchedR2H)
      gfx.blit(self.imgIdx, 1, 0, self.measuredImgW-bx, ly, w-1-idxColumnW, self.measuredImgH-ly-ry, x +1 +idxColumnW, y+ly-1, w-1-idxColumnW, stretchedR2H)
      
      gfx.blit(self.imgIdx, 1, 0, tx-2, self.measuredImgH-ry, 1, ry-1, x, y+ly-1+stretchedR2H, 1, ry-1)
      gfx.blit(self.imgIdx, 1, 0, tx, self.measuredImgH-ry, self.measuredImgW-tx-bx, ry-1, x+1, y+ly-1+stretchedR2H, idxColumnW, ry-1)
      gfx.blit(self.imgIdx, 1, 0, self.measuredImgW-bx, self.measuredImgH-ry, w-1-idxColumnW, ry-1, x +1 +idxColumnW, y+ly-1+stretchedR2H, w-1-idxColumnW, ry-1)
    
    elseif self.iType == 3 then -- a 3 frame button
      --reaper.ShowConsoleMsg('draw '..self.img..' with pink; imgW='..imgW..', w='..w..' imgH='..imgH..', h='..h..'\n')
      local frameW = imgW/3
      if w==0 then w=frameW end
      if h==0 then h=imgH end
      
      if bufferPinkValues[self.imgIdx] then
        if frameW==w  and imgH==h  then --if this image is going to drawn at size, just draw it.
          --reaper.ShowConsoleMsg('normal blit iType 3, iframe= '..(self.iFrame or 0)..', img: '..self.img..'\n')
          gfx.blit(self.imgIdx, 1, 0, (self.iFrame or 0)*frameW +pinkXY, pinkXY, w, h, x, y, w, h)
        else
          --reaper.ShowConsoleMsg('pinkBlit iType 3, iframe= '..(self.iFrame or 0)..', img: '..self.img..'\n')
          local tx, ly, bx,ry = bufferPinkValues[self.imgIdx].tx, bufferPinkValues[self.imgIdx].ly, bufferPinkValues[self.imgIdx].bx, bufferPinkValues[self.imgIdx].ry
          --reaper.ShowConsoleMsg('tx: '..tx..', ly: '..ly..', bx: '..bx..', ry: '..ry..', w: '..w..', h: '..h..', self.measuredImgW: '..self.measuredImgW..', self.measuredImgH: '..self.measuredImgH..', pinkXY:'..pinkXY..', pinkWH: '..pinkWH..' \n')
          local unstretchedC2W, unstretchedR2H = frameW+2 -tx -bx, imgH+2 -ly -ry    --frameW rather than imgH in this case, because it is a 3 state image
          local stretchedC2W, stretchedR2H = w -tx -bx +2, h -ly -ry +2
          pinkBlit(self.imgIdx, ((self.iFrame or 0)*frameW), 0, x, y, tx, ly, bx, ry, unstretchedC2W, unstretchedR2H, stretchedC2W, stretchedR2H)
        end
      else --3 frame button with no pink
        --reaper.ShowConsoleMsg('draw '..self.img..' a 3 frame button with no pink; imgW='..imgW..', w='..w..' imgH='..imgH..', h='..h..'\n')
        gfx.blit(self.imgIdx, 1, 0, (self.iFrame or 0)*frameW, 0, w, h, x, y, w, h)
      end
      
    elseif self.iType ~= nil then
      --reaper.ShowConsoleMsg('blit iType='..self.iType..' image='..self.img..' to z='..z..',   w='..w..',   h='..h..',   x='..x..', y='..y..' \n')
      if bufferPinkValues[self.imgIdx] then
        if imgW==w  and imgH==h  then --if this image is going to drawn at size, just draw it.
          --reaper.ShowConsoleMsg('drawing image '..self.img..' that has pink, but is unstretched\n')
          gfx.blit(self.imgIdx, 1, 0, (self.iFrame or 0)*w +pinkXY, pinkXY, w, h, x, y, w, h)
        else --draw the image using pink stretching.
          --reaper.ShowConsoleMsg('drawing image '..self.imgIdx..': '..self.img..' that has no type, has pink, and is stretched\n')
          local tx, ly, bx,ry = bufferPinkValues[self.imgIdx].tx, bufferPinkValues[self.imgIdx].ly, bufferPinkValues[self.imgIdx].bx, bufferPinkValues[self.imgIdx].ry
          --reaper.ShowConsoleMsg('tx: '..tx..', ly: '..ly..', bx: '..bx..', ry: '..ry..', w: '..w..', h: '..h..', self.measuredImgW: '..self.measuredImgW..', self.measuredImgH: '..self.measuredImgH..', pinkXY:'..pinkXY..', pinkWH: '..pinkWH..' \n')
          pinkBlit(self.imgIdx, 0, 0, x, y, tx, ly, bx, ry, self.measuredImgW-tx-bx, self.measuredImgH-ly-ry, w-tx-bx+pinkWH, h-ly-ry+pinkWH)
        end
      elseif self.iType == 'hThumb' then -- clip off the special case bottom edge pink
        gfx.blit(self.imgIdx, 1, 0, 0, 0, w, h-1, x, y, w, h-1)
      elseif self.iType == 'vThumb' then -- clip off the special case right edge pink
        gfx.blit(self.imgIdx, 1, 0, 0, 0, w-1, h, x, y, w-1, h)
      else --image with no pink
        gfx.blit(self.imgIdx, 1, 0, (self.iFrame or 0)*w, 0, w, h, x, y, w, h)
      end
    
    else gfx.blit(self.imgIdx, 1, 0, 0, 0, iDw, iDh, x, y, w, h) --not an image
    end
    
  end
end



  --------- MOUSE ---------
  
function El:mouseOver()
  if self.mouseOverCol ~= nil then 
    self.drawCol = self.mouseOverCol
    self:addToDirtyZone()
  end
  if self.mouseOverCursor ~= nil then
    gfx.setcursor(429,1)
  end
  if self.img ~= nil then
    if self.iType ~= nil and self.iType == 3 then
      self.iFrame = 1
      self:addToDirtyZone()
    end
  end
end


function El:showTooltip()
  if self.toolTip ~= nil then
    if addTimer(self,'toolTip',0.5) == true then
      if self.onTimerComplete == nil then self.onTimerComplete = {} end
      self.onTimerComplete.toolTip = function()
          local blah, windX, windY = gfx.dock(-1,0,0)
          reaper.TrackCtl_SetToolTip(self.toolTip, windX + gfx.mouse_x +(24*scaleMult), windY + gfx.mouse_y +(48*scaleMult),false)
        end
    end
  end
end

function El:mouseAway()
  if self.mouseOverCol ~= nil then 
    self.drawCol = self.col
    self:addToDirtyZone()
  end
  if self.mouseOverCursor ~= nil then
    gfx.setcursor(1,1)
  end
  if self.img ~= nil then
    if self.iType ~= nil and self.iType == 3 then
      self.iFrame = 0
      self:addToDirtyZone()
    end
  end
  reaper.TrackCtl_SetToolTip('',0,0,true)
  removeTimer(self,'toolTip')
end

function El:mouseDown(x,y)
  if self.img ~= nil then
    if self.iType ~= nil and self.iType == 3 then
      self.iFrame = 2
      self:addToDirtyZone()
    end
  end
  if self.onClick ~= nil and singleClick ~= true then
    singleClick = true
    self.onClick(self)
  end
  if self.onDrag then
    dX, dY = mouseDrag(self)
    self.onDrag(self, 'set', nil, dX, dY)
  end
end

function mouseDrag(self)
  if dragStart == nil then dragStart = {x=gfx.mouse_x, y=gfx.mouse_y} end
  local dX, dY = gfx.mouse_x - dragStart.x, gfx.mouse_y - dragStart.y
  
  local ctrl = gfx.mouse_cap&4
  if ctrl == 4 then -- ctrl
    if dragStart.fine ~= true then
      dragStart = {x=dragStart.x+dX, y=dragStart.y+dY}
      dragStart.fine = true
    end
    dX, dY = (gfx.mouse_x - dragStart.x)*0.25, (gfx.mouse_y - dragStart.y)*0.25
  end
  return dX, dY
end

function passToEl(self,...)
  --argsCheck = {...}
  self.El.action(self.El,...)
end

function El:doubleClick() 
  if self.onDoubleClick ~= nil then
    if type(self.onDoubleClick) == 'string' then
      if self.onDoubleClick == 'resetEl' then passToEl(self,'set','reset') end
      if self.onDoubleClick == 'reset' then self.action(self, 'set', 0) end
    else self.onDoubleClick(self)
    end
  end
end

function El:mouseWheel(wheel_amt)
  if self.action ~= nil then
    self.action(self,'set',wheel_amt)
  end
end





  --------- POPULATE ----------

--colDebug = true
--debugBuffers = true
setScale(1)
buttonStyles = {'alloy', 'soft', 'rounded', 'flat', 'dark_flat', 'transparent_flat', 'dark_planar', 'dark_rounded', 'default_5', 'grey_rounded', 
  'icon', 'icon_field', 'bordered', 'bordered_white', 'filled_flat', 'grey_field', 'grey_icon', 'traditional','reversed', 'sand', 'graphite', 'paper', 'poly',
  'shadow', 'no_shadow'}
scaleFactor = 100

themeFolder = "Assembled_Theme_Resources"

Block:new({})
thinBox = El:new({block=1, z=1, x=0, y=0, w=800, h=800, col={35,35,35}, interactive=false,
  onGfxResize = function()
    thinBox.w, thinBox.h = gfx.w/scaleMult, gfx.h/scaleMult
    thinBox:addToDirtyZone(thinBox.z)
  end
  })
  
topBar = El:new({parent=thinBox, x=0, y=0, w=0, h=16, r={toEdge, thinBox, 'right'}, col={20,20,20} })

DPIdisplay = El:new({parent=topBar, x=0, w=220, y=0,h=16, toolTip='Display Scale',
      text={str='', style=2, align=5, col={150,150,150}},
      onDpiChange = function() 
        DPIdisplay.text.str = 'THIS DISPLAY : '..math.floor(100*gfx.ext_retina)..'%        DRAW : '
        DPIdisplay:addToDirtyZone(DPIdisplay.z)
      end})
      
      
scale100 = El:new({parent=topBar, resizeParent='v', flow=DPIdisplay, z=1, x=0, y=0, w=40, h=16, col={20,20,20}, mouseOverCol={70,70,70}, 
      text={str='100%', style=2, align=5, col={150,150,150}}, toolTip='Draw at 100% Scale',
      onClick = function() setScale(1) end })  
      
scale150 = El:new({parent=topBar, resizeParent='v', flow=scale100, z=1, x=2, y=0, w=40, h=16, col={20,20,20}, mouseOverCol={70,70,70}, 
      text={str='150%', style=2, align=5, col={150,150,150}}, toolTip='Draw at 150% Scale',
      onClick = function() setScale(1.5) end })   
      
scale200 = El:new({parent=topBar, resizeParent='v', flow=scale150, z=1, x=2, y=0, w=40, h=16, col={20,20,20}, mouseOverCol={70,70,70}, 
      text={str='200%', style=2, align=5, col={150,150,150}}, toolTip='Draw at 200% Scale',
      onClick = function() setScale(2) end })
      
exportButton = El:new({parent=topBar, resizeParent='v', flow=scale200, z=1, x=6, y=0, w=100, h=16, col={10,100,80}, mouseOverCol={70,200,150}, 
      text={str='EXPORT THEME', style=2, align=5, col={0,0,0}}, toolTip='Export a copy of theme',
      onClick = function() 
        local name = 'Assembled_Theme_Export'
        local r, newName = reaper.GetUserInputs('Export Theme', 1, 'Theme Name,extrawidth=100', name)
        if newName ~= false then --check if name already exists
          if(reaper.file_exists(themes_path..'/'..newName..'.ReaperTheme')==true) or (reaper.file_exists(themes_path..'/'..newName..'.ReaperThemeZip')==true) then
            r, newName = reaper.GetUserInputs('ERROR : Theme '..newName..' already exists', 1, 'Theme Name,extrawidth=100', newName)
          end
        end
        if newName ~= false then
          if OS:find("Win") ~= nil then themes_path = themes_path:gsub("/","\\") end --to stop it being reported as a bug
          local k = reaper.MB('Export '..newName..'.ReaperTheme to '..themes_path..'?', 'Export Theme', 1)
          if k == 1 then
            
            if setReaperThemeVar('ui_img=', newName..'_Resources', newName) == true and
              osCopy(themes_path..'/Assembled_Theme_Resources', themes_path.."/"..newName..'_Resources') == true then --both the same for any OS?
              local m = reaper.MB(newName..'.ReaperTheme exported. Switch to it now?', 'Exported', 4)
              if m==6 then 
                reaper.OpenColorThemeFile(themes_path..'/'..newName..'.ReaperTheme')
                Quit()
              end
            end
            
          end
        end
        
      end 
      })      
      
eraseButton = El:new({parent=topBar, resizeParent='v', flow=exportButton, z=1, x=6, y=0, w=100, h=16, col={100,10,10}, mouseOverCol={255,70,70}, 
      text={str='ERASE THEME', style=2, align=5, col={0,0,0}}, toolTip='Reset all changes',
      onClick = function() 
        suspendSwitchTheme = true
        local v = reaper.ShowMessageBox('Erase the theme file, then close the Theme Assembler?', 'ERASE THEME', 1)
        if v == 1 then 
          if os.remove(themes_path..'/Assembled_Theme.ReaperTheme') then
            reaper.OpenColorThemeFile(themes_path..'/Default.ReaperTheme')
            gfx.quit()
          end
        end
      end 
      }) 
      
 
---- TCP Box ----

tcpBox = El:new({parent=thinBox, flow=topBar, x=10, y=10, w=448, h=70, col={129,137,137}, interactive=false,
      onReaperChange = function()
        if projectCustCols == nil then getProjectCustCols() end
      end,
      nextFrameTime = 0,
      onFps = function()
        if projectCustCols ~= nil and #projectCustCols>0 and nowTime > tcpBox.nextFrameTime then
          representCustCol = projectCustCols[math.random(1,#projectCustCols)]
          tcpBox.col = representCustCol
          tcpBox.nextFrameTime = nowTime + 2
          tcpBox:addToDirtyZone()
        end
      end
      })

TargetButton:new({parent=tcpBox, x=0, y=0, w=448, h=70, title = 'tcp_idxbg', iType = 'tcpIdxBg', interactive=false, 
      states = {
      bg = {{'tcp_bg', 'normal'}, {'tcp_bgsel', 'selected'}} 
      }
  })
  
idxButton = TargetButton:new({parent=tcpBox, x=0, y=0, w=50, h=50, col={0,0,255,0}, iType = 'idxbgColorHack', title = 'tcp_idxbg', toolTip='Background & Custom Color Strength',
      buttonStyles = {'100', '80', '60', '40', '20', '0', 'v5ish', 'panel'},
      states = {
      norm = {{'tcp_idxbg', 'unselected'}, {'mcp_idxbg', 'mixer unselected'}},
      sel = {{'tcp_idxbg_sel', 'selected'}, {'mcp_idxbg_sel', 'mixer selected'}}
      }
  }) 
  
El:new({parent=tcpBox, x=214, y=0, w=234, h=35, col={38,38,38}, interactive=false})    
  
idxText = El:new({parent=tcpBox, x=0, y=26, w=20, h=16, col={0,0,0,0}, mouseOverCol={255,255,255,100}, 
      text={str='1', style=2, align=5, col={255,255,255}}, toolTip='Track Number Brightness',
      onArrange = function()
        local n = getRtconfigVar('textOverCCbrightness') 
        idxText.text.col = {n,n,n}
      end,
      onClick = function() 
        local val = getRtconfigVar('textOverCCbrightness') or ""
        local r, v = reaper.GetUserInputs('Track Number Text', 1, 'Brightness (0-255)',val)
        local n = math.Clamp(tonumber(v),0,255)
        setRtconfigVar('textOverCCbrightness', n)
        idxText.text.col = {n,n,n}
      end
  })  

El:new({parent=tcpBox, x=26, y=9, img='track_recarm_off_ol', iType=3})

TargetButton:new({parent=tcpBox, x=27, y=10, title = 'track_recarm_off',  toolTip='Track Record Arm',
      buttonStyles = {'dark_shadow', 'dark', 'light_shadow', 'light', 'none_shadow', 'none'},
      states = {
      off = {{'track_recarm_off', 'Record Arm'}, {'track_recarm_auto','Automatic Arm'}},
      on = {{'track_recarm_on','Record Arm On'}, {'track_recarm_auto_on','Automatic Arm On'}, {'track_recarm_norec', 'Record Disabled'}, {'track_recarm_auto_norec','Automatic Disabled'}},
      shadow = {{'track_recarm_off_ol', 'Record Arm Shadow'}, {'track_recarm_auto_ol','Automatic Arm Shadow'}, {'mcp_recarm_off_ol', 'Mixer Record Arm Shadow'}, {'mcp_recarm_auto_ol','Mixer Automatic Arm Shadow'},
            {'track_recarm_on_ol','Record Arm On Shadow'}, {'track_recarm_auto_on_ol','Automatic Arm On Shadow'}, {'track_recarm_norec_ol', 'Record Disabled Shadow'}, {'track_recarm_auto_norec_ol','Automatic Disabled Shadow'}}
      }
  })
  
TargetButton:new({parent=tcpBox, x=48, y=9, title = 'track_monitor_off_ol', toolTip='Track Monitor', 
      buttonStyles = {'dark', 'light', 'light_white', 'none', 'none_white'},
      states = {
      off = {{'track_monitor_off_ol', 'Monitor Off'}},
      on = {{'track_monitor_on_ol','Monitor On'}},
      auto = {{'track_monitor_auto_ol', 'Monitor Auto'}}
      }
  })  
  
tcp_name = TargetButton:new({parent=tcpBox, x=62, y=9,w=120, title = 'tcp_namebg', iType = 'bg', toolTip='Track Name Background',
      buttonStyles = {'dark', 'light', 'none'},
      states = {
      input = {{'tcp_namebg', 'Track Name'}} 
      }
  })
  
tcpNameText = El:new({parent=tcp_name, x=0, y=0, w=80, h=22, col={0,0,0,0}, mouseOverCol={255,255,255,100}, toolTip='Track Name Brightness',
      text={str='Track Name', style=2, align=4, col={255,255,255}},
      onArrange = function()
        local n = getRtconfigVar('trackNameBrightness') 
        tcpNameText.text.col = {n,n,n}
      end,
      onClick = function() 
        local fields = {'trackNameBrightness', 'trackNameLighten', 'lightenThreshold'}
        local fieldVals = {0,0,0}
        for i,v in pairs(fields) do fieldVals[i] = getRtconfigVar(v)  end
        local r, v = reaper.GetUserInputs('Track Name Text', 3, 'Brightness (0-255),Custom Colour Offset (-255-255),Offset Threshold (0-255)',fieldVals[1]..','..fieldVals[2]..','..fieldVals[3])
        local userInputs = {}
        if r~=false then
          for ret in string.gmatch(v, '([^,]+)') do table.insert(userInputs,ret) end
          for i,v in pairs(fields) do
            local n = math.Clamp(tonumber(userInputs[i]),-255,255)
            setRtconfigVar(fields[i], n)
            if i==1 then 
              tcpNameText.text.col = {n,n,n}
              tcpNameText:addToDirtyZone()
            end
          end
        end
      end
  })
  
knobBg = El:new({parent=tcpBox, x=182, y=8, img='tcp_vol_knob_small', iType=1})

TargetButton:new({parent=knobBg, x=2, y=2, z=1, title = 'tcp_vol_knob_stack', iType = 'stack', iTypeStates={stack='stack',knob=1}, iFrame = 1, toolTip='Track Volume Knob',
      onFps = cycleBitmapStack, 
      buttonStyles = {'flower', 'radar', 'segment', 'segment_wide', 'arc', 'black_line', 'white_line', 'green_line', 'black_dot', 'white_dot', 'arc_on_dark',
                      'swipe_green', 'swipe_grey', 'dark_alloy', 'grey', 'none', 'light_post', 'dark_post', 'flat_post',
                      'alloy_light', 'none_light', 'none_none', 'grey_light', 'grey_none', 'dark_alloy_light', 'dark_alloy_none', 'dark_round_light', 'dark_round_none',
                      'soft_light', 'soft_none', 'dark_flat_light', 'dark_flat_none', 'dark_post_light', 'dark_post_none', 'light_post_light', 'light_post_none', 
                      'flat_post_light', 'flat_post_none'},
      states = {
      stack = {{'tcp_vol_knob_stack', 'Volume Knob Pointer'}}, 
      knob = {{'tcp_vol_knob_small', 'Volume Knob'}}
      }
  })
  
TargetButton:new({parent=tcpBox, x=226, y=12, z=1, w=144, h=12, buttonW=200, title = 'meter_strip_h', iType = 'meterH', noIScales = true, onFps = fakeMeterVals, toolTip='Horizontal Meter',
      buttonStyles = {'v6', 'NoArm', 'gradient', 'green_to_red', 'g2r-gradient', 'discharge', 'discharge+', 'grey', '0-6-12', '0-6-18', '0-12-18', '0-12-24'},
      states = {
      meter_v = {{'meter_strip_h', 'Horizontal Meter'}}
      }
  }) 
  
TargetButton:new({parent=tcpBox, x=380, y=8, title = 'track_mute_off_ol', toolTip='Track Mute',
      states = {
      off = {{'track_mute_off_ol', 'Mute'}},
      on = {{'track_mute_on_ol', 'Mute On'}}
      }
  })  
 
TargetButton:new({parent=tcpBox, x=400, y=8, title = 'mcp_solo_off_ol', toolTip='Track Solo', 
      states = {
      off = {{'mcp_solo_off_ol', 'Mixer Solo'},{'track_solo_off_ol', 'Track Solo'}}, 
      on = {{'mcp_solo_on_ol', 'Mixer Solo On'},{'track_solo_on_ol', 'Track Solo On'}},
      defeat = {{'mcp_solodefeat_on_ol','Mixer Solo Defeat'}, {'tcp_solodefeat_on_ol','Track Solo Defeat'}}
      }
  })
  
TargetButton:new({parent=tcpBox, x=424, y=8, title = 'track_phase_norm_ol', toolTip='Track Phase',
      states = {
      off = {{'track_phase_norm_ol', 'Phase Normal'}},
      on = {{'track_phase_inv_ol', 'Phase Inverted'}}
      }
  }) 
      
      
      
      
orderThing = El:new({parent=tcpBox, x=14, y=28, w=440, h=46, col={255,60,60,0}, interactive=false,
      onArrange = function()

        local str = themes_path..'/'..themeFolder..'/'..'rtconfig.txt'
        if OS:find("Win") ~= nil then str = str:gsub("/","\\") end
        local rtConfigTable = {}
        local tableFilled = false
        
        for line in io.lines(str) do
          if string.find(line, 'then tcp') then
            table.insert(rtConfigTable, {line})
            tableFilled = true
          else
            if tableFilled == true then break end
          end
        end
        
        if tableFilled == true then
          for i,v in ipairs(rtConfigTable) do
            if i>=5 then -- apply new field assigments to the orderField elements
              for j, k in pairs({{'tcp.io',42},{'tcp.env',50},{'tcp_fx_group',44},{'tcp_pan_group',100},{'tcp.recmode',48},{'tcp_input_group',100}}) do
                if string.match(v[1],k[1]) then 
                  orderFields[i-4].field, orderFields[i-4].index, orderFields[i-4].w = k[1], i, k[2]
                end
              end
              orderThing:addToDirtyZone()
            end
          end
        end
        
      end
      
      })   

orderFields = {}
orderFields[1] = OrderField:new({rButton=true}) 
orderFields[2] = OrderField:new({flow=orderFields[1], rButton=true})
orderFields[3] = OrderField:new({flow=orderFields[2], rButton=true})
orderFields[4] = OrderField:new({flow=orderFields[3], rButton=true})
orderFields[5] = OrderField:new({flow=orderFields[4], rButton=true})
orderFields[6] = OrderField:new({flow=orderFields[5]}) 
  
TargetButton:new({parent=tcpBox, fieldParent='tcp.io', x=4, y=6, title = 'track_io',  toolTip='Track Routing',
      states = {
      off = {{'track_io', 'Routing M'}, {'track_io_dis', 'Routing'}, {'track_io_r','Routing MR'}, {'track_io_r_dis', 'Routing R'}, 
             {'track_io_s','Routing MS'}, {'track_io_s_dis','Routing S'}, {'track_io_s_r','Routing MSR'},  
             {'track_io_s_r_dis','Routing SR'}},
      shadow = {{'track_io_ol', 'Routing M Shadow'}, {'track_io_dis_ol', 'Routing Shadow'}, {'track_io_r_ol','Routing MR Shadow'}, {'track_io_r_dis_ol', 'Routing R Shadow'}, 
             {'track_io_s_ol','Routing MS Shadow'}, {'track_io_s_dis_ol','Routing S Shadow'}, {'track_io_s_r_ol','Routing MSR Shadow'}, {'track_io_s_r_dis_ol','Routing SR Shadow'}}
      }
  })

TargetButton:new({parent=tcpBox, fieldParent='tcp.env', x=4, y=6, title = 'track_env', toolTip='Track Envelope',
      states = {
      off = {{'track_env', 'Trim'}, {'track_env_latch', 'Latch'}, {'track_env_preview', 'Preview'}, {'track_env_read', 'Read'}, {'track_env_touch', 'Touch'}, 
            {'track_env_write', 'Write'}},
      shadow = {{'track_env_ol', 'Trim Shadow'}, {'track_env_latch_ol', 'Latch Shadow'}, {'track_env_preview_ol', 'Preview Shadow'}, 
          {'track_env_read_ol', 'Read Shadow'}, {'track_env_touch_ol', 'Touch Shadow'}, {'track_env_write_ol', 'Write Shadow'}}
      }
  })  
  
TargetButton:new({parent=tcpBox, fieldParent='tcp_fx_group', x=4, y=6, title = 'track_fx_empty', toolTip='Track Effects',
      states = {
      fx = {{'track_fx_empty', 'Empty'},{'track_fx_norm', 'Normal'},{'track_fx_dis', 'Disabled'}},
      shadow = {{'track_fx_empty_ol', 'Empty Shadow'},{'track_fx_norm_ol', 'Normal Shadow'},{'track_fx_dis_ol', 'Disabled Shadow'}}
      }
  })

TargetButton:new({parent=tcpBox, fieldParent='tcp_fx_group', x=24, y=6, title = 'track_fxempty_h',  toolTip='Track Effects Bypass',
      states = {
      fx = {{'track_fxempty_h', 'Empty'},{'track_fxon_h', 'Normal'},{'track_fxoff_h', 'Disabled'}},
      shadow = {{'track_fxempty_h_ol', 'Empty Shadow'},{'track_fxon_h_ol', 'Normal Shadow'},{'track_fxoff_h_ol', 'Disabled Shadow'}}
      }
  })
  
TargetButton:new({parent=tcpBox, fieldParent='tcp.recmode', x=4, y=6, title = 'track_recmode_in',  toolTip='Track Record Mode',
      states = {
      input = {{'track_recmode_in', 'In'},{'track_recmode_out', 'Out'},{'track_recmode_off', 'Off'}},
      shadow = {{'track_recmode_in_ol', 'Input'},{'track_recmode_out_ol', 'Output'},{'track_recmode_off_ol', 'Disabled'}}
      }
  })
  
TargetButton:new({parent=tcpBox, fieldParent='tcp_input_group', x=4, y=6, title = 'track_fx_in_empty', toolTip='Track Input Effects',
      buttonStyles = {'dark_flat_icon'},
      states = {
      fx = {{'track_fx_in_empty', 'Empty'},{'track_fx_in_norm', 'Normal'}},
      shadow =  {{'track_fx_in_empty_ol', 'Empty Shadow'}}
      }
  }) 
  
tcp_recinput = TargetButton:new({parent=tcpBox, fieldParent='tcp_input_group', x=34, y=6,w=64, title = 'tcp_recinput', iType = 'bg', toolTip='Track Input Background',
      states = {
      input = {{'tcp_recinput', 'Input'}} 
      }
  })
  
tcpInputText = El:new({parent=tcp_recinput, x=0, y=0, w=40, h=20, col={0,0,0,0}, mouseOverCol={255,255,255,100}, toolTip='Track Input Brightness',
      text={str='In text', style=1, align=5, col={255,255,255}},
      onArrange = function()
        local n = getRtconfigVar('inputTextBrightness') 
        inputText.text.col = {n,n,n}
      end,
      onClick = function() 
        local val = getRtconfigVar('inputTextBrightness') or ""
        local r, v = reaper.GetUserInputs('Input Text', 1, 'Brightness (0-255)',val)
        local n = math.Clamp(tonumber(v),0,255)
        setRtconfigVar('inputTextBrightness', n)
        inputText.text.col = {n,n,n}
        inputText:addToDirtyZone()
        tcpInputText.text.col = {n,n,n}
      end
  })
  
tcpPanKnobBg = El:new({parent=tcpBox, fieldParent='tcp_pan_group', x=4, y=4, img='tcp_pan_knob_small', iType=1})

TargetButton:new({parent=tcpPanKnobBg, x=1, y=1, z=1, title = 'tcp_pan_knob_stack', iType = 'stack', iTypeStates={stack='stack',knob=1}, iFrame = 1,
      onFps = cycleBitmapStack, toolTip='Track Pan Knob',
      buttonStyles = {'trails', 'black_dot', 'green_dot', 'grey_dot', 'white_dot', 'black_line', 'green_line', 'grey_line', 'white_line',
                      'black_swipe', 'green_swipe', 'grey_swipe', 'white_swipe', 'swap_swipe',
                      'pale', 'medium', 'dark_alloy', 'grey', 'none', 'dark_field'},
      states = {
      stack = {{'tcp_pan_knob_stack', 'Pan Knob Pointer'}}, 
      knob = {{'tcp_pan_knob_small', 'Pan Knob'}}
      }
  })
  
tcpWidthKnobBg = El:new({parent=tcpBox, fieldParent='tcp_pan_group', x=28, y=4, img='tcp_width_knob_small', iType=1})

TargetButton:new({parent=tcpWidthKnobBg, x=1, y=1, z=1, title = 'tcp_wid_knob_stack', iType = 'stack', iTypeStates={stack='stack',knob=1}, iFrame = 1,
      onFps = cycleBitmapStack, toolTip='Track Width Knob', 
      buttonStyles = {'trails', 'black_dot', 'green_dot', 'grey_dot', 'white_dot', 'black_line', 'green_line', 'grey_line', 'white_line',
                      'black_swipe', 'green_swipe', 'grey_swipe', 'white_swipe', 'swap_swipe',
                      'pale', 'medium', 'dark_alloy', 'grey', 'none', 'dark_field'},
      states = {
      stack = {{'tcp_wid_knob_stack', 'Width Knob Pointer'}}, 
      knob = {{'tcp_width_knob_small', 'Width Knob'}}
      }
  }) 
  
TargetButton:new({parent=tcpBox, fieldParent='tcp_pan_group', x=54, y=6, title='tcp_panbg', iType=1, toolTip='Track Pan Left Background',
      buttonStyles = {'trans_flat','dark_flat','dark_rounded','trans_rounded','icon_field'},
      states = {
      bg = {{'tcp_panbg', 'Pan Background'}}
      }
  })
  
TargetButton:new({parent=tcpBox, fieldParent='tcp_pan_group', x=58, y=1, title = 'tcp_panthumb', iType='hThumb', toolTip='Track Pan Left Fader', 
      buttonStyles = {'soft', 'dark', 'trans_flat', 'dark_flat', 'alloy', 'dark_alloy'},
      states = {tcp = {{'tcp_panthumb', 'Pan Fader'}} }
  })  
  
TargetButton:new({parent=tcpBox, fieldParent='tcp_pan_group', x=54, y=16, title='tcp_widthbg', iType=1, toolTip='Track Pan Right Background', 
      buttonStyles = {'trans_flat','dark_flat','dark_rounded','trans_rounded','icon_field'},
      states = {
      bg = {{'tcp_widthbg', 'Width Background'}}
      }
  })
  
TargetButton:new({parent=tcpBox, fieldParent='tcp_pan_group', x=80, y=11, title = 'tcp_widththumb', iType='hThumb', toolTip='Track Pan Right Fader',
      buttonStyles = {'soft', 'dark', 'trans_flat', 'dark_flat', 'alloy', 'dark_alloy'},
      states = {tcp = {{'tcp_widththumb', 'Width Fader'}} }
  })  
 
  
---- Global Box ----  

globalBox = El:new({parent=thinBox, flow=tcpBox, x=10, y=10, w=124, h=70, col={60,60,60}})

TargetButton:new({parent=globalBox, x=10, y=10, iType='themeFile', 
      buttonStyles = {'dark', 'def6', 'def5', 'cream', 'Classic'},
      styleProxyCols = {
                        {{51,51,51}, {72,72,72}, {45,79,71}, {106,106,106}},
                        {{51,51,51}, {129,137,137}, {19,189,153}, {69,69,69}},
                        {{51,51,51}, {156,164,164}, {117,214,145}, {190,192,192}},
                        {{217,217,204}, {171,162,143}, {102,102,77}, {255,255,255}},
                        {{240,240,240}, {210,205,210}, {118,59,142}, {223,114,26}}
                        },
      states = {
      off = {{'Theme File', 'Base .ReaperTheme file (code colors and font assignments)'}}
      }
  })

  
  
  
---- Transport Box ----  

transportBox = El:new({parent=thinBox, flow=globalBox, x=10, y=20, w=230, h=70, col={51,51,51}, interactive=false})

TargetButton:new({parent=transportBox, x=10, y=10, title = 'transport_home', toolTip='Home', 
      states = {
      off = {{'transport_home', 'Home'}, {'transport_previous','Previous'}}
      }
  })
  
TargetButton:new({parent=transportBox, x=39, y=10, title = 'transport_end', toolTip='End',
      states = {
      off = {{'transport_end', 'End'}, {'transport_next','Next'}}
      }
  })
  
TargetButton:new({parent=transportBox, x=66, y=7, title = 'transport_record', toolTip='Record',
      states = {
      off = {{'transport_record', 'Record'}, {'transport_record_item','Record Item'}, {'transport_record_loop','Record Loop'}},
      on = {{'transport_record_on', 'Record On'}, {'transport_record_item_on','Record Item On'}, {'transport_record_loop_on','Record Loop On'}}
      }
  })
  
TargetButton:new({parent=transportBox, x=100, y=7, title = 'transport_play', toolTip='Play',
      states = {
      off = {{'transport_play', 'Play'}, {'transport_play_sync','Play Sync'}},
      on = {{'transport_play_on', 'Play On'}, {'transport_play_sync_on','Play Sync On'}}
      }
  })
  
TargetButton:new({parent=transportBox, x=133, y=10, title = 'transport_repeat_off', toolTip='Repeat',
      states = {off = {{'transport_repeat_off', 'Repeat'}}, on = {{'transport_repeat_on', 'Repeat On'}} }
  })
  
TargetButton:new({parent=transportBox, x=160, y=10, title = 'transport_stop', toolTip='Stop',
      states = {off = {{'transport_stop', 'Stop'}} }
  })
  
TargetButton:new({parent=transportBox, x=189, y=10, title = 'transport_pause', toolTip='Pause',
      states = {off = {{'transport_pause', 'Pause'}}, on = {{'transport_pause_on', 'Pause On'}} }
  }) 
  
transportText = El:new({parent=transportBox, x=10, y=46, w=210, h=16, col={0,0,0,0}, mouseOverCol={255,255,255,100}, 
      text={str='Transport Text', style=1, align=5, col={255,255,255}}, toolTip='Text Elements Brightness',
      onArrange = function()
        local n = getRtconfigVar('transportTextbrightness') 
        transportText.text.col = {n,n,n}
      end,
      onClick = function() 
        local val = getRtconfigVar('transportTextbrightness') or ""
        local r, v = reaper.GetUserInputs('Transport Text', 1, 'Brightness (0-255)',val)
        local n = math.Clamp(tonumber(v),0,255)
        setRtconfigVar('transportTextbrightness', n)
        transportText.text.col = {n,n,n}
      end
  })  
  
  
  
---- MCP Box ----  
  
mcpBox = El:new({parent=thinBox, flow=transportBox, x=10, y=10, w=310, h=70, col={50,50,80}, interactive=false})  

TargetButton:new({parent=mcpBox, x=10, y=10, z=1, w=12, h=50, buttonH=200, title = 'meter_strip_v', iType = 'meterV', noIScales = true, onFps = fakeMeterVals,
      toolTip='Vertical Meters',
      buttonStyles = {'v6', 'NoArm', 'gradient', 'green_to_red', 'g2r-gradient', 'discharge', 'discharge+', 'grey', '0-6-12', '0-6-18', '0-12-18', '0-12-24'},
      states = {
      meter_v = {{'meter_strip_v', 'Vertical Meter'}}
      }
  })
  
TargetButton:new({parent=mcpBox, x=30, y=10, buttonH=70, title = 'mcp_volthumb', iType='vThumb',  toolTip='Volume Fader',
      buttonStyles = {'alloy', 'soft', 'soft_dark', 'dark', 'dark_&_green', 'grey', 'Imperial', 'Imperial_Dark', 'sand', 'graphite', 'paper', 'poly'},
      states = {mcp = {{'mcp_volthumb', 'Mixer Fader'}}, tcp = {{'tcp_volthumb', 'Track Fader'}} }
  })  
  
mcp_recinput = TargetButton:new({parent=mcpBox, x=66, y=10, w=74, title = 'mcp_recinput', iType = 'bg',  toolTip='Mixer Input Background',
      states = {
      input = {{'mcp_recinput', 'Mixer Input'}} 
      }
  })
  
inputText = El:new({parent=mcp_recinput, x=0, y=0, w=60, h=16, col={0,0,0,0}, mouseOverCol={255,255,255,100}, 
      text={str='Input text', style=1, align=5, col={255,255,255}}, toolTip='Mixer Input Brightness',
      onArrange = function()
        local n = getRtconfigVar('inputTextBrightness') 
        inputText.text.col = {n,n,n}
      end,
      onClick = function() 
        local val = getRtconfigVar('inputTextBrightness') or "" 
        local r, v = reaper.GetUserInputs('Input Text', 1, 'Brightness (0-255)',val)
        local n = math.Clamp(tonumber(v),0,255)
        setRtconfigVar('inputTextBrightness', n)
        inputText.text.col = {n,n,n}
        tcpInputText.text.col = {n,n,n}
        tcpInputText:addToDirtyZone()
      end
  })
  
TargetButton:new({parent=mcp_recinput, x=0, y=10, title = 'mcp_fx_in_empty_ol', toolTip='Mixer Input Effects',
      states = {
      fx = {{'mcp_fx_in_empty_ol', 'Empty'},{'mcp_fx_in_norm_ol', 'Normal'}}
      }
  })
  
TargetButton:new({parent=mcpBox, x=66, y=44, title = 'mcp_recmode_in',  toolTip='Mixer Record Mode',
      states = {
      input = {{'mcp_recmode_in', 'In'},{'mcp_recmode_out', 'Out'},{'mcp_recmode_off', 'Off'}},
      shadow = {{'mcp_recmode_in_ol', 'Borked'},{'mcp_recmode_out_ol', 'Borked'},{'mcp_recmode_off_ol', 'Bastard'}}
      }
  }) 

mcpRecarmBg = El:new({parent=mcpBox, x=110, y=44, img='mcp_recarm_off_ol', iType=3})  
  
TargetButton:new({parent=mcpRecarmBg, x=7, y=0, title = 'mcp_recarm_off', toolTip='Mixer Record Arm', 
      buttonStyles = {'dark_shadow', 'dark', 'light_shadow', 'light', 'none_shadow', 'none'},
      states = {
      off = {{'mcp_recarm_off', 'Mixer Record Arm'}, {'mcp_recarm_auto','Mixer Automatic Arm'}},
      on = {{'mcp_recarm_on','Mixer Record Arm On'}, {'mcp_recarm_auto_on','Mixer Automatic Arm On'}, {'mcp_recarm_norec', 'Mixer Record Disabled'}, {'mcp_recarm_auto_norec','Mixer Automatic Disabled'}},
      }
  }) 
  
mcpPanBg = TargetButton:new({parent=mcpBox, x=154, y=10, title='mcp_panbg', iType=1, toolTip='Mixer Pan Left Background', 
      buttonStyles = {'trans_flat','dark_flat','dark_rounded','trans_rounded','icon_field'},
      states = {
      bg = {{'mcp_panbg', 'Mixer Pan Background'}}
      }
  })
  
TargetButton:new({parent=mcpPanBg, x=6, y=-5, title = 'mcp_panthumb', iType='hThumb', toolTip='Mixer Pan Left Fader', 
      buttonStyles = {'soft', 'dark', 'trans_flat', 'dark_flat', 'alloy', 'dark_alloy'},
      states = {mcp = {{'mcp_panthumb', 'Pan Fader'}} }
  })  
  
TargetButton:new({parent=mcpPanBg, x=0, y=10, title='mcp_widthbg', iType=1, toolTip='Mixer Pan Right Background', 
      buttonStyles = {'trans_flat','dark_flat','dark_rounded','trans_rounded','icon_field'},
      states = {
      bg = {{'mcp_widthbg', 'Mixer Width Background'}}
      }
  })
  
TargetButton:new({parent=mcpPanBg, x=50, y=5, title = 'mcp_widththumb', iType='hThumb', toolTip='Mixer Pan Right Fader',
      buttonStyles = {'soft', 'dark', 'trans_flat', 'dark_flat', 'alloy', 'dark_alloy'},
      states = {mcp = {{'mcp_widththumb', 'Width Fader'}} }
  })  

 
mcpPanKnobBg = El:new({parent=mcpBox, x=162, y=40, img='mcp_pan_knob_small', iType=1})

TargetButton:new({parent=mcpPanKnobBg, x=1, y=1, z=1, title = 'mcp_pan_knob_stack', iType = 'stack', iTypeStates={stack='stack',knob=1}, iFrame = 1,
      onFps = cycleBitmapStack, toolTip='Mixer Pan Knob', 
      buttonStyles = {'trails', 'black_dot', 'green_dot', 'grey_dot', 'white_dot', 'black_line', 'green_line', 'grey_line', 'white_line',
                      'black_swipe', 'green_swipe', 'grey_swipe', 'white_swipe', 'swap_swipe', 'debug35', 'debug201',
                      'pale', 'medium', 'dark_alloy', 'grey', 'none', 'dark_field'},
      states = {
      stack = {{'mcp_pan_knob_stack', 'Mixer Pan Knob Pointer'}}, 
      knob = {{'mcp_pan_knob_small', 'Mixer Pan Knob'}}
      }
  })
  
mcpWidthKnobBg = El:new({parent=mcpBox, x=188, y=40, img='mcp_width_knob_small', iType=1})

TargetButton:new({parent=mcpWidthKnobBg, x=1, y=1, z=1, title = 'mcp_wid_knob_stack', iType = 'stack', iTypeStates={stack='stack',knob=1}, iFrame = 1,
      onFps = cycleBitmapStack, toolTip='Mixer Width Knob', 
      buttonStyles = {'trails', 'black_dot', 'green_dot', 'grey_dot', 'white_dot', 'black_line', 'green_line', 'grey_line', 'white_line',
                      'black_swipe', 'green_swipe', 'grey_swipe', 'white_swipe', 'swap_swipe',
                      'pale', 'medium', 'dark_alloy', 'grey', 'none', 'dark_field'},
      states = {
      stack = {{'mcp_wid_knob_stack', 'Mixer Width Knob Pointer'}}, 
      knob = {{'mcp_width_knob_small', 'Mixer Width Knob'}}
      }
  })
  
mcpFx = TargetButton:new({parent=mcpBox, x=234, y=10, w=40, title = 'mcp_fx_empty', toolTip='Mixer Effects', 
      states = {
      fx = {{'mcp_fx_empty', 'Empty'},{'mcp_fx_norm', 'Normal'},{'mcp_fx_dis', 'Disabled'}}
      }
  })
  
TargetButton:new({parent=mcpFx, x=40, y=0, w=26, title = 'track_fxempty_v', toolTip='Mixer Effects Bypass', 
      states = {
      fx = {{'track_fxempty_v', 'Empty'},{'track_fxon_v', 'Normal'},{'track_fxoff_v', 'Disabled'}}
      }
  })
  
TargetButton:new({parent=mcpBox, x=238, y=34, title = 'mcp_io', toolTip='Mixer Routing', 
      states = {
      off = {{'mcp_io', 'Mixer Routing M'}, {'mcp_io_dis', 'Mixer Routing'}, {'mcp_io_r','Mixer Routing MR'},  {'mcp_io_r_dis', 'Mixer Routing R'}, 
             {'mcp_io_s','Mixer Routing MS'}, {'mcp_io_s_dis','Mixer Routing S'}, {'mcp_io_s_r','Mixer Routing MSR'}, 
             {'mcp_io_s_r_dis','Mixer Routing SR'}}
      }
  })  
  
TargetButton:new({parent=mcpBox, x=272, y=34, title = 'mcp_env', toolTip='Mixer Envelope', 
      states = {
      off = {{'mcp_env', 'Mixer Trim'}, {'mcp_env_latch', 'Mixer Latch'}, {'mcp_env_preview', 'Mixer Preview'}, {'mcp_env_read', 'Mixer Read'}, {'mcp_env_touch', 'Mixer Touch'}, {'mcp_env_write', 'Mixer Write'}},
      }
  })      

  --------- RUNLOOP ----------
 
fps = 24 -- hohoho
lastchgidx = 0
mouseXold = 0
mouseYold = 0
mouseWheelAccum = 0
trackCountOld = 0
dirtyZones ={}
bufIdx = {}
themeCheck()
gfxWold, gfxHold = gfx.w, gfx.h
bufferPinkValues ={}


function runloop()
  c=gfx.getchar()
  themeCheck()
 
  -- mouse stuff
  local isCap = (gfx.mouse_cap&1)
  
  if gfx.mouse_x ~= mouseXold or gfx.mouse_y ~= mouseYold or (firstClick ~= nil and last_click_time ~= nil and last_click_time+.25 < nowTime) then
    firstClick = nil
  end
  
  if gfx.mouse_x ~= mouseXold or gfx.mouse_y ~= mouseYold or isCap ~= mouseCapOld or gfx.mouse_wheel ~= 0 then
  
    local wheel_amt = 0
    if gfx.mouse_wheel ~= 0 then
      mouseWheelAccum = mouseWheelAccum + gfx.mouse_wheel
      gfx.mouse_wheel = 0
      wheel_amt = math.floor(mouseWheelAccum / 120 + 0.5)
      if wheel_amt ~= 0 then mouseWheelAccum = 0 end
    end
    
    local hit = nil
    
    for b in ipairs(els) do -- iterate blocks
      for z = #els[b],1,-1 do -- iterate z backwards
        if els[b][z] ~= nil then
          for j,k in pairs(els[b][z]) do
            
            local x, y, w, h = k.drawX or k.x or 0, k.drawY or k.y or 0, k.drawW or k.w or 0, k.drawH or k.h or 0
            if k.hitBox then x, y, w, h = x + k.hitBox[1], y + k.hitBox[2], k.hitBox[3], k.hitBox[4] end
            if k.interactive ~= false and gfx.mouse_x > x and gfx.mouse_x < x+w and gfx.mouse_y > y and gfx.mouse_y < y+h ~= false then
              hit = k
            end
  
          end
        end
      
      end
    end
    
    if isCap == 0 or mouseCapOld == 0 then
      if activeMouseElement ~= nil and activeMouseElement ~= hit then
        activeMouseElement:mouseAway()
        singleClick = nil
        toolTipTimer = nil
      end
      activeMouseElement = hit
    end
    
    if isCap == 0 and mouseCapOld == 1 then -- mouse-up, reset stuff
      dragStart, singleClick = nil, nil
    end
    
    if activeMouseElement ~= nil then
      if isCap == 0 or mouseCapOld == 0 then
        activeMouseElement:mouseOver()
        activeMouseElement:showTooltip()
      end
      if wheel_amt ~= 0 then       
        activeMouseElement:mouseWheel(wheel_amt)
      end
       
      if isCap == 1 then -- mouse down
        activeMouseElement:mouseDown()
         
         local x,y = gfx.mouse_x,gfx.mouse_y
         if firstClick == nil or last_click_time == nil then 
           firstClick = {gfx.mouse_x,gfx.mouse_y}
           last_click_time = nowTime
         else if nowTime < last_click_time+.25 and math.abs((x-firstClick[1])*(x-firstClick[1]) + (y- firstClick[2])*(y- firstClick[2])) < 4 then 
           activeMouseElement:doubleClick() 
           firstClick = nil
           else
             firstClick = nil
           end 
         end
         
      end
    end
    
    mouseXold, mouseYold, mouseCapOld = gfx.mouse_x, gfx.mouse_y, isCap
  end
  
 
  -- changes every FPS
  nowTime = reaper.time_precise()
  if (nextTime == nil or nowTime > nextTime) then -- do onFrame updates
  
    for b in ipairs(els) do -- iterate blocks
      for z in ipairs(els[b]) do -- iterate z
        if els[b][z] ~= nil then
          
          for j,k in pairs(els[b][z]) do
            if k.onFps and k.w ~= 0 then
              k.onFps(k)
            end
          end
          
        end
      end
    end

    nextTime = nowTime + (1/fps)
    lastTime = nowTime
  end
  
  
  -- changes because a Timer is running
  if Timers then
    for j,k in pairs(Timers) do --iterate Timers
      if nowTime > k.Timers[j] then -- Timer has expired
        k.onTimerComplete[j]()
        removeTimer(k,j)
      end
    end
  end
  
  
  -- changes from Reaper
  chgidx = reaper.GetProjectStateChangeCount(0)
  if chgidx ~= lastchgidx or doReaperGet == true then
    --reaper.ShowConsoleMsg('responding to changes from Reaper\n')
    for b in ipairs(els) do -- iterate blocks
      for z in ipairs(els[b]) do -- iterate z
        if els[z] ~= nil then
          for j,k in pairs(els[b][z]) do

            if k.onReaperChange then k.onReaperChange(k,'get') end
          end
        end
      end
    end
    
    lastchgidx = chgidx
    doReaperGet = false
    doArrange = true 
  end
 
  if gfxWold ~= gfx.w or gfxHold ~= gfx.h then
    doOnGfxResize()
    gfxWold, gfxHold = gfx.w, gfx.h
  end
  
  
  -- change in screen DPI
  if gfx.ext_retina ~= ext_retinaOld or ext_retinaOld == nil then
    --reaper.ShowConsoleMsg('DPI changed or first time\n')
    
    for b in ipairs(els) do -- iterate blocks
      for z in ipairs(els[b]) do -- iterate z
        if els[b][z] ~= nil then
          for j,k in pairs(els[b][z]) do -- iterate elements
            if k.onDpiChange and k.w ~= 0 then
              k.onDpiChange(k)
              doArrange = true
            end
          end
        end
      end
    end
    
    local nScale = 1
    if gfx.ext_retina > 1.33 then nScale = 1.5 end
    if gfx.ext_retina > 1.66 then nScale = 2 end
    setScale(nScale)
    ext_retinaOld = gfx.ext_retina
  end
  
  
 
  -- ARRANGE --
  
  if doArrange == true then -- do Arrange
    --reaper.ShowConsoleMsg('do Arrange\n')
    for b in ipairs(els) do -- iterate blocks 
      for z in ipairs(els[b]) do
        if els[b][z] ~= nil then
          for j,k in pairs(els[b][z]) do 
            k:dirtyXywhCheck(b,z) -- dirtyXywhCheck stores the old xywh, arranges the element, then adds to dirtyZone if it is dirty
          end
        end
      end
    end
    
    doArrange = false
  end




  -- DRAW --  
  
  if doDraw == true then
    --reaper.ShowConsoleMsg('do Draw\n')
    for b in ipairs(els) do -- iterate blocks
      if bufIdx[b] == nil then bufIdx[b] = {} end
      local thisBx, thisBy = els[b][1][1].drawX or 0, els[b][1][1].drawY or 0 
      local prevZDirtyZone = {} -- used to copy dZ from a Z to the next Z, reseting for each block
      
      for z in ipairs(els[b]) do -- iterate z
        
        if prevZDirtyZone.x or (dirtyZones[b][z] ~= nil and dirtyZones[b][z].x2 ~= nil) then -- there is a dirtyZone
          
          if prevZDirtyZone.x then -- prevZDirtyZone is not empty
            if dirtyZones[b] == nil then dirtyZones[b] = {} end                  --this is a lot like the addToDirtyZone function, maybe that could do this
            if dirtyZones[b][z] == nil then dirtyZones[b][z] = {x1={},y1={},x2={},y2={}} end
            dirtyZones[b][z].x1[#dirtyZones[b][z].x1+1] = prevZDirtyZone.x
            dirtyZones[b][z].y1[#dirtyZones[b][z].y1+1] = prevZDirtyZone.y
            dirtyZones[b][z].x2[#dirtyZones[b][z].x2+1] = prevZDirtyZone.x + prevZDirtyZone.w
            dirtyZones[b][z].y2[#dirtyZones[b][z].y2+1] = prevZDirtyZone.y + prevZDirtyZone.h
            prevZDirtyZone = {}
          end
        
          -- FIND THE EXTENTS OF THE DIRTYZONE OF THIS Z --
          local dx1, dy1, dx2, dy2 = nil, nil, nil, nil
          for i=1, #dirtyZones[b][z].x1 do
            if dx1 == nil then dx1 = dirtyZones[b][z].x1[1] end
            if dirtyZones[b][z].x1[i] < dx1 then dx1 = dirtyZones[b][z].x1[i] end
          end
          for i=1, #dirtyZones[b][z].y1 do
            if dy1 == nil then dy1 = dirtyZones[b][z].y1[1] end
            if dirtyZones[b][z].y1[i] < dy1 then dy1 = dirtyZones[b][z].y1[i] end
          end
          for i=1, #dirtyZones[b][z].x2 do
            if dx2 == nil then dx2 = dirtyZones[b][z].x2[1] end
            if dirtyZones[b][z].x2[i] > dx2 then dx2 = dirtyZones[b][z].x2[i] end
          end
          for i=1, #dirtyZones[b][z].x2 do
            if dy2 == nil then dy2 = dirtyZones[b][z].y2[1] end
            if dirtyZones[b][z].y2[i] > dy2 then dy2 = dirtyZones[b][z].y2[i] end
          end
          local dx, dy, dw, dh = dx1, dy1, dx2 - dx1, dy2 - dy1 --dx dy dw dh are the coordinates of the dirtyZone, in screen coordinates
          prevZDirtyZone = {x=dx, y=dy, w=dw, h=dh}
          
          if bufIdx[b][z] == nil then -- this buffer doesn't exist
            if nextBufIdx == nil then nextBufIdx = 1 end
            bufIdx[b][z] = nextBufIdx
            gfx.setimgdim(nextBufIdx, dx-thisBx+dw, dy-thisBy+dh)
            nextBufIdx = nextBufIdx + 1
          else
            local iw, ih = gfx.getimgdim(bufIdx[b][z])
            if iw>0 and ((iw < dx-thisBx+dw) or (ih < dy-thisBy+dh)) then -- check whether this z buffer exists but is too small
              gfx.setimgdim(bufIdx[b][z], dx-thisBx+dw, dy-thisBy+dh) -- fix the buffer size
            end
          end
          
          gfx.dest = 9                                  -- the temp buffer.
          gfx.mode = 2
          gfx.setimgdim(9,dw,dh)                       -- prepare the new temp buffer 
          gfx.set(0)
          gfx.rect(0,0,dw,dh)                          -- erase it
        
          if bufIdx[b][z-1] then -- there is a buffer for the previous z
            gfx.blit(bufIdx[b][z-1],1,0,dx-thisBx,dy-thisBy,dw,dh,0,0,dw,dh) -- blit dZ from clean buffer of previous z BOTH IN BUFFER COORDS NOT SCREEN COORDS!!
          end
          
          for j,k in pairs(els[b][z]) do               -- iterate Els to draw to the buffer
            gfx.mode = 0
            k:drawToBuffer(9,dx,dy,dw,dh)     -- drawToBuffer will decide whether it needs drawing, and if so then self:draw to the temp buffer
          end
           
          -- VISIBLE BUFFERS --
          if debugBuffers == true then
            local border = 0
            --gfx.muladdrect(dx-thisBx+border,dy-thisBy+border,dw-border-border,dh-border-border,1,1,1,1,math.random()/3,math.random()/3,math.random()/3,0)
            gfx.muladdrect(dx,dy,dw,dh,1,1,1,1,math.random()/3,math.random()/3,math.random()/3,0)
          end
          
          --draw the temp buffer to the clean buffer
          gfx.mode = 2
          gfx.dest = bufIdx[b][z]
          gfx.blit(9,1,0, 0, 0, gfx.w, gfx.h, dx-thisBx, dy-thisBy, gfx.w, gfx.h)
          
        else --reaper.ShowConsoleMsg('block'..b..' layer'..z..' was CLEAN\n') 
        end -- end of this dirty z

        dirtyZones[b][z] = nil
      
      end -- end iterating z
    end -- end iterating blocks
    doDraw = false 

  end
  
  --COMP--
  for b in ipairs(els) do -- iterate blocks
    gfx.dest = -1 
    local blockW, blockH = els[b][1][1].drawW,els[b][1][1].drawH -- read draw sizes from the first el
    gfx.blit(bufIdx[b][#bufIdx[b]],1,0, 0, 0, blockW, blockH, els[b][1][1].drawX, els[b][1][1].drawY, blockW, blockH) 
  end
  
  if c>48 and c<59 then
    debugDrawZ = math.floor(c - 48)
  end
  
  if debugDrawZ ~= nil then 
    gfx.a, gfx.dest = 1, -1
    gfx.muladdrect(0,0,gfx.w, gfx.h,0,0,0,0) 
    local iw, ih = gfx.getimgdim(debugDrawZ)
    gfx.blit(debugDrawZ,1,0, 0, 0, gfx.w, gfx.h, 0, 0, gfx.w, gfx.h) 
    text('BUFFER '..debugDrawZ..' w:'..iw..' h:'..ih,0,0,200,20,0,{255,255,255},3)
  end
  
  if c >= 0 then reaper.runloop(runloop) end
  
end


activeMouseElement = nil
gfxWold, gfxHold = 0, 0
doArrange = true
runloop()


function Quit()
  d,x,y,w,h=gfx.dock(-1,0,0,0,0)
  reaper.SetExtState(sTitle,"wndw",w,true)
  reaper.SetExtState(sTitle,"wndh",h,true)
  reaper.SetExtState(sTitle,"dock",d,true)
  reaper.SetExtState(sTitle,"wndx",x,true)
  reaper.SetExtState(sTitle,"wndy",y,true)
  gfx.quit()
end
reaper.atexit(Quit)

end
