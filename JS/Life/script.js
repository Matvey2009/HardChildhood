/*
 Игра"Жизнь"
 13.08.2021
 Матвей Покидько
*/
var canvas=document.getElementById("canvas"), ctx=canvas.getContext("2d"),
    speed = 200, size = 32, width, height, col, row;

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

// Цикл аннимации
setInterval(() => {
    // Заливка фона
    ctx.fillStyle='green';
    ctx.fillRect(0, 0, width, height);
    // Сетка
    drawLins();
    //Обнавление
    uppdate();
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
            arr[i][j] = true;
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

function uppdate(){
    for(let i=0; i<row; i++)
        for(let j=0; j<col; j++){
            //arr[i][j] =! arr[i][j];
        }
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