program pp;

uses graphABC;

const
  M = 100;

var
  r, k: integer;
  arr: array [1..M] of integer;

procedure print;
begin;
  for var i := 1 to M do write(' ', arr[i]);
end;

begin
      sleep(50);
  for var i := 1 to M do arr[i] := random(0, 999);
  
  for var i := 1 to M do
  begin
    setbrushcolor(clrandom);
    rectangle(15 + i * 6, 460, 19 + I * 6, 460 - arr[i] div 3);
    sleep(50);
    setbrushcolor(clrandom);
  end;
  
  print;
  writeln;
  writeln;
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
  end;
  print;
end.