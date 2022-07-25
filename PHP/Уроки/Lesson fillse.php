<?php
    namespace filles;

    require 'Lesson функции.php'; //Подключить файл(Незаменимый файл)
    //include 'x.php'; //Подключить файл(Заменимый файл)
    //Одноразовые подключения
    require_once 'Lesson Цикл.php';
    //

    //Автозакрузка файлов
    function auroloader() {
        $class = 0;
        echo "Подключение класса $class <br/>";
        include_once $class. '.php';
    }
    //spl_autoload_register("autoloader");
    //$x = new Xclass();