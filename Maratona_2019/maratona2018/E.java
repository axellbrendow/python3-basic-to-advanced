import java.util.Arrays;

public class E
{
	public static char[] letras = new char[]
	{
		'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
		'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
	};
	
	public static final int TAMANHO_ALFABETO = 26;
	public static final int[] deslocamentos = new int[TAMANHO_ALFABETO];
	public static int hash(char c) { return c - 'A'; }
	
	public static void main(String[] args)
	{
		String mensagemCifrada = IO.readLine();
		String crib = IO.readLine();
		int tamanhoCrib = crib.length();
		
		Arrays.fill(deslocamentos, tamanhoCrib); // Coloca o tamanho do crib em todas as posições
		
		for (int i = 0; i < tamanhoCrib; i++)
		{
			deslocamentos[hash(crib.charAt(i))] = tamanhoCrib - 1 - i;
		}
	}
}
