<?php //Проект казино
    require_once 'header.php';
?>

<p>Casino</p>

<!--Счётчик кликов js-->
<button type='button' class='button' onclick='js_click()'>
    <output id='js_count'>JS-счётчик: 0</output>
</button>
<br/><hr/><br/>
    
<!--Счётчик кликов php-->
<?php
    $count = 0;
    if (isset($_POST["php_count"]))
        $count = preg_replace('/[^0-9]/', '', $_POST["php_count"])+1;
?>
<form method="post">
    <input type="submit" class="button" name="php_count" value='<?='php-счётчик: '.$count ?>' >
</form>
<br/><hr/><br/>

<!--Рандом на сервере-->
<?php
    $arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    $random = '?';
    if (isset($_POST["php_random"])) {
        $random = rand(0, 36);
        $arr[$random] += 1;
    }
    foreach ($arr as $i) {
        echo $i, ' ';
    }
?>
<form method="post">
    <input type="submit" class="button" name="php_random" value='<?='php-рандом: '.$random ?>' >
</form>
<br/><hr/><br/>

<?php
    var_export($GLOBALS);
    require_once 'footer.php';
?>