public class ContaBancaria{
    private int numero;
    private int agencia;
    private double saldo;
    private Cliente titular;

    public void depositar(double valor){
        if (validarValorPositivo(valor)){
            this.saldo += valor;
            System.out.println("Depósito realizado com sucesso!");
            System.out.printf("Saldo atualizado: %.2f %n", saldo);
        }
        else{
            System.out.println("Transação não autorizada.");
        }
    }

    public void sacar(double valor){
        if (validarValorPositivo(valor) && possuiSaldoSuficiente(valor)){
            this.saldo -= valor;
            System.out.println("Saque realizado com sucesso!");
            System.out.printf("Saldo atualizado: %.2f %n", saldo);
        }
        else{
            System.out.println("Transação não autorizada.");
        }
    }

    public boolean validarValorPositivo(double valor){
        if (valor <= 0){
            return false;
        }

        return true;
    }

    public boolean possuiSaldoSuficiente(double valor){
        if (valor > this.saldo){
            return false;
        }
        
        return true;
    }
    
    public void transferir(double valor, ContaBancaria destino){
        if (validarValorPositivo(valor) && possuiSaldoSuficiente(valor)){
            this.sacar(valor);
            destino.depositar(valor);

            System.out.println("Transferência realizada com sucesso!");
        }
        else{
            System.out.println("Transação não autorizada.");
        }
    }

    public int getNumero(){
        return this.numero;
    }

    public void setNumero(int numero){
        this.numero = numero;
    }

    public int getAgencia(){
        return this.agencia;
    }

    public void setAgencia(int agencia){
        this.agencia = agencia;
    }

    public Cliente getTitular(){
        return this.titular;
    }

    public void setTitular(Cliente titular){
        this.titular = titular;
    }



}