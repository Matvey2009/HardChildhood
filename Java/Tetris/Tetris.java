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
	protected static int block = 30, speed = 1, x = 0, y = 0, randForm, test;
		public int ground[][][] = new int [20][10][1];
		public int form[][][] = { // фигурка / блоки / x,y или r,g,b
		{{1, 2}, {2, 2}, {0, 1}, {1, 1}, {0xff0000}},
		{{1, 2}, {2, 2}, {1, 1}, {1, 0}, {0xffa500}},
		{{1, 2}, {2, 2}, {1, 1}, {2, 1}, {0xffff00}},
		{{0, 2}, {1, 2}, {1, 1}, {2, 1}, {0x00ff00}},
		{{0, 2}, {1, 2}, {2, 2}, {3, 2}, {0x00ffff}},
		{{1, 2}, {2, 2}, {2, 1}, {2, 0}, {0x0000ff}},
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {0xff00ff}}
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
				tetris.repaint();
				switch(event.getKeyCode()) {
					case 37: x--; break; //Лево
					case 38: tetris.rotate(); break; //Поворот
					case 39: x++; break; //Право
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
				if (form[randForm][i][1]+y+1 < 20) test++;
			}
		if (test == 4) y++; else {
			for (int i = 0; i < 4; i++) {
				ground[form[randForm][i][1]+y][form[randForm][i][0]+x][0] = (form[randForm][4][0]);
			}
			random();
		}
	}
		
	//Случайность
	private void random(){
		speed = 400;
		randForm = random.nextInt(7);
		y = -2;
	}
		
	//Поворот фигуры
	private void rotate() {
		int temp;
		for (int i = 0; i < 4; i++) {
			temp = form[randForm][i][0];
			form[randForm][i][0] = -form[randForm][i][1]+3;
			form[randForm][i][1] = temp;
		};
	}
		
	//Графика
	public void paint(Graphics ctx) {
		super.paint(ctx);
		
		//Днище
		for(int i = 0; i < 20; i++){
			for(int j = 0; j < 10; j++){
				ctx.setColor(new Color(ground[i][j][0]));                                                    
				ctx.fillRect(block*j, block*i, block, block);
			}
		}

		//фигуры
		for(int i = 0; i < 4; i++){
			ctx.setColor(new Color(form[randForm][4][0]));
			ctx.fillRect(block*form[randForm][i][0]+x*block, block*form[randForm][i][1]+y*block, block, block);
		}
		
		//Сетка
		ctx.setColor(Color.gray);
		for (int i = 0; i <= 10; i++) ctx.drawLine(block*i, 0, block*i, block*20);
 		for (int i = 0; i <= 20; i++) ctx.drawLine(0, block*i, block*10, block*i);
	}
}