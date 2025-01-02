package day0102;

public class TestClass {

    String name;
    int age;
    String nickName;
    String[] hobby = new String[5];
    TestClass2[] tc2;

    // 생성자
    public TestClass(){
        tc2 = new TestClass2[5];
        initTestClass2(this.tc2);
    };

    public TestClass(String name){
        initTestClass2(this.tc2);
        this.name = name;
    };

    public TestClass(String name, int age){
        initTestClass2(this.tc2);
        this.name = name;
        this.age = age;
    }

    void initTestClass2(TestClass2[] tc){
        for(int i=0; i<tc.length;i++){
            tc[i] = new TestClass2();
        }
    }
}
