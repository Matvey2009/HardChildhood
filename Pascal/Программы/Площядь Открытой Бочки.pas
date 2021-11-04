program p;
var R, H, D, S:real;
begin
  read(R, H);
  D := Pi * R * R;
  S := H * Pi * R * 2;
  writeln( 2 * (S + D));
end.