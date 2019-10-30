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

public class Tetris extends JPanel {
	
	//Переменные
	protected static int block = 30, x = 0, y = 0;
	public int form[][][] = {
		{{0, 0, 0, 0}, { 1, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {255, 0, 0}}, // Z red
		{{0, 1, 0, 0}, { 0, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {255, 165, 0}}, // L orange
		{{0, 0, 0, 0}, { 0, 1, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {255, 255, 0}}, // O yellow
		{{0, 0, 0, 0}, { 1, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {0, 255, 0}}, // S green
		{{0, 0, 0, 0}, { 1, 1, 1, 1}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 255, 255}}, // I aqua
		{{0, 0, 1, 0}, { 0, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {0, 0, 255}}, // J blue
		{{0, 0, 0, 0}, { 1, 1, 1, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}, {255, 0, 255}}  // T purple
	};
	
	public static void main(String[] args) {
		
		//Окно Приложения
		JFrame jFrame = new JFrame ("Tetris");
		jFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setSize (block*10, block*20);
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
	}
	
	//Графика
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);
		

		for(int i = 0; i < 4; i = 0){
			ctx.setColor(new Color(form[0][4][0], form[0][4][1], form[0][4][2]));
			ctx.fillRect(block*form[0][i][0]+x*block, block*form[0][i][1]+y*block, block, block);
		}
	}
}