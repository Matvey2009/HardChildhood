using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Танк
{
    class ListTant
    {
        Tank tank;
        
        public void DriweListTant(Graphics g)
        {
            for (byte i = 0; i < 10; i++)
            {
                tank = new Tank();
                tank.DrawTank(g);
            }
        }
    }
}
