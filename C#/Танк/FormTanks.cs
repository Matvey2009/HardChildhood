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
        public FormTanks()
        {
            InitializeComponent();
        }
        int x;
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Click(object sender, EventArgs e)
        {
            if (timer.Enabled == true) timer.Enabled = false;
            else timer.Enabled = true;
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            label1.Text = x.ToString();
            x++;
            Refresh();
        }
    }
}
