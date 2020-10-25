program p;

var
  i, R, X, L, Temp: integer;
  arr: array of integer;

begin
  read(R);
  L := 0;
  Temp := R;
  while Temp > 0 do
  begin
    L := L + 1;
    Temp := Temp div 10;
  end;
  setLength(arr, L);
  
  for i := 0 to L-1 do
  begin
    arr[i] := R mod 10;
    R := R 
    div 10;
  end;
  
  write(arr);
end.