program p;
var n, i, j:integer;
begin
  read(n);
  for i := 0 to n div 2 do
  begin
    for j := 0 to n-1 do
    begin
      if (j > n div 2 - i - 1) and (j < n div 2 + i + 1) then
        write('*')
      else
        write(' ');
    end;    
    writeln();
  end;
  for i := 0 to n div 2 - 1 do
  begin
    for j := 0 to n-1 do
    begin
      if (j > i) and (j < n - i - 1) then
        write('*')
      else
        write(' ');
    end;    
    writeln();
  end;
  end.