program Task;
var  N, s1, s2, i, X, bigX: integer;
begin
  read(N);
  X := 0;
  s2 := 0;
  
  for i := 0 to N-1 do
  begin
    read(s1);
    if s1 >= s2 then
    begin
      X := X + 1;
      if bigX <= X then 
        bigX := X;
    end
    else
      X := 1;
    s2 := s1;
  end;
  
  write(bigX);
end.