import javax.swing.JFrame;

public class Tetris {
	
	protected static int block = 30;
	
	public static void main(String[] args){
		JFrame jFrame = new JFrame ("Tetris");
		jFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.pack();
		jFrame.setSize (block*10, block*20);
		jFrame.setResizable(false);
		jFrame.setLocationRelativeTo(null);
		jFrame.setVisible(true);		
		
	}
}