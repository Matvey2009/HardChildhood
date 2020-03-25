using System;
using System.Drawing;
using System.Windows.Forms;

namespace Fractal
{
    public partial class fractal : Form
    {
        //Переменые\\
        private Bitmap bitmap;
        private Point point;
        private Point[] angle;
        private Random random;
        private int number, rand;
        private byte count = 5;
        public fractal()
            //Кординаты точек
        {
            InitializeComponent();
            bitmap = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            random = new Random();
            angle = new Point[count];
            angle[0] = new Point(400, 10);
            angle[1] = new Point(790, 790);
            angle[2] = new Point(10, 790);
            angle[3] = new Point(10, 790);
            angle[4] = new Point(50, 300);

            for (byte i = 0; i < count; i++)
                bitmap.SetPixel(angle[i].X, angle[i].Y, Color.Red);
            pictureBox1.Image = bitmap;
        }
        //Запуск\\
        private void pictureBox1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            point = PointToClient(Cursor.Position);
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            for (long i = 0; i < 500; i++)
            { 
                number++;
                rand = random.Next(count);
                point.X = (point.X + angle[rand].X) / 2;
                point.Y = (point.Y + angle[rand].Y) / 2;
                bitmap.SetPixel(point.X, point.Y, Color.Black);
            }
            label1.Text = number.ToString();
            pictureBox1.Image = bitmap;
        }
    }
}

