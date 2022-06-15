#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");

    int count;
    int f = 1;
    cout << "Ведите число для подсчёта факториала" << endl;
    cin >> count;

    //Умножение
    __asm
    {
        mov esi, 1
        mov eax, f
        label:              ;Метка для цикла
            mul esi
            inc esi
        cmp esi, count
        jng label           ;Крутимся в цикли
        mov f, eax
    }

    cout << f;
    system("pause>nul");
}
