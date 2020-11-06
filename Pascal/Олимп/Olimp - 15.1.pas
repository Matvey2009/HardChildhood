program p;
var n, x, y, i:integer;
begin
  y := 0;
  readln(N);
  for i := 1 to N do
  begin
    readln(x);
    if x >0 then
      y := y + 1;
  end;
  write(y);
end.