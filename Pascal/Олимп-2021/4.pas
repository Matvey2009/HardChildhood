program h;

var N, S, K, M, ost: integer;

begin
  read(N, K, M);
  S := (N div (K + M)) * 2;
 ost := N - (S div 2 * (K + M));
 if ost > K then
   S := S + 2
 else if (ost <= K) and (ost > 0) then
   S := S + 1;
  writeln(S);
end.



