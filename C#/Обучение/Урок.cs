using System;
using Обучение2;
using Целое = System.Int32;
using Дробь = System.Double;
using Строка = System.String;
using КвадраМатвеюс = System.Console;

namespace Обучение
{
    struct Точка
    {
        public int x;
        public int y;
        public string name;
        public void Вывод()
        {
            Console.WriteLine(name + " " + x + " " + y);
        }
    }

    class Урок
    {
        Переменые переменые = new Переменые();
        Условия условия = new Условия();
        Типы_данных td = new Типы_данных();

        static void Main(string[] args)
        {
            Урок урок = new Урок();
            урок.Выводнаконсоль();
            Console.ReadKey();

        }

        unsafe
        void Выводнаконсоль()
        {
            //переменые.консоль();
            //условия.Консоль2();
            //td.данные();
            //td.структуры();
            Целое durak = 5;
            Дробь dabil = 0.777;
            Строка iks = "Дирежабыль";
            КвадраМатвеюс.WriteLine(durak + " " + dabil + " " + iks);

            //Объект структуры
            Точка тчк = new Точка();
            тчк.x = 1_234_567;
            тчк.y = 999_876_543;
            тчк.name = "Матвей";
            тчк.Вывод();

            //Указатели\\
            int k = 125;
            int* Указатель = &k;
            Console.WriteLine("Регистор памяти " + (long)Указатель);

            //Динамичекский тип данных
            dynamic d = 1;
            Console.WriteLine(d);
            d = "Матвей";
            Console.WriteLine(d);

            //Округлегие
            Console.WriteLine(Math.Round(Math.PI, 15));
            Console.WriteLine(Math.Abs(-123));
            Console.WriteLine(Math.Pow(10,10));
            Console.WriteLine(Math.Sqrt(16));
            Console.WriteLine(Math.Min(10, 15));
            Console.WriteLine(Math.Sin(30));
            Console.WriteLine(Math.Cos(30));
        }
    }
}