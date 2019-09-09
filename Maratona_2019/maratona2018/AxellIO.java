import java.io.*;
import java.nio.charset.Charset;
import java.nio.channels.FileLock;
import java.nio.file.CopyOption;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.function.Consumer;
import java.util.regex.Pattern;

/**
 * @author Axell Brendow ( https://github.com/axell-brendow )
 */

public class AxellIO
{
	public static final String REGEX_SPACES = " *";
    public static final String REGEX_COMMA = REGEX_SPACES + "," + REGEX_SPACES;
    public static final String REGEX_DOT = REGEX_SPACES + "\\." + REGEX_SPACES;
    public static final String REGEX_INT = REGEX_SPACES + "\\d+" + REGEX_SPACES;
    public static final String REGEX_PHRASE = "\\w+( \\w+)*";
    public static final String REGEX_PHRASES =
    	REGEX_PHRASE +
    	"((" + REGEX_COMMA + "|" + REGEX_DOT + ")" + REGEX_PHRASE + ")*";
    
    public static final String LINE_SEPARATOR =
            System.getProperty("java.vendor.url").equals("http://www.android.com/")
            ? "\n" + (char) 65535 : System.lineSeparator();

    public static final String LAST_LINE_CHAR = LINE_SEPARATOR.substring(LINE_SEPARATOR.length() - 1);
    private static boolean IOError = false;
    private static boolean endOfFile = false;
    
    private static PrintStream printStream = System.out;
    private static FileOutputStream fileOutputStream;
    private static FileLock outputFileLock;
    private static String charset = Charset.defaultCharset().name();
    //private static String charset = "ISO-8859-1";
    private static ArrayList<InputStream> inputStreamStack = new ArrayList<>();
    private static ArrayList<PrintStream> printStreamStack = new ArrayList<>();
    private static InputStream inputStream = System.in; // corrente de entrada padrao
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, Charset.forName(charset)));
    private static ByteArrayOutputStream inputStreamData; // buffer para guardar os dados da corrente de entrada
    private static FileInputStream fileInputStream;
    
    // ----------- FUNCOES DE REDIRECIONAMENTO DE ENTRADA E SAIDA -----------
    
    private static void setFileOutputStream(FileOutputStream fileOutputStream)
    {
        AxellIO.fileOutputStream = fileOutputStream;
    }
    
    private static boolean setPrintStream(PrintStream printStream)
    {
        boolean success = ( Array.exists(printStream) );
        
        if (!success)
        {
            printError("Corrente de impressao nula", "setPrintStream(PrintStream)");
        }
        
        else
        {
            AxellIO.printStream = printStream;
        }
        
        return success;
    }
    
    public static boolean setPrintStream(OutputStream outputStream)
    {
        boolean success = false;
        
        if (Array.exists(outputStream))
        {
            try
            {
                success = setPrintStream( new PrintStream(outputStream, true, charset) );
            }
            
            catch (UnsupportedEncodingException ex)
            {
                printError("Encoding/Charset invalido", "setPrintStream(OutputStream)");
            }
        }
        
        return success;
    }
    
    public static boolean setPrintStream(File file)
    {
        boolean success = false;
        
        if (Array.exists(file))
        {
            try
            {
                setFileOutputStream( new FileOutputStream(file) );
                success = setPrintStream(fileOutputStream);
            }
            
            catch (FileNotFoundException ex)
            {
                printError("Arquivo nao encontrado. (fileName = " + file.getName() + ")", "setPrintStream(File)");
            }
        }
        
        else
        {
            printError("Arquivo nulo", "setPrintStream(File)");
        }
        
        return success;
    }
    
    public static boolean setPrintStream(String fileName)
    {
        return setPrintStream(new File(fileName));
    }
    
    public static void savePrintStream()
    {
        printStreamStack.add(printStream);
    }
    
    public static void recoverSavedPrintStream()
    {
        if (!printStreamStack.isEmpty())
        {
            setPrintStream( printStreamStack.remove(printStreamStack.size() - 1) );
        }
    }
    
    /**
     * Atribui quais sao os dados da entrada padrao da classe (para serem recuperados posteriormente)
     * @param inputStreamData corrente de saida com os bytes da corrente de entrada
     */
    
    private static void setInputStreamData(ByteArrayOutputStream inputStreamData)
    {
        if (inputStreamData == null)
        {
            printError("Dados da corrente de entrada nulos", "setInputStreamData(ByteArrayOutputStream)");
        }
        
        else
        {
            AxellIO.inputStreamData = inputStreamData;
        }
    }
    
    /**
     * Define a entrada padrao da classe
     * 
     * @param inputStream nova entrada padrao da classe
     */
    
    public static void setInputStream(InputStream inputStream)
    {
        if (inputStream == null)
        {
            printError("Corrente de entrada nula", "setInputStream(InputStream)");
        }
        
        else
        {
            AxellIO.inputStream = inputStream;
            
            redefineReader();
            resetEOFAndIOError();
        }
    }
    
    public static boolean setInputStream(String fileName)
    {
        boolean success = false;
        
        if (Array.exists(fileName))
        {
            try
            {
                setInputStream( new FileInputStream( new File(fileName) ) );
                success = true;
            }
            
            catch (FileNotFoundException ex)
            {
                printFileError("Arquivo nao encontrado", fileName, "setInputStream(File)");
            }
        }
        
        else
        {
            printError("Arquivo nulo", "setInputStream(File)");
        }
        
        return success;
    }
    
    public static boolean setInputStream(File file)
    {
        boolean success = false;
        
        if (Array.exists(file))
        {
            try
            {
                setInputStream( new FileInputStream(file) );
                success = true;
            }
            
            catch (FileNotFoundException ex)
            {
                printFileError("Arquivo nao encontrado", file, "setInputStream(File)");
            }
        }
        
        else
        {
            printError("Arquivo nulo", "setInputStream(File)");
        }
        
        return success;
    }
    
    public static void saveInputStream()
    {
        inputStreamStack.add(inputStream);
    }
    
    public static void recoverSavedInputStream()
    {
        if (!inputStreamStack.isEmpty())
        {
            setInputStream( inputStreamStack.remove(inputStreamStack.size() - 1) );
        }
    }
    
    /**
     * Muda o charset padrao da classe
     * 
     * @param charset novo charset
     */
    
    public static void setCharset(String charset)
    {
        AxellIO.charset = charset;
        
        redefineReader();
    }
    
    // ----------- FUNCOES DE SAIDA DE DADOS -----------
    
    public static void printErr(Object data)
    {
        System.err.print(data);
    }
    
    public static void printlnErr()
    {
    	printErr(LINE_SEPARATOR);
    }
    
    public static void printlnErr(Object data)
    {
    	printErr(data + LINE_SEPARATOR);
    }
    
    public static void printS(Object data)
    {
        System.out.print(data);
    }
    
    public static void printlnS()
    {
    	printS(LINE_SEPARATOR);
    }
    
    public static void printlnS(Object data)
    {
    	printS(data + LINE_SEPARATOR);
    }
    
    public static void print(Object data)
    {
        try
        {
            new PrintStream(printStream, true, charset).print(data);
        }
        
        catch (UnsupportedEncodingException ex){}
    }
    
    public static void println()
    {
        print(LINE_SEPARATOR);
    }
    
    public static void println(Object data)
    {
        print(data + LINE_SEPARATOR);
    }
    
    // ----------- FUNCOES DE UTILIDADE -----------
    
    private static void resetEOFAndIOError()
    {
        IOError = false;
        endOfFile = false;
    }
    
    private static String createFileErrorMsg(String msg, String fileName)
    {
        return
        	( Array.exists(msg) ? msg : "Erro" ) +
        	" (fileName = " +
        	( Array.exists(fileName) ? fileName : "unknown" ) + ")";
    }
    
    private static String createFileErrorMsg(String msg, File file)
    {
        String errorMsg = "";
        
        if (Array.exists(file))
        {
            errorMsg = createFileErrorMsg(msg, file.getName());
        }
        
        return errorMsg;
    }
    
    public static void printError(Class myClass, String errorMessage, String methodReference)
    {
        if (Array.exists(myClass, errorMessage, methodReference))
        {
            String errorMsg = ( errorMessage.isEmpty() ? "Mensagem de erro nao encontrada" : errorMessage );
            printlnErr("[" + myClass.getName() + "]: " + errorMsg + ". - funcao " + methodReference);
        }
    }
    
    private static void printError(String errorMessage, String methodReference)
    {
        printError(AxellIO.class, errorMessage, methodReference);
    }
    
    public static void printFileError(Class myClass, String errorMessage, String fileName, String methodReference)
    {
        printError(myClass, createFileErrorMsg(errorMessage, fileName), methodReference);
    }
    
    public static void printFileError(Class myClass, String errorMessage, File file, String methodReference)
    {
        printError(myClass, createFileErrorMsg(errorMessage, file), methodReference);
    }
    
    private static void printFileError(String errorMessage, String fileName, String methodReference)
    {
        printError(AxellIO.class, createFileErrorMsg(errorMessage, fileName), methodReference);
    }
    
    private static void printFileError(String errorMessage, File file, String methodReference)
    {
        printError(AxellIO.class, createFileErrorMsg(errorMessage, file), methodReference);
    }
    
    public static void closePrintStream(PrintStream printStream)
    {
        if (Array.exists(printStream))
        {
            printStream.close();
        }
    }
    
    public static boolean closeOutputStream(OutputStream outputStream)
    {
        boolean success = false;
        
        if (Array.exists(outputStream))
        {
            try
            {
                outputStream.close();
                success = true;
            }
            
            catch (IOException ex)
            {
                printError(AxellIO.class, "Nao foi possivel fechar a corrente de saida", "closeOutputStream(OutputStream)");
            }
        }
        
        return success;
    }
    
    public static boolean closeInputStream(InputStream inputStream)
    {
        boolean success = false;
        
        if (Array.exists(inputStream))
        {
            try
            {
                inputStream.close();
                success = true;
            }
            
            catch (IOException ex)
            {
                printError(AxellIO.class, "Nao foi possivel fechar a corrente de entrada", "closeInputStream(InputStream)");
            }
        }
        
        return success;
    }
    
    public static boolean createFile(File file)
    {
        boolean success = false;
        
        if (Array.exists(file))
        {
            try
            {
                file.createNewFile();
                success = true;
            }

            catch (IOException ex)
            {
                printFileError("Nao foi possivel criar o arquivo", file, "createFile(File)");
            }
        }
        
        return success;
    }
    
    public static FileInputStream createFileInputStream(File file)
    {
        FileInputStream fileInputStream = null;
        
        if (Array.exists(file))
        {
            try
            {
                fileInputStream = new FileInputStream(file);
            }

            catch (FileNotFoundException ex)
            {
                fileInputStream = null;
                printFileError("Arquivo nao encontrado", file, "createFileInputStream(File)");
            }
        }
        
        return fileInputStream;
    }
    
    public static FileOutputStream createFileOutputStream(File file)
    {
        FileOutputStream fileOutputStream = null;
        
        if (Array.exists(file))
        {
            try
            {
                fileOutputStream = new FileOutputStream(file);
            }

            catch (FileNotFoundException ex)
            {
                fileOutputStream = null;
                printFileError("Arquivo nao encontrado", file, "createFileOutputStream(File)");
            }
        }
        
        return fileOutputStream;
    }
    
    public static ByteArrayOutputStream saveInputStreamData(InputStream inputStream)
    {
        ByteArrayOutputStream outputStream = null;
        
        if (Array.exists(inputStream))
        {
            outputStream = new ByteArrayOutputStream(); // cria uma corrente de saida
            
            saveInputStream();
            setInputStream(inputStream);
            
            int charByte = readByte(); // le um caractere da corrente de entrada da classe

            while (isPossibleToRead()) // checa se o fim da corrente nao foi alcancado
            {
                outputStream.write(charByte); // escreve o caractere na corrente de saida

                charByte = readByte(); // le o proximo caractere da corrente de entrada da classe
            }
            
            recoverSavedInputStream();
        }
        
        return outputStream;
    }
    
    public static FileLock lockFileOutputStream(FileOutputStream fileOutputStream)
    {
        FileLock fileLock = null;
        
        if (Array.exists(fileOutputStream))
        {
            try
            {
                fileLock = fileOutputStream.getChannel().lock();
            }

            catch (IOException ex)
            {
                fileLock = null;
                printError("Nao foi possivel trancar a corrente de saida", "lockFileOutputStream(FileOutputStream)");
            }
        }
        
        return fileLock;
    }
    
    public static boolean unlock(FileLock fileLock)
    {
        boolean success = false;
        
        if (Array.exists(fileLock))
        {
            try
            {
                fileLock.release();
                success = true;
            }

            catch (IOException ex)
            {
                printError("Nao foi possivel destrancar o arquivo", "unlock(FileLock)");
            }
        }
        
        return success;
    }
    
    public static <T> boolean toFile(Iterable<T> iterable, File file, Consumer<Boolean> toDoBeforeClose)
    {
        boolean success = false;
        
        if (Array.exists(iterable))
        {
            savePrintStream();
            success = setPrintStream(file);
            
            if (success)
            {
                iterable.forEach( (element) -> println(element.toString()) );
                
                toDoBeforeClose.accept(success);
                
                closePrintStream();
            }
            
            recoverSavedPrintStream();
        }
        
        return success;
    }
    
    public static void closePrintStream()
    {
        closePrintStream(printStream);
    }
    
    public static boolean closeInputStream()
    {
        return closeInputStream(inputStream);
    }
    
    public static boolean hasIOError()
    {
        return IOError;
    }
    
    public static boolean endOfFile()
    {
        return endOfFile;
    }
    
    public static boolean isPossibleToRead()
    {
    	return !hasIOError() && !endOfFile();
    }
    
    public static boolean lockOutputFile()
    {
        return ( lockFileOutputStream(fileOutputStream) != null );
    }
    
    public static boolean unlockOutputFile()
    {
        return unlock(outputFileLock);
    }
    
    /**
     * Salva os dados (bytes) da corrente de entrada num campo da classe
     */
    
    public static void saveInputStreamData()
    {
        setInputStreamData( saveInputStreamData(inputStream) );
    }
    
    /**
     * Redefine o leitor da entrada padrao da classe
     */
    
    private static void redefineReader()
    {
        reader = new BufferedReader(new InputStreamReader(inputStream, Charset.forName(charset)));
    }
    
    /**
     * Recupera os ultimos dados da entrada padrao que tenham sido salvos pela funcao saveInputStreamData()
     */
    
    public static void recoverLastInputStreamData()
    {
        setInputStream( new ByteArrayInputStream(inputStreamData.toByteArray()) );
    }
    
    /**
     * Le a entrada padrao de {@link AxellIO} ate' o ultimo
     * \r ou \n da linha (depende do sistema operacional).
     */
    
    public static void skipLine()
    {
        while (isPossibleToRead() && !LAST_LINE_CHAR.equals(read() + ""));
    }
    
    /**
     * Le a entrada padrao de {@link AxellIO} ate' o ultimo
     * \r ou \n da linha (depende do sistema operacional).
     * O parametro {@code lastInput} e' usado para saber
     * se o ultimo caractere lido ja' nao e' o ultimo caractere
     * de uma linha.
     * 
     * @param lastInput Ultimo caractere lido.
     * 
     * @return {@code true} se {@code lastInput} ja' e' o ultimo
     * caractere de uma linha. Caso contrario, {@code false}.
     */
    
    public static boolean skipLine(char lastInput)
    {
    	boolean alreadyLastLineChar = true;
    	
        // so' limpa se a ultima leitura nao for o ultimo
    	// caractere que marca a quebra de linha
        if (!LAST_LINE_CHAR.equals(lastInput + ""))
        {
            skipLine();
            
            alreadyLastLineChar = false;
        }
        
        return alreadyLastLineChar;
    }
    
    /**
     * Le a entrada padrao {@link java.lang.System.in} ate' o ultimo
     * \r ou \n da linha (depende do sistema operacional).
     */
    
    public static void skipLineS()
    {
        while (isPossibleToRead() && !LAST_LINE_CHAR.equals(readS() + ""));
    }
    
    /**
     * Le a entrada padrao {@link java.lang.System.in} ate' o ultimo
     * \r ou \n da linha (depende do sistema operacional).
     * O parametro {@code lastInput} e' usado para saber
     * se o ultimo caractere lido ja' nao e' o ultimo caractere
     * de uma linha.
     * 
     * @param lastInput Ultimo caractere lido.
     * 
     * @return {@code true} se {@code lastInput} ja' e' o ultimo
     * caractere de uma linha. Caso contrario, {@code false}.
     */
    
    public static boolean skipLineS(char lastInput)
    {
    	boolean alreadyLastLineChar = true;
    	
        // so' limpa se a ultima leitura nao for o ultimo
    	// caractere que marca a quebra de linha
        if (!LAST_LINE_CHAR.equals(lastInput + ""))
        {
            skipLineS();
            
            alreadyLastLineChar = false;
        }
        
        return alreadyLastLineChar;
    }
    
    public static void pause()
    {
        while ( skipLineS( readS() ) );
    }
    
    public static void pause(String text)
    {
        printS(text);
        pause();
    }
    
    public static boolean copyChildsOf(File sourceFolder, File destinationFolder, CopyOption... copyOptions)
    {
        boolean success = false;
        
        if
        (
            Array.exists(sourceFolder, destinationFolder) &&
            sourceFolder.isDirectory() &&
            destinationFolder.exists() ? destinationFolder.isDirectory() :
            destinationFolder.mkdirs()
        )
        {
            success = true;
            
            String destFolderPathStr =
                    destinationFolder.getAbsolutePath() + File.separator;
            Path destPath;
            
            for (File file : sourceFolder.listFiles())
            {
                destPath = Paths.get(destFolderPathStr + file.getName());
                
                try
                {
                    Files.copy(file.toPath(), destPath, copyOptions);
                }
                
                catch (IOException ex)
                {
                    success = false;
                }
            }
        }
        
        return success;
    }
    
    public static boolean copyChildsOf(String sourceFolderStr, String destinationFolderStr, CopyOption... copyOptions)
    {
        boolean success = false;
        
        if (Array.exists(sourceFolderStr, destinationFolderStr))
        {
            success =
            copyChildsOf
            (
                new File(sourceFolderStr),
                new File(destinationFolderStr),
                copyOptions
            );
        }
        
        return success;
    }
    
    public static boolean copyFilesRecursively(File sourceFolder, File destinationFolder, CopyOption... copyOptions)
    {
        boolean success = false;
        
        if (Array.exists(sourceFolder, destinationFolder))
        {
            success = true;
            File[] folders = sourceFolder.listFiles((file)->file.isDirectory());
            File folder;
            File newDestFolderFile;
            
            String newDestFolder;
            String destFolder =
                    destinationFolder.getAbsolutePath() +
                    File.separator;
            
            for (int i = 0; success && i < folders.length; i++)
            {
                folder = folders[i];
                newDestFolder = destFolder + folder.getName();
                newDestFolderFile = new File(newDestFolder);
                
                success =
                copyFilesRecursively(folder, newDestFolderFile, copyOptions);
            }
            
            success = success &&
                    copyChildsOf(sourceFolder, destinationFolder, copyOptions);
        }
        
        return success;
    }
    
    // ----------- FUNCOES DE ENTRADA DE DADOS -----------
    
    /**
     * Le um byte da entrada padrao de {@link AxellIO}.
     * 
     * @return o byte lido.
     */
    
    public static int readByte()
    {
        int readByte = 0;
        
        try
        {
            readByte = reader.read();
            IOError = false;
        }
        
        catch (IOException ex)
        {
            IOError = true;
            printError("Nao foi possivel ler da entrada padrao", "readByte()");
        }
        
        endOfFile = ( readByte == -1 );
        
        return readByte;
    }
    
    /**
     * Le um byte da entrada padrao {@link java.lang.System.in}.
     * 
     * @return o byte lido.
     */
    
    public static int readByteS()
    {
        int readByte = 0;
        
        try
        {
            readByte = System.in.read();
            IOError = false;
        }
        
        catch (IOException ex)
        {
            IOError = true;
            printError("Nao foi possivel ler da entrada padrao", "readByteS()");
        }
        
        endOfFile = ( readByte == -1 );
        
        return readByte;
    }
    
    /**
     * Le um caractere da entrada padrao de {@link AxellIO}.
     * 
     * @return o caractere lido.
     */
    
    public static char read()
    {
        return (char) readByte();
    }
    
    /**
     * Le um caractere da entrada padrao {@link java.lang.System.in}.
     * 
     * @return o caractere lido.
     */
    
    public static char readS()
    {
        return (char) readByteS();
    }
    
    /**
     * Le uma String que tenha apenas alguns caracteres especificos
     * @param text texto a ser mostrado para o usuario antes da obtencao da String
     * @param accept arranjo de caracteres que simbolizam os intervalos
     * especificos a serem aceitos:
     * d - digits (0-9)
     * u - upperCases (ABC)
     * l - lowerCases (abc)
     * a - alphabet (ABCabc)
     * f - float (4.5) (aceita multiplos pontos ".", cuidar desse caso)
     * s - string (qualquer coisa diferente de um espaco em branco e uma quebra de linha)
     * 
     * @return {@code null} se o usuario nao informar os caracteres desejados.
     * Caso contrario, a string com os caracteres especificos.
     */
    
    public static String readSpecificString(String text, char[] accept)
    {
        String specificString = null;
        boolean isAcceptingNumber = Array.contains('d', accept) || Array.contains('f', accept);
        char input;
        
        print(text);

        do
        {
            input = read();
            
        } while (isPossibleToRead() && ( MyString.newLineOnInput(input) || input == ' ' ));

        if (isPossibleToRead() && ( MyString.isOnInterval(input, accept) || (isAcceptingNumber && input == '-') ))
        {
            specificString = "" + input;

            input = read();

            while (isPossibleToRead() && ( MyString.isOnInterval(input, accept) ))
            {
                specificString += input;
                input = read();
            }

            if (!isPossibleToRead() || (!MyString.newLineOnInput(input) && input != ' ' && input != ',') || (isAcceptingNumber && specificString.equals("-")))
            {
                specificString = null;
            }
        }
        
        skipLine(input);
        
        return specificString;
    }
    
    /**
     * Le uma String que tenha apenas alguns caracteres especificos
     * @param text texto a ser mostrado para o usuario antes da obtencao da String
     * @param accept caractere que simboliza o intervalo especifico de caracteres:
     * d - digits (0-9)
     * u - upperCases (ABC)
     * l - lowerCases (abc)
     * a - alphabet (ABCabc)
     * f - float (4.5) (aceita multiplos pontos ".", cuidar desse caso)
     * s - string (qualquer coisa diferente de um espaco em branco e uma quebra de linha)
     * 
     * @return {@code null} se o usuario nao informar os caracteres desejados.
     * Caso contrario, a string com os caracteres especificos.
     */
    
    public static String readSpecificString(String text, char accept)
    {
        return readSpecificString(text, new char[] { accept });
    }
    
    /**
     * Le uma linha da entrada padrao de {@link AxellIO}.
     * 
     * @return linha lida da entrada padrao de {@link AxellIO}.
     */
    
    public static String readLine()
    {
        char input = read();
        String line = "";
        
        while (isPossibleToRead() && !MyString.newLineOnInput(input))
        {
            line += input;
            input = read();
        }
        
        skipLine(input);
        
        return line;
    }
    
    /**
     * Le uma linha da entrada padrao {@link java.lang.System.in}.
     * 
     * @return linha lida da entrada padrao {@link java.lang.System.in}.
     */
    
    public static String readLineS()
    {
        char input = readS();
        String line = "";
        
        while (AxellIO.isPossibleToRead() && !MyString.newLineOnInput(input))
        {
            line += input;
            input = readS();
        }
        
        return line;
    }
    
    /**
     * Le as linhas da entrada padrao de {@link AxellIO} ate' encontrar uma
     * linha nao vazia.
     * 
     * @return Linha nao vazia lida da entrada padrao de {@link AxellIO}.
     */
    
    public static String readLinesUntilANonEmptyLine()
    {
        String line = readLine();
        
        while (isPossibleToRead() && line.isEmpty())
        {
            line = readLine();
        }
        
        return line;
    }
    
    /**
     * Le uma linha da entrada padrao de {@link AxellIO} e remove os espacos
     * em branco 'a esquerda e 'a direita.
     * 
     * @return Linha lida da entrada padrao de {@link AxellIO} com os espacos
     * em branco 'a esquerda e 'a direita removidos.
     */
    
    public static String readLineAndTrim()
    {
        return readLine().trim();
    }
    
    /**
     * Exibe a mensagem {@code text} e le uma linha da entrada padrao de
     * {@link AxellIO}.
     * 
     * @param text mensagem a ser exibida
     * 
     * @return Linha lida da entrada padrao de {@link AxellIO}.
     */
    
    public static String readLine(String text)
    {
        print(text);
        
        return readLine();
    }
    
    /**
     * Exibe a mensagem {@code text} e le uma linha da entrada padrao de
     * {@link AxellIO} e remove os espacos em branco 'a esquerda e 'a direita.
     * 
     * @param text mensagem a ser exibida
     * 
     * @return Linha lida da entrada padrao de {@link AxellIO} com os espacos
     * em branco 'a esquerda e 'a direita removidos.
     */
    
    public static String readLineAndTrim(String text)
    {
        return readLine(text).trim();
    }
    
    /**
     * Exibe a mensagem {@code text} e le uma linha da entrada padrao de
     * {@link AxellIO} e remove todos os espacos em branco.
     * 
     * @param text mensagem a ser exibida
     * 
     * @return Linha lida da entrada padrao de {@link AxellIO} com todos os
     * espacos em branco removidos.
     */
    
    public static String readLineAndRemoveAllWhiteSpaces(String text)
    {
        return MyString.removePattern(" *", readLine(text));
    }
    
    /**
     * Exibe a mensagem {@code text} e le uma linha da entrada padrao de
     * {@link AxellIO} e checa se ela casa com o padrao {@code regex}.
     * 
     * @param text mensagem a ser exibida
     * @param regex padrao de casamento
     * 
     * @return {@code null} se a linha lida da entrada padrao de {@link AxellIO}
     * nao casar com o padrao {@code regex}. Caso contrario, a linha lida.
     */
    
    public static String readLineWithRegex(String text, String regex)
    {
        String line = readLine(text);
        
        if (!Pattern.matches(regex, line))
        {
            line = null;
        }
        
        return line;
    }
    
    /**
     * Exibe a mensagem {@code text} e le uma linha da entrada padrao de
     * {@link AxellIO} e checa se ela casa com o padrao {@code regex}.
     * Posteriormente remove todos os espacos em branco que a linha tiver.
     * 
     * @param text mensagem a ser exibida
     * @param regex padrao de casamento
     * 
     * @return {@code null} se a linha lida da entrada padrao de {@link AxellIO}
     * nao casar com o padrao {@code regex}. Caso contrario, a linha lida com
     * todos os espacos em branco removidos.
     */
    
    public static String readLineWithRegexAndRemoveAllWhiteSpaces(String text, String regex)
    {
        String line = readLineWithRegex(text, regex);
        
        if (Array.exists(line))
        {
            line = MyString.removeAllWhiteSpaces(line);
        }
        
        return line;
    }
    
    public static String readLineWithRegexAndTrim(String text, String regex)
    {
        String line = readLineWithRegex(text, regex);
        
        if (Array.exists(line))
        {
            line = line.trim();
        }
        
        return line;
    }
    
    /**
     * O conjunto de strings {@code config} e' formado pelo seguinte padrao:
     * <p>text, regex, text, regex, ...</p>
     * 
     * <p>Onde "text" e' a mensagem a ser exibida antes de ler uma linha
     * da entrada padrao de {@link AxellIO}. E "regex" e' o padrao ao qual
     * a linha lida depois da mensagem "text" deve obdecer.</p>
     * 
     * @param config conjunto de strings no seguinte formato:
     * <p>text, regex, text, regex, ...</p>
     * 
     * @return {@code null} se alguma das linhas lidas nao obdecer ao respectivo
     * padrao regex. Caso contrario, um arranjo de strings com cada uma das
     * linhas lidas.
     */
    
    public static String[] readLinesWithRegex(String... config)
    {
        String[] lines = null;
        
        if (Array.exists((Object) config) && config.length > 0 && config.length % 2 == 0)
        {
            lines = new String[config.length / 2];
            int counterOfLines = 0;
            String auxLine = readLineWithRegex(config[counterOfLines], config[counterOfLines + 1]);
            
            while (Array.exists(auxLine) && counterOfLines < config.length - 1)
            {
                lines[counterOfLines] = auxLine;
                counterOfLines += 2;
                
                if (counterOfLines < config.length - 1)
                {
                    auxLine = readLineWithRegex(config[counterOfLines], config[counterOfLines + 1]);
                }
            }
            
            if (!Array.exists(auxLine))
            {
                lines = null;
            }
            
        }
        
        return lines;
    }
    
    /**
     * O conjunto de strings {@code config} e' formado pelo seguinte padrao:
     * <p>text, regex, text, regex, ...</p>
     * 
     * <p>Onde "text" e' a mensagem a ser exibida antes de ler uma linha
     * da entrada padrao de {@link AxellIO}. E "regex" e' o padrao ao qual
     * a linha lida depois da mensagem "text" deve obdecer.</p>
     * 
     * @param config conjunto de strings no seguinte formato:
     * <p>text, regex, text, regex, ...</p>
     * 
     * @return {@code null} se alguma das linhas lidas nao obdecer ao respectivo
     * padrao regex. Caso contrario, um arranjo de strings com cada uma das
     * linhas lidas sendo removidos todos os seus espacos em branco.
     */
    
    public static String[] readLinesWithRegexAndRemoveAllWhiteSpaces(String... config)
    {
        String[] lines = readLinesWithRegex(config);
        
        if (Array.exists((Object) lines))
        {
            for (int i = 0; i < lines.length; i++)
            {
                lines[i] = MyString.removeAllWhiteSpaces(lines[i]);
            }
        }
        
        return lines;
    }
    
    /**
     * Le linhas da entrada padrao de {@link AxellIO} ate' que alguma
     * case com o padrao {@code regex.
     * 
     * @param text mensagem a ser exibida
     * @param regex padrao de casamento
     * 
     * @return a ultima linha lida.
     */
    
    public static String readLineWithRegexUntilMatch(String text, String regex)
    {
		String line;
		
		do
		{
			line = readLineWithRegex(text, regex);
			
		} while (!Array.exists(line));
		
		return line;
    }
    
    public static String readString(String text)
    {
        return readSpecificString(text, 's');
    }
    
    public static int readint(String text)
    {
        String data = readSpecificString(text, 'd');
        return data == null ? 0 : Integer.parseInt(data);
    }

    public static Integer readInt(String text)
    {
        String data = readSpecificString(text, 'd');
        return data == null ? null : Integer.valueOf(data);
    }

    public static float readfloat(String text)
    {
        String data = readSpecificString(text, 'f');
        return !MyString.hasOneOrNoneDot(data) ? 0 : Float.parseFloat(data);
    }

    public static Float readFloat(String text)
    {
        String data = readSpecificString(text, 'f');
        return !MyString.hasOneOrNoneDot(data) ? null : Float.valueOf(data);
    }

    public static double readdouble(String text)
    {
        String data = readSpecificString(text, 'f');
        return !MyString.hasOneOrNoneDot(data) ? 0 : Double.parseDouble(data);
    }

    public static Double readDouble(String text)
    {
        String data = readSpecificString(text, 'f');
        return !MyString.hasOneOrNoneDot(data) ? null : Double.valueOf(data);
    }
}