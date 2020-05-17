using System;
using System.Drawing;

namespace Танк
{
    class Shot : Aobject
    {
        private PointF position0;
        private Pen pen;

        /// <summary>
        /// Конструкор снаряда
        /// </summary>
        public Shot()
        {
            speed = 16;
        }

        //Рисунок пульки
        public void DrawShot(Graphics g)
        {
            position0 = position;
            position = Position();
            pen = new Pen(color, 3);
            g.DrawLine(pen, position, position0);
        }
    }
}
