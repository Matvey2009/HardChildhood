<?php
    $x = 125 <=> 6; //Возрощает -1 или 0 или 1 взависимости от ведёных значений
    echo $x, '<br/>';

    if(5 > 3)
        echo "5 больше 3", '<br/>';

    if (1 === true)
        echo "'===' Позначению и по типу данных", '<br/>';
    else
        echo "'!===' Не позначению и по не типу данных", '<br/>';

    if (5 > 0 and 5 != 0 || true) {
        echo "Привет", '<br/>';
        echo "Всем", '<br/>';
    } else if (5 < 3 && (1 > 2 or 5 > 3))
        echo "Я Матвей", '<br/>';
    else
        echo "Хорошо", '<br/>';
    
    // Другой синтаксис(для скриптов)
    if (20 > 10):
        echo 20 > 10;
    elseif (20 > 0):
        echo "Да 20 больше 0", '<br/>';
    else:
        echo 'Шкаф', '<br/>';
    endif;

    echo '<br/>';

    // Тернальный синтаксис()
    echo 5 > 2 ? "Да" : "Нет", '<br/>';

    $x = 7;
    switch($x){
        case 0:
            echo 'Да';
        break;
        case 1:
            echo 'ДаДа';
        break;
        case 5:
            echo 'ДаДаДа';
        break;
        default:
            echo 'Всё остальное', '<br/>';
        break;
    }

    match($x) {
        0 => print "Да match $x = 0",
        1 => print "Да match $x = 1",
        7 => print "Да match $x = 7",
        default => print "Всё остальное"
    };
    echo '<br/>';
