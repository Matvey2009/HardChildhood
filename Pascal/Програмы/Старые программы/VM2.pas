program p;
var N, D:int64;
begin
  read(D);
  N := 1;
  for var i := 1 to D do
    N := N * 2;
  write(N);
end.