import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class Study09 {
    public static void main(String[] args) throws Exception {
        String dogName = "C:/workspace/pyStudy/dog.png";
        String targetFileName = "C:/workspace/pyStudy/testFile.png";

        InputStream is = new FileInputStream(dogName);
        OutputStream os = new FileOutputStream(targetFileName);

        byte[] data = new byte[1024];
        while(true){
            int num = is.read(data);
            if(num == -1) break;
            os.write(data,0,num);
        }
            os.flush();
            os.close();
            is.close();

            System.out.println("복사완료!");   
    }
}
