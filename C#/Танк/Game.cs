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
            ListParty.Add(new ListUnit());
            ListParty.Add(new ListUnit(Color.Red, new Point(10, 20)));
            ListParty.Add(new ListUnit(Color.Blue, new Point(90, 20), 5));
            ListParty.Add(new ListUnit(new Point(90, 80), 3, 2));
            ListParty.Add(new ListUnit(Color.Yellow, new Point(10, 80), 5));

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

            foreach (ListUnit party in ListParty)
                party.DriweListUnit(g, listShot);

            listShot.DrawListShot(g);
        }
    }
}
