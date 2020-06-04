namespace KNB
{
    partial class Победы
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.Button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.labelplayer = new System.Windows.Forms.Label();
            this.labelGame = new System.Windows.Forms.Label();
            this.labelWin = new System.Windows.Forms.Label();
            this.labelLose = new System.Windows.Forms.Label();
            this.labelDraw = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Button1
            // 
            this.Button1.BackColor = System.Drawing.SystemColors.Desktop;
            this.Button1.Location = new System.Drawing.Point(306, 254);
            this.Button1.Name = "Button1";
            this.Button1.Size = new System.Drawing.Size(188, 149);
            this.Button1.TabIndex = 0;
            this.Button1.Text = "Stone";
            this.Button1.UseVisualStyleBackColor = false;
            this.Button1.Click += new System.EventHandler(this.Button1_Click);
            // 
            // button2
            // 
            this.button2.BackColor = System.Drawing.SystemColors.Desktop;
            this.button2.Location = new System.Drawing.Point(574, 254);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(200, 149);
            this.button2.TabIndex = 1;
            this.button2.Text = "Scissors";
            this.button2.UseVisualStyleBackColor = false;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.BackColor = System.Drawing.SystemColors.Desktop;
            this.button3.Location = new System.Drawing.Point(33, 254);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(200, 149);
            this.button3.TabIndex = 2;
            this.button3.Text = "Paper";
            this.button3.UseVisualStyleBackColor = false;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // labelplayer
            // 
            this.labelplayer.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.labelplayer.Font = new System.Drawing.Font("Arial Narrow", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelplayer.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.labelplayer.Location = new System.Drawing.Point(27, 118);
            this.labelplayer.Name = "labelplayer";
            this.labelplayer.Size = new System.Drawing.Size(366, 57);
            this.labelplayer.TabIndex = 3;
            // 
            // labelGame
            // 
            this.labelGame.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.labelGame.Font = new System.Drawing.Font("Arial Narrow", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelGame.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.labelGame.Location = new System.Drawing.Point(638, 118);
            this.labelGame.Name = "labelGame";
            this.labelGame.Size = new System.Drawing.Size(200, 56);
            this.labelGame.TabIndex = 50;
            // 
            // labelWin
            // 
            this.labelWin.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.labelWin.Font = new System.Drawing.Font("Arial Narrow", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelWin.ForeColor = System.Drawing.Color.Yellow;
            this.labelWin.Location = new System.Drawing.Point(13, 9);
            this.labelWin.Name = "labelWin";
            this.labelWin.Size = new System.Drawing.Size(113, 35);
            this.labelWin.TabIndex = 51;
            this.labelWin.Text = "Победы:";
            // 
            // labelLose
            // 
            this.labelLose.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.labelLose.Font = new System.Drawing.Font("Arial Narrow", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelLose.ForeColor = System.Drawing.Color.Red;
            this.labelLose.Location = new System.Drawing.Point(334, 9);
            this.labelLose.Name = "labelLose";
            this.labelLose.Size = new System.Drawing.Size(150, 35);
            this.labelLose.TabIndex = 52;
            this.labelLose.Text = "Поражения:";
            // 
            // labelDraw
            // 
            this.labelDraw.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.labelDraw.Font = new System.Drawing.Font("Arial Narrow", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelDraw.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.labelDraw.Location = new System.Drawing.Point(674, 9);
            this.labelDraw.Name = "labelDraw";
            this.labelDraw.Size = new System.Drawing.Size(100, 35);
            this.labelDraw.TabIndex = 53;
            this.labelDraw.Text = "Ничьи:";
            // 
            // Победы
            // 
            this.AccessibleDescription = "";
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.labelDraw);
            this.Controls.Add(this.labelLose);
            this.Controls.Add(this.labelWin);
            this.Controls.Add(this.labelGame);
            this.Controls.Add(this.labelplayer);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.Button1);
            this.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.Name = "Победы";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button Button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label labelplayer;
        private System.Windows.Forms.Label labelGame;
        private System.Windows.Forms.Label labelWin;
        private System.Windows.Forms.Label labelLose;
        private System.Windows.Forms.Label labelDraw;
    }
}

