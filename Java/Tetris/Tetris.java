/* 27.10.2019
 * Matvey
 * Tetris
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.KeyListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.Random;

public class Tetris extends JPanel {

	//Переменные
	protected static int block = 30, speed = 400, test, color, look, line;
		private int form[][] = new int[4][2];
		public int ground[][][] = new int [20][10][1];
		public int forms[][][] = { // фигурка / блоки / x,y или r,g,b
		{{ 0,  0}, {-1,  0}, { 1,  0}, { 2,  0}, {0x00ffff}}, // I aqua
		{{ 0,  0}, { 1,  0}, { 0,  1}, { 1,  1}, {0xffff00}}, // O yellow
		{{ 0,  0}, {-1,  0}, { 1,  0}, { 0,  1}, {0xff00ff}}, // T purple
		{{ 0,  0}, { 0, -1}, {-1,  1}, { 0,  1}, {0xffa500}}, // L orange
		{{ 0,  0}, { 0, -1}, { 0,  1}, { 1,  1}, {0x0000ff}}, // J blue
		{{ 0,  0}, { 1,  0}, {-1,  1}, { 0,  1}, {0x00ff00}}, // S green
		{{ 0,  0}, {-1,  0}, { 0,  1}, { 1,  1}, {0xff0000}}, // Z red
	};

	Random random = new Random();
	private static Color colorBlock;
	private static Image image = new ImageIcon("fon.png").getImage();

	public static void main(String[] args) {

		//Окно Приложения
		JFrame jFrame = new JFrame ("Tetris");
		jFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setSize (block*15+17, block*20+40);
		jFrame.setResizable(false);
		jFrame.setLocationRelativeTo(null);
		jFrame.setVisible(true);
		Tetris tetris = new Tetris();
		jFrame.add(tetris);
		tetris.newBlock();

		//Проверка
		jFrame.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent event) {
				tetris.repaint();
				switch(event.getKeyCode()) {
					case 37: tetris.move(-1); break; //Лево x--
					case 38: tetris.rotate(); break; //Поворот
					case 39: tetris.move(+1); break; //Право x++
					case 40: speed = 40; break; //низ
				}
			}
		});

		while (true) {
			tetris.game();
			tetris.repaint();
			try {
				Thread.sleep(speed);
			} catch (Exception e) {}
		}
	}
		
	// Логический Блок
	private void game() {
		test = 0;
		for (int i = 0; i < 4; i++) {
				if (form[i][1]+1 < 20 && ground[form[i][1]+1][form[i][0]][0] == 0) test++;
			}
		if (test == 4)
			for (int i = 0; i < 4; i++) form[i][1]++;
		else {
			for (int i = 0; i < 4; i++) {
				ground[form[i][1]][form[i][0]][0] = color;
			}
			clear();
			newBlock();
		}
	}
	
	//Случайность
	private void newBlock(){
		color = forms[look][4][0];
		colorBlock = new Color(color);
		for (int i = 0; i < 4; i++){
			form[i][0] = forms[look][i][0]+3;
			form[i][1] = forms[look][i][1];
		}
		speed = 300;
		look = random.nextInt(7);
	}
	
	//Движени фигуры 2
	private void move(int move) {
		
		test = 0;

			for (int i = 0; i < 4; i++) {
				if (form[i][0]+move < 10 && form[i][0]+move >= 0 && ground[form[i][1]][form[i][0]+move][0] == 0) test++;	
			}
		if (test == 4)
			for (int i = 0; i < 4; i++)
				form[i][0] += move;
	
	}

	//Поворот фигуры
	private void rotate() {
		int temp;
		
		for (int i = 0; i < 4; i++) {
			temp = form[i][0];
			form[i][0] = -form[i][1]+form[0][1]+form[0][0];
			form[i][1] = temp-form[0][0]+form[0][1];
		};
	}
	
	//Очистка ряда
	private void clear() {
		int temp;
		for (int i = 0; i < 20; i++) {
			temp = 0;
			for (int j = 0; j < 10; j++)
				if (ground[i][j][0] > 0)
					temp++;
			if (temp >= 10) {
				line++;
				for (int iClear = i; iClear > 0; iClear--)
					for (int j = 0; j < 10; j++)
						if (iClear > 0)
							ground[iClear][j][0] = ground[iClear-1][j][0];
			}
		}
	}
	
	 //Графика
	public void paint(Graphics ctx) {

		//Чёрный
		ctx.setColor(Color.black);
		ctx.fillRect(10*block, 0, 5*block, 20*block);
		
		//Просмотр
		for(int i = 0; i < 4; i++){
			ctx.setColor(new Color(forms[look][4][0]));
			ctx.fillRect(block*forms[look][i][0]+11*block, block*forms[look][i][1]+3*block, block-1, block-1);
		}
		
		//Панель
		ctx.setFont(new Font("Corier New", Font.BOLD, 20));
		ctx.setColor(Color.red);
		ctx.drawString(("Speed: " + speed), 11*block, 200);
		ctx.drawString(("Line: " + line), 11*block, 240);

		//Днище
		for(int i = 0; i < 20; i++){
			for(int j = 0; j < 10; j++){
				ctx.setColor(new Color(ground[i][j][0]));                                                    
				ctx.fillRect(block*j, block*i, block, block);
			}
		}

		//fon
		ctx.drawImage(image, 20, 150, null);

		//фигуры
		for(int i = 0; i < 4; i++){
			ctx.setColor(colorBlock);
			ctx.fillRect(form[i][0]*block, form[i][1]*block, block, block);
		}

		//Сетка
		ctx.setColor(Color.gray);
		for (int i = 0; i <= 10; i++) ctx.drawLine(block*i, 0, block*i, block*20);
 		for (int i = 0; i <= 20; i++) ctx.drawLine(0, block*i, block*10, block*i);
	}
}