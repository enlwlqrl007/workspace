package day0102;

class FiveCal extends FourCal{
    
    public FiveCal(int a, int b){
        this.first = a;
        this.second = b;       
    }
    
    @Override  // 최신버전은 어노테이션을 사용하지않아도 괜찮
    int div(){
        if(this.second == 0){
            return 0;
        }else{
            return this.first / this.second;
        }
    }

    int pow(){
        int result = 1;
        for(int i=0; i<second;i++){
            result *= first;
        }
        return result;
    }
}

public class Study05 {
    public static void main(String[] args) {
        FiveCal a = new FiveCal(4,2);

        // a.setData(4, 2);
        System.out.println(a.pow());
        System.out.println(a.add());
        System.out.println(a.div());
    }

}
