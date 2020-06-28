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
        public Shot(dynamic unit)
        {
            color = unit.color;
            pen = new Pen(color, 3);
            position = unit.position;
            target = unit.target;
            vector = (float)Math.Atan2(unit.target.Y - unit.position.Y,
                unit.target.X - unit.position.X);
            speed = 16;
            Sound.Shot();
        }

        //Расчёт полёта снаряда
        public void MoveShot()
        {
            position0 = position;
            position = Position();
            speed *= 0.98f;
        }

        //Рисунок пульки
        public void DrawShot(Graphics g)
        {
            g.DrawLine(pen, position, position0);
        }
    }
}
