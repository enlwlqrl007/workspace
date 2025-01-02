package day0102;

class Calculator{
    int result = 0;

    int add(int num){
        this.result += num;

        return this.result;
    }
}

public class Study03 {
    public static void main(String[] args) {
        Calculator cal1 = new Calculator();
        Calculator cal2 = new Calculator();    

        System.out.println(cal1.add(3));
        System.out.println(cal1.add(4));

        System.out.println(cal2.add(3));
        System.out.println(cal2.add(7));
    }
    

    
}
