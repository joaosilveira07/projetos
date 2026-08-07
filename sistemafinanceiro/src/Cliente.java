public class Cliente {
    private String nome;
    private String cpf;
    private String dataNasc;

    public Cliente(String nome, String cpf, String dataNasc){
        this.nome = nome;
        this.cpf = cpf;
        this.dataNasc = dataNasc;
    }
    
    public void alterarNome(String nome){
        if (nome != null && !nome.isBlank()){
            this.nome = nome;
        }
    }

    public void alterarDataNascimento(String dataNasc){
        this.dataNasc = dataNasc;
    }

    public String getNome(){
        return this.nome;
    }

    public String getCpf(){
        return this.cpf;
    }

    public String getDataNasc(){
        return this.dataNasc;
    }

}
