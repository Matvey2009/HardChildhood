using System.Drawing;

namespace Танк
{
    class Crator
    {
        public PointF position;
        public byte time;

        public Crator(PointF position)
        {
            this.position = position;
        }

        public void DrawCrator(Graphics g)
        {
            g.TranslateTransform(position.X, position.Y);
            g.FillEllipse(new SolidBrush(Color.FromArgb(128, 128, 128, 128)),
                new RectangleF(-32, -32, 64, 64));
            g.ResetTransform();
        }
    }
}