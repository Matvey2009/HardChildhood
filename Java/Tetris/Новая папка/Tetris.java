/* 27.10.2019
 * Matvey
 * Tetris
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.Random;

public class Tetris extends JPanel {

	//Переменные
	protected static int block = 30, x = 0, y = 0, randForm;
		public int form[][][] = { // фигурка / блоки / x,y или r,g,b
		{{1, 2}, {2, 2}, {0, 1}, {1, 1}, {255, 0, 0}}, // -/_ red
		{{1, 2}, {2, 2}, {1, 1}, {1, 0}, {255, 165, 0}}, // 1_ orange
		{{1, 2}, {2, 2}, {1, 1}, {2, 1}, {255, 255, 0}}, // O yellow
		{{0, 2}, {1, 2}, {1, 1}, {2, 1}, {0, 255, 0}}, // S green
		{{0, 2}, {1, 2}, {2, 2}, {3, 2}, {0, 255, 255}}, // I aqua
		{{1, 2}, {2, 2}, {2, 1}, {2, 0}, {0, 0, 255}}, // J blue
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}
	};
	
	Random random = new Random();

	public static void main(String[] args) {

		//Окно Приложения
		JFrame jFrame = new JFrame ("Tetris");
		jFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setSize (block*10+17, block*20+40);
		jFrame.setResizable(false);
		jFrame.setLocationRelativeTo(null);
		jFrame.setVisible(true);
		Tetris tetris = new Tetris();
		jFrame.add(tetris);

		//Проверка
		jFrame.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent event) {
				switch(event.getKeyCode()) {
					case 37: x--; break; //Лево
					case 38: y--; break; //Низ
					case 39: x++; break; //Право
					case 40: y++; break; //Верх
				}
			}
		});

		while (true) {
			tetris.game();
			tetris.repaint();
			try {
				Thread.sleep(500);
			} catch (Exception e) {}
		}
	}

	// Логический Блок
	private void game() {
		y++;
		if(y == 20) random();
	}
		
	//Random
		private void random(){
		randForm = random.nextInt(7);
		y = -2;
	}
	
	

	//Графика
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);

		for(int i = 0; i < 4; i++){
			ctx.setColor(new Color(form[randForm][4][0], form[randForm][4][1], form[randForm][4][2]));
			ctx.fillRect(block*form[randForm][i][0]+x*block, block*form[randForm][i][1]+y*block, block, block);
		}
		
		//Сетка
		ctx.setColor(Color.gray);
		for (int i = 0; i <= 10; i++) ctx.drawLine(block*i, 0, block*i, block*20);
		for (int i = 0; i <= 20; i++) ctx.drawLine(0, block*i, block*10, block*i);
	}
}