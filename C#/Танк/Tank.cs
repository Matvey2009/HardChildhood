using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Танк
{
    class Tank
    {
        public Bitmap bitmap = new Bitmap(Properties.Resources.Танкpng);

        Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

        int x = 0;
        public void DrawTank(Graphics g, Point position)
        {
            x++;
            //Корпус
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(x);
            g.DrawImage(bitmap, -68, -70, body, GraphicsUnit.Pixel);
            g.ResetTransform();
            //Башня
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(x / 2);
            g.DrawImage(bitmap, -48, -87, tower, GraphicsUnit.Pixel);
            g.ResetTransform();
        }
    }
}
