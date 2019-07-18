package br.com.teteapi.testeimagens;



import br.com.teteapi.testeimagens.Conexao;
import java.awt.Component;
import java.awt.Container;
import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JViewport;

public class IncluirDados {
//getColumnLabel - para trazer os metadados do Postgre

    public Connection conexao = null;
    private final Conexao conexao_Oracle;
    private Statement statement;
    private ResultSet resultset;
    private ResultSetMetaData metadata;

    public IncluirDados() throws SQLException, IOException, ClassNotFoundException {
        conexao_Oracle = Conexao.getInstancy();
        this.conexao = conexao_Oracle.getConexao();
    }

    public void executaInclusao(String sql) throws SQLException {
        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);
        statement.executeUpdate(sql);
    }

    public void incluirdados(Container container, String tabela) throws SQLException, IOException, ClassNotFoundException {
        String sql = "SELECT * FROM public." + tabela + " LIMIT 1";
        //(sql);
        statement = conexao.createStatement(
                ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_READ_ONLY);
        resultset = statement.executeQuery(sql);
        String sqlinsert = "INSERT INTO public." + tabela + "(";

        // Estrutura
        Component components[] = container.getComponents();
        for (Component component : components) {
            if (component instanceof JTextField) {
                JTextField field = (JTextField) component;
                String nome = field.getName().toUpperCase();
                if (field.getText().equals("  /  /    ")){
                    field.setText("");
                    System.out.println(field.getText());
                }
                if (!field.getText().equals("") && !field.getText().equals("  /  /    ") ||
                        (field.getColumns() == 1) || (field.getColumns() == 2)
                        || (field.getColumns() == 3)) {
                    try {
                        int numCols = resultset.getMetaData().getColumnCount();
                        int conta = 1;
                        while (conta <= numCols) {
                            String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                            if ((colsName.equals(nome))) {
                                sqlinsert += resultset.getMetaData().getColumnName(conta).toUpperCase() + ",";
                            }
                            conta++;
                        }
                    } catch (SQLException erro) {
                        JOptionPane.showMessageDialog(null, erro);
                    }
                }
            }
        }

//combo
        Component components1[] = container.getComponents();
        for (Component component1 : components1) {
            if (component1 instanceof JComboBox) {
                JComboBox field = (JComboBox) component1;
                String nome = field.getName().toUpperCase();
                try {
                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if ((colsName.equals(nome))) {
                            sqlinsert += resultset.getMetaData().getColumnName(conta).toUpperCase() + ",";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }

//check
        Component components70[] = container.getComponents();
        for (Component component5 : components70) {
            if (component5 instanceof JCheckBox) {
                JCheckBox field = (JCheckBox) component5;
                String nome = field.getName().toUpperCase();
                try {
                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if ((colsName.equals(nome))) {
                            sqlinsert += resultset.getMetaData().getColumnName(conta).toUpperCase() + ",";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }
        //radio
        Component components3[] = container.getComponents();
        for (Component component2 : components3) {
            if (component2 instanceof JRadioButton) {
                JRadioButton field = (JRadioButton) component2;
                String nome = field.getName().toUpperCase();
                try {
                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if ((colsName.equals(nome)) && (field.isSelected() == true)) {
                            sqlinsert += resultset.getMetaData().getColumnName(conta).toUpperCase() + ",";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }
        
        //JSpinner
        Component components30[] = container.getComponents();
        for (Component component2 : components30) {
            if (component2 instanceof JSpinner) {
                JSpinner field = (JSpinner) component2;
                String nome = field.getName().toUpperCase();
                try {
                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if (colsName.equals(nome)) {
                            sqlinsert += resultset.getMetaData().getColumnName(conta).toUpperCase() + ",";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }

        // TEXTAREA
        Component components40[] = container.getComponents();
        for (Component component2 : components40) {
            if (component2 instanceof JScrollPane) {
                JScrollPane js = (JScrollPane) component2;
                Component scrollPane[] = js.getComponents();
                for (Component scroll : scrollPane) {
                    if (scroll instanceof JViewport) {
                        JViewport jv = (JViewport) scroll;
                        Component viewReport[] = jv.getComponents();
                        for (Component view : viewReport) {
                            if (view instanceof JTextArea) {
                                JTextArea ta = (JTextArea) view;
                                String nome = ta.getName().toUpperCase();
                                if (!ta.getText().equals("")) {
                                    try {
                                        int numCols = resultset.getMetaData().getColumnCount();
                                        int conta = 1;
                                        while (conta <= numCols) {
                                            String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                                            if (colsName.equals(nome)) {
                                                sqlinsert += resultset.getMetaData().getColumnName(conta).toUpperCase() + ",";
                                            }
                                            conta++;
                                        }
                                    } catch (SQLException erro) {
                                        JOptionPane.showMessageDialog(null, erro);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        sqlinsert = sqlinsert.substring(0, sqlinsert.length() - 1);
        sqlinsert = sqlinsert + ") Values ( ";

//        JOptionPane.showMessageDialog(null, sqlinsert);
        // Conteudo
        Component components4[] = container.getComponents();
        for (Component component4 : components4) {
            if (component4 instanceof JTextField) {
                JTextField field = (JTextField) component4;
                System.out.println(field.getName().toUpperCase());
                if (field.getName().toUpperCase().equals("DT_TRANSACAO")) {
                    sqlinsert += "'" + field.getText().toUpperCase() + "',";
                } else {
                    String nome = field.getName().toUpperCase();
                    String conteudo = field.getText();
                    if (conteudo.equals("  /  /    ")){
                        conteudo = null;
                    }
                    if (!field.getText().equals("") && 
                            !field.getText().equals("  /  /    ") || (field.getColumns() == 1)) {
                        try {
                            int numCols = resultset.getMetaData().getColumnCount();
                            int conta = 1;
                            while (conta <= numCols) {
                                String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                                String teste = resultset.getMetaData().getColumnTypeName(conta).toUpperCase();
                                if ((field.getColumns() == 1) && (colsName.equals(nome))) {

                                    if (resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("CHAR")
                                            || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("VARCHAR")
                                            || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("CHARACTER VARYING")
                                            || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("BPCHAR")
                                            || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("VARCHAR2")) {

                                        sqlinsert += "'" + conteudo.toUpperCase() + "',";
                                        conta++;
                                    } else {
                                        UltimaSequencia ultimo = new UltimaSequencia();
                                        ultimo.ultimasequencia1(colsName, tabela);
                                        sqlinsert += ultimo.ult + ",";
                                        field.setText(ultimo.ult);
                                        conta++;
                                    }
                                } else {

                                    if (colsName.equals(nome)) {

                                        if (resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("CHAR")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("VARCHAR")
                                                
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("CHARACTER VARYING")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("TIMESTAMP WHITHOUT TIME ZONE")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("TIMESTAMP")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("BPCHAR")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("VARCHAR2")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("DATE")) {

                                            if (resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("DATE")) {
                                                if (conteudo.length() == 4) {
                                                    conteudo = "01/01/" + conteudo;
                                                }
                                            }

                                            sqlinsert += "'" + conteudo.toUpperCase() + "',";

                                        } else if ((resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("NUMBER"))
                                                || (resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("INT4"))
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("SERIAL")
                                                || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("NUMERIC")) {
                                            //  sqlinsert += conteudo.replaceAll(",", ".") + ",";
                                            conteudo = conteudo.replaceAll("\\.", "");
                                            conteudo = conteudo.replaceAll("\\,", "\\.");
                                            conteudo = conteudo.replaceAll("[R$ ]", "");
                                            sqlinsert += conteudo.replaceAll("\\,", "\\.") + ",";

                                        }
                                    }
                                    conta++;
                                }
                            }
                        } catch (SQLException erro) {
                            JOptionPane.showMessageDialog(null, erro);
                        }
                    }
                }
            }
        }
//conteudo combo
        Component components2[] = container.getComponents();
        for (Component component2 : components1) {
            if (component2 instanceof JComboBox) {
                JComboBox field = (JComboBox) component2;
                String nome = field.getName().toUpperCase();

                try {

                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if ((colsName.equals(nome))) {
                            sqlinsert += "'" + field.getSelectedItem().toString() + "',";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }

//conteudo check
        Component components80[] = container.getComponents();
        for (Component component2 : components2) {
            if (component2 instanceof JCheckBox) {
                JCheckBox field = (JCheckBox) component2;
                String nome = field.getName().toUpperCase();

                try {

                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if ((colsName.equals(nome))) {
                            if (field.isSelected()) {
                                sqlinsert += "'T',";
                            } else {
                                sqlinsert += "'F',";
                            }
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }
        //radio
        Component components5[] = container.getComponents();
        for (Component component2 : components5) {

            if (component2 instanceof JRadioButton) {
                JRadioButton field = (JRadioButton) component2;
                String nome = field.getName().toUpperCase();
                try {
                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if ((colsName.equals(nome)) && (field.isSelected() == true)) {
                            sqlinsert += "'" + field.getToolTipText().toString() + "',";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }
        
        //radio
        Component components500[] = container.getComponents();
        for (Component component2 : components500) {

            if (component2 instanceof JSpinner) {
                JSpinner field = (JSpinner) component2;
                String nome = field.getName().toUpperCase();
                try {
                    int numCols = resultset.getMetaData().getColumnCount();
                    int conta = 1;
                    while (conta <= numCols) {
                        String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                        if (colsName.equals(nome)) {
                            sqlinsert += "'" + (Integer) field.getValue() + "',";
                        }
                        conta++;
                    }
                } catch (SQLException erro) {
                    JOptionPane.showMessageDialog(null, erro);
                }
            }
        }

        //CONTEUDO DO TEXTAREA
        Component components60[] = container.getComponents();
        for (Component component6 : components60) {
            if (component6 instanceof JScrollPane) {
                JScrollPane js = (JScrollPane) component6;
                Component scrollPane[] = js.getComponents();
                for (Component scroll : scrollPane) {
                    if (scroll instanceof JViewport) {
                        JViewport jv = (JViewport) scroll;
                        Component viewReport[] = jv.getComponents();
                        for (Component view : viewReport) {
                            if (view instanceof JTextArea) {
                                JTextArea ta = (JTextArea) view;
                                String nome = ta.getName().toUpperCase();
                                String conteudo = ta.getText().toUpperCase();
                                if (!ta.getText().equals("")) {
                                    try {
                                        int numCols = resultset.getMetaData().getColumnCount();
                                        int conta = 1;
                                        while (conta <= numCols) {
                                            String colsName = resultset.getMetaData().getColumnName(conta).toUpperCase();
                                            if (colsName.equals(nome)) {
                                                if (resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("CHAR")
                                                        || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("VARCHAR")
                                                        || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("CHARACTER VARYING")
                                                        || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("BPCHAR")
                                                        || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("VARCHAR2")
                                                        || resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("DATE")) {

                                                    sqlinsert += "'" + conteudo.toUpperCase() + "',";

                                                } else if ((resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("NUMBER"))
                                                        || (resultset.getMetaData().getColumnTypeName(conta).toUpperCase().equals("SERIAL"))) {
                                                    conteudo = conteudo.replaceAll("\\.", "");
                                                    conteudo = conteudo.replaceAll("\\,", "\\.");
                                                    conteudo = conteudo.replaceAll("[R$ ]", "");
                                                    sqlinsert += conteudo.replaceAll("\\,", "\\.") + ",";
                                                }
                                            }
                                            conta++;
                                        }
                                    } catch (SQLException erro) {
                                        JOptionPane.showMessageDialog(null, erro);
                                    }
                                }

                            }
                        }
                    }
                }
            }
        }

        // JOptionPane.showMessageDialog(null, sqlinsert);
        sqlinsert = sqlinsert.substring(0, sqlinsert.length() - 1);
        sqlinsert += ")";
        //(sqlinsert);
        //JOptionPane.showMessageDialog(null, sqlinsert);

        try {
            System.out.println(sqlinsert);
            statement.executeUpdate(sqlinsert);
            //("Incluído com sucesso!");
        } catch (SQLException sqlex) {
            String mensagem = "";
            if (sqlex.getErrorCode() == 1 || sqlex.getSQLState().equals("23505")) {
                mensagem = "Registro já existente no banco de dados!";
            } else {
                mensagem = sqlex.getMessage();
            }
            //("Erro ao incluir o registro! SQL passado:\n" + sqlex.getMessage());
            throw new SQLException(mensagem);
        }

    }

}
