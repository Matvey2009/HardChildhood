using System.Collections.Generic;
using System.Drawing;
using Game2D;

namespace Танк
{
    class Action
    {
        private List<ListUnit> ListParty;

        //Обход всех юнитов
        public void ActUnit(List<ListUnit> ListParty, ListShot listShot)
        {
            this.ListParty = ListParty;

            foreach (ListUnit party in ListParty)
                foreach (dynamic unit in party.listUnits)
                    if (unit.act != Act.DEAD) Logic(unit);
        }

        //Логика действий
        private void Logic(dynamic unit)
        {
            {
                switch(unit.act)
                {
                    case Act.WAIT:
                        goto case Act.FIRE;
                        ActWAIT(unit);
                        break;

                    case Act.FIND:
                        ActFIND(unit);
                        break;

                    case Act.MOVE:
                        ActMOVE(unit);
                        break;

                    case Act.FIRE:
                        ActFIRE(unit);
                        break;

                    default:
                        unit.act = Act.WAIT;
                        break;
                }
            }
        }

        //Процес ожидание
        private void ActWAIT(dynamic unit)
        {
            //Есле танк мёртв
            if (unit.live <= 0)
                unit.act = Act.DEAD;

            //Поиск цели
            unit.target = FindTarget(unit);

        }

        //Процес поиска
        private void ActFIND(dynamic unit)
        {

        }

        //Процес зближение
        private void ActMOVE(dynamic unit)
        {

        }

        //Процес отаки
        private void ActFIRE(dynamic unit)
        {
            unit.vector = unit.Vector(unit.vector, unit.speed);
            unit.PositionUnit();
        }

        //Поиск цели
        private PointF FindTarget(dynamic unit)
        {
            PointF target = PointF.Empty;
            foreach (ListUnit party in ListParty)
                foreach (dynamic findUnit in party.listUnits)
                {
                    if (unit.color != findUnit.color && findUnit.act != Act.DEAD)
                        target = Func2D.Delta(unit.position, findUnit.position); //!ИСПРАВИТЬ!\\
                }
            return target;
        }
    }
}
