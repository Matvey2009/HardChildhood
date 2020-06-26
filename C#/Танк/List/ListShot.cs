using System;
using System.Collections.Generic;
using System.Drawing;
using System.Threading.Tasks;

namespace Танк
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();
        public List<Bang> listBang = new List<Bang>();

        //Добавление выстрела
        async public void newShot(dynamic unit)
        {
            listShot.Add(new Shot(unit));
            await Task.Run(() => Console.Beep(50, 50));
        }

        //Удалене функции 
        async public void RemoveShot(Shot shot)
        {
            await Task.Run(() => Console.Beep(100, 100));
                listBang.Add(new Bang(shot.position));
            listShot.Remove(shot);
        }

        //Отрисовка пульки
        public void DrawListShot(Graphics g)
        {
            foreach (Shot shot in listShot)
                shot.DrawShot(g);

            foreach (Bang bang in listBang)
                bang.DrawBang(g);
        }
    }
}
