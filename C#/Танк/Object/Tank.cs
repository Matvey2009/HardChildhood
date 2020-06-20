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
        private Pen pen;

        /// <summary>
        /// Конструкор танка
        /// </summary>
        public Tank(Color color)
        {
            this.color = color;
            speed = 1;
            live = 50;
            act = Act.WAIT;
        }

        //Отрисовка танка
        public void DrawUnit(Graphics g, Point cursor)
        {
            //target = cursor;
            vectorTower = Vector(vectorTower, speed*2);

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

            pen = new Pen(color, 3);
            g.DrawEllipse(pen, position.X-15, position.Y-15, 32, 32);

            DrawInfo(g);
            #endregion
        }
    }
}
