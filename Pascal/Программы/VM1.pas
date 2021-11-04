program p;
var N, M:int64;
begin
  read(N);
  M := 0;
  while N > 0 do
  begin
    N := N div 2;
    M := M + 1;
  end;
  write(M);
end.