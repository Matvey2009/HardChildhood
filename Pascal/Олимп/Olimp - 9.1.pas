program p;
var n, i, m : integer;
begin
  read(n);
  for i := 1 to trunc(sqrt(n)) do
    if n mod i = 0 then
      m := m + 1;
  write(m);
end.