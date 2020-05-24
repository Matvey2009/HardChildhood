using System;
using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class ListUnit
    {
        private Size window = FormTanks.window;
        private Random random = new Random();
        private List<object> listUnits = new List<object>();
        private byte count = 10;

        /// <summary>
        /// Команда
        /// </summary>
        public ListUnit(Color color, int x)
        {
            CreateListUnit(color, x);
        }
        
        //Создаём лист танков
        public List<object> CreateListUnit(Color color, int x)
        {
            for (byte i = 1; i <= count; i++) 
            {
                listUnits.Add(new Tank
                {
                    color = color,
                    position = StartPosition(x)
                });

                listUnits.Add(new Car
                {
                    color = color,
                    position = StartPosition(x)
                });
            }
            return listUnits;
        }

        //Отрисовка лист танков
        public void DriweListUnit(Graphics g, Point cursor, ListShot listShot)
        {
            foreach (dynamic unit in listUnits)
            {
                unit.DrawUnit(g, cursor);

                unit.timeShot++;
                if (unit.timeShot > 120)
                {
                    listShot.newShot(unit);
                    unit.timeShot = 0;
                }
            }
        }

        //Стартовая позиция
        private Point StartPosition(int x)
        {
            Point position = new Point();
            position.X = window.Width * x / 100 + random.Next(-200, 200);
            position.Y = random.Next(50, window.Height - 50);

            return position;
        }
    }
}
