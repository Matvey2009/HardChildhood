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
            vector = Vector();
            position0 = position;
            position = Position();
            pen = new Pen(Color.DarkOrange, 3);
            g.DrawLine(pen, position, position0);
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
