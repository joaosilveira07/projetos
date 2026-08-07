public class ContaBancaria{
    private int numero;
    private int agencia;
    private double saldo;
    private Cliente titular;

    public ContaBancaria(int numero, int agencia, Cliente titular){
        this.numero = numero;
        this.agencia = agencia;
        this.saldo = 0;
        this.titular = titular;
    }
    
    public boolean depositar(double valor){
        if (validarValorPositivo(valor)){
            this.saldo += valor;
            return true;
        }
        else{
            return false;
        }
    }

    public boolean sacar(double valor){
        if (validarValorPositivo(valor) && possuiSaldoSuficiente(valor)){
            this.saldo -= valor;
            return true;
        }
        else{
            return false;
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
    
    public boolean transferir(double valor, ContaBancaria destino){
        if (this.sacar(valor)){
            return destino.depositar(valor);
        }

        return false;
    }

    public int getNumero(){
        return this.numero;
    }

    public int getAgencia(){
        return this.agencia;
    }

    public Cliente getTitular(){
        return this.titular;
    }

    public double getSaldo(){
        return this.saldo;
    }

}