<?php
    //h3 Протокал Http
    echo "<h3>Протокал HTTP</h3>";
    echo "<h3>GET Запросы</h3>";

    http://localhost:3000/Уроки/Lesson%20HTTP.php?TEST
    $x = "TEST";
    if (isset($_GET['x'])){
        $x = $_GET['x'];
        echo 'Принято из строки браузера', $x, '<br/>';
    }
    var_export($_GET);