using System.Drawing;

namespace Aquarium
{
    class Fish : AFish, IFish
    {
        public Fish()
        {
            bitmap = new Bitmap(Properties.Resources.Fish);
            speed = 1.5f;
        }

        public void DrawFish(Graphics g)
        {
            g.DrawImage(bitmap, position);
        }
    }
}