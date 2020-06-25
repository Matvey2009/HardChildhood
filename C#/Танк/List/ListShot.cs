using System;
using System.Collections.Generic;
using System.Drawing;
using System.Threading.Tasks;

namespace Танк
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();

        //Добавление выстрела
        async public void newShot(dynamic unit)
        {
            listShot.Add(new Shot(unit));
            await Task.Run(() => Console.Beep(50, 50));
        }

        //Удалене функции
        public void RemoveShot(Shot shot)
        {
            listShot.Remove(shot);
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
