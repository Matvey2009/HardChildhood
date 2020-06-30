using System;
using System.Drawing;

namespace Танк
{
    abstract class Aobject
    {
        public Color color;     //Цвет команды
        public PointF position;//Местоподожение
        public PointF target; //Цель
        public float vector; //Угол повророта корпуса
        public float speed; //Скорость

        //Расчёт позиции
        public PointF Position()
        {
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);

            return position;
        }

        //Расчёт растаяния между точками (float)
        public float Delta(PointF point1, PointF point2)
        {
            float catetX = point1.X - point2.X;
            float catetY = point1.Y - point2.Y;
            return (float)Math.Sqrt(catetX * catetX + catetY * catetY);
        }
    }
}
