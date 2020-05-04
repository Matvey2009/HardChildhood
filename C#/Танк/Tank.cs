using System.Drawing;

namespace Танк
{
    class Tank : Unit, IDrawn
    {
        private static Size size = new Size (128, 128);
        private float vectorTower; //Угол повророта башня
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.Танкpng);
        private Rectangle body = new Rectangle(new Point(0, 0), size);
        private Rectangle tower = new Rectangle(new Point(128, 0), size);

        //Отрисовка танка
        public void DrawUnit(Graphics g, Point cursor)
        {
            speed = 1;
            target = cursor;
            vector = Vector(vector, speed);
            vectorTower = Vector(vectorTower, speed*2);
            Position();

            #region *** Отрисовка по частям ***
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

            DrawInfo(g);
            #endregion
        }
    }
}
