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

        //Номер и полоска жизни
        public void DrawInfo(Graphics g)
        {
            //Наименование
            g.TranslateTransform(position.X, position.Y);
            g.DrawString(id.ToString(), font, color, -7 , -40);
            g.ResetTransform();
            //Полоска жизни
            g.TranslateTransform(position.X, position.Y);
            g.DrawLine(pen, -20, -20, 20, -20);
            g.ResetTransform();
        }

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
