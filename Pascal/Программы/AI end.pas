Program AI;
label m;
var a, b, x, y, i :integer;
begin
  a := 0;
  b := 1000;
  writeln('Задумайте число от 1 до 1000');
  m:
 x :=  (b - a) div 2 + a;
  writeln('Это число ', x,'? есле больше 1, если меньше то 0, а есле угадали то Любое другое');
i :=i+1;
  read (y);
  if y = 0 then
    begin
    b := x;
    goto m;
    end;
  if y = 1 then
    begin
    a := x;
    goto m;
    end
   else
writeln('угадал с попытки ', i);
end.

