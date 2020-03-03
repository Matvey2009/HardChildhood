using System;

namespace Обучение2
{
    class Условия
        
    {
        public void Консоль2()
        {
            bool a = true & true; //и
            bool b = false ^ true; //либо
            bool x = a | b; //или
            if (x)
            {
                Console.WriteLine("Условия выполнино");
            }
            else
            {
                Console.WriteLine("Условия не выполнино");
            }

            Console.WriteLine($"Равенство + и + - {true & true}\n");
            Console.WriteLine($"Равенство + и + - {true & false}\n");
            Console.WriteLine($"Равенство + и + - {false & false}\n");

            Console.WriteLine($"Равенство + либо + - {true ^ true}\n");
            Console.WriteLine($"Равенство + либо + - {true ^ false}\n");
            Console.WriteLine($"Равенство + либо + - {false ^ false}\n");

            Console.WriteLine($"Равенство + или + - {true | true}\n");
            Console.WriteLine($"Равенство + или + - {true | false}\n");
            Console.WriteLine($"Равенство + или + - {false | false}\n");

            int i = 2147300000;
            bool y = true;
            do
            {
                //y = i < 10;
                Console.WriteLine(i++);
            }
            while (y);
        }
    }
}
