class Payment {
    Integer id;
}
class Payment extends Account {
    public Payment (Integer id){
        super (Payment);
    }
    void oid printDataPaymnet (){
    System.out.println ("id:" + id);

}