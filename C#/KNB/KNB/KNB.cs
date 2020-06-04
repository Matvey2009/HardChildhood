using System;

namespace KNB
{

    class KNB
    {
        Bot bot = new Bot();

        public int win, lose, draw;
        public byte stepbot;
        public string result;

        public void StepGame(byte player)
        {
            bot.randbot();
            stepbot = bot.bot;

            //Ничья
            if (player == stepbot)
            {
                result = "Ничья";
                draw++;
            }
            //Победа
            else if ((player == 0 & stepbot == 1) ||
                    (player == 1 & stepbot == 2) ||
                    (player == 2 & stepbot == 0))
                 {
                 result = "Победа";
                 win++;

                 }
            //Поражение
            else
            {
                result = "Поражение";
                lose++;
            }
        }
    }
}
