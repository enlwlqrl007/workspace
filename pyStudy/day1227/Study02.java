package day1227;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Study02 {
    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>(Arrays.asList(1,2,3));
        List<Integer> b = new ArrayList<>(Arrays.asList(4,5,6));    

        List<Integer> combined = new ArrayList<>(a);
        combined.addAll(b);
        System.out.println(combined);

        List<Integer> repeated = new ArrayList<>();
        for(int i=0;i<3;i++){
            repeated.addAll(a);
        }
        System.out.println(repeated);

        System.out.println(a.size());

        System.out.println(a.get(2)+"dog");

        a.set(2,4);
        System.out.println(a);

        a.remove(1);
        System.out.println(a);

        a = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
        a.subList(5, a.size()).clear();
        System.out.println(a);


    }
    


}
