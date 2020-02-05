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

            Console.Write("Сравнение 2_<_3 - ");
            x = 2 < 3;
            Console.WriteLine(x);
            Console.WriteLine();

            Console.Write("Сравнение 2_=_3 - ");
            x = 2 == 3;
            Console.WriteLine(x);
            Console.WriteLine();

        }
    }
}
