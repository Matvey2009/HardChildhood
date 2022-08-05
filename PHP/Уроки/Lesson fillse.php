<?php
    namespace filles;

    require 'Lesson функции.php'; //Подключить файл(Незаменимый файл)
    //include 'x.php'; //Подключить файл(Заменимый файл)
    //Одноразовые подключения
    require_once 'Lesson OOP.php';
    //

    //Автозакрузка файлов
    function auroloader() {
        $class = 0;
        echo "Подключение класса $class <br/>";
        include_once $class. '.php';
    }
    //spl_autoload_register("autoloader");
    //$x = new Xclass();


    echo '<h3>Импорт пространсвта имён</h3><br/>';
    #$hero = new Hero ("Test one", 50); Так нельзя
    $hero = new \lessons\Hero ("Test one", 50);     

    use \lessons\Hero; #Заранее подключить пространство имён
    $hero2 = new \lessons\Hero ("Bob", 30);
    echo $hero2 -> name, '<br/>';

    use \lessons\Hero as lh; #Тоже самое с псеводонимом
    $hero3 = new lh ("Key", 70);
    echo $hero3 -> name, '<br/>';
    #use \lessons\{Hero, Unit, SuperHero} as Sh; --- Пример как подключить множество классов с другово пространства имён

    use const \lessons\TEMP;
    echo TEMP, '<br/>';

    #use function \lessons\Имя функции;

    #Файловая система
    echo '<h3>Файловая система</h3><br/>';
    #die = exit = exit() = exit(0) - "Выход из скрипта", "Возмоэно с собщение об ошибки"
    $file = fopen('Text.txt', 'w') or die("Не удалос отрыть файл");
    # 'r': файл открывается только для чтения. Если файла не существует, возвращает false
    # 'r+': файл открывается только для чтения с возможностью записи. Если файла не существует, возвращает false
    # 'w': файл открывается для записи. Если такой файл уже существует, то он перезаписывается, если нет - то он создается
    # 'w+': файл открывается для записи с возможностью чтения. Если такой файл уже существует, то он перезаписывается, если нет - то он создается
    # 'a': файл открывается для записи. Если такой файл уже существует, то данные записываются в конец файла, а старые данные остаются. Если файл не существует, то он создается
    # 'a+': файл открывается для чтения и записи. Если файл уже существует, то данные дозаписываются в конец файла. Если файла нет, то он создается
    fwrite($file, "Просто текст\n");
    fwrite($file, "Ещё одна запись".PHP_EOL);
    fclose($file);

    # Чтения файла
    $file = fopen('Text.txt', 'r') or die("Не удалось отрыть файл");
    while (!feof($file)) {
        $str = htmlentities(fgets($file));
        echo $str, '<br/>';
    }
    fclose($file);
    echo '<br/>';

    # Чтения файла полность
    $str = htmlentities(file_get_contents('Text.txt'));
    echo 'Файл целеком', '<br/>';
    echo $str, '<br/>';

    #Создание папки
    if (mkdir("New folder"))
        echo "Каталог создан", '<br/>';
    else
        echo "Каталог не создан", '<br/>';

    #Определения местонахождения
    $path = getcwd();
    echo $path, '<br/>';
    
    #Копиравания файла
    if (copy("Text.txt", "Text2.txt"))
        echo "Файл скопирован", '<br/>';
    else
        echo "Ошибка", '<br/>';

    #Перемещение файла
    if (!rename("Text2.txt", "New folder/Text3.txt"))
        echo "Файл перемещен", '<br/>';
    else
        echo "Ошибка перемещения", '<br/>';

    #Перемещение файла
    if (!unlink("New folder/Text3.txt"))
        echo "Файл удалён", '<br/>';
    else
        echo "Ошибка удаления", '<br/>';
    
    #Создание папки
    if (rmdir("New folder"))
        echo "Каталог удалён", '<br/>';
    else
        echo "Каталог не удалён", '<br/>';

    #Открытие чтения и вывод содержимого папок
    $dir = getcwd();
    if (is_dir($dir)) {
        if ($temp = opendir($dir)) { #Открываем каталог
            while (($file = readdir($temp)) !== false) {#Считываем по 1 элементу
                if ($file == '.' || $file == '..')#Пропуск точек
                    continue;
                if (is_dir($file))
                    echo "Каталог: ", $file, '<br/>';
                else
                    echo "Файл: ", $file, '<br/>';

            }
            closedir($temp); #Закрытия каталога
        } 
    }