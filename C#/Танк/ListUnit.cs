using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Танк
{
    class ListUnit
    {
        private Random random = new Random();
        private List<object> listUnits = new List<object>();
        private byte count = 10;

        //Создаём лист танков
        public List<object> CreateListUnit()
        {
            for (byte i = 1; i <= count; i++) 
            {
                listUnits.Add(new Tank
                {
                    position = StartPosition()
                });

                listUnits.Add(new Car
                {
                    position = StartPosition()
                });
            }
            return listUnits;
        }

        //Отрисовка лист танков
        public void DriweListUnit(Graphics g, Point cursor)
        {
            foreach (dynamic unit in listUnits)
            {
                unit.DrawUnit(g, cursor);
            }
        }

        //Стартовая позиция
        private Point StartPosition()
        {
            Point position = new Point();
            position.X = random.Next(1280);
            position.Y = random.Next(720);

            return position;
        }
    }
}
