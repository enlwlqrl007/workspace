package day0102;

public class Study01 {
    public static void main(String[] args) {
        // TestClass tc1 = new TestClass();
        // tc1.name = "윤석열";
        // tc1.age = 60;
        // tc1.nickName = "대통령";

        // TestClass tc2 = new TestClass();
        // tc1.name = "문재인";
        // tc1.age = 64;
        // tc1.nickName = "전 대통령";

        TestClass[] tcs = new TestClass[10];
        for(int i=0; i<tcs.length;i++){
            tcs[i] = new TestClass();
        }
        tcs[0].name = "윤석열";
        tcs[0].age = 60;
        tcs[0].nickName = "대통령";

        tcs[1].name = "문재인";
        tcs[1].age = 64;
        tcs[1].nickName = "전 대통령";

        System.out.println(tcs[1].name);

        TestClass tc1 = new TestClass();
        TestClass tc2 = new TestClass("박근혜");
        TestClass tc3 = new TestClass("이명박",70);

        System.out.println(tc1.name + ", " + tc2.name + ", " + tc3.name);
        System.out.println(tc2.name);
        System.out.println(tc3.name + ", " + tc3.age);
    }
    

    
}
