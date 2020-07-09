using System;
using System.Collections.Generic;
using System.Drawing;

namespace Танк
{
    class Action
    {
        private readonly Random random = new Random();
        private List<ListUnit> ListParty;
        private ListShot listShot;

        //Обход всех юнитов
        public void ActUnit(List<ListUnit> ListParty, ListShot listShot)
        {
            this.ListParty = ListParty;
            this.listShot = listShot;

            foreach (ListUnit party in ListParty)
                foreach (dynamic unit in party.listUnits)
                    if (unit.act != Act.DEAD)
                        Logic(unit);
        }

        //Логика действий
        private void Logic(dynamic unit)
        {
            {
                switch (unit.act)
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
        private void ActWAIT(dynamic unit)
        {
            //Есле танк мёртв
            if (unit.live <= 0)
                ActDead(unit);

            //Поиск цели
            else
            {
                //Поиск ближайщего танка
                float findDelta = unit.vision*2, minDelta = unit.vision*2;
                foreach (ListUnit party in ListParty)
                    foreach (dynamic findUnit in party.listUnits)
                    {
                        if (unit.color != findUnit.color && findUnit.act != Act.DEAD)
                            findDelta = unit.Delta(unit.position, findUnit.position);

                        if (findDelta < minDelta)
                        {
                            minDelta = findDelta;
                            unit.target = findUnit.position;
                        }
                    }

                //Проверка на атаку
                if (minDelta < unit.vision)
                    unit.act = Act.FIRE;

                //Проверка на движение
                else if (minDelta < unit.vision*2)
                    unit.act = Act.MOVE;

                //Поиск врага
                else
                {
                    unit.target = new PointF(
                        unit.position.X + random.Next(-128, 128),
                        unit.position.Y + random.Next(-128, 128));
                    unit.act = Act.FIND;
                }
            }
        }

        //Процес поиска
        private void ActFIND(dynamic unit)
        {
            if (unit.Delta(unit.position, unit.target) > unit.speed*32)
            {
                unit.vector = unit.Vector(unit.vector, unit.speed);
                unit.PositionUnit();
            }
            else
                unit.act = Act.WAIT;
        }

        //Процес сближение
        private void ActMOVE(dynamic unit)
        {
            if (unit.Delta(unit.position, unit.target) > unit.vision)
            {
                unit.vector = unit.Vector(unit.vector, unit.speed);
                unit.PositionUnit();
            }
            else
                unit.act = Act.WAIT;
        }

        //Процес атаки
        private void ActFIRE(dynamic unit)
        {
            if (unit.timeShot < 120)
            {
                unit.timeShot++;
                unit.vector = unit.Vector(unit.vector, unit.speed);
            }
            else
            {
                listShot.newShot(unit);
                unit.timeShot = 0;
                unit.act = Act.WAIT;
            }
        }

        //Смерть танка
        public void ActDead(dynamic unit)
        {
            unit.act = Act.DEAD;
            unit.speed = 0.0f;
            unit.live = 0.0f;
            unit.color = Color.Black;
        }
    }
}