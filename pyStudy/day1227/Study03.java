package day1227;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Study03 {
    public static void main(String[] args) {
        List<Object> a = new ArrayList<>(Arrays.asList(1,2,3));
        a.add(4);
        System.out.println(a);

        a.add(Arrays.asList(5, 6, 7));
        System.out.println(a);

        List<Integer> b = new ArrayList<>(Arrays.asList(1,4,3,2));
        System.out.println(b);
        Collections.sort(b);
        System.out.println(b);
        b.sort(Collections.reverseOrder());
        System.out.println(b);

        List<String> str = new ArrayList<>(Arrays.asList("a","c","b","e"));
        Collections.sort(str);
        System.out.println(str);

        List<String> c = new ArrayList<>(Arrays.asList("a","c","b","e"));
        Collections.reverse(c);
        System.out.println(c);

        List<Integer> d = new ArrayList<>(Arrays.asList(1,2,3));
        System.out.println(d.indexOf(3));
        
        d.add(1,4);
        System.out.println(d);

        List<Integer> e = new ArrayList<>(Arrays.asList(1,2,3,1,2,3));
        e.remove((Integer)3);
        System.out.println(e);
        e.remove((Integer)3);
        System.out.println(e);

        List<Integer> f = new ArrayList<>(Arrays.asList(1,2,3));
        System.out.println(f.remove(f.size()-1));
        System.out.println(f);
        
        List<Integer> g = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        System.out.println(g.remove(1));
        System.out.println(g);

        List<Integer> h = new ArrayList<>(Arrays.asList(1,2,3,1));
        System.out.println(Collections.frequency(h, 1));

        List<Integer> i = new ArrayList<>(Arrays.asList(1,2,3));
        i.addAll(Arrays.asList(4,5));
        System.out.println(i);

    }
}
