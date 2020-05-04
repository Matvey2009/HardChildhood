using System.Drawing;

namespace Танк
{
    class Shot : Aobject
    {
        Pen pen;

        //Рисунок пульки
        public void DrawShot(Graphics g, Point cursor)
        {
            target = cursor;
            pen = new Pen(Color.DarkOrange, 3);
            g.DrawLine(pen, position, target);
        }
    }
}
