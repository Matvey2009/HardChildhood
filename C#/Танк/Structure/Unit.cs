﻿using System;
using System.Drawing;
using System.Windows.Forms;
using System.Xml.Schema;

namespace Танк
{
    abstract class Unit : Aobject
    {
        private static uint ID;

        public uint id = ++ID;
        public Act act;

        public float live;
        public float vision;
        public byte timeShot;

        private Font font = new Font("Areal", 10, FontStyle.Bold, GraphicsUnit.Point);
        private SolidBrush color = new SolidBrush(Color.Yellow);
        private Pen penR = new Pen(Color.Red, 3);
        private Pen penG = new Pen(Color.Green, 3);
        private float angle;
        public float centre;

        //Номер и полоска жизни
        public void DrawInfo(Graphics g)
        {
            if (centre < -20) centre = -20;
            //Наименование
            g.TranslateTransform(position.X, position.Y);
            g.DrawString(act.ToString(), font, color, -7 , -40);
            g.ResetTransform();
            //Полоска жизни
            g.TranslateTransform(position.X, position.Y);
            g.DrawLine(penG, -20, -20, centre, -20);
            g.DrawLine(penR, centre, -20, 20, -20);
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
                if ((vector < angle && (angle - vector) < 180) ^ (angle - vector) > -180)
                    vector = (vector - speed + 360) % 360;
                else
                    vector = (vector + speed) % 360;
            }
            else
                vector = angle;

            return vector;
        }

        //Расчёт позиции unit
        public PointF PositionUnit()
        {
            if (vector == angle)
                position = Position();

            return position;
        }
    }
}
