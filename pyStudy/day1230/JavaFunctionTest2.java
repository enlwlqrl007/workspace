package day1230;

public class JavaFunctionTest2 {
    public static void main(String[] args) {
    
        JavaFunctionTest1 obj1 = new JavaFunctionTest1();
        JavaFunctionTest1 obj2 = new JavaFunctionTest1();

        obj1.defaultX = 1;
        System.out.println(obj1.defaultX);

        obj1.publicY = 2;
        System.out.println(obj1.publicY);

        obj1.setPrivateZ(3);
        System.out.println(obj1.getPrivateZ());

        int t1 = obj1.staticVal;
        System.out.println(t1);

        int t2 = JavaFunctionTest1.staticVal;
        System.out.println(t2);

        obj1.defaultX = 6;
        obj2.defaultX = 8;
        System.out.println(obj1.defaultX);
        System.out.println(obj2.defaultX);

        obj1.staticVal++;
        System.out.println(obj1.staticVal);
        obj2.staticVal++;
        System.out.println(obj2.staticVal);
    }
}
