program p;
var a1, b1, a2, b2, max1, max2, H:integer;
begin
read(a1, b1, a2, b2);
  if a1 > b1 then max1 := a1
  else max1 := b1;

  if a2 > b2 then max2 := a2
  else max2 := b2;

  H := max1 + max2;

  write(H);
end.