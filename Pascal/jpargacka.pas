program Gr;
uses GraphABC;
begin
  for var x := 0 to Window.Width -1 do
  for var y := 0 to Window.Height -1 do 
SetPixel(x, y, RGB(1*x-y, x-1*y, x+y));
end.