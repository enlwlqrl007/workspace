public class Study04 {
    public static void main(String[] args) {
        String a = "apple";
        String b = "banana";

        System.out.println(a);
        System.out.println(b);

        String food = "python's favorite food is perl";
        System.out.println(food);
        
        String say = "\"python\" is very easy. he says.";
        System.out.println(say);

        String multiline = """
                동해물과 백두산이
                마르고 닳도록
                하느님이 보우하사
                우리나라 만세!
                """;
        System.out.println(multiline);

        String firstName = "길동";
        String lastName = "홍";
        String t = lastName + firstName;
        System.out.println(t);

        String c = "뿅뿅";
        System.out.println(c.repeat(2));
        System.out.println("-".repeat(20));

        System.out.println(c.length());

    }
        
}
