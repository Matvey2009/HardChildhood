program p;
var N, E, M, D:int64;
begin
  read(N);
  M := 0;
  E := 1;
  
  while N > 0 do
  begin
    E := E + E;
    D := E * 4 div 100;
    E := E - D - E * 24 div 100;
    N := N - D;
    M := M + 1;
    write(D, ' ');
  end;
  writeln();
  write(M);
end.