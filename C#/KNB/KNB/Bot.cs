using System;

namespace KNB
{
    class Bot
    {
        public byte bot;
        Random random = new Random();

        public void randbot()
        {
            bot = (byte)random.Next(2);
        }
    }
}
