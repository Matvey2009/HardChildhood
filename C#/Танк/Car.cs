using System.Drawing;

namespace Танк
{
    class Car : Unit, IDrawn
    {
        private static Size size = new Size(64, 64);
        private Bitmap bitmap = new Bitmap(Properties.Resources.car);
        private Rectangle body = new Rectangle(new Point(0, 0), size);
        private Pen pen;

        //Отрисовка танка
        public void DrawUnit (Graphics g, Point cursor)
        {
            speed = 2;
            target = cursor;
            vector = Vector(vector, speed);
            PositionUnit();

            //Машина
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -16, -32, body, GraphicsUnit.Pixel);
            g.ResetTransform();
            g.ResetTransform();

            pen = new Pen(color, 3);
            g.DrawEllipse(pen, position.X - 5, position.Y - 5, 8, 8);

            DrawInfo(g);
        }
    }
}
