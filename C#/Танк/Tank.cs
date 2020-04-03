using System;
using System.Drawing;

namespace Танк
{
    class Tank
    {
        public int id;//Нопер танка
        public PointF position;//Местоподожение

        private float vector; //Угол повророта корпуса
        private float vectorTower; //Угол повророта башня
        private Bitmap bitmap = new Bitmap(Properties.Resources.Танкpng);
        private PointF target;//Цель
        private float speed = 1;
        private Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        private Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

        //Отрисовка танка
        public void DrawTank(Graphics g, Point cursor)
        {
            target = cursor;
            Position();
            Vector();
            vectorTower = vector;

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

        //Расчёт поворота танка
        private float Vector()
        {
            float catetX = target.X - position.X;
            float catetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(catetY, catetX) * 180 / Math.PI + 90);

            return vector;
        }

        //Расчёт позиции танка
        private PointF Position()
        {
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);
            return position;
        }
    }
}
