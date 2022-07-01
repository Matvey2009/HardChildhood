<?php
    $arr = array(11, 22, 33, 44, 55, 66, 77, 88, 99);
    #echo $arr, '</br>';
    echo $arr[2], '</br>';
    echo print_r($arr), '</br>';
    echo var_dump($arr), '</br>';
    echo var_export($arr), '<br/>';
    echo '<br/>';

    $arr2 = ['Имя' => 'Вася', 'Возврост' => 72, 'Класс' => '5-A', 'Оценки' => [3, 4, 5, 'Болел'], 'Ученик' => true];
    echo print_r($arr2['Класс']), '</br>';
    echo var_dump($arr2), '</br>';
    echo var_export($arr2['Ученик']), '<br/>';
    echo $arr2['Ученик'], '</br>';//Различия в выводе данных
    echo var_dump($arr2['Ученик']), '</br>';

    $week = [1 => 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']; //Авто индексация
    echo $week[3], '</br>';
    $week[] = 'Вс';//Автодобавление
    echo $week[7], '</br>';
    echo count($week), '</br>';
    sort($week); //asort По убыванию
    echo var_export($week), '</br>';
