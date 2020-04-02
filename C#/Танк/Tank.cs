using System;
using System.Drawing;

namespace Танк
{
    class Tank
    {
        public int id;//Нопер танка
        float vector; //Угол повророта корпуса
        float vectorTower; //Угол повророта башня
        public Bitmap bitmap = new Bitmap(Properties.Resources.Танкpng);
        public Point position;//Местоподожение
        Point target;//Цель
        Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));
        Random random = new Random();


        //Отрисовка танка
        public void DrawTank(Graphics g)
        {
            //Корпус
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -68, -70, body, GraphicsUnit.Pixel);
            g.ResetTransform();
            //Башня
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vectorTower);
            g.DrawImage(bitmap, -48, -87, tower, GraphicsUnit.Pixel);
            g.ResetTransform();
        }

        //Расчёт позиции танка
        public Point Position()
        {
            position.X = random.Next(1280);
            position.Y = random.Next(720);
            return position;
        }
    }
}
