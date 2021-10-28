program AB;

var X1, Y1, X2, Y2, A, B: real;

begin
  writeln('Введите 4 координаты');
  read(X1, Y1, X2, Y2);
  A := (Y1 - Y2) /( X1 - X2);
  B := Y2 - X2 * A;
  writeln('Уровнение прямой: Y = X * ', A, '+', B);
end.