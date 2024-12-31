import java.util.Scanner;

public class Study14 {
    public static void main(String[] args) throws Exception {
        String fileName = "study14.txt";
        Scanner scan = new Scanner(System.in);
        boolean flag = true;
        int op;

        while(flag) {
            showMenu();
            op = scan.nextInt();
            switch (op) {
                case 1:
                    System.out.print("날짜를 입력: ");
                    String date = scan.next();
                    System.out.print("내역을 입력: ");
                    String content = scan.next();
                    System.out.print("금액 입력: ");
                    String amount = scan.next();
                    MoneyManager mm = new MoneyManager(fileName, true, date, content, Integer.parseInt(amount));
                    mm.save(fileName);
                    break;

                case 2:
                    
                    break;

                case 3:
                    
                    break;

                case 4:
                    flag = false;
                    break;                    

                default:
                    break;
            }
        }

    }

    static void showMenu(){
        System.out.println("----------------");
        System.out.println("1. 수입 입력");
        System.out.println("2. 지출 입력");
        System.out.println("3. 내역 출력");
        System.out.println("4. 종료");
        System.out.println("----------------");
        System.out.println(">>");
    }

}
