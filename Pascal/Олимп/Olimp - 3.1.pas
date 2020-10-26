program p;
var x1, x2, x3, x4, d, t:integer;
begin
  read(d);
  x1 := (d div 1000);
  x2 := (d - x1 * 1000) div 100;
  x3 := (d - x1 * 1000 - x2 * 100) div 10;
  x4 := d mod 10;
  x1 := (x1 + 7) mod 10;
  x2 := (x2 + 7) mod 10;
  x3 := (x3 + 7) mod 10;
  x4 := (x4 + 7) mod 10;
  writeln(x3, x4, x1, x2)
end.