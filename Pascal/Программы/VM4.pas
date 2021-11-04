program p;
var G, R:integer;
begin
  read(G);
  R := 0;
  while G > 0 do
  begin
    G := G div 10;
    R := R + 1;
  end;
  write(R);
end.