import java.util.regex.Pattern;

/**
 * @author Axell Brendow ( https://github.com/axell-brendow )
 */

public class MyString
{
    // ----------------------- CONSTANTES DA CLASSE
    
    public static final MyString EMPTY = new MyString();
    
    // ----------------------- ATRIBUTOS DA CLASSE
    
    private String str;
    
    // ----------------------- CONSTRUTORES
    
    public MyString()
    {
        this("");
    }
    
    /**
     * Inicia o objeto com a string {@code str}.
     * 
     * <p>Obs.: Nao e' permitida string nula</p>
     * 
     * @param str string inicial
     */
    
    public MyString(String str)
    {
        if (Array.exists(str))
        {
            this.str = str;
        }
    }
    
    // ----------------------- METODOS
    
    // ----------------------- METODOS ESTATICOS
    
    /**
     * Converte a {@code str} para um objeto {@link MyString}
     * 
     * @param str string a ser convertida
     * 
     * @return Objeto {@link MyString} equivalente de {@code str}.
     */
    
    public static MyString convert(String str)
    {
        MyString convertedStr = null;
        
        if (Array.exists(str))
        {
            convertedStr = new MyString(str);
        }
        
        return convertedStr;
    }
    
    /**
     * Obtem o primeiro caractere de {@code str}. Caso {@code str} esteja vazia,
     * e' retornada uma string vazia.
     * 
     * @param str string de referencia
     * 
     * @return O primeiro caractere de {@code str}. Caso {@code str} esteja
     * vazia, e' retornada uma string vazia.
     */
    
    public static String getFirstChar(String str)
    {
        String firstChar = "";
        
        if (Array.exists(str) && str.length() > 0)
        {
            firstChar += str.charAt(0);
        }
        
        return firstChar;
    }
    
    /**
     * Obtem o ultimo caractere da string {@code str}. Caso {@code str} esteja
     * vazia, e' retornada uma string vazia.
     * 
     * @param str string de referencia
     * 
     * @return O ultimo caractere da string {@code str}. Caso {@code str} esteja
     * vazia, e' retornada uma string vazia.
     */
    
    public static String getLastChar(String str)
    {
        String lastChar = "";
        
        if (Array.exists(str))
        {
            int length = str.length();
            
            if (length > 0)
            {
                lastChar += str.charAt(length - 1);
            }
        }
        
        return lastChar;
    }
    
    /**
     * Cria clones de uma string e os concatena.
     * 
     * @param str string a ser clonada
     * @param numberOfClones numero de clones a serem criados
     * 
     * @return String com todos os clones concatenados, justapostos.
     */
    
    public static String createClonesAndConcatThem(String str, int numberOfClones)
    {
        String clones = "";
        
        for (int i = 0; i < numberOfClones; i++)
        {
            clones += str;
        }
        
        return clones;
    }
    
    /**
     * Cria uma string de tamanho {@code blockSize} que comeca com a string
     * {@code str}.
     * 
     * <p>Ex: alignLeft("abc", 5) = "abc  "</p>
     * 
     * @param str string a ser alinhada
     * @param blockSize tamanho do bloco de caracteres desejado
     * 
     * @return Uma string de tamanho {@code blockSize} que comeca com a string
     * {@code str}.
     */
    
    public static String alignLeft(String str, int blockSize)
    {
        if (Array.exists(str))
        {
            str += createClonesAndConcatThem(" ", blockSize - str.length());
        }
        
        return str;
    }
    
    /**
     * Cria uma string de tamanho {@code blockSize} que tem em seu meio a string
     * {@code str}.
     * 
     * <p>Ex: alignCenter("abc", 5) = " abc "</p>
     * 
     * @param str string a ser alinhada
     * @param blockSize tamanho do bloco de caracteres desejado
     * 
     * @return Uma string de tamanho {@code blockSize} que tem em seu meio a
     * string {@code str}.
     */
    
    public static String alignCenter(String str, int blockSize)
    {
        if (Array.exists(str))
        {
            blockSize -= str.length();
            int paddingLeft = blockSize / 2;

            str = createClonesAndConcatThem(" ", paddingLeft) +
                    str +
                    createClonesAndConcatThem(" ", blockSize - paddingLeft);
        }
        
        return str;
    }
    
    /**
     * Cria uma string de tamanho {@code blockSize} que termina com a string
     * {@code str}.
     * 
     * <p>Ex: alignRight("abc", 5) = "  abc"</p>
     * 
     * @param str string a ser alinhada
     * @param blockSize tamanho do bloco de caracteres desejado
     * 
     * @return Uma string de tamanho {@code blockSize} que termina com a string
     * {@code str}.
     */
    
    public static String alignRight(String str, int blockSize)
    {
        if (Array.exists(str))
        {
            str = createClonesAndConcatThem(" ", blockSize - str.length()) + str;
        }
        
        return str;
    }
    
    /**
     * Cria uma string de tamanho {@code blockSize} que tem em seu meio a string
     * {@code str}.
     * 
     * <p>Ex: centerStrOnABlock("abc", 5) = " abc "</p>
     * 
     * @param str string a ser alinhada
     * @param blockSize tamanho do bloco de caracteres desejado
     * 
     * @return Uma string de tamanho {@code blockSize} que tem em seu meio a
     * string {@code str}.
     */
    
    public static String centerStrOnABlock(String str, int blockSize)
    {
        return alignCenter(str, blockSize);
    }
    
    /**
     * Conta quantos caracteres iguais ao da variavel {@code c} existem em
     * {@code str}.
     * 
     * @param c caractere a ser procurado
     * @param str string a ser percorrida
     * 
     * @return Quantos caracteres iguais ao da variavel {@code c} existem em
     * {@code str}.
     */
    
    public static int countChars(char c, String str)
    {
        int times = 0;
        int length = str.length();

        for (int i = 0; i < length; i++)
        {
            if (str.charAt(i) == c)
            {
                times++;
            }
        }

        return times;
    }
    
    /**
     * Gera uma nova string sem o caractere no indice {@code index} da string
     * {@code str}.
     * 
     * @param index indice do caractere a ser removido
     * @param str string de referencia
     * 
     * @return Uma nova string sem o caractere no indice {@code index} da string
     * {@code str}.
     */
    
    public static String removeCharAt(int index, String str)
    {
        String newStr = "";
        
        if (Array.exists(str))
        {
            int length = str.length();
            
            if (!Array.indexIsOutOfBounds(index, length))
            {
                for (int i = 0; i < index; i++)
                {
                    newStr += str.charAt(i);
                }
                
                for (int i = index + 1; i < length; i++)
                {
                    newStr += str.charAt(i);
                }
            }
        }
        
        return newStr;
    }
    
    /**
     * Gera uma nova string sem o ultimo caractere da string {@code str}.
     * 
     * @param str string de referencia
     * 
     * @return Uma nova string sem o ultimo caractere da string {@code str}.
     */
    
    public static String removeLastChar(String str)
    {
        String newStr = "";
        
        if (Array.exists(str))
        {
            newStr = removeCharAt(str.length() - 1, str);
        }
        
        return newStr;
    }
    
    /**
     * Faz a conversao de arranjo de caracteres para String
     * 
     * @param charArray arranjo de caracteres a ser convertido
     * 
     * @return String com os mesmos caracteres do arranjo na mesma ordem
     */
    
    public static String charArrayToString(char[] charArray)
    {
        String str = "";
        
        for (char c : charArray)
        {
            str += c;
        }
        
        return str;
    }
    
    /**
     * Subtitui o caractere no indice {@code index} da string {@code str} pelo
     * caractere {@code character}.
     * 
     * @param index indice do caractere a ser substituido
     * @param character caractere a ser colocado no lugar
     * @param str string de referencia
     * 
     * @return Clone de {@code str} com o caractere no indice {@code index}
     * substituido pelo caractere {@code character}.
     */
    
    public static String setCharAt(int index, char character, String str)
    {
        String newStr = "";
        
        if (Array.exists(str))
        {
            int length = str.length();
            
            if (!Array.indexIsOutOfBounds(index, length))
            {
                for (int i = 0; i < index; i++)
                {
                    newStr += str.charAt(i);
                }
                
                newStr += character;
                
                for (int i = index + 1; i < length; i++)
                {
                    newStr += str.charAt(i);
                }
            }
        }
        
        return newStr;
    }
    
    /**
     * Inverte/espelha a string {@code str} em relacao ao seu meio.
     * 
     * @param str string de referencia
     * 
     * @return A string {@code str} invertida/espelhada em relacao ao seu meio.
     */
    
    public static String invert(String str)
    {
        String invertedStr = "";
        
        if (Array.exists(str))
        {
            int length = str.length();
            
            for (int i = length - 1; i > -1; i--)
            {
                invertedStr += str.charAt(i);
            }
        }
        
        return invertedStr;
    }
    
    /**
     * Checa se {@code str} tem a subcadeia {@code substring} comecando no
     * indice {@code startIndex}. Caso tiver, o indice final da subcadeia em
     * {@code str} e' retornado. Caso contrario, o retorno e' -1.
     * 
     * @param startIndex indice inicial
     * @param substring subcadeia a ser procurada
     * @param str string de referencia
     * 
     * @return O indice final da subcadeia em {@code str}. Caso {@code str} nao
     * tenha a subcadeia comecando no indice {@code startIndex}, o retorno e'
     * -1.
     */
    
    public static int hasSubstringAt(int startIndex, String substring, String str)
    {
        int endingIndex = -1;
        
        if (Array.exists(substring, str))
        {
            int substringLength = substring.length();
            int strLength = str.length();
            
            if (!Array.rangeIsOutOfBounds(startIndex, substringLength, strLength) &&
                str.substring(startIndex, startIndex + substringLength).equals(substring))
            {
                endingIndex = startIndex + substringLength;
            }
        }
        
        return endingIndex;
    }
    
    /**
     * Checa se {@code reference} casa com o padrao {@code regex}.
     * 
     * @param regex padrao de casamento
     * @param reference string de referencia
     * 
     * @return {@code true} se {@code reference} casa com o padrao
     * {@code regex}. Caso contrario, {@code false}.
     */
    
    public static boolean matches(String regex, String reference)
    {
        boolean matches = false;
        
        if (Array.exists(regex, reference))
        {
            matches = Pattern.compile(regex).matcher(reference).matches();
        }
        
        return matches;
    }
    
    /**
     * Checa se {@code reference} casa com o padrao {@code regex} sendo usadas
     * as flags da classe {@link Pattern}.
     * 
     * @param regex padrao de casamento
     * @param reference string de referencia
     * @param flags adicao das flags desejadas
     * 
     * @return {@code true} se {@code reference} casa com o padrao
     * {@code regex}. Caso contrario, {@code false}.
     */
    
    public static boolean matches(String regex, String reference, int flags)
    {
        boolean matches = false;
        
        if (Array.exists(regex, reference))
        {
            matches = Pattern.compile(regex, flags).matcher(reference).matches();
        }
        
        return matches;
    }
    
    /**
     * Checa se {@code reference} casa com o padrao {@code regex} sendo usada
     * a flag {@code CASE_INSENSITIVE} da classe {@link Pattern}.
     * 
     * @param regex padrao de casamento
     * @param reference string de referencia
     * 
     * @return {@code true} se {@code reference} casa com o padrao
     * {@code regex}. Caso contrario, {@code false}.
     */
    
    public static boolean matchesCaseInsensitive(String regex, String reference)
    {
        return matches(regex, reference, Pattern.CASE_INSENSITIVE);
    }
    
    /**
     * Checa se {@code str1} e' igual a {@code str2} ignorando diferencas entre
     * minusculas e maiusculas.
     * 
     * @param str1 primeira string de referencia
     * @param str2 segunda string de referencia
     * 
     * @return {@code true} se {@code str1} e' igual a {@code str2} ignorando
     * diferencas entre minusculas e maiusculas. Caso contrario, {@code false}.
     */
    
    public static boolean equalsCaseInsensitive(String str1, String str2)
    {
        boolean equals = false;
        
        if (Array.exists(str1, str2))
        {
            equals = matchesCaseInsensitive(Pattern.quote(str1), str2);
        }
        
        return equals;
    }
    
    /**
     * Remove todos os padroes {@code regex} da string {@code str}.
     * 
     * @param regex padrao de casamento
     * @param str string de referencia
     * 
     * @return String resultante da remocao de todos os padroes {@code regex}
     * da string {@code str}.
     */
    
    public static String removePattern(String regex, String str)
    {
        String newStr = "";
        
        if (Array.exists(regex, str))
        {
            newStr = Pattern.compile(regex).matcher(str).replaceAll("");
        }
        
        return newStr;
    }
    
    /**
     * Remove todas as ocorrencias de {@code substring} em {@code str}.
     * 
     * @param substring subcadeia a ser removida
     * @param str string de referencia
     * 
     * @return String resultante da remocao de todas as ocorrencias de
     * {@code substring} em {@code str}.
     */
    
    public static String removeSubstring(String substring, String str)
    {
        String newStr = "";
        
        if (Array.exists(substring))
        {
            newStr = removePattern(Pattern.quote(substring), str);
        }
        
        return newStr;
    }
    
    /**
     * Gera uma string resultante da remocao de todos os espacos em branco da
     * string {@code str}.
     * 
     * @param str string de referencia
     * 
     * @return Uma string resultante da remocao de todos os espacos em branco da
     * string {@code str}.
     */
    
    public static String removeAllWhiteSpaces(String str)
    {
        String newStr = null;
        
        if (Array.exists(str))
        {
            newStr = removePattern(" *", str);
        }
        
        return newStr;
    }
    
    /**
     * Checa se existe algum caractere de quebra de linha num dado caractere
     * @param input caractere a ser analisado
     * @return true se o caractere for algum dos que marcam a quebra de linha
     */
    
    public static boolean newLineOnInput(char input)
    {
        return AxellIO.LINE_SEPARATOR.contains(input + "");
    }
    
    /**
     * Checa se um determinado caractere esta' num intervalo de caracteres
     * @param input caractere a ser analisado
     * @param lowerLimit limite inferior do intervalo
     * @param upperLimit limite superior do intervalo
     * @return true se o caractere estiver no intervalo e false se nao estiver
     */
    
    public static boolean isOnInterval(char input, char lowerLimit, char upperLimit)
    {
        return input >= lowerLimit && input <= upperLimit;
    }
    
    public static boolean isDigit(char input)
    {
        return isOnInterval(input, '0', '9');
    }
    
    public static boolean isLowerCase(char input)
    {
        return isOnInterval(input, 'a', 'z');
    }
    
    public static boolean isUpperCase(char input)
    {
        return isOnInterval(input, 'A', 'Z');
    }
    
    public static boolean isLetter(char input)
    {
        return isLowerCase(input) || isUpperCase(input);
    }
    
    public static boolean isFloat(char input)
    {
        return isDigit(input) || input == '.';
    }
    
    public static boolean isString(char input)
    {
        return !newLineOnInput(input) && input != ' ';
    }
    
    /**
     * Checa se {@code data} tem um ou nenhum ponto final.
     * 
     * @param data String a ser analisada
     * 
     * @return {@code true} se {@code data} tem um ou nenhum ponto final. Caso
     * contrario, {@code false}.
     */
    
    public static boolean hasOneOrNoneDot(String data)
    {
        return Array.exists(data) && /*data.charAt(0) != '.' &&*/ MyString.countChars('.', data) <= 1;
    }
    
    /**
     * Checa se um determinado caractere esta' num intervalo especifico de caracteres
     * @param input caractere a ser analisado
     * @param accept caractere que simboliza o intervalo especifico de caracteres:
     * d - digits (0-9)
     * u - upperCases (ABC)
     * l - lowerCases (abc)
     * a - alphabet (ABCabc)
     * f - float (4.5) (aceita multiplos pontos ".", cuidar desse caso)
     * s - string (qualquer coisa diferente de um espaco em branco e uma quebra de linha)
     * 
     * @return true se o caractere estiver no intervalo e false caso nao esteja
     */
    
    public static boolean isOnInterval(char input, char accept)
    {
        boolean bool = false;

        switch (accept)
        {
            case 'd':
                bool = isDigit(input);
                break;

            case 'u':
                bool = isUpperCase(input);
                break;

            case 'l':
                bool = isLowerCase(input);
                break;

            case 'a': // alphabet
                bool = isLetter(input);
                break;

            case 'f':
                bool = isFloat(input);
                break;
                    
            case 's':
                bool = isString(input);
                break;
        }

        return bool;
    }
    
    /**
     * Checa se um determinado caractere esta' em algum intervalo usual de caracteres
     * @param input caractere a ser analisado
     * @param accept arranjo de caracteres que simbolizam os intervalos
     * especificos a serem aceitos:
     * d - digits (0-9)
     * u - upperCases (ABC)
     * l - lowerCases (abc)
     * a - alphabet (ABCabc)
     * f - float (4.5) (aceita multiplos pontos ".", cuidar desse caso)
     * s - string (qualquer coisa diferente de um espaco em branco e uma quebra de linha)
     * 
     * @return true se o caractere estiver no intervalo e false caso nao esteja
     */
    
    public static boolean isOnInterval(char input, char[] accept)
    {
        boolean bool = false;
        int index = 0;

        while (index < accept.length && bool == false)
        {
            switch (accept[index])
            {
                case 'd':
                    bool = isDigit(input);
                    break;

                case 'u':
                    bool = isUpperCase(input);
                    break;

                case 'l':
                    bool = isLowerCase(input);
                    break;

                case 'a': // alphabet
                    bool = isLetter(input);
                    break;

                case 'f':
                    bool = isFloat(input);
                    break;
                    
                case 's':
                    bool = isString(input);
                    break;
            }

            index++;
        }

        return bool;
    }
    
    /**
     * Checa se uma String contem apenas caracteres especificos
     * @param str String a ser analisada
     * @param accept caractere que simboliza o intervalo especifico de caracteres:
     * d - digits (0-9)
     * u - upperCases (ABC)
     * l - lowerCases (abc)
     * a - alphabet (ABCabc)
     * f - float (4.5) (aceita multiplos pontos ".", cuidar desse caso)
     * s - string (qualquer coisa diferente de um espaco em branco e uma quebra de linha)
     * 
     * @return true se a String tiver apenas os caracteres especificos, caso contrario, false
     */
    
    public static boolean isSpecificString(String str, char accept)
    {
        if (str == null || str.length() == 0) return false;
        
        char firstChar = str.charAt(0);
        int length = str.length();
        
        boolean isValid = isOnInterval(firstChar, accept) ||
                ((accept == 'd' || accept == 'f') && firstChar == '-' && length > 1);
        
        for (int i = 1; i < length && isValid; i++)
        {
            isValid = isOnInterval(str.charAt(i), accept);
        }
        
        return isValid;
    }
    
    public static int getint(String str)
    {
        return !isSpecificString(str, 'd') ? 0 : Integer.parseInt(str);
    }
    
    public static Integer getInt(String str)
    {
        return !isSpecificString(str, 'd') ? null : Integer.valueOf(str);
    }
    
    public static double getdouble(String str)
    {
        if (isSpecificString(str, 'f'))
        {
            return !hasOneOrNoneDot(str) ? 0.0 : Double.parseDouble(str);
        }
        
        else
        {
            return 0.0;
        }
    }
    
    public static Double getDouble(String str)
    {
        if (isSpecificString(str, 'f'))
        {
            return !hasOneOrNoneDot(str) ? null : Double.valueOf(str);
        }
        
        else
        {
            return null;
        }
    }
    
    public static Boolean getBoolean(String str)
    {
        switch (str)
        {
            case "true":
            case "T":
            case "1":
                return true;
                
            case "false":
            case "F":
            case "0":
                return false;
                
            default:
                return null;
        }
    }
    
    public static boolean getboolean(String str)
    {
        Boolean bool = getBoolean(str);
        
        return ( Array.exists(bool) ? bool : false );
    }
    
    // ----------------------- METODOS NAO ESTATICOS
    
    /**
     * @return String deste objeto
     */
    
    @Override
    public String toString()
    {
        return str;
    }
    
    /**
     * @return Tamanho da string deste objeto.
     */
    
    public int length()
    {
        return str.length();
    }
    
    /**
     * @return String deste objeto
     */
    
    public String get()
    {
        return toString();
    }
    
    /**
     * Substitui a string deste objeto por {@code newStr}.
     * 
     * <p>Obs.: Nao e' permitida string nula</p>
     * 
     * @param newStr nova string do objeto
     */
    
    public void set(String newStr)
    {
        if (Array.exists(newStr))
        {
            this.str = newStr;
        }
    }
    
    /**
     * @return Novo objeto {@code MyString} com a mesma string deste objeto.
     */
    
    @Override
    public MyString clone()
    {
        return convert(get());
    }
    
    /**
     * Checa se este objeto e o objeto {@code object} tem a mesma representacao
     * textual.
     * 
     * @param object objeto a ser analisado
     * 
     * @return {@code true} se este objeto e o objeto {@code object} tem a mesma
     * representacao textual. Caso contrario, {@code false}.
     */
    
    @Override
    public boolean equals(Object object)
    {
        boolean equals = Array.exists(object);
        
        if (equals)
        {
            equals = get().equals(object);
        }
        
        return equals;
    }
    
    /**
     * @return {@code true} se este objeto estiver com a cadeia vazia "". Caso
     * contrario, {@code false}.
     */
    
    public boolean isEmpty()
    {
        return equals(EMPTY);
    }
    
    /**
     * Obtem o caractere no indice {@code index} da string deste objeto.
     * 
     * @param index indice do caractere
     * 
     * @return '\0' caso o indice seja invalido. Caso contrario, o caractere no
     * indice {@code index} da string deste objeto.
     */
    
    public char getCharAt(int index)
    {
        char c = '\0';
        
        if (!Array.indexIsOutOfBounds(index, length()))
        {
            c = get().charAt(index);
        }
        
        return c;
    }
    
    /**
     * Obtem o primeiro caractere da string deste objeto. Caso ela esteja vazia,
     * e' retornada uma string vazia.
     * 
     * @return O primeiro caractere da string deste objeto. Caso ela esteja
     * vazia, e' retornada uma string vazia.
     */
    
    public MyString getFirstChar()
    {
        return convert( getFirstChar(get()) );
    }
    
    /**
     * Obtem o ultimo caractere da string deste objeto. Caso ela esteja vazia,
     * e' retornada uma string vazia.
     * 
     * @return O ultimo caractere da string deste objeto. Caso ela esteja vazia,
     * e' retornada uma string vazia.
     */
    
    public MyString getLastChar()
    {
        return convert( getLastChar(get()) );
    }
    
    /**
     * Gera um novo objeto {@code MyString} sem o caractere no indice
     * {@code index} da string deste objeto.
     * 
     * @param index indice do caractere a ser removido
     * 
     * @return Um novo objeto {@code MyString} sem o caractere no indice
     * {@code index} da string deste objeto.
     */
    
    public MyString removeCharAt(int index)
    {
        return convert( removeCharAt(index, get()) );
    }
    
    /**
     * Gera um novo objeto {@code MyString} sem o ultimo caractere da string
     * deste objeto.
     * 
     * @return Um novo objeto {@code MyString} sem o ultimo caractere da string
     * deste objeto.
     */
    
    public MyString removeLastChar()
    {
        return convert( removeLastChar(get()) );
    }
    
    /**
     * Subtitui o caractere no indice {@code index} da string deste objeto pelo
     * caractere {@code character}.
     * 
     * @param index indice do caractere a ser substituido
     * @param character caractere a ser colocado no lugar
     */
    
    public void setCharAt(int index, char character)
    {
        set( setCharAt(index, character, get()) );
    }
    
    /**
     * Inverte/espelha a string deste objeto em relacao ao seu meio.
     * 
     * @return A string deste objeto invertida/espelhada em relacao ao seu meio.
     */
    
    public MyString invert()
    {
        return convert( invert(get()) );
    }
    
    /**
     * Checa se a string deste objeto tem a subcadeia {@code substring}
     * comecando no indice {@code startIndex}. Caso tiver, o indice final da
     * subcadeia na string deste objeto e' retornado. Caso contrario, o retorno
     * e' -1.
     * 
     * @param startIndex indice inicial
     * @param substring subcadeia a ser procurada
     * 
     * @return O indice final da subcadeia na string deste objeto. Caso a string
     * deste objeto nao tenha a subcadeia comecando no indice
     * {@code startIndex}, o retorno e' -1.
     */
    
    public int hasSubstringAt(int startIndex, String substring)
    {
        return hasSubstringAt(startIndex, substring, get());
    }
    
    /**
     * Checa se a string deste objeto casa com o padrao {@code regex}.
     * 
     * @param regex padrao de casamento
     * 
     * @return {@code true} se a string deste objeto casa com o padrao
     * {@code regex}. Caso contrario, {@code false}.
     */
    
    public boolean matches(String regex)
    {
        return Pattern.matches(regex, get());
    }
    
    /**
     * Checa se a string deste objeto casa com o padrao {@code regex} sendo
     * usadas as flags da classe {@link Pattern}.
     * 
     * @param regex padrao de casamento
     * @param flags adicao das flags desejadas
     * 
     * @return {@code true} se a string deste objeto casa com o padrao
     * {@code regex}. Caso contrario, {@code false}.
     */
    
    public boolean matches(String regex, int flags)
    {
        return Pattern.compile(regex, flags).matcher(get()).matches();
    }
    
    /**
     * Checa se a string deste objeto casa com o padrao {@code regex} sendo
     * usada a flag {@code CASE_INSENSITIVE} da classe {@link Pattern}.
     * 
     * @param regex padrao de casamento
     * 
     * @return {@code true} se a string deste objeto casa com o padrao
     * {@code regex}. Caso contrario, {@code false}.
     */
    
    public boolean matchesCaseInsensitive(String regex)
    {
        return matches(regex, get(), Pattern.CASE_INSENSITIVE);
    }
    
    /**
     * Checa se a string deste objeto e' igual a {@code str} ignorando
     * diferencas entre minusculas e maiusculas.
     * 
     * @param str string de referencia
     * 
     * @return {@code true} se a string deste objeto e' igual a {@code str}
     * ignorando diferencas entre minusculas e maiusculas. Caso contrario,
     * {@code false}.
     */
    
    public boolean equalsCaseInsensitive(String str)
    {
        return equalsCaseInsensitive(get(), str);
    }
    
    /**
     * Remove todos os padroes {@code regex} da string deste objeto.
     * 
     * @param regex padrao de casamento
     * 
     * @return String resultante da remocao de todos os padroes {@code regex}
     * da string deste objeto.
     */
    
    public MyString removePattern(String regex)
    {
        return convert( removePattern(regex, get()) );
    }
    
    /**
     * Remove todas as ocorrencias de {@code substring} na string deste objeto.
     * 
     * @param substring subcadeia a ser removida
     * 
     * @return String resultante da remocao de todas as ocorrencias de
     * {@code substring} na string deste objeto.
     */
    
    public MyString removeSubstring(String substring)
    {
        return convert( removeSubstring(substring, get()) );
    }
    
    /**
     * Gera uma string resultante da remocao de todos os espacos em branco da
     * string deste objeto.
     * 
     * @return Uma string resultante da remocao de todos os espacos em branco da
     * string deste objeto.
     */
    
    public MyString removeAllWhiteSpaces()
    {
        return convert( removeAllWhiteSpaces(get()) );
    }
    
    /**
     * @return String deste objeto sem espacos em branco no final e no inicio.
     */
    
    public MyString trim()
    {
        return convert( get().trim() );
    }
    
    /**
     * Compara a string deste objeto 'a {@code str} lexicograficamente.
     * 
     * <p>Obs.1: caso {@code str} seja {@code null}, Integer.MAX_VALUE e'
     * retornado.</p>
     * 
     * <p>Obs.2: a comparacao lexicografica e' semelhante 'a comparacao
     * alfabetica, porem e' feita de acordo com os codigos decimais dos
     * caracteres.</p>
     * 
     * <p>Ex: "A" vem antes de "a" na ordem lexicografica, pois o codigo
     * decimal de 'A' e' menor que o de 'a'.</p>
     * 
     * @param str string a se comparar
     * 
     * @return 0 se as strings forem iguais; um valor negativo se a string deste
     * objeto vier antes de {@code str} na ordem lexicografica e um valor
     * positivo se vier depois.
     */
    
    public int compareTo(String str)
    {
        int difference = Integer.MAX_VALUE;
        
        if (Array.exists(str))
        {
            difference = get().compareTo(str);
        }
        
        return difference;
    }
    
    /**
     * Compara a string deste objeto 'a string de {@code myStr}
     * lexicograficamente.
     * 
     * <p>Obs.1: caso {@code myStr} seja {@code null}, Integer.MAX_VALUE e'
     * retornado.</p>
     * 
     * <p>Obs.2: a comparacao lexicografica e' semelhante 'a comparacao
     * alfabetica, porem e' feita de acordo com os codigos decimais dos
     * caracteres.</p>
     * 
     * <p>Ex: "A" vem antes de "a" na ordem lexicografica, pois o codigo
     * decimal de 'A' e' menor que o de 'a'.</p>
     * 
     * @param myStr objeto com a string a ser comparada
     * 
     * @return 0 se as strings forem iguais; um valor negativo se a string deste
     * objeto vier antes da string de {@code myStr} na ordem lexicografica e um
     * valor positivo se vier depois.
     */
    
    public int compareTo(MyString myStr)
    {
        int difference = Integer.MAX_VALUE;
        
        if (Array.exists(myStr))
        {
            difference = compareTo(myStr.get());
        }
        
        return difference;
    }
    
    /**
     * Cria uma nova string onde primeiro vem a string {@code str} e depois a
     * string deste objeto.
     * 
     * @param str string a ser a primeira
     * 
     * @return Uma nova string onde primeiro vem a string {@code str} e depois a
     * string deste objeto.
     */
    
    public MyString prepend(String str)
    {
        return convert(str + get());
    }
    
    /**
     * Cria uma nova string onde primeiro vem a string de {@code myStr} e depois
     * a string deste objeto.
     * 
     * @param myStr string a ser a primeira
     * 
     * @return Uma nova string onde primeiro vem a string de {@code myStr} e depois
     * a string deste objeto.
     */
    
    public MyString prepend(MyString myStr)
    {
        return convert(myStr + get());
    }
    
    public MyString substring(int startIndex, int substringLength)
    {
        MyString mySubstring = null;
        
        if (!Array.rangeIsOutOfBounds(startIndex, substringLength, length()))
        {
            mySubstring = convert( get().substring(startIndex, startIndex + substringLength) );
        }
        
        return mySubstring;
    }
    
    public Integer getInt()
    {
        return getInt(get());
    }
    
    public Double getDouble()
    {
        return getDouble(get());
    }
    
    public Boolean getBoolean()
    {
        return getBoolean(get());
    }
    
    public boolean contains(String substring)
    {
        boolean contains = false;
        
        if (Array.exists(substring))
        {
            contains = get().contains(substring);
        }
        
        return contains;
    }
    
    public MyString toUpperCase()
    {
        return convert( get().toUpperCase() );
    }
    
    public MyString toLowerCase()
    {
        return convert( get().toLowerCase() );
    }
    
    public MyString replace(char charToFind, char charToReplace)
    {
        return convert( get().replace("" + charToFind, "" + charToReplace) );
    }
    
    public MyString replace(String strToFind, String strToReplace)
    {
        return convert( get().replace(strToFind, strToReplace) );
    }
    
    public MyString[] split(String delimiterRegex)
    {
        MyString[] myStrs = null;
        
        if (Array.exists(delimiterRegex))
        {
            String[] splitedStrs = get().split(delimiterRegex);
            myStrs = new MyString[splitedStrs.length];
            
            for (int i = 0; i < splitedStrs.length; i++)
            {
                myStrs[i] = convert(splitedStrs[i]);
            }
        }
        
        return myStrs;
    }
    
    /**
     * Faz o split da string deste objeto considerando a string " " como
     * delimitador.
     * 
     * @return split da string deste objeto considerando a string " " como
     * delimitador.
     */
    
    public MyString[] split()
    {
        return split(" ");
    }
}