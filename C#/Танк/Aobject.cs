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
    }
}
