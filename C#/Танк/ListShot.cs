using System.Collections.Generic;
using System.Drawing;
using System.Security.Cryptography.X509Certificates;

namespace Танк
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();

        //Добавление выстрела
        public void newShot(dynamic unit)
        {
            listShot.Add(new Shot
            {
                color = unit.color,
                position = unit.position,
                target = unit.target,
                //vector = Vector(),
                speed = 16
            });
        }

        //Отрисовка пульки
        public void DrawListShot(Graphics g)
        {
            foreach (Shot shot in listShot)
            {
                shot.DrawShot(g);
            }
        }
    }
}
