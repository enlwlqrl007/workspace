public class Study05 {
    public static void main(String[] args) {
        
        String a = "Life is too short, You need Python";
        System.out.println(a.charAt(3));
        System.out.println(a.charAt(a.length()-2));

        System.out.println(a.substring(0, 4));       // "Life"
        System.out.println(a.substring(19));        // "You need Python"
        System.out.println(a.substring(0, 19));     // "Life is too short, "

        String str = "20241226Sunny";

        // 날짜와 날씨 분리
        String date = str.substring(0, 8);          // "20241226"
        String weather = str.substring(8);         // "Sunny"
        System.out.println(date);
        System.out.println(weather);
    }
}
