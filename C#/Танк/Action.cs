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
            unit.act = Act.FIRE;
        }

        //Процес поиска
        private void ActFIND(dynamic unit)
        {
            //Unit ищет цель

        }

        //Процес зближение
        private void ActMOVE(dynamic unit)
        {
            //Tанк едет пока растояние сокрота 
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
            float findDelta = 1000, minDelta = 1000;

            foreach (ListUnit party in ListParty)
                foreach (dynamic findUnit in party.listUnits)
                {
                    if (unit.color != findUnit.color && findUnit.act != Act.DEAD)
                        findDelta = Func2D.Delta(unit.position, findUnit.position);

                    if (findDelta < minDelta)
                    {
                        minDelta = findDelta;
                        unit.target = findUnit.position;
                    }    
                }
            return unit.target;
        }
    }
}