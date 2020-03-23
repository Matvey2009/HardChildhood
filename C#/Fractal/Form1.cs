using System;
using System.Drawing;
using System.Windows.Forms;

namespace Fractal
{
    public partial class Form1 : Form
    {
        //Переменые
        private Bitmap bitmap;
        private Point point;
        private Point[] angle;
        private Random random;
        private int number, rand;

        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }
}
