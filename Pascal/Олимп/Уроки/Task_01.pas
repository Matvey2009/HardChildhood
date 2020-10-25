Program Task1;
var x, y:integer;
begin
  read(x);
  writeln(x div 100);
  writeln((x mod 100) div 10);
  writeln(x mod 10);
  if (x < 100) or (x > 999)
  then writeln('FALSE')
  else
    if (x div 100) + ((x mod 100) div 10) + (x mod 10) = 13 then writeln('ENTER')
    else writeln('LOCK');
end.