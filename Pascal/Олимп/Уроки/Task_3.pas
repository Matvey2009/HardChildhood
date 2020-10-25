Program Task_3;
var A, B, C, D, S, M, N :integer;
Begin
  read(A, B, C, D);
  S := (A + B + C + D);
  M := (S mod 10);
  N := (S mod 100) div 10;
  if (M = 1) and (N <> 1) then writeln(S + ' птица')
  else
  if (M > 1) and (M < 5) and (N <> 1) then writeln(S + ' птицы')
  else writeln(S + ' птиц');
end.