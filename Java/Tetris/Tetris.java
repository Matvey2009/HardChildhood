/*27.10.2019
 * Matvey
 * Tetris
 */

import java.awt.Color;                                                                                                                
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Tetris extends JPanel {
	
	//Переменные
	protected static int block = 30, x = 10;
	
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
		
		while (true) {
			tetris.game();
			tetris.repaint();
			try {
				Thread.sleep(50);
			} catch (Exception e) {}
		}
	}
	
	// Логический Блок
	private void game() {
		x++;
	}
	
	//Графика
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);
		
		ctx.setColor(Color.green);
		ctx.fillRect(50, x, 50, 50);
	}
}