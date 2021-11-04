Program Task_2;
var A, B, C:integer;
Begin
  read(A, B, C);
  if (A < B) and (A < C) then writeln(B + C);
  if (B < A) and (B < C) then writeln(A + C);
  if (C < A) and (C < B) then writeln(A + B);
end.