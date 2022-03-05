--05.02.2022--

os.setlocale('rus_rus.1251')
lib = require("lib")

text = [[
O}-nbR6X|XzARJX"R>-X'AR|ARXY"-}§U'AR|ARX>7}vc§X}-¶'RnvcX7Xn-Ybvc§UzARJvXb-XO}-5-+§XRAX¶z-¶AQ!Xn}-Ybv+§U¶}65vXf-}QZ->7X}6ORbQ'RX¶RJ7>-}:::UzARJvXORnR>7}TXLIc§XblXb6Xf}-zQWL§Uf>7Y7>-}X'XO>l"7X¶nR6c§XY-}6!§UO>6}X¶7}Qb66Xn¶!'RcXJ-A->67§UJv}X}mJRnb7'§Xf->6bQ§X">lOX7Xn>-z:::UzARJvXb-X'>Rn-A7X>!"R>X¶f-}U7X¶Rf6}XA7+RbQ'R§X>6}R"7zbR§U-X'RO"-XO>l¶A7qQX>6}-b+R}7zbR§URbXA6J!X}mJ7>RcXb-5vn-}:::UO}-nbR6X|XzARJX"R>-X'AR|ARXJv}§U'ARXn">lOX"lqlXnvf}6¶b6AXb->lYl§U-X'RO"-XAvX5}-!§X¶'-Y6ATXLblXY6§Ul¶fR'Rc¶!X7Xlc>7X¶nRcXfv}:::LU'ARXf>R¶A7AXb->XAv¶!z7X75>6b§U¶'-Y6ATXLb6XnR}blc¶!§Xn¶6X>vX}m"7§Un-YbRXAR§XzARX>vX">lOX">lO-X}mJ7>§UIARXO}-nbR6§X-X5b-z7AXb6AXf>RJ}6>:::LU5-Alf!A¶!X>7}}7RbvXY-}§U7Xlc"6AX75X¶6>"Z-Xn¶6Xf}R+R6:UO}-nbR6X|XzARJX'AR|ARXJv}X¶XARJRm§UO}-nbR6X|XzARJX"R>-X'AR|ARXY"-}:::U
]]

abc(text)
print()
num(text)
probel(text)

print()

text = text:gsub('X', ' ') -- 01 --
text = text:gsub('U', '\n')-- 02 --
text = text:gsub(':', '.') -- 03 --
text = text:gsub('§', ',') -- 04 --
text = text:gsub('L', '?') -- 05 -- 

text = text:gsub('O', 'ã') -- 06 --
text = text:gsub('}', 'ë') -- 07 --
text = text:gsub('-', 'à') -- 08 -- 
text = text:gsub('n', 'â') -- 09 --
text = text:gsub('b', 'í') -- 10 --
text = text:gsub('R', 'î') -- 11 --
text = text:gsub('6', 'å') -- 12 --
text = text:gsub('|', '-') -- 13 --
text = text:gsub('z', '÷') -- 14 --
text = text:gsub('A', 'ò') -- 37 --
text = text:gsub('J', 'á') -- 15 --
text = text:gsub('"', 'ä') -- 16 --
text = text:gsub('>', 'ð') -- 17 --
text = text:gsub("'", "ê") -- 18 --
text = text:gsub('Y', 'æ') -- 19 --
text = text:gsub('7', 'è') -- 20 --
text = text:gsub('v', 'û') -- 21 --
text = text:gsub('c', 'é') -- 22 --
text = text:gsub('¶', 'ñ') -- 23 --
text = text:gsub('5', 'ç') -- 24 -- 
text = text:gsub('+', 'õ') -- 25 --
text = text:gsub('Q', 'ü') -- 26 --
text = text:gsub('!', 'ÿ') -- 27 --
text = text:gsub('f', 'ï') -- 28 --
text = text:gsub('Z', 'ö') -- 29 --
text = text:gsub('T', ':') -- 31 --
text = text:gsub('I', 'ý') -- 32 --
text = text:gsub('l', 'å') -- 33 --
text = text:gsub('W', '!') -- 34 --
text = text:gsub('m', 'é') -- 35 --
text = text:gsub('q', 'q') -- 36 --
text = text:gsub('?', '"') -- 37 -- 
text = text:gsub('å', 'ó') -- 38 -- 

print(text)

io.read()