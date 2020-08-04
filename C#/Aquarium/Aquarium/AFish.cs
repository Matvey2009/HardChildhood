using System;
using System.Drawing;

namespace Aquarium
{
    abstract class AFish
    {
        public PointF position = new PointF();
        public PointF target = new PointF();
        public Bitmap bitmap;
        private Random random = new Random();
        public float speed;

        //Рассчёт позиции
        public PointF Position()
        {
            if (Math.Abs(position.X - target.X) < speed*2 &&
                Math.Abs(position.Y - target.Y) < speed*2)
                Target();

            if (target.X > position.X)
                position.X += speed;
            else
                position.X -= speed;

            if (target.Y > position.Y)
                position.Y += speed;
            else
                position.Y -= speed;

            return position;
        }

        //Рассчёт цели
        public PointF Target()
        {
            target.X = random.Next(0, 1800);
            target.Y = random.Next(0, 1080);

            return target;
        }   
    
    }
}
