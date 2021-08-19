/*
 Игра"Жизнь"
 13.08.2021
 Матвей Покидько
*/
var canvas=document.getElementById("canvas"), ctx=canvas.getContext("2d"),
    btnPlay = document.getElementById("play"), btnClear=document.getElementById('clear'),
    speed = 200, size = 16, width, height, col, row, game = false, focus = false;

// Размеры окна
onResize();
window.addEventListener("resize", onResize);
function onResize(){
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
    row = Math.ceil(height / size);
    col = Math.ceil(width / size);
}

//Старт Пауза
btnPlay.onclick = () => {
    focus = true;
    game = !game;
    if (game)
        btnPlay.innerHTML = 'Пауза';
    else 
        btnPlay.innerHTML = 'Старт';
}

//Рестарт
btnClear.onclick = ()=>{
    focus = true;
    arr = arrNew();
    game = false;
}

//Отслежевание курсора при нажатие клика
onclick = (e)=>{
    if (!focus){
        let x = Math.floor(e.clientX / size);
        let y = Math.floor(e.clientY / size);
        arr[y][x] = !arr[y][x];
    }
    focus = false;
}   

// Цикл аннимации
setInterval(() => {
    // Заливка фона
    ctx.fillStyle='#272727';
    ctx.fillRect(0, 0, width, height);
    // Сетка
    drawLins();
    //Обнавление
    if (game)
        update();
    // Отрисовка
    drawCell();
}, speed);

//Масив клеток
arr = arrNew();
function arrNew(){
    let arr = [];
    for(let i=0; i<row; i++){
        arr[i] = [];
        for(let j=0; j<col; j++)
            arr[i][j] = false;
    }
    return arr;
}

function drawLins(){
    ctx.lineWidth = 0.25;
    ctx.strokeStyle='black';
    //Горезантальные линии
    ctx.beginPath();
    for(let i=0; i<height; i+=size){
        ctx.moveTo(0, i);
        ctx.lineTo(width, i);
    }
    ctx.stroke();
    ctx.closePath();

    //Вертикальные линии
    ctx.beginPath();
    for(let i=0; i<width; i+=size){
        ctx.moveTo(i, 0);
        ctx.lineTo(i, height);
    }
    ctx.stroke();
    ctx.closePath();
}

function update(){
    let buffer = copyArr(arr);
    for(let i=1; i<row-1; i++)      
        for(let j=1; j<col-1; j++){
            // Подсчёт соседий
            let count = arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1] + arr[i][j-1]+arr[i][j+1] + arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1];
            
            if (!arr[i][j] && count == 3)
                buffer[i][j] = true;
            else if (arr[i][j] == true && (count == 3 || count == 2))
                buffer[i][j] = true;
            else
                buffer[i][j] = false;
        }
    arr = copyArr(buffer);
}

function copyArr(arr){
    let buffer = [];
    for(let i=0; i<row; i++){
        buffer[i] = [];
        for(let j=0; j<col; j++)
            buffer[i][j] = arr[i][j];
    }
    return buffer;
}

function drawCell(){
    ctx.fillStyle = 'white';

    for(let i=0; i<row; i++)
        for(let j=0; j<col; j++){
            if (arr[i][j]){
                ctx.beginPath();
                ctx.arc(j * size + size / 2, i * size + size / 2, size / 2 - 2, 0, 2*Math.PI);
                ctx.fill();
                ctx.closePath();
            }
        }
}