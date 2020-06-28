using System.Collections.Generic;

namespace Танк.Script
{
    class Shooting
    {
        private Shot shot;
        private Bang bang;
        private Crator crater;

        //Расчёт стрельбы
        public void ActShot(List<ListUnit> ListParty, ListShot listShot)
        {
            //Расчёт пуль
            for (int i = 0; i < listShot.listShot.Count; i++)
            {
                shot = listShot.listShot[i];
                shot.MoveShot();

                if (shot.speed < 5)
                    listShot.RemoveShot(shot);
         
            }

            //Расчёт взрывов
            for (int i = 0; i < listShot.listBang.Count; i++)
            {
                bang = listShot.listBang[i];
                if (bang.time > 96)
                    //_-_-_-_-_ Расчёт дамагА _-_-_-_-_\\
                    listShot.RemoveBang(bang);
                else
                    bang.time += 1;
            }    
        }
    }
}