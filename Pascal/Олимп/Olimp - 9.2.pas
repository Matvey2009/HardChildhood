program p;
var x, y, m, a, b, c:integer;
begin
  read(x, y);
      while x > 0 do
        begin
        a := x mod 10;
        x := x div 10;
        m := m*10 + a;
      end;
  x := m;
      while y > 0 do
        begin
        a := y mod 10;
        y := y div 10;
        m := m*10 + a;
      end;
  y := m;
  c := x + y;
      while c > 0 do
        begin
        a := c mod 10;
        c := c div 10;
        m := m*10 + a;
      end;
  
  write(c);
end.