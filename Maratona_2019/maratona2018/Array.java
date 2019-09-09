import java.util.*;
import java.util.function.*;

/**
 * @author Axell Brendow ( https://github.com/axell-brendow )
 */

public class Array
{
    /**
     * Checa se todos os objetos recebidos nao sao nulos.
     * 
     * @param objects objetos
     * 
     * @return {@code true} se todos os objetos recebidos nao sao nulos. Caso
     * contrario, {@code false}.
     */
    
    public static boolean exists(Object... objects)
    {
        boolean exists = false;
        
        if (objects != null && objects.length > 0)
        {
            exists = ( objects[0] != null );
            
            for (int i = 1; exists && i < objects.length; i++)
            {
                exists = ( objects[i] != null );
            }
        }
        
        return exists;
    }
    
    /**
     * Percorre os elementos de {@code collection} ate' que a funcao booleana de
     * {@code checker} retorne {@code false} ou acabem os elementos.
     * 
     * <p>{@code checker} recebe um {@code T} como parametro que e' o proprio
     * objeto.</p>
     * 
     * @param <T> tipo dos objetos da colecao
     * @param collection colecao de objetos
     * @param checker interface para checagem dos elementos
     * 
     * @return  {@code true} se todos os elemento de {@code collection} fizerem
     * a funcao booleana de {@code checker} retornar {@code true}. Caso
     * contrario, {@code false}.
     */
    
    public static <T> boolean forEach(Collection<T> collection, Function<T, Boolean> checker)
    {
        boolean success = false;
        
        if (exists(collection, checker))
        {
            Iterator<T> iterator = collection.iterator();
            success = iterator.hasNext();
            
            while (success && iterator.hasNext())
            {
                success = checker.apply(iterator.next());
            }
        }
        
        return success;
    }
    
    /**
     * Percorre os elementos de {@code array} ate' que a funcao booleana de
     * {@code checker} retorne {@code false} ou acabem os elementos.
     * 
     * <p>{@code checker} recebe um {@code Integer} como parametro que e' o
     * indice do objeto no arranjo e um {@code T} que e' o proprio objeto.</p>
     * 
     * @param <T> tipo dos objetos do arranjo
     * @param array arranjo de objetos
     * @param checker interface para checagem dos elementos
     * 
     * @return  {@code true} se todos os elemento de {@code array} fizerem
     * a funcao booleana de {@code checker} retornar {@code true}. Caso
     * contrario, {@code false}.
     */
    
    public static <T> boolean forEach(T[] array, BiFunction<Integer, T, Boolean> checker)
    {
        boolean success = false;
        
        if (exists(array, checker) && array.length > 0)
        {
            success = true;
            
            for (int i = 0; success && i < array.length; i++)
            {
                success = checker.apply(i, array[i]);
            }
        }
        
        return success;
    }
    
    public static <T> ArrayList<T> cut(ArrayList<T> arrayList, int[] indexes)
    {
        ArrayList<T> newArrayList = null;
        
        if (!anyIndexIsOutOfBounds(indexes, arrayList))
        {
            newArrayList = new ArrayList<>();
            
            for (int i = 0; i < indexes.length; i++)
            {
                newArrayList.add( arrayList.get( indexes[i] ) );
            }
        }
        
        return newArrayList;
    }
    
    /**
     * Cria um arranjo de inteiros com tamanho {@code size} e com elementos
     * gerados pelo {@code elementsManager}. Para fazer isso,
     * {@code elementsManager} recebera' um {@code Integer} que e' o indice do
     * elemento no arranjo e um {@code int[]} que e' o proprio arranjo (isso
     * pode ser util para sequencia numericas que dependem dos termos ja'
     * gerados). O retorno de {@code elementsManager} sera' o elemento a ser
     * inserido no indice recebido.
     * 
     * <p>Ex: createIntArray(10, (index, array) -&gt index) cria um arranjo com 10
     * posicoes com os numeros de 0 a 9.</p>
     * 
     * @param size tamanho do arranjo a ser gerado
     * @param elementsManager interface responsavel por criar os elementos do
     * arranjo
     * 
     * @return Arranjo gerado
     */
    
    public static int[] createIntArray(int size, BiFunction<Integer, int[], Integer> elementsManager)
    {
        int[] intArray = null;
        
        if (exists(elementsManager) && size > 0)
        {
            intArray = new int[size];
            
            for (int i = 0; i < size; i++)
            {
                intArray[i] = elementsManager.apply(i, intArray);
            }
        }
        
        return intArray;
    }
    
    public static int[] createIntArrayFromTo(int from, int to)
    {
        int[] intArray;
        
        if (from <= to)
        {
            intArray =
            createIntArray(to - from + 1, (index, array) -> index + from);
        }
        
        else
        {
            intArray =
            createIntArray(from - to + 1, (index, array) -> from - index);
        }
        
        return intArray;
    }
    
    /**
     * Encontra o indice do primeiro elemento de {@code arrayList} que fizer a
     * funcao booleana de {@code checker} retornar {@code true}. Caso nenhum
     * satisfaca a condicao, -1 e' retornado.
     * 
     * @param <T> tipo dos objetos de {@code arrayList}
     * @param checker interface com funcao avaliadora dos objetos de
     * {@code arrayList}
     * @param arrayList lista de objetos
     * 
     * @return O indice do primeiro elemento de {@code arrayList} que fizer a
     * funcao booleana de {@code checker} retornar {@code true}. Caso nenhum
     * satisfaca a condicao, -1 e' retornado.
     */
    
    public static <T> int first(Function<T, Boolean> checker, ArrayList<T> arrayList)
    {
        int index = -1;
        
        if (exists(checker, arrayList) && !arrayList.isEmpty())
        {
            int i = 0;
            int size = arrayList.size();
            boolean found = checker.apply( arrayList.get(i) );
            
            for (i = 1; !found && i < size; i++)
            {
                found = checker.apply( arrayList.get(i) );
            }
            
            if (found)
            {
                index = i - 1;
            }
        }
        
        return index;
    }
    
    /**
     * Checa se existe algum elemento de {@code arrayList} que faz a funcao
     * booleana de {@code checker} retornar {@code true}. O retorno e'
     * {@code true} se algum satisfazer 'a condicao e {@code false} caso
     * contrario.
     * 
     * @param <T> tipo dos objetos de {@code arrayList}
     * @param checker interface com funcao avaliadora dos objetos de
     * {@code arrayList}
     * @param arrayList lista de objetos
     * 
     * @return {@code true} se todos os elemento de {@code arrayList} fizerem a
     * funcao booleana de {@code checker} retornar {@code true}. Caso contrario,
     * {@code false}.
     */
    
    public static <T> boolean any(Function<T, Boolean> checker, ArrayList<T> arrayList)
    {
        return ( first(checker, arrayList) != -1 );
    }
    
    /**
     * Troca os elementos dos indices {@code index1} e {@code index2} entre si.
     * 
     * @param <T> tipo dos objetos de {@code arrayList}
     * @param index1 indice do primeiro elemento
     * @param index2 indice do segundo elemento
     * @param arrayList lista de objetos
     * 
     * @return {@code true} se {@code index1} e {@code index2} foram indices
     * validos e {@code arrayList} nao for {@code null}. Caso contrario
     * {@code false}.
     */
    
    public static <T> boolean swap(int index1, int index2, ArrayList<T> arrayList)
    {
        boolean success = false;
        
        if (exists(arrayList))
        {
            int size = arrayList.size();
            
            if
            (
                !indexIsOutOfBounds(index1, size) &&
                !indexIsOutOfBounds(index2, size)
            )
            {
                T copy = arrayList.get(index1);
                
                arrayList.set(index1, arrayList.get(index2));
                arrayList.set(index2, copy);
                
                success = true;
            }
        }
        
        return success;
    }
    
    /**
     * Espelha o indice {@code index} em relacao ao meio do conjunto de tamanho
     * {@code setSize}.
     * 
     * @param index indice
     * @param setSize tamanho do conjunto
     * 
     * @return Indice espelhado do indice {@code index} em relacao ao meio do
     * conjunto de tamanho {@code setSize}.
     */
    
    public static int reflect(int index, int setSize)
    {
        return setSize - 1 - index;
    }
    
    /**
     * Checa se, a partir do indice {@code start}, e' possivel acessar
     * {@code numberOfElements} elementos num conjunto de tamanho
     * {@code setSize}.
     * 
     * <p>Obs.: Nao checa se o valor de {@code setSize} e' valido.</p>
     * 
     * @param start indice inicial
     * @param numberOfElements quantidade de elementos
     * @param setSize tamanho do conjunto
     * 
     * @return 0 se nao for ocorrer transbordamento do limite do conjunto;
     * {@code numberOfElements} se {@code numberOfElements < 0}; um valor
     * positivo x caso o transbordamento for ocorrer depois do ultimo elemento.
     * O valor x indica quantos elementos depois do ultimo seriam necessarios
     * para nao ocorrer o transbordamento.
     */
    
    public static int limitOverflow(int start, int numberOfElements, int setSize)
    {
        int limitOverflow;
        
        if (start < 0)
        {
            //AxellIO.println("[AxellIO]: Parametro start < 0 na funcao limitOverflow() - (start = " + start + ")");
            
            limitOverflow = start;
        }
        
        else if (numberOfElements < 0)
        {
            //AxellIO.println("[AxellIO]: Parametro numberOfElements < 0 na funcao limitOverflow() - (numberOfElements = " + numberOfElements + ")");
            
            limitOverflow = numberOfElements;
        }
        
        else if (start + numberOfElements > setSize)
        {
            //AxellIO.println("[AxellIO]: Parametros start e numberOfElements quebram o limite na funcao limitOverflow() - (start = " + start + " | numberOfElements = " + numberOfElements + ")");
            
            limitOverflow = (start + numberOfElements) - setSize;
        }
        
        else
        {
            limitOverflow = 0; // 0 = nao ha' transbordamento
        }
        
        return limitOverflow;
    }
    
    /**
     * Checa se, a partir do indice {@code start}, e' possivel acessar
     * {@code numberOfElements} elementos num conjunto de tamanho
     * {@code setSize}. Caso {@code backward} seja {@code true}, a checagem e'
     * feita no sentido contrario (&lt-).
     * 
     * <p>Obs.: Nao checa se o valor de {@code setSize} e' valido.</p>
     * 
     * @param start indice inicial
     * @param numberOfElements quantidade de elementos
     * @param setSize tamanho do conjunto
     * @param backward se {@code true}, a checagem e' feita no sentido contrario
     * (&lt- para tras).
     * 
     * @return 0 se nao for ocorrer transbordamento do limite do conjunto;
     * {@code numberOfElements} se {@code numberOfElements < 0}; um valor
     * positivo x caso o transbordamento for ocorrer depois do ultimo elemento.
     * O valor x indica quantos elementos depois do ultimo seriam necessarios
     * para nao ocorrer o transbordamento; um valor negativo y caso o
     * transbordamento for ocorrer antes do primeiro elemento. O valor y indica
     * quantos elementos antes do primeiro seriam necessarios para nao ocorrer o
     * transbordamento;
     */
    
    public static int limitOverflow(int start, int numberOfElements, int setSize, boolean backward)
    {
        int limitOverflow;
        
        if (backward)
        {
            limitOverflow = -limitOverflow(reflect(start, setSize), numberOfElements, setSize);
        }
        
        else
        {
            limitOverflow = limitOverflow(start, numberOfElements, setSize);
        }
        
        return limitOverflow;
    }
    
    /**
     * Checa se, a partir do indice {@code start}, e' possivel acessar
     * {@code numberOfElements} elementos do arranjo {@code array}. Caso
     * {@code backward} seja {@code true}, a checagem e' feita no sentido
     * contrario (&lt- para tras).
     * 
     * @param start indice inicial
     * @param numberOfElements quantidade de elementos
     * @param array arranjo
     * @param backward se {@code true}, a checagem e' feita no sentido contrario
     * (&lt- para tras).
     * 
     * @return {@code Integer.MIN_VALUE} se {@code array == null}; 0 se nao for
     * ocorrer transbordamento do limite do arranjo; {@code numberOfElements}
     * se {@code numberOfElements < 0}; um valor positivo x caso o
     * transbordamento for ocorrer depois do ultimo elemento. O valor x indica
     * quantos elementos depois do ultimo seriam necessarios para nao ocorrer o
     * transbordamento; um valor negativo y caso o transbordamento for ocorrer
     * antes do primeiro elemento. O valor y indica quantos elementos antes do
     * primeiro seriam necessarios para nao ocorrer o transbordamento.
     */
    
    public static <T> int limitOverflow(int start, int numberOfElements, T[] array, boolean backward)
    {
        int limitOverflow = Integer.MIN_VALUE;
        
        if (exists(array))
        {
            limitOverflow = limitOverflow(start, numberOfElements, array.length, backward);
        }
        
        return limitOverflow;
    }
    
    /**
     * Checa se, a partir do indice {@code start}, e' possivel acessar
     * {@code numberOfElements} elementos da colecao {@code collection}. Caso
     * {@code backward} seja {@code true}, a checagem e' feita no sentido
     * contrario (&lt- para tras).
     * 
     * @param start indice inicial
     * @param numberOfElements quantidade de elementos
     * @param collection colecao
     * @param backward se {@code true}, a checagem e' feita no sentido contrario
     * (&lt- para tras).
     * 
     * @return {@code Integer.MIN_VALUE} se {@code collection == null}; 0 se nao
     * for ocorrer transbordamento do limite da colecao; {@code numberOfElements}
     * se {@code numberOfElements < 0}; um valor positivo x caso o
     * transbordamento for ocorrer depois do ultimo elemento. O valor x indica
     * quantos elementos depois do ultimo seriam necessarios para nao ocorrer o
     * transbordamento; um valor negativo y caso o transbordamento for ocorrer
     * antes do primeiro elemento. O valor y indica quantos elementos antes do
     * primeiro seriam necessarios para nao ocorrer o transbordamento.
     */
    
    public static int limitOverflow(int start, int numberOfElements, Collection collection, boolean backward)
    {
        int limitOverflow = Integer.MIN_VALUE;
        
        if (exists(collection))
        {
            limitOverflow = limitOverflow(start, numberOfElements, collection.size(), backward);
        }
        
        return limitOverflow;
    }
    
    /**
     * Checa se e' possivel acessar o indice {@code index} num conjunto de
     * tamanho {@code setSize}.
     * 
     * <p>Obs.: Nao checa se o valor de {@code setSize} e' valido.</p>
     * 
     * @param index indice
     * @param setSize tamanho do conjunto
     * 
     * @return 0 se nao for ocorrer transbordamento do limite do conjunto;
     * um valor positivo x caso o transbordamento for ocorrer depois do ultimo
     * elemento. O valor x indica quantos elementos depois do ultimo seriam
     * necessarios para nao ocorrer o transbordamento.
     */
    
    public static int limitOverflow(int index, int setSize)
    {
        return limitOverflow(index, 1, setSize);
    }
    
    /**
     * Checa se e' possivel acessar o indice {@code index} do arranjo
     * {@code array}.
     * 
     * @param index indice
     * @param array arranjo
     * 
     * @return 0 se nao for ocorrer transbordamento do limite do arranjo; um
     * valor positivo x caso o transbordamento for ocorrer depois do ultimo
     * elemento. O valor x indica quantos elementos depois do ultimo seriam
     * necessarios para nao ocorrer o transbordamento.
     */
    
    public static <T> int limitOverflow(int index, T[] array)
    {
        return limitOverflow(index, 1, array, false);
    }
    
    /**
     * Checa se e' possivel acessar o indice {@code index} do arranjo
     * {@code array}.
     * 
     * @param index indice
     * @param collection colecao
     * 
     * @return 0 se nao for ocorrer transbordamento do limite do arranjo; um
     * valor positivo x caso o transbordamento for ocorrer depois do ultimo
     * elemento. O valor x indica quantos elementos depois do ultimo seriam
     * necessarios para nao ocorrer o transbordamento.
     */
    
    public static int limitOverflow(int index, Collection collection)
    {
        return limitOverflow(index, 1, collection, false);
    }
    
    public static boolean rangeIsOutOfBounds(int start, int numberOfElements, int setSize)
    {
        return ( limitOverflow(start, numberOfElements, setSize) != 0 );
    }
    
    public static boolean anyRangeIsOutOfBounds(int[][] ranges, int setSize)
    {
        boolean outOfBounds = true;
        
        if (exists((Object) ranges) && ranges.length > 0 && ranges[0].length == 2)
        {
            outOfBounds = ( rangeIsOutOfBounds(ranges[0][0], ranges[0][1], setSize) );
            
            for (int i = 1; !outOfBounds && i < ranges.length; i++)
            {
                outOfBounds = ( rangeIsOutOfBounds(ranges[i][0], ranges[i][1], setSize) );
            }
        }
        
        return outOfBounds;
    }
    
    public static boolean rangeIsOutOfBounds(int start, int numberOfElements, int setSize, boolean backward)
    {
        return ( limitOverflow(start, numberOfElements, setSize, backward) != 0 );
    }
    
    public static <T> boolean rangeIsOutOfBounds(int start, int numberOfElements, T[] array, boolean backward)
    {
        return ( limitOverflow(start, numberOfElements, array, backward) != 0 );
    }
    
    public static <T> boolean rangeIsOutOfBounds(int start, int numberOfElements, Collection collection, boolean backward)
    {
        return ( limitOverflow(start, numberOfElements, collection, backward) != 0 );
    }
    
    public static boolean anyRangeIsOutOfBounds(int[][] ranges, Collection collection)
    {
        boolean outOfBounds = true;
        
        if (exists(collection))
        {
            outOfBounds = anyRangeIsOutOfBounds(ranges, collection.size());
        }
        
        return outOfBounds;
    }
    
    public static boolean indexIsOutOfBounds(int index, int setSize)
    {
        return ( limitOverflow(index, setSize) != 0 );
    }
    
    public static boolean anyIndexIsOutOfBounds(int[] indexes, int setSize)
    {
        boolean outOfBounds = true;
        
        if (exists((Object) indexes) && indexes.length > 0)
        {
            outOfBounds = ( indexIsOutOfBounds(indexes[0], setSize) );
            
            for (int i = 1; !outOfBounds && i < indexes.length; i++)
            {
                outOfBounds = ( indexIsOutOfBounds(indexes[i], setSize) );
            }
        }
        
        return outOfBounds;
    }
    
    public static <T> boolean indexIsOutOfBounds(int index, T[] array)
    {
        return ( limitOverflow(index, array) != 0 );
    }
    
    public static <T> boolean indexIsOutOfBounds(int index, Collection collection)
    {
        return ( limitOverflow(index, collection) != 0 );
    }
    
    public static boolean anyIndexIsOutOfBounds(int[] indexes, Collection collection)
    {
        boolean outOfBounds = true;
        
        if (exists(collection))
        {
            outOfBounds = anyIndexIsOutOfBounds(indexes, collection.size());
        }
        
        return outOfBounds;
    }
    
    /**
     * Preenche a matriz {@code matrix} com os valores {@code value}.
     * 
     * @param matrix matriz a ser preenchida
     * @param value valor a ser colocado
     */
    
    public static void fill(int[][] matrix, int value)
    {
        if (exists((Object) matrix) && matrix.length > 0 && matrix[0].length > 0)
        {
            for (int[] line : matrix)
            {
                Arrays.fill(line, value);
            }
        }
    }
    
    /**
     * Usando a convensao de preencher as matrizes de inteiros com -1 antes de
     * usa'-las, esse metodo serve para remover todas as linhas e colunas nao
     * utilizadas na matriz {@code matrix}.
     * 
     * @param matrix matriz a ser analisada
     * 
     * @return Nova matriz com todas as linhas e colunas nao utilizadas na
     * matriz {@code matrix} removidas.
     */
    
    public static int[][] fit(int[][] matrix)
    {
        int[][] newMatrix = matrix;
        
        if (exists((Object) matrix) && matrix.length > 0 && matrix[0].length > 0)
        {
            int numberOfColumns = getNumberOfElementsOf(matrix[0]);
            int numberOfLines = getNumberOfLinesOf(matrix);
            
            newMatrix = new int[numberOfLines][numberOfColumns];
            
            for (int i = 0; i < numberOfLines; i++)
            {
                System.arraycopy(matrix[i], 0, newMatrix[i], 0, numberOfColumns);
            }
        }
        
        return newMatrix;
    }
    
    /**
     * Gera uma matriz que e' resultado do corte, a partir da linha 0, da matriz
     * {@code matrix}, incluindo {@code numberOfLines} linhas para baixo.
     * 
     * @param matrix matrix a ser ajustada
     * @param numberOfLines numero de linhas a serem pegas
     * 
     * @return Uma matriz que e' resultado do corte, a partir da linha 0, da
     * matriz {@code matrix}, incluindo {@code numberOfLines} linhas para baixo.
     */
    
    public static int[][] fit(int[][] matrix, int numberOfLines)
    {
        int[][] smallerMatrix = new int[numberOfLines][matrix[0].length];
        
        System.arraycopy(matrix, 0, smallerMatrix, 0, numberOfLines);
        
        return smallerMatrix;
    }
    
    /**
     * Gera um arranjo que e' resultado do corte, a partir da posicao 0, do
     * arranjo {@code array}, incluindo {@code numberOfElements} elementos para
     * frente.
     * 
     * @param array arranjo a ser ajustado
     * @param numberOfElements numero de elementos a serem pegos
     * 
     * @return Um arranjo que e' resultado do corte, a partir da posicao 0, do
     * arranjo {@code array}, incluindo {@code numberOfElements} elementos para
     * frente.
     */
    
    public static int[] fit(int[] array, int numberOfElements)
    {
        int[] smallerArray = new int[numberOfElements];
        
        System.arraycopy(array, 0, smallerArray, 0, numberOfElements);
        
        return smallerArray;
    }
    
    /**
     * Usando a convensao de preencher os arranjos de inteiros com -1 antes de
     * usa'-los, esse metodo gera um arranjo que contem apenas os elementos de
     * fato inseridos em {@code array}. Remove os valores -1.
     * 
     * @param array arranjo a ser ajustado
     * 
     * @return Um arranjo que contem apenas os elementos de fato inseridos em
     * {@code array}.
     */
    
    public static int[] fit(int[] array)
    {
        return fit(array, getNumberOfElementsOf(array));
    }
    
    /**
     * Adiciona o valor {@code value} ao arranjo {@code array}. Porem, caso
     * {@code value} ja' estiver em {@code array} ou em {@code valuesToIgnore},
     * ele nao e' adicionado.
     * 
     * @param array arranjo a ser preenchido
     * @param value valor a ser colocado
     * @param valuesToIgnore valores a serem ignorados
     */
    
    public static void addValueIfItDoesntExistInArray(int[] array, int value, int[] valuesToIgnore)
    {
        int numberOfElements = Array.getNumberOfElementsOf(array);
        
        if (numberOfElements < array.length &&
                !Array.contains(value, valuesToIgnore) &&
                !Array.contains(value, array))
        {
            array[numberOfElements] = value;
        }
    }
    
    /**
     * Percorre o arranjo {@code values} adicionando seus valores ao arranjo
     * {@code array}. Porem, valores que ja' estiverem em {@code array} ou que
     * estiverem em {@code valuesToIgnore} nao sao adicionados.
     * 
     * @param array arranjo a ser preenchido
     * @param values valores a serem colocados
     * @param valuesToIgnore valores a serem ignorados
     */
    
    public static void addEachValueIfItDoesntExistInArray(int[] array, int[] values, int[] valuesToIgnore)
    {
        for (int i = 0; i < values.length; i++)
        {
            addValueIfItDoesntExistInArray(array, values[i], valuesToIgnore);
        }
    }
    
    /**
     * Usando a convensao de preencher as matrizes de inteiros com -1 antes de
     * usa'-las, esse metodo serve para saber quantas linhas da matriz ja' foram
     * usadas a partir da linha 0 e em sequencia.
     * 
     * @param matrix matriz a ser percorrida
     * 
     * @return Quantas linhas da matriz ja' foram usadas a partir da linha 0 e
     * em sequencia.
     */
    
    public static int getNumberOfLinesOf(int[][] matrix)
    {
        int numberOfLines = 0;
        
        if (exists((Object) matrix))
        {
            for (int i = 0; i < matrix.length && matrix[i][0] != -1; i++)
            {
                numberOfLines++;
            }
        }
        
        return numberOfLines;
    }
    
    /**
     * Usando a convensao de preencher os arranjos de objetos com null antes de
     * usa'-los, esse metodo serve para saber quantos objetos foram colocados
     * no arranjo a partir da posicao 0 e em sequencia.
     * 
     * @param array arranjo a ser percorrido
     * 
     * @return Quantos objetos foram colocados no arranjo a partir da posicao
     * 0 e em sequencia.
     */
    
    public static int getNumberOfElementsOf(Object[] array)
    {
        int numberOfElements = indexOf(null, array);
        
        return ( numberOfElements != -1 ? numberOfElements : array.length );
    }
    
    /**
     * Usando a convensao de preencher os arranjos de inteiros com -1 antes de
     * usa'-los, esse metodo serve para saber quantos inteiros foram colocados
     * no arranjo a partir da posicao 0 e em sequencia.
     * 
     * @param array arranjo a ser percorrido
     * 
     * @return Quantos inteiros foram colocados no arranjo a partir da posicao
     * 0 e em sequencia.
     */
    
    public static int getNumberOfElementsOf(int[] array)
    {
        int numberOfElements = 0;
        
        if (exists((Object) array) && array.length > 0)
        {
            numberOfElements = indexOf(-1, array);
        }
        
        return ( numberOfElements != -1 ? numberOfElements : array.length );
    }
    
    /**
     * Percorre o arranjo procurando o seu maior elemento.
     * 
     * @param array arranjo a ser pesquisado
     * 
     * @return Maior elemento do arranjo.
     */
    
    public static int getGreatest(int[] array)
    {
        int greatest = 0;
        
        if (exists((Object) array) && array.length > 0)
        {
            int current;
            
            greatest = array[0];
            
            for (int i = 1; i < array.length; i++)
            {
                current = array[i];
                
                if (current > greatest)
                {
                    greatest = current;
                }
            }
        }
        
        return greatest;
    }
    
    /**
     * Percorre o arranjo concatenando os seus elementos.
     * 
     * @param array arranjo a ser percorrido.
     * 
     * @return String com todos os elementos do arranjo concatenados.
     */
    
    public static String toString(char[] array)
    {
        String str = "";
        
        for (int i = 0; i < array.length; i++)
        {
            str += array[i];
        }
        
        return str;
    }
    
    /**
     * Cria um novo arranjo com todos os elementos do primeiro e, logo apos, todos
     * os elementos do segundo.
     * 
     * @param array1 primeiro arranjo
     * @param array2 segundo arranjo
     * 
     * @return Um novo arranjo com todos os elementos do primeiro e, logo apos,
     * todos os elementos do segundo.
     */
    
    public static int[] concatArrays(int[] array1, int[] array2)
    {
        int[] newArray = new int[array1.length + array2.length];
        int counterOfTheNewArray = 0;

        for (int i = 0; i < array1.length; i++)
        {
            newArray[counterOfTheNewArray++] = array1[i];
        }

        for (int i = 0; i < array2.length; i++)
        {
            newArray[counterOfTheNewArray++] = array2[i];
        }

        return newArray;
    }
    
    /**
     * Cria um novo arranjo com todos os elementos do primeiro e, logo apos, todos
     * os elementos do segundo.
     * 
     * @param array1 primeiro arranjo
     * @param array2 segundo arranjo
     * 
     * @return Um novo arranjo com todos os elementos do primeiro e, logo apos,
     * todos os elementos do segundo.
     */
    
    public static char[] concatArrays(char[] array1, char[] array2)
    {
        char[] newArray = new char[array1.length + array2.length];
        int counterOfTheNewArray = 0;

        for (int i = 0; i < array1.length; i++)
        {
            newArray[counterOfTheNewArray++] = array1[i];
        }

        for (int i = 0; i < array2.length; i++)
        {
            newArray[counterOfTheNewArray++] = array2[i];
        }

        return newArray;
    }
    
    /**
     * Percorre um arranjo de caracteres contando quantos vezes determinado
     * caractere aparece.
     * 
     * @param c caractere a ser procurado
     * @param binary1 arranjo a ser percorrido
     * 
     * @return Quantas vezes o caractere da variavel c aparece no arranjo.
     */
    
    public static int countChars(char c, char[] binary1)
    {
        int count = 0;
        
        for (int i = 0; i < binary1.length; i++)
        {
            count += ( binary1[i] == c ? 1 : 0 );
        }
        
        return count;
    }
    
    /**
     * Percorre o arranjo procurando um elemento.
     * 
     * @param value elemento a ser procurado
     * @param array arranjo a ser percorrido
     * 
     * @return Indice do elemento no arranjo. Caso nao seja encontrado, o retorno
     * e' -1.
     */
    
    public static int indexOf(Object value, Object[] array)
    {
        int index = -1;
        
        for (int i = 0; index == -1 && i < array.length; i++)
        {
            if (array[i].equals(value))
            {
                index = i;
            }
        }
        
        return index;
    }
    
    /**
     * Percorre o arranjo procurando um elemento.
     * 
     * @param value elemento a ser procurado
     * @param array arranjo a ser percorrido
     * 
     * @return Indice do elemento no arranjo. Caso nao seja encontrado, o retorno
     * e' -1.
     */
    
    public static int indexOf(int value, int[] array)
    {
        int index = -1;
        
        for (int i = 0; index == -1 && i < array.length; i++)
        {
            if (array[i] == value)
            {
                index = i;
            }
        }
        
        return index;
    }
    
    /**
     * Percorre o arranjo fonte procurando cada um de seus elementos no arranjo
     * de pesquisa.
     * 
     * @param sourceArray arranjo fonte
     * @param arrayToSearch arranjo de pesquisa
     * 
     * @return Os indices, no arranjo fonte e de pesquisa respectivamente, do 
     * primeiro elemento que for encontrado nos dois arranjos. O arranjo retornado
     * tem exatamente dois espacos.
     */
    
    public static int[] indexOf(int[] sourceArray, int[] arrayToSearch)
    {
        int[] indexes = new int[2];
        indexes[0] = indexes[1] = -1;
        int searchIndex;
        
        for (int i = 0; indexes[0] == -1 && i < sourceArray.length; i++)
        {
            searchIndex = indexOf(sourceArray[i], arrayToSearch);
            
            if (searchIndex != -1)
            {
                indexes[0] = i;
                indexes[1] = searchIndex;
            }
        }
        
        return indexes;
    }
    
    /**
     * Percorre o arranjo procurando um elemento.
     * 
     * @param value elemento a ser procurado
     * @param array arranjo a ser percorrido
     * 
     * @return Indice do elemento no arranjo. Caso nao seja encontrado, o retorno
     * e' -1.
     */
    
    public static int indexOf(char value, char[] array)
    {
        int index = -1;
        
        for (int i = 0; index == -1 && i < array.length; i++)
        {
            if (array[i] == value)
            {
                index = i;
            }
        }
        
        return index;
    }
    
    /**
     * Percorre a matriz procurando um arranjo.
     * 
     * @param array arranjo a ser procurado
     * @param matrix matriz ou arranjo de arranjos a ser percorrido
     * 
     * @return Indice do arranjo na matriz. Em outras palavras, indice da linha
     * da matriz em que o arranjo esta'.
     */
    
    public static int indexOf(char[] array, char[][] matrix)
    {
        int index = -1;
        
        for (int i = 0; index == -1 && i < matrix.length; i++)
        {
            if (exists((Object) matrix[i]) && Arrays.equals(matrix[i], array))
            {
                index = i;
            }
        }
        
        return index;
    }
    
    public static boolean contains(Object value, Object[] array)
    {
        return indexOf(value, array) != -1;
    }
    
    public static boolean contains(char value, char[] array)
    {
        return indexOf(value, array) != -1;
    }
    
    public static boolean contains(char[] array, char[][] matrix)
    {
        return indexOf(array, matrix) != -1;
    }
    
    public static boolean contains(int value, int[] array)
    {
        return indexOf(value, array) != -1;
    }
    
    public static boolean containsAnyOf(int[] sourceArray, int[] arrayToSearch)
    {
        return indexOf(sourceArray, arrayToSearch)[0] != -1;
    }
}
