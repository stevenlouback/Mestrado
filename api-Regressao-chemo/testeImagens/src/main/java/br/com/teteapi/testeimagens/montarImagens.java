package br.com.teteapi.testeimagens;

import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.io.File;
import java.io.IOException;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;

/**
 *
 * @author Mfsantos
 */
public class montarImagens extends javax.swing.JFrame {

    Mensagens msg = new Mensagens();
    ValidaSair sair = new ValidaSair();
    IncluirDados incluir;

    public montarImagens() {
        initComponents();

        this.setName("IMAGENS");

        try {
            this.incluir = new IncluirDados();
        } catch (SQLException ex) {
            Logger.getLogger(montarImagens.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(montarImagens.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(montarImagens.class.getName()).log(Level.SEVERE, null, ex);
        }

        this.setResizable(false);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel15 = new javax.swing.JLabel();
        Botao_Gravar = new javax.swing.JButton();
        jTFIdentificaImagem = new javax.swing.JTextField();
        jTFValorResultado = new javax.swing.JTextField();
        jLabel16 = new javax.swing.JLabel();
        jTFCaminho = new javax.swing.JTextField();
        jPfoto = new javax.swing.JPanel();
        jLbFoto1 = new javax.swing.JLabel();
        jBselecionarFoto1 = new javax.swing.JButton();
        jTFIdAmostra = new javax.swing.JTextField();

        setDefaultCloseOperation(javax.swing.WindowConstants.DO_NOTHING_ON_CLOSE);
        setTitle("Ajuste de Estoque");
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                formWindowClosing(evt);
            }
        });

        jPanel1.setName("AMOSTRATESTES"); // NOI18N

        jLabel15.setText("Identificação Imagem");

        Botao_Gravar.setText("Confirmar");
        Botao_Gravar.setToolTipText("Gravar - F4");
        Botao_Gravar.setPreferredSize(new java.awt.Dimension(110, 35));
        Botao_Gravar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Botao_GravarActionPerformed(evt);
            }
        });

        jTFIdentificaImagem.setName("NMAMOSTRATESTES"); // NOI18N

        jTFValorResultado.setName("VLRESULTADO"); // NOI18N

        jLabel16.setText("Resultado");

        jTFCaminho.setName("DUMMY"); // NOI18N

        jPfoto.setBorder(javax.swing.BorderFactory.createEtchedBorder());

        jLbFoto1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLbFoto1.setText("Logo Empresa");
        jLbFoto1.setFocusable(false);

        jBselecionarFoto1.setText("Selecionar");
        jBselecionarFoto1.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jBselecionarFoto1.setFocusable(false);
        jBselecionarFoto1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jBselecionarFoto1ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPfotoLayout = new javax.swing.GroupLayout(jPfoto);
        jPfoto.setLayout(jPfotoLayout);
        jPfotoLayout.setHorizontalGroup(
            jPfotoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPfotoLayout.createSequentialGroup()
                .addGap(2, 2, 2)
                .addComponent(jLbFoto1, javax.swing.GroupLayout.PREFERRED_SIZE, 166, javax.swing.GroupLayout.PREFERRED_SIZE))
            .addComponent(jBselecionarFoto1, javax.swing.GroupLayout.PREFERRED_SIZE, 166, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        jPfotoLayout.setVerticalGroup(
            jPfotoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPfotoLayout.createSequentialGroup()
                .addGap(28, 28, 28)
                .addComponent(jLbFoto1, javax.swing.GroupLayout.PREFERRED_SIZE, 160, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(10, 10, 10)
                .addComponent(jBselecionarFoto1, javax.swing.GroupLayout.PREFERRED_SIZE, 19, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        jTFIdAmostra.setColumns(1);
        jTFIdAmostra.setEnabled(false);
        jTFIdAmostra.setName("IDAMOSTRATESTES"); // NOI18N

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTFIdentificaImagem, javax.swing.GroupLayout.PREFERRED_SIZE, 296, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel15))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTFValorResultado, javax.swing.GroupLayout.PREFERRED_SIZE, 296, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel16)))
                            .addComponent(jTFIdAmostra, javax.swing.GroupLayout.PREFERRED_SIZE, 123, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jPfoto, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jTFCaminho)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(Botao_Gravar, javax.swing.GroupLayout.PREFERRED_SIZE, 126, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap())
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addComponent(jLabel15)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jTFIdentificaImagem, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addComponent(jLabel16)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jTFValorResultado, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(62, 62, 62)
                        .addComponent(jTFIdAmostra, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                        .addGap(0, 27, Short.MAX_VALUE)
                        .addComponent(jPfoto, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(Botao_Gravar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jTFCaminho, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void formWindowClosing(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowClosing
        sair.windowclosing(this, Botao_Gravar);
    }//GEN-LAST:event_formWindowClosing

    private void Botao_GravarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Botao_GravarActionPerformed
        if (jTFIdentificaImagem.getText().equals("")) {
            msg.Mensagem_Visual(1, "Informe a identificação da Imagem.");
            jTFIdentificaImagem.grabFocus();
            return;
        }

        if (jTFValorResultado.getText().equals("")) {
            msg.Mensagem_Visual(1, "Informe o Valor do Resultado.");
            jTFValorResultado.grabFocus();
            return;
        }

        if (jTFCaminho.getText().equals("")) {
            msg.Mensagem_Visual(1, "Selecione a Imagem.");
            jBselecionarFoto1.grabFocus();
            return;
        }

        try {
            incluir.incluirdados(jPanel1, "amostraTestes");
            gravaItemCompra();
            incluir.conexao.commit();
        } catch (SQLException ex) {
            try {
                incluir.conexao.rollback();
            } catch (SQLException ex1) {
            }
            msg.Mensagem_Visual(1, "Erro na Inclusão. Detalhe: " + ex.getMessage());
            return;
        } catch (IOException ex) {
            try {
                incluir.conexao.rollback();
            } catch (SQLException ex1) {
            }
            msg.Mensagem_Visual(1, "Erro na Inclusão. Detalhe: " + ex.getMessage());
            return;
        } catch (ClassNotFoundException ex) {
            try {
                incluir.conexao.rollback();
            } catch (SQLException ex1) {
            }
            msg.Mensagem_Visual(1, "Erro na Inclusão. Detalhe: " + ex.getMessage());
            return;
        }

        msg.Mensagem_Visual(2, "Atualizado.");
        this.dispose();

    }//GEN-LAST:event_Botao_GravarActionPerformed

    private void jBselecionarFoto1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jBselecionarFoto1ActionPerformed
        JFileChooser file = new JFileChooser();
        FileNameExtensionFilter filter = new FileNameExtensionFilter(
                "JPG, GIF e PNG Images", "png", "jpeg", "jpg", "gif");  //Cria um filtro
        file.setFileFilter(filter);
        file.setFileSelectionMode(JFileChooser.FILES_ONLY);

        int i = file.showSaveDialog(null);

        if (i == 1) {
            jTFCaminho.setText("");
        } else {
            File arquivo = file.getSelectedFile();
            jTFCaminho.setText(arquivo.getPath());

            ImageIcon icon = new ImageIcon(jTFCaminho.getText());
            carregaFoto(icon);
        }

    }//GEN-LAST:event_jBselecionarFoto1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new montarImagens().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton Botao_Gravar;
    private javax.swing.JButton jBselecionarFoto1;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLbFoto1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPfoto;
    private javax.swing.JTextField jTFCaminho;
    private javax.swing.JTextField jTFIdAmostra;
    private javax.swing.JTextField jTFIdentificaImagem;
    private javax.swing.JTextField jTFValorResultado;
    // End of variables declaration//GEN-END:variables

    public void carregaFoto(ImageIcon icon) {
        icon.setImage(icon.getImage().getScaledInstance(15, 15, 100));
        jPfoto.setBackground(null);
        jLbFoto1.setText("");
        jLbFoto1.setIcon(icon);
    }

    public void gravaItemCompra() throws SQLException {
        if ((!jTFCaminho.getText().equals("")) && (!jTFCaminho.getText().equals("Somente Remover!!!"))) {
            try {
                BufferedImage imagem = UtilImagem.carregaImg(jTFCaminho.getText());
                if (imagem.getHeight() > 15) {
                    imagem = UtilImagem.redimensionaImg(imagem, 15, 15);
                }

                leituraPixelsRGB(imagem);
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, "Erro ao Carregar Imagem.\n ERRO: " + ex.getMessage(), "Erro!", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    public void leituraPixelsRGB(BufferedImage image) throws SQLException {

        Raster raster = image.getRaster();
        int cores[] = new int[255];
        // esse vetor "cores[]" vai armazenar as cores RGB  
        // [0] será Red(R), [1] será Green(G) e [2] será Blue(B)

        int contador = 0;
        for (int linha = 0; linha < image.getWidth(); linha++) {
            int nrLinha = linha + 1;
            for (int coluna = 0; coluna < image.getHeight(); coluna++) {
                int nrColuna = coluna + 1;
                raster.getPixel(linha, coluna, cores); // captura da combinação de cor do pixel  
                System.out.println("R(" + cores[0] + ") G(" + cores[1] + ") B(" + cores[2] + ")");
                contador += 1;

                String sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                        + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + jTFIdAmostra.getText()
                        + "," + contador
                        + "," + nrLinha
                        + "," + nrColuna
                        + ", 'R'"
                        + "," + cores[0]
                        + ")";

                incluir.executaInclusao(sql);
                contador += 1;
                sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                        + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + jTFIdAmostra.getText()
                        + "," + contador
                        + "," + nrLinha
                        + "," + nrColuna
                        + ", 'G'"
                        + "," + cores[1]
                        + ")";

                incluir.executaInclusao(sql);
                contador += 1;
                sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                        + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + jTFIdAmostra.getText()
                        + "," + contador
                        + "," + nrLinha
                        + "," + nrColuna
                        + ", 'B'"
                        + "," + cores[2]
                        + ")";
                incluir.executaInclusao(sql);
            }
        }

    }
}
