Просто текст </br>
<h1>code html</h1></br>
<!--Комментарий html-->
<? print('Hello World') ?>
</br>

<?php
    /*
    Основы php
    */
    $x = 2;
    echo '<br/>';
    $x += 2.345; //Преобразует в флоат
    echo $x, '<br/>';
    print($x); //Выводит одно значение, с return: 1(True)
    //Можно выводить много значений
    echo '<br/>';
    print_r($x); //Выводит c типом данных для отладки
    echo '<br/>';
    var_dump($x);//Выводит форматируя строку    
    echo '<br/>';
    var_export($x);//Выводит в формате исполняемого кода
    echo '<br/>';
    echo 'Конкатонация $x' . "  Склейка строк - $x";//Одинаррные ковычки с переменными
    echo '<br/>';
    $x = 'кон';
    echo $x .= "котонация";
    echo '<br/>';
    $x = null; //Отсутсвие данных
    var_dump($x);//По другому null ну увидеть
    echo '<br/>';
    echo (int)123.456, '<br/>'; //Отынковка 
    //(bull) - True or False
    //(float), (doauble), (real)
    //(string)
    //(object) - Превращение в объект
    //(unset) - Превращает в null(Удаление из памяти)
    //(binary) - Бинарный код

    //Код html(код php(код html(Код JS)))
    echo('<script>console.log("from php whiz love")</script>');
    //Код html(Код JS)
    ?> <script>console.log("from php whiz love 2")</script> <?php
    echo '<br/>';

    $x = 5;
    $y = $x;
    echo 'X и Y = ', $x, " и ", $y, '<br/>';
    $x = 111;
    echo 'X и Y = ', $x, " и ", $y, '<br/>';
    echo 'Передача по ссылке', '<br/>';

    $x = 5;
    $y = &$x;
    echo 'X и Y = ', $x, " и ", $y, '<br/>';
    $x = 111;
    echo 'X и Y = ', $x, " и ", $y, '<br/>';
    echo '<br/>';

    $zzz = "Колдунство с переменной";
    $x = 'zzz'; //Это строка
    echo $x, '</br>';
    echo $$x, '</br>';
    echo '</br>';

    $a = 'Hello';
    $$a = ' World';
    echo $a, $$a, '</br>';
    echo "$a ${$a}", '</br>';
    echo "$a $Hello", '</br>';
    echo '</br>';

    echo 1 + 2, " ";
    echo 3 - 4, " ";
    echo 5 * 6, " ";
    echo 7 / 8, " ";
    echo 10%25, " ";
    echo '</br>';
    echo abs(-123), '</br>';
    echo min(4324, 54654), '</br>';
    echo max(80, 32, 71), '</br>';
    echo pow(9, 9), '</br>';
    echo sqrt(16), '</br>';
    echo rand(10, 30), '</br>';
    echo Mt_rand(1, 100), '</br>';// Более коректный алгоритм рандома
    echo 'floor: ', floor(5.9), '</br>'; // Округление в меньш
    echo 'ceil: ', ceil(5.1), '</br>'; // Округление в большы
    echo 'round: ', round(4.4999999999), '</br>'; // Округление в меньш
    echo 'pi: ', M_PI, '</br>'; // Округление в меньш
    echo 'pi: ', M_E, '</br>'; // Округление в меньш
    echo '</br>';

    $x = 10;
    $y = $x++;
    echo 'X++: ', $x, " ", $y, '</br>';

    $x = 10;
    $y = ++$x;
    echo '++X: ', $x, " ", $y, '</br>';

    $x = 10;
    $y = $x--;
    echo 'X--: ', $x, " ", $y, '</br>';

    $x = 10;
    $y = --$x;
    echo '--X: ', $x, " ", $y, '</br>';
    
    echo date('d.m.Y H:i'), '</br>';

    echo 2 + '2', '</br>';
    echo '2' + '2', '</br>';
    echo 2 + true, '</br>';
    echo '2' * false, '</br>';
    $x = false;
    echo 'empty: ', empty($x), '</br>';
    echo 'isset: ', isset($x), '</br>';
    $x;
    echo 'empty: ', empty($x), '</br>';
    echo 'isset: ', isset($x), '</br>';
    $x = 1;
    echo 'empty: ', empty($x), '</br>';
    echo 'isset: ', isset($x), '</br>';
    $x = 0;
    echo 'empty: ', empty($x), '</br>';
    echo 'isset: ', isset($x), '</br>';
    $x = null;
    echo 'empty: ', empty($x), '</br>';
    echo 'isset: ', isset($x), '</br>';

    echo strlen('Hello'), '</br>';
    echo trim('                  Hello                  World                  '), '</br>';
    echo strtoupper('Hello'), '</br>';
    echo strtolower('Hello'), '</br>';
    echo "Хеширование-hello ", md5('hello'), '</br>';
    echo "Хеширование-0 ", md5(0), '</br>';
    echo "Хеширование-Много текста ", md5(' mnbghjvyu mhgyujhm ncxdkfvuytfvtgyufvyukfku mgdfgdfgdsgdsfgesr'), '</br>';

    phpinfo();