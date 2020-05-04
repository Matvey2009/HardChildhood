using System.Drawing;

namespace Танк
{
    class Car : Unit, IDrawn
    {
        private static Size size = new Size(64, 64);
        private Bitmap bitmap = new Bitmap(Properties.Resources.car);
        private Rectangle body = new Rectangle(new Point(0, 0), size);

        //Отрисовка танка
        public void DrawUnit (Graphics g, Point cursor)
        {
            speed = 3;
            target = cursor;
            vector = Vector(vector, speed);
            Position();

            //Машина
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -16, -32, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            DrawInfo(g);
        }
    }
}
