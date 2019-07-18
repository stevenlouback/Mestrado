package br.com.teteapi.testeimagens;

import java.awt.Frame;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JInternalFrame;
import javax.swing.JOptionPane;

public class ValidaSair {

    public void windowclosing(Frame tela, JButton botao) {

        if (!botao.isEnabled()) {

            int opcao_escolhida = JOptionPane.showConfirmDialog(null, "Deseja Sair  da tela ?", "Sair da Tela", JOptionPane.YES_NO_OPTION);
            if (opcao_escolhida == JOptionPane.YES_OPTION) {
                tela.dispose();
            }

        } else {

            tela.dispose();
        }

    }
    
    public void windowclosingDialog(JDialog tela, JButton botao) {

        if (!botao.isEnabled()) {

            int opcao_escolhida = JOptionPane.showConfirmDialog(null, "Deseja Sair  da tela ?", "Sair da Tela", JOptionPane.YES_NO_OPTION);
            if (opcao_escolhida == JOptionPane.YES_OPTION) {
                tela.dispose();
            }

        } else {

            tela.dispose();
        }

    }
    public void windowclosingInt(JInternalFrame tela, JButton botao) {

        if (!botao.isEnabled()) {

            int opcao_escolhida = JOptionPane.showConfirmDialog(null, "Deseja Sair  da tela ?", "Sair da Tela", JOptionPane.YES_NO_OPTION);
            if (opcao_escolhida == JOptionPane.YES_OPTION) {
                tela.dispose();
            }

        } else {

            tela.dispose();
        }

    }

    public void windowclosing1(Frame tela, JButton botao) {

//                if (!botao.isEnabled()) {

        int opcao_escolhida = JOptionPane.showConfirmDialog(null, "Deseja Sair  da tela ?", "Sair da Tela", JOptionPane.YES_NO_OPTION);
        if (opcao_escolhida == JOptionPane.YES_OPTION) {
            tela.dispose();
        }

//             } else {

        //tela.dispose();
//             }

    }
}
