program u;

var m, n, i, r, temp: integer;
  s: string;

begin
  read(m, n);
  temp := 0;
  
  for i := m to n do
  begin
    s := IntToStr(i * i);
    r := StrToInt(s.Substring(Length(s) - Length(IntToStr(i))));
    if i = r then
    begin
      writeln(i);
      temp := 1;
    end;
  end;
  
  if temp = 0 then
    writeln(0);
end.