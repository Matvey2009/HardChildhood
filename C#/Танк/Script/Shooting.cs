using System.Collections.Generic;

namespace Танк.Script
{
    class Shooting
    {
        private ListShot listShot;

        //Расчёт стрельбы
        public void ActShot(List<ListUnit> ListParty, ListShot listShot)
        {
            this.listShot = listShot;

            foreach (Shot shot in listShot.listShot)
            {
                shot.MoveShot();
                if (shot.speed < 5)
                    listShot.RemoveShot(shot);
            }
        }
    }
}
