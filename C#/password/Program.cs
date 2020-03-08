using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace password
{
    class Program
    {
        static void Main(string[] args)
        {
            //Переменые
            string password = "1234", _password = "";

            //Провекрка пороля
            while (password != _password)
            {
                Console.WriteLine("Введите пароль: ");
                _password = Console.ReadLine();
                if (_password != password) Console.WriteLine("Доступ закрыт");
            }

            //Старт
            Console.WriteLine("Доступ открыт");
            Console.ReadKey();
        }
    }
}
