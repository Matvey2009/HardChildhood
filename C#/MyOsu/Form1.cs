using System;
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
        private SoundPlayer soundPlayer = new SoundPlayer(Resource1.click);
        int score = 0;

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
            int gipotinoza = (int) Math.Sqrt(catetX * catetX + catetY * catetY);

            label1.Text = gipotinoza.ToString();
        }

        // Обънавление окна 
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Перемещение Круга
        private void randomTarget()
        {
            point.X = Width / 2 + random.Next(-4, 4) * 100;
            point.Y = Height / 2 + random.Next(-3, 3) * 100;
            
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
            score++;
            soundPlayer.Play();
            randomTarget();
        }
    }
}
