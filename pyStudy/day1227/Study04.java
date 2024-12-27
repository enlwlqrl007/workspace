package day1227;

import java.util.Arrays;

public class Study04 {
    public static void main(String[] args) {
        Object[] t1 = {1,2,"a","b"};
        System.out.println(Arrays.toString(t1));
        System.out.println(t1[2]);

        // 튜플 슬라이싱
        Object[] subT1 = Arrays.copyOfRange(t1, 1, t1.length);
        System.out.println(Arrays.toString(subT1));

        Object[] t2 = {3,4};
        Object[] t3 = new Object[t1.length + t2.length];
        System.arraycopy(t1, 0, t3, 0, t1.length);
        System.arraycopy(t2, 0, t3, t1.length, t2.length);
        System.out.println(Arrays.toString(t3));
        
    }
}
