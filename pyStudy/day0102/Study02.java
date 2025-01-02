package day0102;

public class Study02 {
    public static void main(String[] args) {
        String[] strArr = new String[10];
        

        System.out.println(strArr[0]);
        
        TestClass tc = new TestClass("노무현",70);
        tc.hobby[0] = "독서";
        System.out.println(tc.hobby[0]);

        TestClass[] tcs = new TestClass[5];
        tcs[0] = new TestClass("윤석열");
        tcs[1] = new TestClass("문재인");
        tcs[2] = new TestClass("박근혜");

        tcs[1].hobby[0] = "독서";
        System.out.println(tcs[1].hobby[0]);

        tcs[1].tc2[0].address = "양산";
        System.out.println(tcs[1].tc2[0].address);

    }
    

    
}
