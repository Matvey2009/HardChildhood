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

        // Запуск окна
        public Form1()
        {
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);
            UpdateStyles();


        }

        // Отрисовка окна
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics ctx = e.Graphics;
            ctx.SmoothingMode = SmoothingMode.AntiAlias;

            int score = 0;
            score++;
            label1.Text = score.ToString();
            
                var position = this.PointToClient(Cursor.Position);

            point.X = 600 + random.Next(-4, 4) * 100;
            point.Y = 600 + random.Next(-3, 3) * 100;

            ctx.DrawEllipse(new Pen(Color.Black, 2), point.X, point.Y, 100, 100);
            ctx.DrawImage(target, position.X-50, position.Y-50, 100, 100);        
        }

        // Обънавление окна 
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }
    }
}
