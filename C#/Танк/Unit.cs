using System;
using System.Drawing;

namespace Танк
{
    abstract class Unit
    {
        public int id;//Нопер Unit
        public PointF position;//Местоподожение

        public PointF target;//Цель
        public float speed = 1;
        public float vector; //Угол повророта корпуса

        //Расчёт поворота unit
        public float Vector()
        {
            float catetX = target.X - position.X;
            float catetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(catetY, catetX) * 180 / Math.PI + 90);

            return vector;
        }

        //Расчёт позиции unit
        public PointF Position()
        {
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);
            return position;
        }
    }
}
