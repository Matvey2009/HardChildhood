using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Танк
{
    class ListTant : List<Tank>
    {
        Tank tank = new Tank();
        List<Tank> listTank = new List<Tank>();

        //Создаём лист танков
        public List<Tank> CreateListTant()
        {
            for (byte i = 1; i <= 10; i++) 
            {
                listTank.Add(new Tank()
                {
                    id = i,
                    position = tank.Position()
                });
            }
            return listTank;
        }

        //Отрисовка лист танков
        public void DriweListTant(Graphics g)
        {
            foreach (Tank tank in listTank)
            {
                tank.DrawTank(g);
            }
        }
    }
}
