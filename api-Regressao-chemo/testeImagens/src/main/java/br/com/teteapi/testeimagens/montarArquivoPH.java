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
import jxl.Cell;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;

/**
 *
 * @author Mfsantos
 */
public class montarArquivoPH extends javax.swing.JFrame {

    Mensagens msg = new Mensagens();
    ValidaSair sair = new ValidaSair();
    IncluirDados incluir;

    public montarArquivoPH() {
        initComponents();

        this.setName("IMAGENS");

        try {
            this.incluir = new IncluirDados();
        } catch (SQLException ex) {
            Logger.getLogger(montarArquivoPH.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(montarArquivoPH.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(montarArquivoPH.class.getName()).log(Level.SEVERE, null, ex);
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
        jTFNomePlanilha = new javax.swing.JTextField();
        jTFCaminho = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        jLabel16 = new javax.swing.JLabel();
        jLabel17 = new javax.swing.JLabel();
        jTFNomePlanilha1 = new javax.swing.JTextField();
        jButton2 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DO_NOTHING_ON_CLOSE);
        setTitle("Montar Modelos através do Arquivo XLSx");
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                formWindowClosing(evt);
            }
        });

        jPanel1.setName("AMOSTRATESTES"); // NOI18N

        jLabel15.setText("Planilha X");

        Botao_Gravar.setText("Carregar Banco de Dados");
        Botao_Gravar.setToolTipText("Gravar - F4");
        Botao_Gravar.setPreferredSize(new java.awt.Dimension(110, 35));
        Botao_Gravar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Botao_GravarActionPerformed(evt);
            }
        });

        jTFNomePlanilha.setEnabled(false);
        jTFNomePlanilha.setName("NMAMOSTRATESTES"); // NOI18N

        jTFCaminho.setName("DUMMY"); // NOI18N

        jButton1.setText("Selecionar");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jLabel16.setText("Identificação");

        jLabel17.setText("Planilha Y");

        jTFNomePlanilha1.setEnabled(false);
        jTFNomePlanilha1.setName("NMAMOSTRATESTES"); // NOI18N

        jButton2.setText("Selecionar");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jLabel15)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel16)
                                    .addComponent(jTFCaminho, javax.swing.GroupLayout.PREFERRED_SIZE, 228, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(Botao_Gravar, javax.swing.GroupLayout.PREFERRED_SIZE, 184, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTFNomePlanilha1, javax.swing.GroupLayout.PREFERRED_SIZE, 677, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jTFNomePlanilha, javax.swing.GroupLayout.PREFERRED_SIZE, 677, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel17))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jButton1)
                                    .addComponent(jButton2))))
                        .addGap(213, 213, 213))))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(jLabel15)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jTFNomePlanilha, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jLabel17)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(jTFNomePlanilha1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jButton2)))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addContainerGap()
                                .addComponent(jButton1)))
                        .addGap(11, 11, 11)
                        .addComponent(jLabel16)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jTFCaminho, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(Botao_Gravar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 794, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void formWindowClosing(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowClosing
        sair.windowclosing(this, Botao_Gravar);
    }//GEN-LAST:event_formWindowClosing

    private void Botao_GravarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Botao_GravarActionPerformed
        if (jTFNomePlanilha.getText().equals("")) {
            msg.Mensagem_Visual(1, "Selecione a Planilha de Dados X.");
            jButton2.grabFocus();
            return;
        }
        if (jTFNomePlanilha1.getText().equals("")) {
            msg.Mensagem_Visual(1, "Selecione a Planilha de Dados Y.");
            jButton2.grabFocus();
            return;
        }

        if (jTFCaminho.getText().equals("")) {
            msg.Mensagem_Visual(1, "Não informou a descrição do modelo.");
            jTFCaminho.grabFocus();
            return;
        }

        ExemploJXL jxls = new ExemploJXL();
        try {
            jxls.leituraArquivoDados(jTFNomePlanilha.getText(), jTFNomePlanilha1.getText(), jTFCaminho.getText());
            incluir.conexao.commit();
        } catch (IOException ex) {
            msg.Mensagem_Visual(1, "Erro na Inclusão. Detalhe: " + ex.getMessage());
            return;
        } catch (SQLException ex) {
            msg.Mensagem_Visual(1, "Erro na Inclusão. Detalhe: " + ex.getMessage());
            return;
        } catch (ClassNotFoundException ex) {
            msg.Mensagem_Visual(1, "Erro na Inclusão. Detalhe: " + ex.getMessage());
            return;
        }

        msg.Mensagem_Visual(2, "Atualizado.");
        this.dispose();

    }//GEN-LAST:event_Botao_GravarActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        JFileChooser file = new JFileChooser();
        FileNameExtensionFilter filter = new FileNameExtensionFilter(
                "XLS, XLSX, CSV - Planilhas Excel", "xls", "xlsx", "csv");  //Cria um filtro
        file.setFileFilter(filter);
        file.setFileSelectionMode(JFileChooser.FILES_ONLY);

        int i = file.showSaveDialog(null);

        if (i == 1) {
            jTFNomePlanilha.setText("");
        } else {
            File arquivo = file.getSelectedFile();
            jTFNomePlanilha.setText(arquivo.getPath());
//            jTFCaminho.setText(arquivo.getPath().replace(arquivo.getName(), ""));

        }


    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        JFileChooser file = new JFileChooser();
        FileNameExtensionFilter filter = new FileNameExtensionFilter(
                "XLS, XLSX, CSV - Planilhas Excel", "xls", "xlsx", "csv");  //Cria um filtro
        file.setFileFilter(filter);
        file.setFileSelectionMode(JFileChooser.FILES_ONLY);

        int i = file.showSaveDialog(null);

        if (i == 1) {
            jTFNomePlanilha1.setText("");
        } else {
            File arquivo = file.getSelectedFile();
            jTFNomePlanilha1.setText(arquivo.getPath());
//            jTFCaminho.setText(arquivo.getPath().replace(arquivo.getName(), ""));

        }

    }//GEN-LAST:event_jButton2ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new montarArquivoPH().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton Botao_Gravar;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLabel17;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JTextField jTFCaminho;
    private javax.swing.JTextField jTFNomePlanilha;
    private javax.swing.JTextField jTFNomePlanilha1;
    // End of variables declaration//GEN-END:variables

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

//                String sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
//                        + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + jTFIdAmostra.getText()
//                        + "," + contador
//                        + "," + nrLinha
//                        + "," + nrColuna
//                        + ", 'R'"
//                        + "," + cores[0]
//                        + ")";
//
//                incluir.executaInclusao(sql);
//                contador += 1;
//                sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
//                        + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + jTFIdAmostra.getText()
//                        + "," + contador
//                        + "," + nrLinha
//                        + "," + nrColuna
//                        + ", 'G'"
//                        + "," + cores[1]
//                        + ")";
//
//                incluir.executaInclusao(sql);
//                contador += 1;
//                sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
//                        + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + jTFIdAmostra.getText()
//                        + "," + contador
//                        + "," + nrLinha
//                        + "," + nrColuna
//                        + ", 'B'"
//                        + "," + cores[2]
//                        + ")";
//                incluir.executaInclusao(sql);
            }
        }

    }

}
