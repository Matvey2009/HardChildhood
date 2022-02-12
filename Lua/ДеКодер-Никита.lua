--05.02.2022--

os.setlocale('rus_rus.1251')
lib = require("lib")

text = [[
O}-nbR6X|XzARJX"R>-X'AR|ARXY"-}§U'AR|ARX>7})c§X}-¶'Rn)cX7Xn-Yb)c§UzARJ)Xb-XO}-5-+§XRAX¶z-¶AQ!Xn}-Yb)+§U¶}65)Xf-}QZ->7X}6ORbQ'RX¶RJ7>-}:::UzARJ)XORnR>7}TXLIc§XblXb6Xf}-zQWL§Uf>7Y7>-}X'XO>l"7X¶nR6c§XY-}6!§UO>6}X¶7}Qb66Xn¶!'RcXJ-A->67§UJ)}X}mJRnb7'§Xf->6bQ§X">lOX7Xn>-z:::UzARJ)Xb-X'>Rn-A7X>!"R>X¶f-}U7X¶Rf6}XA7+RbQ'R§X>6}R"7zbR§U-X'RO"-XO>l¶A7qQX>6}-b+R}7zbR§URbXA6J!X}mJ7>RcXb-5)n-}:::UO}-nbR6X|XzARJX"R>-X'AR|ARXJ)}§U'ARXn">lOX"lqlXn)f}6¶b6AXb->lYl§U-X'RO"-XA)X5}-!§X¶'-Y6ATXLblXY6§Ul¶fR'Rc¶!X7Xlc>7X¶nRcXf)}:::LU'ARXf>R¶A7AXb->XA)¶!z7X75>6b§U¶'-Y6ATXLb6XnR}blc¶!§Xn¶6X>)X}m"7§Un-YbRXAR§XzARX>)X">lOX">lO-X}mJ7>§UIARXO}-nbR6§X-X5b-z7AXb6AXf>RJ}6>:::LU5-Alf!A¶!X>7}}7Rb)XY-}§U7Xlc"6AX75X¶6>"Z-Xn¶6Xf}R+R6:UO}-nbR6X|XzARJX'AR|ARXJ)}X¶XARJRm§UO}-nbR6X|XzARJX"R>-X'AR|ARXY"-}:::U
]]

abc(text)
print()
num(text)
probel(text)

print()

text = text:gsub('X', ' ')
text = text:gsub('U', '\n')
text = text:gsub(':', '.')
text = text:gsub('§', ',')
   
text = text:gsub('|', '|')
text = text:gsub('R', 'O')
text = text:gsub('}', '}')

text = text:gsub('¶', '¶')
text = text:gsub('-', '-')
text = text:gsub('7', '7')
text = text:gsub("'", "'")
text = text:gsub('î', 'î')
text = text:gsub('A', 'í')


print(text)

io.read()