program p;
var i,  n, v:integer;
 arr: array of integer;
begin
  read(n);
  setLength(arr, n);
  
  for i := 0 to n-1 do
  begin
    read(arr[i]);
  if arr[i] = 0 then writeln(2)
  else if arr[i] = 1 then writeln(0)
  else if arr[i] = 2 then writeln(1)
  end;
end. 