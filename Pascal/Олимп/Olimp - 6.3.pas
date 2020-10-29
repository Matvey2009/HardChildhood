program p;
var i, n, x, x1, x2 ,x3:int64;
begin
  read(n);
  x1 := 1;
  x2 := 1;
  x3 := 1;
  if n < 4 then
     x := 1
  else 
  for i := 4 to n do
  begin
    x := x1 + x2 + x3;
    x1 := x2;
    x2 := x3;
    x3 := x;
  end;
  write(x);
end.