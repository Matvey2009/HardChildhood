using System.Diagnostics;
using System.Windows.Forms;

namespace KNB
{
    public partial class Победы : Form
    {
        KNB knb = new KNB();

        public Победы()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, System.EventArgs e)
        {
            labelplayer.Text = "Вы выбрали Камень";
            knb.StepGame(0);
            StepGame();
        }

        private void button2_Click(object sender, System.EventArgs e)
        {
            labelplayer.Text = "Вы выбрали Ножницы";
            knb.StepGame(1);
            StepGame();
        }

        private void button3_Click(object sender, System.EventArgs e)
        {
            labelplayer.Text = "Вы выбрали Бумагу";
            knb.StepGame(2);
            StepGame();
        }
        private void StepGame()
        {
            labelDraw.Text = knb.draw.ToString();
            labelLose.Text = knb.lose.ToString();
            labelWin.Text = knb.win.ToString();

            labelGame.Text = knb.result;
        }
    }
}
