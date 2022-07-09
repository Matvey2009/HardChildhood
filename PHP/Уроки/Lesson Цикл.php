<?php
$x = 10;

while ($x > 0):
    $x--;
    if ($x == 3) {
        continue; // Остановиться и продолжить цикл
    if ($x == 7) {
        break; // Полностью прервать цикл
    }
    }
    echo $x;
endwhile;
echo '<br/>';

// Цикл с счетчиками
for ($i = 0; $i < 10; $i++){
    echo $i, ' ';
}
echo '<br/>';

// Цикл с двойным счетчиком
for ($i = 0, $j = 100; $i < 10; $i++, $j += 50){
    echo $i, '-', $j, ' ';
}

echo '<br/>';

//Цикл без операций
for ($i = 0; $i < 15; print $i++.' ');
echo '<br/>';

$arr = [11, 22, 33, 44, 55, 66, 77];
foreach ($arr as $element)
    echo $element, ' ';

echo '<br/>';

//Именованый масив
$arr = ['a' => 10, 'b' => 20, 'c' => 30];
foreach($arr as $key => $element)
echo $key, ' - ', $element, ' ';