import java.util.Arrays;

public class E
{
	public static final int TAMANHO_ALFABETO = 26;
	public static final int[] deslocamentos = new int[TAMANHO_ALFABETO];
	
	public static int hash(char c) { return c - 'A'; }
	
	public static void inicializarBoyerMoore(String crib, int tamanho)
	{
		Arrays.fill(deslocamentos, tamanho); // Coloca o tamanho do crib em todas as posições
		
		for (int i = 0; i < tamanho - 1; i++)
		{
			deslocamentos[hash(crib.charAt(i))] = tamanho - 1 - i;
		}
	}
	
	public static int boyerMoore(String string, String substring)
	{
		int count = 0, i = 0;
		int tamanhoSubStr = substring.length();
		
		inicializarBoyerMoore(substring, tamanhoSubStr);
		
		//while ()
		
		return count;
	}
	
	public static void main(String[] args)
	{
		String mensagemCifrada = IO.readLine();
		String crib = IO.readLine();
		
		IO.println(boyerMoore(mensagemCifrada, crib));
	}
}
