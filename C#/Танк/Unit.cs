using System;
using System.Drawing;

namespace Танк
{
    abstract class Unit
    {
        private static uint ID;

        public uint id = ++ID;//Нопер Unit
        public PointF position;//Местоподожение

        public PointF target;//Цель
        public float speed = 1;
        public float vector; //Угол повророта корпуса

        private Font font = new Font("Areal", 10, FontStyle.Bold, GraphicsUnit.Point);
        private SolidBrush color = new SolidBrush(Color.Yellow);
        private Pen pen = new Pen(Color.Red, 3);
        private float angle;

        //Номер и полоска жизни
        public void DrawInfo(Graphics g)
        {
            //Наименование
            g.TranslateTransform(position.X, position.Y);
            g.DrawString(vector.ToString(), font, color, -7 , -40);
            g.ResetTransform();
            //Полоска жизни
            g.TranslateTransform(position.X, position.Y);
            g.DrawLine(pen, -20, -20, 20, -20);
            g.ResetTransform();
        }

        //Расчёт поворота unit
        public float Vector(float vector, float speed)
        {
            //Угол на цель
            float catetX = target.X - position.X;
            float catetY = target.Y - position.Y;
            angle = (float)(Math.Atan2(catetY, catetX) * 180 / Math.PI + 90);
            if (angle < 0) angle += 360;

            //Текущий угол
            if (Math.Abs(vector - angle) > speed)
            {
                if ((vector < angle && (angle - vector) < 180) ^ (angle - vector) < 180)
                    vector = (vector - speed + 360) % 360;
                else
                    vector = (vector + speed) % 360;
            }
            else
                vector = angle;

            return vector;
        }

        //Расчёт позиции unit
        public PointF Position()
        {
            if (vector == angle)
            {
                position.X += speed * (float)Math.Cos(vector);
                position.Y += speed * (float)Math.Sin(vector);
            }

            return position;
        }
    }
}
