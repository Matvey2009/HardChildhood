Program Paradox;
var pris, variant, variant2, void, game, win :integer;
 label m;
begin
while game <= 99 do
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
  if (void = pris) or (void = variant) then goto m
  else
  begin
    writeln ('ПОДСКАЗКА! В коробке ', void, ' - пусто. Выберите снова');
    variant2 := variant;
    while (variant2 = variant) or (variant2 = void) do variant2 := random (3)+1;
    //readln (variant);
  end;
  
  if variant2 = pris then
    begin
    writeln('Вы  Выиграли');
    win := win + 1;
    end
  else writeln ('Вы Проиграли');
  end;
end.