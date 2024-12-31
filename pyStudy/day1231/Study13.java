import java.util.Scanner;

public class Study13 {
    public static void main(String[] args) throws Exception{
        FileManeger fm = new FileManeger("study13.txt");
        Scanner scan = new Scanner(System.in);
        boolean flag = true;

        while(flag){
            System.out.println("1. 입력\n"
                                +"2. 출력\n"
                                +"3. 종료\n");
            System.out.println("-------------");
            System.out.print(">>");
            int op = scan.nextInt() ;
            
            switch (op) {
                case 1 :
                    System.out.print("내용을 입력하세요 =>");
                    String str = scan.next();
                    fm.saveData(str);
                    break;

                case 2 :
                    String result = fm.loadData();
                    System.out.println(result);
                    break;

                case 3 :
                    flag = false;
                    break;            

                default:
                    System.out.println("잘못 입력하셨습니다.");
                    break;
            }
        }
    }
}