<?php
    function funk(){
        echo "Hello word", '<br/><br/>';        
    }
    funk();
    
    function funk2($x){
        echo $x, '<br/><br/>';        
    }
    funk2("Я человек");

    function funk3($x){
        return $x * 2;
        echo 'T', '<br/><br/>';
    }
    print(funk3(12));
    echo '<br/>';

    function funk4($x = 15){
        return $x * 2;
    }
    print(funk4(32));
    echo '<br/>';
    print(funk4());
    
    function funk5(string $x){
        var_dump($x);
    }
    echo '<br/>';
    print(funk5(12.345));

    //Анонимные функции
    $f = function($x){
        echo '</br>', $x;
    };
    echo $f("Переменная = анонимная функция");

    $x = fn() => 7 + 8;
    echo '</br>', $x();