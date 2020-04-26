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
            target = cursor;
            Position();
            Vector();
            speed = 3;

            //Машина
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -36, -48, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            DrawInfo(g);
        }
    }
}
