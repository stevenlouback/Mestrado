package br.com.teteapi.testeimagens;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
/**
 * @author MFSantos. Data Criação: 11/05/2013
 */
public class Conexao {

    private static Conexao instancy;
    private Connection conexao = null;
    private final String url;
    private final String driver;
    private final String usuario;
    private final String senha;

    private Conexao() throws IOException, ClassNotFoundException,  SQLException {

        /*
        A parcela da URL depois do jdbc:h2: aponta para um arquivo no sistema operacional 
        - o caminho pode ser absoluto (começando com “/”), 
        relativo ao diretório atual (começando com “./”) 
        ou ao diretório do usuário no SO (começando com “~/”). 
        Também será necessário entrar com o login e senha do administrador. 
        Se a URL apontar para um arquivo não existente o banco será criado 
        (verifique que um arquivo [nome do banco].db apareceu no local indicado); 
        também será criado um usuário administrador com o login e senha informados.
        */        

        this.url = "jdbc:postgresql://localhost:5432/Quimiometria";
        this.driver  = "org.postgresql.Driver";
        this.usuario = "postgres";
        this.senha   = "postgres";

        
        try {
            Class.forName(this.driver);
        } catch (ClassNotFoundException e) {
            throw new ClassNotFoundException("Driver do banco de dados não localizado!");
        }

        try {
            this.conexao = DriverManager.getConnection(this.url, this.usuario, this.senha);
            this.conexao.setAutoCommit(false);
            System.out.println("Conectado com sucesso");
        } catch (SQLException e) {
            throw new SQLException("Falha na conexão com o banco de dados!\n"+e.getMessage());
        }
    }

    public static Conexao getInstancy() throws IOException, ClassNotFoundException, SQLException {
        if (instancy == null) {
            instancy = new Conexao();
        }
        return instancy;
    }

    public Connection getConexao() {
        return this.conexao;
    }

    public void desconecta() throws SQLException {
        try {
            this.conexao.close();
            instancy = null;
        } catch (SQLException e) {
            throw new SQLException("Não foi possível desconectar do Banco de Dados\n"+e.getMessage());
        }
    }
}
