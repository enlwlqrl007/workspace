package day1227.javaStudy;

public class JavaStudy01 {
    public static void main(String[] args) {
        Box<String> box1 = new Box<>();
        box1.content = "안녕하세요.";
        String str = box1.content;
        System.out.println(str);

        Box<Integer> box2 = new Box<>();
        box2.content = 100;
        int val = box2.content;
        System.out.println(val);

        
    }
}
