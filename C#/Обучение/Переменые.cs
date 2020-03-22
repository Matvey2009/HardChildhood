using System;

namespace Обучение
{
    class Переменые
    {
        public void консоль()
        {
            Console.Write("Сравнение 2_>_3 - ");
            Console.WriteLine(2 > 3);
            Console.WriteLine();

            Console.Write("Сравнение 2_>_3 - ");
            bool x = 2 > 3;
            Console.WriteLine(x);
            Console.WriteLine();

            x = 2 < 3;
            Console.WriteLine($"Сравнение 2_<_3 - {x}\n");
            
            x = 2 == 3;
            Console.WriteLine($"Равенство 2_=_3 - {x}\n");


           int a = 16;
           Console.WriteLine($"Остаток от деления : {a % 5}\n");
           Console.WriteLine($"Побитовый сдвиг вниз 16 >> 1 : {a >>= 1}\n");
           Console.WriteLine($"Побитовый сдвиг верх 8 << 1 : {a <<= 2}\n");

            int b = 100, c = 3;
            decimal d = (decimal) b / c;
            Console.WriteLine(d);

            Console.WriteLine($"Бинарный код 0b100001 - {0b100001}\n");
            Console.WriteLine($"Байт код код 0xA1 - {0xA1}\n");
            Console.WriteLine($"Число степени 3.2e4 - {3.2e4}\n");
            Console.WriteLine($"Число степени(-) 1.2e-3 - {1.2e-3}\n");
            Console.WriteLine($"Уни код \u0420 - {"\u0420"}\n");
            Console.WriteLine($"ASC|| \x5A - {"\x5A"}\n");

            DateTime mydr = new DateTime(2009, 01, 25);
            Console.WriteLine($"Моё День Рождения - {mydr}\n");
            Console.WriteLine($"День Недели Моего День Рождения - {mydr.DayOfWeek}\n");
            DateTime today = DateTime.Now;
            Console.WriteLine($"Число - {(today - mydr).Days}\n");
        }
    }
}
