using System;
using System.Threading.Tasks;

namespace Танк
{
    class Sound
    {
        //Звук заставки
        async public static void SW()
        {
            while (true)
            await Task.Run(() =>
            {
                Console.Beep(440, 500);
                Console.Beep(440, 500);
                Console.Beep(440, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 1000);
                Console.Beep(659, 500);
                Console.Beep(659, 500);
                Console.Beep(659, 500);
                Console.Beep(698, 350);
                Console.Beep(523, 150);
                Console.Beep(415, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 1000);
            });
        }
        private void Music()
        {
            Console.Beep(261, 400);
            Console.Beep(293, 400);
            Console.Beep(440, 400);
            Console.Beep(293, 400);
            Console.Beep(493, 400);
            Console.Beep(440, 400);
            Console.Beep(349, 400);
            Console.Beep(293, 400);
            Console.Beep(349, 400);
            Console.Beep(349, 400);
            Console.Beep(493, 400);
            Console.Beep(440, 400);
            Console.Beep(493, 400);
        }
    }
}
