package day1230;

public class Study06 {
    public static void main(String[] args) {
        int[] marks = {90, 25, 88, 77, 80};
        int number = 0;
        for(int mark:marks){
            number++;
            if(mark <60){
                continue;
            }
            System.out.printf("%d번 학생 축하합니다.\n", number);
        }
    }
}
