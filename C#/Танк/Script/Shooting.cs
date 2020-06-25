using System.Collections.Generic;

namespace Танк.Script
{
    class Shooting
    {
        //Расчёт стрельбы
        public void ActShot(List<ListUnit> ListParty, ListShot listShot)
        {
            foreach (Shot shot in listShot.listShot)
            {
                shot.MoveShot();
                /*if (shot.speed < 2)
                    listShot.RemoveShot(shot);*/
            }
        }
    }
}
