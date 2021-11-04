Program Paradox;
var pris, variant, void, game, win :integer;
 label m;
begin
while game <= 999 do
begin
  game := game + 1;
  writeln(game);
  writeln('Всего игр ', game, '. Побед ', win, '(', win / game * 100, ')');
  pris := random(3)+1;
  writeln ('Выбери BOX 1, 2, 3');
  variant := random (3)+1;
  //readln (variant);
  writeln ('Вы выбрали ', variant);
  m:
  void := random(3)+1;
  if void = pris then goto m
  else
  begin
    writeln ('ПОДСКАЗКА! В коробке ', void, ' - пусто. Выберите снова');
    variant := random (3)+1;
    
    //readln (variant);
  end;
  
  if variant = pris then
    begin
    writeln('Вы  Выиграли');
    win := win + 1;
    end
  else writeln ('Вы Проиграли');
  end;
end.