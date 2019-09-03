import java.util.Scanner;

class Par<TIPO1, TIPO2>
{
	public TIPO1 v1;
	public TIPO2 v2;
	
	Par(TIPO1 v1, TIPO2 v2)
	{
		this.v1 = v1;
		this.v2 = v2;
	}
	
	Par() { }
	
	@Override
	public String toString()
	{
		return "[" + v1 + ", " + v2 + "]";
	}
}

public class A
{
	public static final int corte = 10000 * 10000 * 10 + 7;
	
	public static void print(Object msg) { System.out.print(msg); }
	
	public static void println(Object msg) { print(msg + "\n"); }
	
	@SuppressWarnings("unchecked")
	public static Par<Integer, Integer>[] gerarCombinacoesDosIndices(
			int linha, int coluna, int numLinhas, int numColunas)
	{
		Par<Integer, Integer>[] combinacoes = (Par<Integer, Integer>[]) new Par[numLinhas * numColunas];
		
		for (int i = 0, k = 0; i < numLinhas; i++)
		{
			for (int j = 0; j < numColunas; j++)
			{
				combinacoes[k++] = new Par<>(i, j);
			}
		}
		
		return combinacoes;
	}
	
	public static <T> void gerarCombinacoes(Par<T, T>[] arranjo, Par<T, T>[][] combinacoes)
	{
		for (int i = 0, k = 0; i < arranjo.length; i++)
		{
			for (int j = i + 1; j < arranjo.length; j++)
			{
				combinacoes[k][0] = arranjo[i];
				combinacoes[k][1] = arranjo[j];
				k++;
			}
		}
	}
	
	public static boolean existeMDC(int num1, int num2)
	{
		boolean existe = false;
		int menor = Math.min(num1, num2);
		
		for (int i = 2; !existe && i <= menor; i++)
		{
			existe = num1 % i == 0 && num2 % i == 0;
		}
		
		return existe;
	}
	
	public static int possibilidadesSlackline(Par<Integer, Integer>[][] matriz, int minimo, int maximo)
	{
		double distancia;
		int numPossibilidades = 0, deltaX, deltaY;
		Par<Integer, Integer> par0, par1;
		
		for (int i = 0; i < matriz.length; i++)
		{
			par0 = matriz[i][0];
			par1 = matriz[i][1];
			deltaX = Math.abs(par1.v1 - par0.v1);
			deltaY = Math.abs(par1.v2 - par0.v2);
			distancia = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
			
			if (existeMDC(deltaX, deltaY) ||
					(deltaX == 0 && deltaY > 1) ||
					(deltaY == 0 && deltaX > 1) ||
					distancia < minimo || distancia > maximo)
			{
//				print("(" + deltaX + "," + deltaY + ") ");
				
			}
			
			else numPossibilidades = ++numPossibilidades % corte;
			
//			println("");
		}
		
		return numPossibilidades;
	}
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args)
	{
		int numLinhas, numColunas, minimo, maximo, total, numCombinacoes;
		Scanner scan = new Scanner(System.in);
		
		numLinhas = scan.nextInt();
		numColunas = scan.nextInt();
		minimo = scan.nextInt();
		maximo = Integer.parseInt(scan.next());
		total = numLinhas * numColunas;
		numCombinacoes = total * (total - 1) / 2;
		
		Par<Integer, Integer>[] paresOrdenados = gerarCombinacoesDosIndices(0, 0, numLinhas, numColunas);
		
		for (Par<Integer, Integer> par : paresOrdenados) { println("" + par); }
		
		Par<Integer, Integer>[][] combinacoes = (Par<Integer, Integer>[][]) new Par[numCombinacoes][2];
		
		gerarCombinacoes(paresOrdenados, combinacoes);
		
		for (Par<Integer, Integer>[] paresOrdenadosLoop : combinacoes)
		{
			print("[ ");
			
			for (Par<Integer, Integer> parOrdenado : paresOrdenadosLoop)
			{
				print(parOrdenado + " ");
			}
			
			println("]");
		}
		
		println("Quantidade = " + possibilidadesSlackline(combinacoes, minimo, maximo) + "\n");
		
		scan.close();
	}
}
