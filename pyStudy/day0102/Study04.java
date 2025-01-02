package day0102;

public class Study04 {
    public static void main(String[] args) {
        
        FourCal a = new FourCal();
        // a.setData(4,2);   생성자를 추가 안했을 경우 -> 메서드를 만들어서 사용한 것
        
        System.out.println(a.add());
        System.out.println(a.sub());
        System.out.println(a.mul());
        System.out.println(a.div());

    }
}
