using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();
        public List<Bang> listBang = new List<Bang>();
        public List<Crator> listCrator = new List<Crator>();

        //Добавление выстрела
        public void newShot(dynamic unit)
        {
            listShot.Add(new Shot(unit));
        }

        //Удалене функции 
        public void RemoveShot(Shot shot)
        {
            listBang.Add(new Bang(shot.position));
            listShot.Remove(shot);
        }

        public void RemoveBang(Bang bang)
        {
            listCrator.Add(new Crator(bang.position));
            listBang.Remove(bang);
        }

        //Удалене кратора 
        public void RemoveCrator(Crator crator)
        {
            listCrator.Remove(crator);
        }

        //Отрисовка кратора
        public void DrawListCrator(Graphics g)
        {
            foreach (Crator crator in listCrator)
                crator.DrawCrator(g);
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
