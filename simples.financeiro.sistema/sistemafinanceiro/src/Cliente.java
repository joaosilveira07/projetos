public class Cliente {
    private String nome;
    private String cpf;
    private String dataNasc;

    public String getNome(){
        return this.nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getCpf(){
        return this.cpf;
    }

    public void setCpf(String cpf){
        this.cpf = cpf;
    }

    public String getDataNasc(){
        return this.dataNasc;
    }

    public void setDataNasc(String dataNasc){
        this.dataNasc = dataNasc;
    }
}
