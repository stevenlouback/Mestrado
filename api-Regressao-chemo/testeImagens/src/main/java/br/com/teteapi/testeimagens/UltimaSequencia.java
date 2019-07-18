package br.com.teteapi.testeimagens;



import br.com.teteapi.testeimagens.Conexao;
import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JOptionPane;

public class UltimaSequencia {

    public String ult;
    public int banco;
    public Connection conexao = null;
    private Conexao conexao_Oracle;
    private Statement statement;
    private ResultSet resultset;
    private ResultSetMetaData metadata;

    public UltimaSequencia() throws SQLException, IOException, ClassNotFoundException {
        conexao_Oracle = Conexao.getInstancy();
        this.conexao = conexao_Oracle.getConexao();

    }

    public void ultimasequencia1(String campo, String tabela) throws SQLException {
        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);
        try {
            resultset = statement.executeQuery("SELECT COALESCE(MAX(" + campo + "),0) + 1 AS ULTIMO FROM public." + tabela);
            resultset.first();
            ult = resultset.getString("ULTIMO");
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null, erro);
        }

    }

    public void ultimasequencia2(String campo, String tabela, String campo2, String condicao) throws SQLException {

        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);

        String sql;
        try {
            sql = "SELECT COALESCE(MAX(" + campo + "),0) + 1 AS ULTIMO FROM public." + tabela
                    + " WHERE " + campo2 + " = '" + condicao + "'";

            resultset = statement.executeQuery(sql);
//            JOptionPane.showMessageDialog(null,sql);
            resultset.first();
            ult = resultset.getString("ULTIMO");
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null, erro);
        }

    }

    public void ultimasequencia3(String campo, String tabela, String atributo, int operacao) throws SQLException {

        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);

        try {
            resultset = statement.executeQuery("SELECT COALESCE(MAX(" + campo + "),0) + 1 AS ULTIMO"
                    + " FROM public." + tabela + " WHERE " + atributo + " = 1");
            resultset.first();
            ult = resultset.getString("ULTIMO");
        } catch (SQLException erro) {
            JOptionPane.showMessageDialog(null, erro);
        }

    }

    public void UltimaSequencia5(String campo, String tabela) throws SQLException {
        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);

        try {
            String sql = ("SELECT COALESCE(MAX(" + campo + "),0) + 1 AS ULTIMO FROM public." + tabela);
//            //(sql);                        
            resultset = statement.executeQuery(sql);
            resultset.first();
            ult = resultset.getString("ULTIMO");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e);
        } finally {
            statement.close();
        }

    }
    
    public void UltimaSequencia6(String campo,String campocondicao1, String campocondicao2,
            String condicao1, String condicao2, String tabela) throws SQLException {
        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);

        try {
            String sql = ("SELECT COALESCE(MAX(" + campo + "),0) + 1 AS ULTIMO FROM public." + tabela+""
                    + " where "+campocondicao1+" = '"+condicao1+"'"
                    + " and "+campocondicao2+" = '" + condicao2+"'");
//            //(sql);                        
            resultset = statement.executeQuery(sql);
            resultset.first();
            ult = resultset.getString("ULTIMO");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e);
        } finally {
            statement.close();
        }

    }
}
