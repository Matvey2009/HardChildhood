Program pp; 
const M = 100;
var r:integer; arr : array [1..M] of integer;


procedure print;
begin;
for var i := 1 to M do write  (' ', arr[i]);
end;

Begin
for var i := 1 to M do arr[i] := random (0, 999);
print;
writeln;
writeln;

//Сортировка
for var i := 1 to M-1 do
  begin  
    if arr[i] > arr[i+1] then
      begin  
        r := arr[i];
        arr[i] := arr[i+1];
        arr[i+1] := arr[i];
      end;
  end;


print;
End.