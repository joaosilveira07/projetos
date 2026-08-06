public class Main {
    public static void main(String[] args) {
        ContaBancaria conta1 = new ContaBancaria();
        conta1.depositar(500);
        conta1.depositar(0);
        conta1.depositar(-500);

        conta1.sacar(250);
        conta1.sacar(0);
        conta1.sacar(500);
    }
}
