program p;
var h, r :integer;
label m;
begin
m:
write('Вeдите чесло');
read(h);
r := h mod 2;
if r = 1 then writeln('нечет')
else writeln('чёт');
goto m;
end.