﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Обучение
{
    class Типы_данных
    {
        public void данные()
        {
            Console.WriteLine($"bool(8bit) - {true}\n");
            Console.WriteLine($"sbyte(8bit) - {-123}\n");
            Console.WriteLine($"byte(8b it) - {250}\n");
            Console.WriteLine($"short(16bit) - {-32000}\n");
            Console.WriteLine($"unshort(16bit) - {60000}\n");
            Console.WriteLine($"int(32bit) - {-123456}\n");
            Console.WriteLine($"uint(32bit) - {9876543210}\n");
            Console.WriteLine($"long(64bit) - {-64000000000}\n");
            Console.WriteLine($"unlong(64bit) - {12800000000}\n");
            Console.WriteLine($"float(32bit) - {123.456f}\n");
            Console.WriteLine($"double(64bit) - {123.4567890f}\n");
            Console.WriteLine($"decimal(128bit) - {123456.789}\n");
            Console.WriteLine($"char(16bit) - {"x"}\n");
            Console.WriteLine($"string(ссылка) - {"hello"}\n");
        }
    }
}
