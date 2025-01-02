package day0102;

class Family{
    static String lastName = "김";
}

public class Study06 {
    public static void main(String[] args) {
        System.out.println(Family.lastName);

        Family a = new Family();
        Family b = new Family();

        System.out.println(a.lastName);
        System.out.println(b.lastName);

        Family.lastName = "최";
        System.out.println(Family.lastName);
        System.out.println(a.lastName);
        System.out.println(b.lastName);

        a.lastName = "박";
        System.out.println(Family.lastName);
        System.out.println(a.lastName);
        System.out.println(b.lastName);


    }

}
