using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace Aquarium
{
    public partial class Form1 : Form
    {
        public static Size window;
        public Graphics g;
        private Fishes fishes;

        //Окно приложения
        public Form1()
        {
            window = ClientSize;
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                     ControlStyles.AllPaintingInWmPaint |
                     ControlStyles.UserPaint, true);
            UpdateStyles();
        }

        //Таймер
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            fishes.DrawListFish(g);
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = !timer1.Enabled;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            fishes = new Fishes();
        }
    }
}