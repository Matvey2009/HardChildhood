program p;
var V, M, G:integer;
begin
  read(V, M);
  writeln('До обмена ', V, ' ', M);
  G := V;
  V := M;
  M := G;
  writeln('После обмена ', V,' ', M);
end.