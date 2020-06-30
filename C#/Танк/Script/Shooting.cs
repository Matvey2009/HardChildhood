using System.Collections.Generic;
using System.Windows.Forms;

namespace Танк.Script
{
    class Shooting
    {
        private Shot shot;
        private Bang bang;
        private Crator crator;
        private float delta;

        //Расчёт стрельбы
        public void ActShot(List<ListUnit> ListParty, ListShot listShot)
        {
            //Расчёт пуль
            for (int i = 0; i < listShot.listShot.Count; i++)
            {
                shot = listShot.listShot[i];
                shot.MoveShot();

                if (shot.Delta(shot.position, shot.target) < 16 || shot.speed < 5)
                {
                    //Расчёт Дамажа
                    foreach (ListUnit party in ListParty)
                        foreach (dynamic unit in party.listUnits)
                        {
                            if (unit.act != Act.DEAD)
                            {
                                delta = unit.Delta(unit.position, shot.position);
                                if (delta < 32)
                                    unit.live -= 100 / delta;
                            }
                        }

                    listShot.RemoveShot(shot);
                }
            }

            //Расчёт взрывов
            for (int i = 0; i < listShot.listBang.Count; i++)
            {
                bang = listShot.listBang[i];
                if (bang.time > 96)
                    listShot.RemoveBang(bang);
                else
                    bang.time += 4;
            }

            //Расчёт краторов
            for (int i = 0; i < listShot.listCrator.Count; i++)
            {
                crator = listShot.listCrator[i];
                if (crator.time > 300)
                    listShot.RemoveCrator(crator);
                else
                    crator.time++;
            }
        }
    }
}