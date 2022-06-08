// Binarka.cpp

#include <iostream>
#include <bitset>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RUS");

    int x = 0b011;
    int y = 0x5;
    int z;
    cout << "x = " << x << ", бинарно: " << bitset<4>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<4>(y) << endl;
    cout << endl;

    cout << "Бинарное не" << endl;
    x = ~x;
    y = ~y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << endl;

    cout << "Бинарное i" << endl;
    x = 3;
    y = 5;
    z = x & y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << "z = " << z << ", бинарно: " << bitset<8>(z) << endl;
    cout << endl;

    cout << "Бинарное |" << endl;
    x = 3;
    y = 5;
    z = x | y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << "z = " << z << ", бинарно: " << bitset<8>(z) << endl;
    cout << endl;

    cout << "Бинарное либо" << endl;
    x = 3;
    y = 5;
    z = x ^ y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << "z = " << z << ", бинарно: " << bitset<8>(z) << endl;
    cout << endl;

    cout << "Бинарное сдвижение вправо" << endl;
    x = 3;
    y = x <<1;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << endl;

    cout << "Бинарное сдвижение влево" << endl;
    x = 3;
    y = x << 1;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;
    cout << "y = " << y << ", бинарно: " << bitset<8>(y) << endl;
    cout << endl;

    x &= y;
    cout << "x = " << x << ", бинарно: " << bitset<8>(x) << endl;

    system("pause>nul");
    return 0;
}