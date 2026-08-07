public class Main {
    public static void main(String[] args) {
        Cliente cliente1 = new Cliente("José Luiz", "12345678900", "06/11/2005");
        
        ContaBancaria conta1 = new ContaBancaria(0001, 99, cliente1);

    }
}