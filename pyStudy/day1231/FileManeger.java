import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Writer;

public class FileManeger {    
    //필드
    String fileName;

    //생성자
    public FileManeger(String fileName) {
        this.fileName = fileName;
    }

    //메소드
    public void saveData(String str) throws Exception {
        String data = this.loadData();
        OutputStream os = new FileOutputStream(this.fileName);
        Writer writer = new OutputStreamWriter(os, "UTF-8");                
        writer.write((data + str + "\n"));
        writer.flush();
        writer.close();
    }

    public String loadData() throws Exception{
        InputStream is = new FileInputStream(this.fileName);
        Reader reader = new InputStreamReader(is, "UTF-8");
        char[] data = new char[100];        
        int num = reader.read(data);        
        reader.close();
        String str = new String(data,0,num);
        return str;
    }
}