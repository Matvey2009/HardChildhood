/*
 * Progect: Библиотека для роcчетов в 2D
 * Version: 1.0.0.1
 * Data:    20.06.2020
 * Autor:   Matvey
 */

using System;
using System.Drawing;

namespace Game2D
{
    public static class Func2D
    {
        ///<summary>
        ///Расчёт состаяния между точками (int)
        ///</summary>
        public static int Delta(Point point1, Point point2)
        {
            int catetX = point1.X - point2.X;
            int catetY = point1.Y - point2.Y;
            return (int)Math.Sqrt(catetX * catetX + catetY * catetY);
        }
        
        ///<summary>
        ///Расчёт состаяния между точками (float)
        ///</summary>
        public static float Delta(PointF point1, PointF point2)
        {
            float catetX = point1.X - point2.X;
            float catetY = point1.Y - point2.Y;
            return (float)Math.Sqrt(catetX * catetX + catetY * catetY);
        }
    }
}
