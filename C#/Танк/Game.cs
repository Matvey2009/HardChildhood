using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class Game
    {
        private List<ListUnit> ListParty;
        private ListShot listShot;

        //Старт Игры
        public void StartGame()
        {
            ListParty = new List<ListUnit>();
            ListParty.Add(new ListUnit(Color.Red, new Point(30, 20)));
            ListParty.Add(new ListUnit(Color.Blue, new Point(70, 80)));
            ListParty.Add(new ListUnit());
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
