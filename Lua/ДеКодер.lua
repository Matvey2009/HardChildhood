--05.02.2022--

os.setlocale('rus_rus.1251')
lib = require("lib")

text = [[
yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8?@yoy0?vyoy0v`ivo"N|ewy|8vNevN¦eyGv¦e`ewy|eG?@yoy0?vyoy0vNvki2iPiv8k`i¦v6i6"`8v6e2yo8?@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8¦@@¦yN`i?v¦yN`i?v`iv8#"Syve69w!v¦yN`i?@iv6iSi`i0vNeNyoN|"0?v|i|v"v0`y?v`yvoevN`i?@|ew>?v|ew>ve2i#"v¶ive|`e0vN|ew>?@2¦i#"v`iv|8N|"v0`yvo8M8?vkoyvPyvw>?vkoyvPyvw>¦¦¦@e`i?ve`i?ve`iv0y`9vNv80ivN¦y#i?@e`i?ve`iv6e|eGv"v¦e##v¶i22i#i?@"v6efy08vwi|vN#ioeNw`evewv2e#"?@6e¶i2>#v9v¦Nyv68w"?v6ewy29#v6i2e#"+@@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8?@yoy0?vyoy0v`ivo"N|ewy|8vNevN¦eyGv¦e`ewy|eG?@yoy0?vyoy0vNvki2iPiv8k`i¦v6i6"`8v6e2yo8?@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8¦@@`8vfweveNe2y``ekev¦vXweGv`yv6eG08veNe2yK@9v`"fykevNvNe2eGv6eoy#iw!?v`yvN6eNe2y`?@`yv¶`i#v9?vfwev|v2yoyvwi|eGv`yv62"N6eNe2#y`?@oiv8P?vwi|"0v|i|v9?v`yvoi#wv62y0"#v'`e2y#!0¦@`evNi0"v`ek"?v|v`yGv0y`9vN"#|e0v¦yo8w?@`ivo"N|ewy|8?vNi0"?vNi0"v¦v6#9Nv"o8w?@0y`9ve|8wi#ev2y¶8oy2P`e0vw80i`e0?@¦ewve`iv62"M#iv##2e¦!zve|eIe|e9``i9zzz@@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8?@yoy0?vyoy0v`ivo"N|ewy|8vNevN¦eyGv¦e`ewy|eG?@yoy0?vyoy0vNvki2iPiv8k`i¦v6i6"`8v6e2yo8?@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8¦@@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8?@yoy0?vyoy0v`ivo"N|ewy|8vNevN¦eyGv¦e`ewy|eG?@yoy0?vyoy0vNvki2iPiv8k`i¦v6i6"`8v6e2yo8?@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8¦@@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8?@yoy0?vyoy0v`ivo"N|ewy|8vNevN¦eyGv¦e`ewy|eG?@yoy0?vyoy0vNvki2iPiv8k`i¦v6i6"`8v6e2yo8?@yoy0?vyoy0v¦vNeNyo`yyvNy#ev`ivo"N|ewy|8¦@@ivoevoy2y¦`"vweGvoi#y|e?@w8oivoe22iw!N9v28oywv`y#yk|e?@N`ifi#iv6y2yy4iw!v¦Nyv0eNw>?@"v|i|I`"28o!ve2ry4iw!v¦Nyv6eNw>¦@`ev9v¦yo!v¶`i#?vPoyM!v0y`9?vPoyM!vw>@68N|iGv¦N#v`ef!ve28wv¶ive|`e0v|ew>?@9v6e#y¦>yv`i2¦8vwy2yvS¦yw>?@0>vyoy0?vyoy0v¦vNeNyo`yyvNy#e¦@
]]

abc(text)

text = text:gsub('v', ' ')
text = text:gsub('@', '\n')
text = text:gsub('z', '.')
text = text:gsub('?', ',')
text = text:gsub('y', 'å')
text = text:gsub('o', 'ä')
text = text:gsub('0', 'ì')
text = text:gsub('¦', 'â')
text = text:gsub('N', 'c')
text = text:gsub('e', 'î')
text = text:gsub('`', 'í')
text = text:gsub('#', 'ë')
text = text:gsub('i', 'à')
text = text:gsub('"', 'è')
text = text:gsub('|', 'ê')
text = text:gsub('w', 'ò')
text = text:gsub('8', 'ó')
text = text:gsub('G', 'é')
text = text:gsub('k', 'ã')
text = text:gsub('2', 'ð')
text = text:gsub('P', 'æ')
text = text:gsub('6', 'ï')
text = text:gsub('ð', 'á')
text = text:gsub('S', 'ö')
text = text:gsub('9', 'ÿ')
text = text:gsub('!', 'ü')
text = text:gsub('>', 'û')
text = text:gsub('á', 'ð')
text = text:gsub('¶', 'ç')
text = text:gsub('M', 'ø')
text = text:gsub('f', '÷')
text = text:gsub('4', 'õ')
text = text:gsub('I', '-')
text = text:gsub('ð', 'á')
text = text:gsub('r', 'ú')
text = text:gsub('ë', 'þ')



print(text)

io.read()