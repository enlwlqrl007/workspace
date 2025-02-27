import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

public class Study11 {
    public static void main(String[] args) {
        try{
            Reader reader = new FileReader("study10.txt");

            // 문자(char) 읽기
            while (true) {
                int data = reader.read();
                if(data == -1) break;
                System.out.println((char)data);
            }
            reader.close();
            System.out.println("------------------");
            // 문자 배열로 읽기
            reader = new FileReader("study10.txt");
            char[] data = new char[100];
            while (true) {
                int num = reader.read(data);
                if(num == -1) break;
                for(int i=0; i<num; i++){
                    System.out.println(data[i]);
                }
            }
            reader.close();

        }catch(FileNotFoundException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
