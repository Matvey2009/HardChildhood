using System.Drawing;

namespace Aquarium
{
    class Crab : AFish, IFish
    {
        public Crab()
        {
            bitmap = new Bitmap(Properties.Resources.Lobster);
            speed = 1.0f;
        }

        public void DrawFish(Graphics g)
        {
            g.DrawImage(bitmap, position);
        }
    }
}