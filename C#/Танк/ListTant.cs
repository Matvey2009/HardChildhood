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
        private Random random = new Random();
        private List<Tank> listTank = new List<Tank>();
        private byte count = 10;

        //Создаём лист танков
        public List<Tank> CreateListTant()
        {
            for (byte i = 1; i <= count; i++) 
            {
                listTank.Add(new Tank()
                {
                    id = i,
                    position = StartPosition()
                });
            }
            return listTank;
        }

        //Стартовая позиция
        private Point StartPosition()
        {
            Point position = new Point();
            position.X = random.Next(1280);
            position.Y = random.Next(720);
            return position;
        }

        //Отрисовка лист танков
        public void DriweListTant(Graphics g, Point cursor)
        {
            foreach (Tank tank in listTank)
            {
                tank.DrawTank(g, cursor);
            }
        }
    }
}
