using System.Drawing;

namespace Танк
{
    class Tank : Unit
    {
        private float vectorTower; //Угол повророта башня
        private Bitmap bitmap = new Bitmap(Properties.Resources.Танкpng);
        private Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        private Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

        //Отрисовка танка
        public void DrawTank(Graphics g, Point cursor)
        {
            target = cursor;
            Position();
            Vector();
            vectorTower = vector;
            speed = 1;

            //Корпус
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -68, -70, body, GraphicsUnit.Pixel);
            g.ResetTransform();
            //Башня
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vectorTower);
            g.DrawImage(bitmap, -48, -87, tower, GraphicsUnit.Pixel);
            g.ResetTransform();
        }
    }
}
