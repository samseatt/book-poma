-- Apply print-only image geometry without changing canonical or web sources.
function Image(image)
  local source = image.src
  if source:match("chapter%-arrow%.png$") then
    image.attributes.width = "0.82in"
  elseif source:match("interlude%-gear%.png$") then
    image.attributes.width = "0.86in"
  elseif source:match("separator%.png$") then
    return pandoc.RawInline("latex", "\\pomaseparator{}")
  elseif source:match("/[^/]+%-open/opening%.") then
    image.attributes.width = "1.50in"
  elseif source:match("/coda/") or source:match("/overture/") or
         source:match("/prologue/image%-01%.") or source:match("/epilogue/image%-01%.") then
    image.attributes.width = "1.00in"
  elseif source:match("/part%-opening/") then
    image.attributes.width = "4.35in"
  elseif source:match("/prologue/") or source:match("/epilogue/") then
    image.attributes.width = "2.25in"
  end
  image.attributes["fig-align"] = "center"
  return image
end

-- A Markdown thematic break (`---` on its own line) is the semantic marker
-- for a scene separator. It shares the print treatment used by legacy
-- separator.png references while manuscripts transition away from the image.
function HorizontalRule()
  return pandoc.RawBlock("latex", "\\pomaseparator{}")
end

-- STIX Two Text is the body face; important mathematical characters are
-- routed through STIX Two Math. This preserves semantics without requiring
-- the canonical Markdown to use LaTeX syntax.
local math = {
  [0x00B2] = "^{2}", [0x00B3] = "^{3}", [0x00B9] = "^{1}",
  [0x00D7] = "\\times", [0x2070] = "^{0}", [0x207B] = "^{-}",
  [0x2080] = "_{0}", [0x2082] = "_{2}", [0x2084] = "_{4}",
  [0x2093] = "_{x}", [0x2191] = "\\uparrow", [0x2192] = "\\rightarrow",
  [0x2200] = "\\forall", [0x2203] = "\\exists", [0x2205] = "\\varnothing",
  [0x221A] = "\\surd", [0x2260] = "\\neq", [0x2261] = "\\equiv",
  [0x27E9] = "\\rangle",
}

local bullet_icons = {
  [0x2705] = true, [0x274C] = true, [0x2757] = true,
  [0x1F449] = true, [0x1F4CC] = true, [0x1F538] = true,
  [0x1F539] = true, [0x26A0] = true, [0xF0B7] = true,
}

local function flush_text(result, buffer)
  if #buffer > 0 then
    table.insert(result, pandoc.Str(table.concat(buffer)))
    for i = #buffer, 1, -1 do buffer[i] = nil end
  end
end

function Str(str)
  local result, buffer, changed = {}, {}, false
  for _, codepoint in utf8.codes(str.text) do
    local replacement = math[codepoint]
    if replacement then
      flush_text(result, buffer)
      table.insert(result, pandoc.RawInline("latex", "\\ensuremath{" .. replacement .. "}"))
      changed = true
    elseif bullet_icons[codepoint] then
      flush_text(result, buffer)
      table.insert(result, pandoc.RawInline("latex", "\\textbullet{}"))
      changed = true
    elseif codepoint == 0x200D or codepoint == 0x20E3 or codepoint == 0xFE0F or
           (codepoint >= 0x1F3FB and codepoint <= 0x1F3FF) then
      changed = true
    elseif codepoint >= 0x1F000 or codepoint == 0x23F3 or codepoint == 0x2640 or
           (codepoint >= 0x2694 and codepoint <= 0x26FF) or
           (codepoint >= 0x2700 and codepoint <= 0x27BF) then
      -- Decorative Markdown-era pictographs are omitted from print.
      changed = true
    else
      table.insert(buffer, utf8.char(codepoint))
    end
  end
  flush_text(result, buffer)
  return changed and result or str
end

local function contains_persian(inline)
  local text = pandoc.utils.stringify(inline)
  for _, codepoint in utf8.codes(text) do
    if codepoint >= 0x0600 and codepoint <= 0x06FF then return true end
  end
  return false
end

function Para(para)
  local first, last
  for index, inline in ipairs(para.content) do
    if contains_persian(inline) then
      first = first or index
      last = index
    end
  end
  if first then
    -- Only the Persian run receives the Persian font and RTL direction. A
    -- translated line can share the Markdown paragraph without accidentally
    -- being typeset in a font that has no Latin glyphs.
    table.insert(
      para.content,
      first,
      pandoc.RawInline("latex", "\\makebox[\\linewidth][r]{\\begingroup\\persianfont\\textdir TRT ")
    )
    table.insert(para.content, last + 2, pandoc.RawInline("latex", "\\endgroup}"))
  end
  return para
end
