program p;
var n:integer;
begin
  read(n);
  if n mod 4 = 0 then write(-n)
  else if (n + 1) mod 4 = 0 then write(0)
  else if (n + 2) mod 4 = 0 then write(n+1)
  else write(1)
end.