using System.Collections.Generic;
using System.Drawing;
using System.Net.Http.Headers;

namespace Танк
{
    class Action
    {
        //Обход всех юнитов
        public void ActUnit(List<ListUnit> ListParty, ListShot listShot)
        {
            foreach (ListUnit party in ListParty)
                foreach (dynamic unit in party.listUnits)
                    if (unit.act != Act.DEAD) Logic(unit);
        }

        //Логика действий
        private void Logic(dynamic unit)
        {
            {
                unit.vector = unit.Vector(unit.vector, unit.speed);
                unit.PositionUnit();

                switch(unit.act)
                {
                    case Act.WAIT:
                        break;

                    case Act.FIND:
                        break;

                    case Act.MOVE:
                        break;

                    case Act.FIRE:
                        break;

                    default:
                        unit.act = Act.WAIT;
                        break;
                }
            }
        }
    }
}
