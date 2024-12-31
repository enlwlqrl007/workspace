public class MoneyManager {
    
    static int num = 1; // 순서

    int objNum;         // 일련번호
    boolean plusMinus;  // 수입, 지출(true 수입, false 지출)
    String date;        // 날짜
    String content;     // 내역
    int amount;         // 금액

    public MoneyManager(String fileName, boolean pm, String date, String content, int amount) throws Exception {
        this.objNum = ++num;
        FileManeger fm = new FileManeger(fileName);
        String str = fm.loadData();
        String[] subStr = str.split("\n");
        String[] subSubstr = subStr[subStr.length-1].split(",");
        this.objNum = Integer.valueOf(subSubstr[0]) + 1;
        this.plusMinus = pm;
        this.date = date;
        this.content = content;
        this.amount = amount;
    }

    public void save(String fileName) throws Exception{
        String data = this.toString();
        FileManeger fm = new FileManeger(fileName);
        fm.saveData(data);
        System.out.println("저장완료!");

    }

    // 일련번호, 수입or지출, 날짜, 내역, 금액
    public String toString(){
        String pm = this.plusMinus ? "수입" : "지출";
        String str = String.valueOf(this.objNum) + ","
                    + pm + ","
                    + this.date + ","
                    + this.content + ","
                    + String.valueOf(this.amount);

        return str;
    }

}
