using System.Collections.Generic;
using System.Drawing;
using Танк.Script;

namespace Танк
{
    class Game
    {
        private List<ListUnit> ListParty;
        private ListShot listShot;
        private Action actoin;
        private Shooting shooting;

        //Старт Игры
        public void StartGame()
        {
            ListParty = new List<ListUnit>();
            ListParty.Add(new ListUnit(Color.Red, new Point(25, 20), 10));
            ListParty.Add(new ListUnit(Color.Blue, new Point(75, 80), 10));

            //Sound.SW();
            //Sound();

            listShot = new ListShot();
            actoin = new Action();
            shooting = new Shooting();
        }

        //Шаг Игры
        public void StepGame(Graphics g) 
        {
            actoin.ActUnit(ListParty, listShot);
            shooting.ActShot(ListParty, listShot);

            listShot.DrawListCrator(g);

            foreach (ListUnit party in ListParty)
                party.DriweListUnit(g);

            listShot.DrawListShot(g);
        }
    }
}
