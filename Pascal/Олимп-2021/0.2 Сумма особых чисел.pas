program G;

var
  N, S, i, X: integer;

begin
  write('Введите число элемента(N): ');
  readln(N);
  
  for i := 1  to N do
  begin
    read(X);
    if X > i then
      S := S + X;
  end;

  
writeln('Ввывод особых элементов', S);
end.