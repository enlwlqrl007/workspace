package day0102;

public class FourCal {
    // 필드
    int first;
    int second;

    // 생성자
    // public FourCal(int first, int second){
    //     this.first = first;
    //     this.second = second;
    // }

    // 메서드
    void setData(int first, int second){
        this.first = first;
        this.second = second;
    }
    
    int add(){
        return this.first + this.second;
    }

    int sub(){
        return this.first - this.second;
    }

    int mul(){
        return this.first * this.second;
    }

    int div(){
        return this.first / this.second;
    }
}
