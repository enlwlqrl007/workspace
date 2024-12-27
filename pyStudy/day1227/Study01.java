package day1227;

import java.util.Arrays;
import java.util.List;

public class Study01 {
    public static void main(String[] args) {
        List<Integer> a = Arrays.asList(1, 3, 5, 7, 9);
        List<Object> b = Arrays.asList();
        List<String> c = Arrays.asList("Life", "is", "too", "short");
        List<Object> d = Arrays.asList(1,2,"Life","is");
        List<Object> e = Arrays.asList(1,2,Arrays.asList("Life","is"));

        // 리스트 인덱싱
        System.out.println(((List<?>)e.get(2)).get(1));
        System.out.println(a.get(a.size()-2));
        System.out.println(((List<?>)e.get(e.size()- 1)).get(0));

        // 리스트 슬라이싱
        a = Arrays.asList(1,2,3,4,5);
        System.out.println(a.subList(0, 2));
        System.out.println(a.subList(0, 3));
        System.out.println(a.subList(3, a.size()));

    }
}
