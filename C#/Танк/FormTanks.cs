﻿using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace Танк
{
    public partial class FormTanks : Form
    {
        private Game game;
        public static Size window;
        public Graphics g;
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
            window = ClientSize;
            game = new Game();
            game.StartGame();
        }

        //Обновление окна
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            cursor = PointToClient(Cursor.Position);
            game.StepGame(g);
        }

        //Таймер
        private void timer_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Старт-Стоп
        private void Form1_Click(object sender, EventArgs e)
        {
            timer.Enabled = !timer.Enabled;
        }

        // Двойной клик
        private void FormTanks_DoubleClick(object sender, EventArgs e)
        {
            if (FormBorderStyle == FormBorderStyle.Sizable)
                FormBorderStyle = FormBorderStyle.None;
            else FormBorderStyle = FormBorderStyle.Sizable;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            window = ClientSize;
            game = new Game();
            game.StartGame();
            Refresh();
        }
    }
}
