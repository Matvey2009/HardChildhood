<?php
    namespace lessons;

    define('SIZE', 1920); //Константа

    class Unit {
        const PI = 3.14;
        public $name;
        private $life;
        protected $pos;
        
        public function __construct($name, $life = 100) {
            $this -> name = $name;
            $this -> life = $life;
            $this -> pos = 200;
        }

        public function get_life($pass) {
            echo self:: PI, '</br>';
            if ($pass == '12345')
                return $this -> life;
            else
                return 0;
        }
    }

    echo Unit:: PI, '</br>';
    $unit = new Unit('Matvey', 200);
    echo $unit -> name, '</br>';
    #echo $unit -> life, '</br>'; <-- Ошибка доступа
    echo $unit -> get_life("12345");
    echo '</br>', '</br>';

    class Hero extends Unit {
        public static $color = 'black';
        public $armor = 100;

        public function __construct($name, $life){
            parent:: __construct($name, $life);
            $this -> armor = 1000;
        }

        public function get_pos(){
            echo parent:: PI; // sefl тоже работает
            return $this -> pos;
        }

        //Gettors and Sectors
        public function __get($name){
            return $this -> $name;
        }

        public function __set($name, $walue){
            $this -> $name = $walue;
            return $this -> $name;
        }
    }
    echo Hero:: $color, '</br>';
    $hero = new Hero('red', 512);
    echo $hero -> armor, '</br>';
    #echo $hero -> pos; //Ошибка доступа
    echo $hero -> get_pos(), '</br>';

    //Проверка объекта на принодлежности к класу
    echo 'instansoff hero - ', $hero instanceof Hero, '</br>';
    echo 'instansoff hero - ', $hero instanceof Unit, '</br>';
    echo 'instansoff hero - ', $unit instanceof Hero, '</br>';
    //Набор функций для вставки в класс
    trait Action {
        public function talk(){
            echo 'Я герой', '</br>';
        }
    }

    class SuperHero extends Unit {
        use Action;
    }
    
    $superhero = new SuperHero('Batman', 500);
    $superhero -> talk();