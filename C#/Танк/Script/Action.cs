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
                    if (unit.act != Act.DEAD) Logic(unit);
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
                KillUnit(unit);

            //Поиск цели
            else
            {
                //Поиск ближайщего танка
                float findDelta = unit.vision, minDelta = unit.vision;
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
                if (minDelta < 512)
                {
                    unit.act = Act.FIRE;
                }

                //Проверка на движение
                else if (minDelta < 1024)
                {
                    unit.act = Act.MOVE;
                }

                //Поиск врага
                else
                {
                    unit.target.X = unit.position.X + random.Next(-64, 64);
                    unit.target.Y = unit.position.Y + random.Next(-64, 64);
                    unit.act = Act.FIND;
                }
            }
        }

        //Процес поиска
        private void ActFIND(dynamic unit)
        {
            //Unit ищет цель
        }

        //Процес сближение
        private void ActMOVE(dynamic unit)
        {
            //Tанк едет пока растояние сокрота 
        }

        //Процес атаки
        private void ActFIRE(dynamic unit)
        {
            unit.vector = unit.Vector(unit.vector, unit.speed);
            unit.PositionUnit();

            unit.timeShot++;
            if (unit.timeShot > 120)
            {                         
                listShot.newShot(unit);
                unit.timeShot = 0;
                unit.act = Act.WAIT;
            }
        }

        //Смерть танка
        public void KillUnit(dynamic unit)
        {
            unit.act = Act.DEAD;
            unit.speed = 0.0f;
            unit.live = 0.0f;
            unit.color = Color.Black;
        }
    }
}