Program remove;

var x:integer;

Begin
  write('Ведите число');
  read(x);
  if (x < 100) and (x > 0)
  then writeln('> 100')
  else writeln('< 100'); 
  writeln(10 div 3);
  writeln(10 mod 3);
  while x > 0 do 
  begin
    x := x-1;
    writeln(x);
  end;
End.