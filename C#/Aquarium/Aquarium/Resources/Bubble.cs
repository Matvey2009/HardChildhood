using System.Drawing;

namespace Aquarium
{
    class Bubble : AFish, IFish
    {
        public Bubble()
        {
            bitmap = new Bitmap(Properties.Resources.Bubble);
            speed = 0.5f;
        }

        public void DrawFish(Graphics g)
        {
            g.DrawImage(bitmap, position);
        }
    }
}