public class ContaBancaria{
    private int numero;
    private int agencia;
    private double saldo;
    private Cliente titular;

    public void depositar(double valor){
        validarValor(valor);

        this.saldo += valor;
        System.out.println("Depósito realizado com sucesso!");
        System.out.printf("Saldo atualizado: %.2f %n", saldo);
    }

    public void sacar(double valor){
        validarValor(valor);

        if (valor > this.saldo){
            System.out.println("Saque não autorizado. Saldo insuficiente.");
        }
        else{
            this.saldo -= valor;
            System.out.println("Saque realizado com sucesso!");
            System.out.printf("Saldo atualizado: %.2f %n", saldo);
        }
    }

    public void validarValor(double valor){
        if (valor <= 0){
            System.out.println("Transação não autorizada.");
        }
        else if (valor > this.saldo){
            System.out.println("Transação não autorizada.");
        }
    }
    
    public void transferir(double valor, ContaBancaria destino){
        validarValor(valor);

        
    }


}