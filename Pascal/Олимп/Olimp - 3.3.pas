program p;
var v : double;
  i, k, z : integer;
begin
  read(k);
  v := 0;
  z := 1;
  
  for i := 0 to k -1 do
    begin
    v := v + 4/(i*2+1) * z;
    z := z * -1;
    end;
  write(v:0:9);
end.