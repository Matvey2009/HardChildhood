Program P;
var a, b, i: byte;
    run:word;
Begin
//read
randomize;
run := random(0, 100);
writeln(run);

case run of
1: write ('это один');
2..50: write ('много');
51..100: write ('слишком много');
else write ('0');
end;

a := 10;
b := 5;
i := 0;

for var j := 0 to 24  do
write ('      ');

if a > b then
  Begin
    while i < 8 do
    begin
      writeln (a + b);
      i := i+1;
    end
  end
else
  repeat
    write (a * b);
  until i < 4;
end.