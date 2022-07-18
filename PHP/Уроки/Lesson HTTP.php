<?php
    //h3 Протокал Http
    echo "<h3>Протокал HTTP</h3>";
    echo "<h3>GET Запросы</h3>";

    //http://localhost:3000/Уроки/Lesson%20HTTP.php?x=12345
    if (isset($_GET['x'])){
        echo "Передача значения", '<br/>';
        $x = $_GET['x'];
        echo 'Принято из строки браузера', $x, '<br/>';
    }

    //http://localhost:3000/Уроки/Lesson%20HTTP.php?x=Hello&y=wolrd
    if (isset($_GET['x']) && isset($_GET['y'])){
        echo "Передача значений", '<br/>';
        $x = $_GET['x'];
        $y = $_GET['y'];
        echo 'Принято из строки браузера', $x, $y, '<br/>';
    }

    echo "Get запрос из клика по ссылке", '<br/>';
    echo '<a href = "http://localhost:3000/Уроки/Lesson%20HTTP.php?x=Нажата&y=Ссылка">Ссылка с вложеном get запросом</a><br/><br/>';

    echo "Get Запрос по нажматию пустой кнопки";
    ?> <form>
        <a href = 'http://localhost:3000/Уроки/Lesson%20HTTP.php?x=Нажата&y=кнопка'>
            <input type="button" value="Кнопака с GET запросом">
        </a>
    </form><br/><br/> <?php

    echo "get запрос с полем для ввода";
    ?>
        <form method="GET" action="http://localhost:3000/Уроки/Lesson%20HTTP.php">
            Введите ваше имя: <input type="text" name="y">
            <input type="submit" name="x" value="Привет"/>
        </form>
    <?php
    //Вывод данных
    echo "<h5>Данные масива _GET</h5>";
    var_export($_GET);
    echo '<br/><br/>';

    //gt
    echo "<h5>Данные масива Все данные из GLOBALS</h5>";
    var_export($GLOBALS);
    echo '<br/><br/>';