package day1230;

public class Study10 {
    public static void main(String[] args) {
        int num1 = 1;
        int num2 = 3;
        
        int s = mySum(num1,num2);

        System.out.println(s);
        sayHi();
    }

    // static : 정적변수
    static int mySum(int x, int y){
        int result = x + y;

        return result;
    }

    static void sayHi(){
        System.out.println("Hi~!");
    }

}
