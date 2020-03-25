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
            Console.WriteLine(name);
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

        }

        Точка точка = new Точка();

    }

}