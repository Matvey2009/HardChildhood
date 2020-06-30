using System.Drawing;

namespace Танк
{
    class Crator
    {
        public PointF position;
        public ushort time;

        public Crator(PointF position)
        {
            this.position = position;
        }

        public void DrawCrator(Graphics g)
        {
            g.TranslateTransform(position.X, position.Y);
            g.FillEllipse(new SolidBrush(Color.FromArgb(64/time+16, 32, 16, 0)),
                new RectangleF(-32, -32, 64, 64));
            g.ResetTransform();
        }
    }
}