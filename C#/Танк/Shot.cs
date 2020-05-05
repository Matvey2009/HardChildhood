using System;
using System.Drawing;

namespace Танк
{
    class Shot : Aobject
    {
        private PointF position0;
        Pen pen;

        //Рисунок пульки
        public void DrawShot(Graphics g)
        {
            position = Position();
            pen = new Pen(Color.DarkOrange, 3);
            g.DrawLine(pen, position, position0);
        }

        //Расчёт позиции unit
        public PointF Position()
        {
            vector = Vector();
            position0 = position;
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);

            return position;
        }

        //Угол на цель
        private float Vector()
        {
            float catetX = target.X - position.X;
            float catetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(catetY, catetX) * 180 / Math.PI + 90);
            if (vector < 0) vector += 360;

            return vector;
        }
    }
}
