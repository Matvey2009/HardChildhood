--05.02.2022--

os.setlocale('rus_rus.1251')
lib = require("lib")

text = [[
p<:5w9n<7x]95a<wg95Ga9vaC/:a1a]5<w95-<pGyofJv<MAe/IfI<wyw5oaM95a<Gy]a9vae/IfI<ga9y-<7yJM5-<I1fJ5MAT/G<M5woa9vp6<g1xJMy<ba'9f]a595-e/G<M1aG5gf6<>xw95-<JxaMAe/'Gx7fo<w9a<]5og5<g5o5J<9a59A-/y<J9yoyJv<wyoAa<7a1MAT/>oy<g5]AT<bx1v<:51AG<wpMa59A-/1fJJapo<:1a59ya<wa7MAe/y<p<'fbAo<MG5-<g5o5J<9a59A-e/MG5y<9abaJ9Aa<7a1MAT/G<gox>ye<G5<w1fIa<'fM57a9vp/Mp9xoyJv<My65<]9y<w5y/ba'<b55aJMGfe<ba'<G]5695Ga9vpe/ba'<Joa'e<ba'<5y'9ye<ba'<onbGyT/]x>a<9fJMfo5<:15bx5]a9vaC/y<G5M<5:pMv<pGyofJv<MAe/IfI<wyw5oaM95a<Gy]a9vae/IfI<ga9y-<7yJM5-<I1fJ5MAT/y<Ja1]#a<bvaMJp<G<x:5a9vae/y<]op<9ag5<G5JI1aJoy<G95Gv/y<b55aJMG5e<y<G]5695Ga9vae/y<5y'9ve<y<Joa'Ae<y<onb5GvT/
]]

abc(text)
print()
num(text)
probel(text)

print()

text = text:gsub('<', ' ')
text = text:gsub('/', '\n')
text = text:gsub('y', 'è')
text = text:gsub('G', 'â') -- Â Ñ
text = text:gsub('p', 'ÿ') -- ß Ó Ê Â
text = text:gsub('o', 'ë')
text = text:gsub('a', 'å') 
text = text:gsub('5', 'î')
text = text:gsub('I', 'ê')
text = text:gsub('f', 'à')
text = text:gsub('>', 'ø')
text = text:gsub(':', 'ï')
text = text:gsub('w', 'ì')
text = text:gsub('9', 'í')
text = text:gsub('7', '÷')
text = text:gsub('n', 'þ')
text = text:gsub(']', 'ä')
text = text:gsub('g', 'ã')
text = text:gsub('v', 'ü')
text = text:gsub('C', ':')
text = text:gsub('/', '/')
text = text:gsub("1", "ð")
text = text:gsub('-', 'é')
text = text:gsub('î', 'î')
text = text:gsub('J', 'ñ')
text = text:gsub('M', 'ò')
text = text:gsub('A', 'û')
text = text:gsub('e', ',')
text = text:gsub('T', '.')
text = text:gsub('6', 'õ')
text = text:gsub('b', 'á')
text = text:gsub("'", "ç")
text = text:gsub('>', '>')
text = text:gsub('#', 'ö')
text = text:gsub('x', 'ó')


print(text)

io.read()