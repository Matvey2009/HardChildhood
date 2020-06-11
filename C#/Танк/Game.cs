using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class Game
    {
        private List<ListUnit> ListParty;
        private ListShot listShot;
        private Action actoin;

        //Старт Игры
        public void StartGame()
        {
            ListParty = new List<ListUnit>();
            ListParty.Add(new ListUnit());
            ListParty.Add(new ListUnit(Color.Red, new Point(10, 20)));
            ListParty.Add(new ListUnit(Color.Blue, new Point(90, 20), 20));
            ListParty.Add(new ListUnit(new Point(90, 80), 10, 10));
            ListParty.Add(new ListUnit(Color.Yellow, new Point(10, 80), 10));
            actoin = new Action();

            //Sound.SW();
            //Sound();

            listShot = new ListShot();
        }

        //Шаг Игры
        public void StepGame(Graphics g, Point cursor) 
        {
            actoin.ActUnit(ListParty, listShot);

            foreach (ListUnit party in ListParty)
                party.DriweListUnit(g, cursor, listShot);

            listShot.DrawListShot(g);
        }
    }
}
