using System;
using System.Drawing;
using System.Threading.Tasks;

namespace Танк
{
    class Game
    {
        private ListUnit RedParty, BlueParty;
        private ListShot listShot;

        //Старт Игры
        public void StartGame()
        {
            RedParty = new ListUnit();
            RedParty.CreateListUnit(Color.Red, 20);

            BlueParty = new ListUnit();
            BlueParty.CreateListUnit(Color.Blue, 80);

            SW();
            //Sound();

            listShot = new ListShot();
        }

        //Шаг Игры
        public void StepGame(Graphics g, Point cursor) 
        {
            RedParty.DriweListUnit(g, cursor, listShot);
            BlueParty.DriweListUnit(g, cursor, listShot);

            listShot.DrawListShot(g);
        }

        //Звук заставки
        async private void SW()
        {
            await Task.Run(() =>
            {
                Console.Beep(440, 500);
                Console.Beep(440, 500);
                Console.Beep(440, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 1000);
                Console.Beep(659, 500);
                Console.Beep(659, 500);
                Console.Beep(659, 500);
                Console.Beep(698, 350);
                Console.Beep(523, 150);
                Console.Beep(415, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 1000);
            });
        }
        private void Sound()
        {
            //261
            //293
            //329
            //349
            //392
            //440
            //493
            Console.Beep(261, 400);
            Console.Beep(293, 400);
            Console.Beep(440, 400);
            Console.Beep(293, 400);
            Console.Beep(493, 400);
            Console.Beep(440, 400);
            Console.Beep(349, 400);
            Console.Beep(293, 400);
            Console.Beep(349, 400);
            Console.Beep(349, 400);
            Console.Beep(493, 400);
            Console.Beep(440, 400);
            Console.Beep(493, 400);
        }
    }
}
