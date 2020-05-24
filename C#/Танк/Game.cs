using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class Game
    {
        private List<ListUnit> ListParty;
        private ListUnit RedParty, BlueParty;
        private ListShot listShot;

        //Старт Игры
        public void StartGame()
        {
            ListParty = new List<ListUnit>();

            ListParty.Add(new ListUnit(Color.Red, 20));
            ListParty.Add(new ListUnit(Color.Blue, 80));
            ListParty.Add(new ListUnit(Color.Yellow, 30));
            ListParty.Add(new ListUnit(Color.Green, 40));
            ListParty.Add(new ListUnit(Color.Cyan, 50));
            ListParty.Add(new ListUnit(Color.Orange, 60));

            Sound.SW();
            //Sound();

            listShot = new ListShot();
        }

        //Шаг Игры
        public void StepGame(Graphics g, Point cursor) 
        {
            foreach (ListUnit party in ListParty)
                party.DriweListUnit(g, cursor, listShot);

            listShot.DrawListShot(g);
        }

        
    }
}
