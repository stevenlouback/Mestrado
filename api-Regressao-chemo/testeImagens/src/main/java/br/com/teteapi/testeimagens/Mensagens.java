package br.com.teteapi.testeimagens;

import javax.swing.JOptionPane;

/**
 *
 * @author 
 */
public class Mensagens {

    public void Mensagem_Visual(int tipo, String mensagem) {
//      Tipos de Mensagem vem na variável Tipo:
//        1: Mensagem de Erro
//        2: Alerta
        if (tipo == 1) {
            JOptionPane.showMessageDialog(null, mensagem, "Erro", JOptionPane.ERROR_MESSAGE);
        } else if (tipo == 2) {
            JOptionPane.showMessageDialog(null, mensagem, "Atenção", JOptionPane.INFORMATION_MESSAGE);
        }
    }

    public boolean Mensagem_Pergunta(String pergunta, String titulo) {
        int opcao_escolhida = JOptionPane.showConfirmDialog(null, pergunta, titulo, JOptionPane.YES_NO_OPTION);
        if (opcao_escolhida == JOptionPane.YES_OPTION) {
            return true;
        }
        return false;
    }
}
