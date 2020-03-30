using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Танк
{
    public partial class FormTanks : Form
    {
        Graphics g;
        Bitmap bitmap = new Bitmap(Properties.Resources.Танкpng);
        Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

        public FormTanks()
        {
            InitializeComponent();
            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);
            UpdateStyles();
        }
        int x;
        private void Form1_Load(object sender, EventArgs e)
        {
            ///////////////////////////////////
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            if (timer.Enabled == true) timer.Enabled = false;
            else timer.Enabled = true;
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            Refresh();
        }
        Point position = new Point(0, 600);
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            label1.Text = x.ToString();
            x++;
            g = e.Graphics;

            position.X = position.X + 1;
            position.Y = position.Y - 1;

            //Танк 1
            g.DrawImage(bitmap, position.X, position.Y, body, GraphicsUnit.Pixel);
            g.DrawImage(bitmap, position.X, position.Y, tower, GraphicsUnit.Pixel);

            //Танк 2
            g.DrawImage(bitmap, position.X - 128, position.Y + 128, body, GraphicsUnit.Pixel);
            g.DrawImage(bitmap, position.X - 128, position.Y + 128, tower, GraphicsUnit.Pixel);
        }
    }
}
