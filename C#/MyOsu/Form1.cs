using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyOsu
{
    public partial class Form1 : Form
    {
        // Переменные обьекты
        private Bitmap target = Resource1.kurs;
        private Point point = Point.Empty;
        private Random random = new Random();
        int score = 0;

        // Запуск окна
        public Form1()
        {
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);
            UpdateStyles();

            randomTarget();

        }

        // Отрисовка окна
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics ctx = e.Graphics;
            ctx.SmoothingMode = SmoothingMode.AntiAlias;

            
            label1.Text = score.ToString();
            
                Point position = this.PointToClient(Cursor.Position);

           

            Rectangle cursorPosition = new Rectangle(position.X - 50, position.Y - 50, 100, 100);
            Rectangle targetPosition = new Rectangle(point.X, point.Y, 100, 100);

            ctx.DrawEllipse(new Pen(Color.Black, 2), targetPosition);
            ctx.DrawImage(target, cursorPosition);    
        }

        // Обънавление окна 
        private void timer1_Tick(object sender, EventArgs e)
        {
            score++;
            Refresh();
        }
        //Перемещение Круга
        private void randomTarget()
        {
            point.X = 600 + random.Next(-4, 4) * 100;
            point.Y = 600 + random.Next(-3, 3) * 100;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            randomTarget();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            randomTarget();
        }
    }
}
