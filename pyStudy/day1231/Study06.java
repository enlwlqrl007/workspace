import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Study06 {
    public static void main(String[] args) {
        try{
            OutputStream os = new FileOutputStream("test4.db");

            byte[] array = {10, 20, 30, 40, 50};

            os.write(array, 1,3);
            
            os.flush();
            os.close();

        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
