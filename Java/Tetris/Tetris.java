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
		//y++;
	}
	
	//Графика
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);
		
		ctx.setColor(Color.green);
		ctx.fillRect(x*block, y*block, 30, 30);
	}
}