using System;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Media;
using System.Windows.Forms;

namespace MyOsu
{
    public partial class Form1 : Form
    {
        // Переменные обьекты
        private Bitmap target = Resource1.kurs;
        private Point point = Point.Empty;
        private Random random = new Random();
        private Pen pen = new Pen(Color.Black, 2);
        private Stopwatch stopwatch = new Stopwatch();
        private SoundPlayer soundPlayer = new SoundPlayer(Resource1.click);
        int score = 0, scoreAll, time, step, gipotinoza;

        // Запуск окна
        public Form1()
        {
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);
            UpdateStyles();
            Cursor.Hide();
            randomTarget();
            stopwatch.Start();
        }

        // Отрисовка окна
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics ctx = e.Graphics;
            ctx.SmoothingMode = SmoothingMode.AntiAlias;
            
                Point position = this.PointToClient(Cursor.Position);

            Rectangle cursorPosition = new Rectangle(position.X - 50, position.Y - 50, 100, 100);
            Rectangle targetPosition = new Rectangle(point.X, point.Y, 100, 100);

            ctx.DrawEllipse(pen, targetPosition);
            ctx.DrawImage(target, cursorPosition);

            int catetX = cursorPosition.X - targetPosition.X;
            int catetY = cursorPosition.Y - targetPosition.Y;
            gipotinoza = (int) Math.Sqrt(catetX * catetX + catetY * catetY);
        }

        // Обънавление окна 
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Перемещение Круга
        private void randomTarget()
        {
            Point position = point;
            point.X = Width / 2 + random.Next(-4, 4) * 100;
            point.Y = Height / 2 + random.Next(-3, 3) * 100;
            if (position == point) randomTarget();
            
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            StepGame();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            StepGame();
        }

        //Ход игры
        private void StepGame()
        {
            time = (int)stopwatch.Elapsed.TotalMilliseconds;
            step++;
            soundPlayer.Play();

            //Инфа
            score = 36000 / time + 600 / gipotinoza;
            scoreAll += score;
            label1.Text = ("Очки: " + score.ToString());
            label2.Text = ("Таймер: " + time.ToString());
            label3.Text = ("точность"+ gipotinoza.ToString());
            label4.Text = ("step: " + step.ToString());
            label5.Text = ("Общие очки" + scoreAll.ToString());
            randomTarget();
            stopwatch.Restart();
        }
    }
}
