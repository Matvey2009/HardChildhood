using System.Drawing;

namespace Танк
{
    class Car : Unit
    {
        private Bitmap bitmap = new Bitmap(Properties.Resources.car);
        private Rectangle body = new Rectangle(new Point(0, 0), new Size(64, 64));

        //Отрисовка танка
        public void DrawCar(Graphics g, Point cursor)
        {
            target = cursor;
            Position();
            Vector();
            speed = 3                      ;

            //Машина
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -68, -70, body, GraphicsUnit.Pixel);
            g.ResetTransform();
        }
    }
}
