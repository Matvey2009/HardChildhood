program p;
var n : integer;

begin
  read(n);
  while n > trunc(sqrt(n)) * trunc(sqrt(n)) do
    n := n + 1;
  write(n);
end.