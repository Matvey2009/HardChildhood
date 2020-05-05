using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Танк
{
    public partial class FormTanks : Form
    {
        public Graphics g;
        private ListUnit listUnit;
        private Point cursor;
        Shot shot;

        //Окно
        public FormTanks()
        {
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);
            UpdateStyles();
        }

        //Загруска окна
        private void Form1_Load(object sender, EventArgs e)
        {
            listUnit = new ListUnit();
            listUnit.CreateListUnit();
            SW();
            //Sound();

            shot = new Shot();
            shot.position = new PointF(50, 50);
            shot.target = new PointF(1000, 600);
            shot.speed = 20;
        }

        //Обновление окна
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            cursor = PointToClient(Cursor.Position);
            listUnit.DriweListUnit(g, cursor);

            shot.DrawShot(g);
        }

        //Таймер
        private void timer_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Старт-Стоп
        private void Form1_Click(object sender, EventArgs e)
        {
            if (timer.Enabled == true) timer.Enabled = false;
            else timer.Enabled = true;
        }
        //Звук заставки
        async private void SW()
        {
            await Task.Run(() =>
            {
                Console.Beep(440, 500);
                Console.Beep(440, 500);
                Console.Beep(440, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 1000);
                Console.Beep(659, 500);
                Console.Beep(659, 500);
                Console.Beep(659, 500);
                Console.Beep(698, 350);
                Console.Beep(523, 150);
                Console.Beep(415, 500);
                Console.Beep(349, 350);
                Console.Beep(523, 150);
                Console.Beep(440, 1000);
            });
        }
         private void Sound()
        {
            //261
            //293
            //329
            //349
            //392
            //440
            //493
            Console.Beep(261, 400);
            Console.Beep(293, 400);
            Console.Beep(440, 400);
            Console.Beep(293, 400);
            Console.Beep(493, 400);
            Console.Beep(440, 400);
            Console.Beep(349, 400);
            Console.Beep(293, 400);
            Console.Beep(349, 400);
            Console.Beep(349, 400);
            Console.Beep(493, 400);
            Console.Beep(440, 400);
            Console.Beep(493, 400);
        }
    }
}
