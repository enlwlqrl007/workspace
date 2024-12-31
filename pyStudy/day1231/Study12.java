import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Writer;

public class Study12 {
    public static void main(String[] args) throws Exception{
        write("하이");
        
        String data = read();
        System.out.println("파일 읽은것: "+ data);
    }

    // throws Exception => try catch문이랑 똑같음
    public static void write(String str)throws Exception{
        OutputStream os = new FileOutputStream("study12.txt");
        Writer writer = new OutputStreamWriter(os,"UTF-8");
        writer.write(str); // str -> 파라미터로 받은거
        writer.flush();
        writer.close();
    }

    public static String read() throws Exception{
        InputStream is = new FileInputStream("study12.txt");
        Reader reader = new InputStreamReader(is, "UTF-8");
        char[] data = new char[100];
        int num = reader.read(data);
        reader.close();
        String str = new String(data, 0, num);
        return str;
    }
}
