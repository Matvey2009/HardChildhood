using System;
using System.Drawing;
using System.Windows.Forms;

namespace Танк
{
    public partial class FormTanks : Form
    {
        Graphics g;
        ListTant listTant, listCar;
        private Point cursor;

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
            listTant = new ListTant();
            listTant.CreateListTant();

            listCar = new ListTant();
            listCar.CreateListCar();
        }

        //Обновление окна
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            cursor = PointToClient(Cursor.Position);
            listTant.DriweListTant(g, cursor);
            listCar.DriweListCar(g, cursor);
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
    }
}
