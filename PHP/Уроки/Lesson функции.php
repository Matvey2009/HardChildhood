<?php
    function funk(){
        echo "Hello word", '<br/><br/>';        
    }
    funk();
    
    function funk2($x){
        global $z;
        $z = 123;
        echo $x, '<br/><br/>';
    }
    funk2("Я человек");
    echo $z, '<br/>';

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
    print(funk4())  ;
    
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

    //Импорт внешних данных
    $y = "Строка";
    $f2 = function() use($y) {
        echo $y, '</br>';
    };
    $f2();
    

    $x = fn() => 7 + 8;
    echo '</br>', $x();

    #Генератор YELD
    echo '<br/><p>Генератор YELD</p>';
    function funk6(){
        yield 1;
        yield 2;
        yield from[3, 4];
        yield from new ArrayIterator([5, 6]);
        yield from funk7();
        yield 9;
        yield 10;
    }
    function funk7(){
        yield 7;
        yield from funk8();
    }
    function funk8(){
        yield 8;
    }
    foreach(funk6() as $x){
        echo "$x "; 
    }
    #Вызов