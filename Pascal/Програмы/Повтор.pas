Program repeatt;

var x:integer;
Dinarr : array of integer;
StatArr : array[0..5] of integer;

Begin
  //write('Ведите число');
  //read(x);
  //if (x < 100) and (x > 0)
  //then writeln('> 100')
  //else writeln('< 100'); 
  //writeln(10 div 3);
  //writeln(10 mod 3);
  //while x > 0 do 
  begin
    x := x-1;
    writeln(x);
  end;
  
  StatArr[1] := 111;
  writeln(StatArr[0]);
  writeln(StatArr);
  
  SetLength(Dinarr, 10);
    writeln(Dinarr);
    for var i := 0 to High(Dinarr) do
      Dinarr[i] := i * i;
    writeln(Dinarr)
End.