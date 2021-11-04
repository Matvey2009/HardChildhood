program gr;
uses graphABC;
begin
pen.color :=rgb (0, 0, 255);
line(200, 100, 150, 50); 
line(100, 100, 150, 50); 
DrawRectangle(100, 100, 200, 200);
DrawCircle (150, 150, 30);
pen.color :=rgb (255, 255, 0);
DrawCircle (500, 50, 50);
pen.color :=rgb (150, 75, 0);
line(800, 200, 0, 200); 
end.