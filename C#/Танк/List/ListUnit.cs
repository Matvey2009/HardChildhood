using System;
using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class ListUnit
    {
        private Size window = FormTanks.window;
        private Random random = new Random();
        public List<object> listUnits = new List<object>();
        private byte count = 3;

        /// <summary> Команда: Пустой <summary> \\\
        public ListUnit()
        {
            Color color = Color.FromArgb(255, Color.FromArgb (random.Next(0XFFFFFF+1))); 
            CreateListUnit(color, new Point(50, 50), count, count);
        }

        /// <summary> Команда: Цвет и Позиция <summary> \\\
        public ListUnit(Color color, Point start)
        {
            CreateListUnit(color, start, count, count);
        }

        /// <summary> Команда: Цвет и Позиция и Число юнитов <summary> \\\
        public ListUnit(Color color, Point start, byte unit)
        {
            CreateListUnit(color, start, unit, unit);
        }

        /// <summary> Цвет и Позиция и Танки и Машинки </summary>
        public ListUnit(Color color, Point start, byte tank, byte car)
        {
            CreateListUnit(color, start, tank, car);
        }

        /// <summary>Позиция танков и машинок о/summary>
        public ListUnit(Point start, byte tank, byte car)
        {
            Color color = Color.FromArgb(255, Color.FromArgb(random.Next(0xFFFFFF + 1)));
            CreateListUnit(color, start, tank, car);
        }

        //Создаём лист танков
        public List<object> CreateListUnit
            (Color color, Point start, byte tank, byte car)
        {
            for (byte i = 1; i <= car; i++)
                NewUnit(new Car(color), start);

            for (byte i = 1; i <= tank; i++)
                NewUnit(new Tank(color), start);

            return listUnits;
        }

        //Добовлем unita в список
        private void NewUnit(dynamic unit, Point start)
        {
            listUnits.Add(unit);
            unit.position = StartPosition(start);
        }

        //Отрисовка лист танков
        public void DriweListUnit(Graphics g)
        {
            foreach (dynamic unit in listUnits)
                unit.DrawUnit(g);
        }

        //Стартовая позиция
        private Point StartPosition(Point start)
        {
            Point position = new Point();
            position.X = window.Width * start.X / 100 + random.Next(-200, 200);
            position.Y = window.Height * start.Y / 100 + random.Next(-200, 200);

            return position;
        }
    }
}
