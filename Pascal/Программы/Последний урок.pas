program pp;

uses graphABC;

const
  M = 100;

var
  arr: array [1..M] of integer;
  r, k: integer;

begin
  for var i := 1 to M do arr[i] := random(0, 999);

  //Сортировка 
  setbrushcolor(clrandom);
  k := M;
  for var g := 1 to M - 1 do
  begin
    k := k - 1;
    for var i := 1 to k do
    begin
      if arr[i] > arr[i + 1] then
      begin
        r := arr[i];
       arr[i] := arr[i + 1];
        arr[i + 1] := r;
      end;
     end;

  //очистка икрана
  lockDrawing;
  clearwindow;
  
  
       //Рисования графика
  for var i := 1 to M do
  begin
    setbrushcolor(clGray);
    rectangle(15 + i * 6, 460, 19 + I * 6, 460 - arr[i] div 3);
    setbrushcolor(clrandom);
  end;
   sleep(20);
   Redraw;
   end;
end.