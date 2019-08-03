/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.beans;

import com.google.gson.Gson;
import com.mf2solucoes.application.modelDb.amostra;
import com.mf2solucoes.application.modelDb.matrizX;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.application.repository.amostras;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.repository.parametros;
import com.mf2solucoes.application.service.amostraService;
import com.mf2solucoes.tools.Histograma;
import com.mf2solucoes.tools.Mensagens;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.awt.image.Raster;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.Serializable;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Base64;
//import java.util.Base64;
import java.util.Date;
import java.util.List;
import javax.imageio.ImageIO;
//import javax.faces.view.ViewScoped;
//import javax.faces.bean.ViewScoped;
import org.omnifaces.cdi.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import lombok.Getter;
import lombok.Setter;
import org.primefaces.event.FileUploadEvent;
import org.primefaces.model.UploadedFile;

/**
 *
 * @author Marlons
 */
@Named("cargaBean")
@ViewScoped
public class cargaIsoladaBean implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private modelo modelo;

    @Setter
    @Getter
    private amostra amostra;

    @Setter
    @Getter
    private BufferedImage image;

    @Setter
    @Getter
    private parametro parametroResultado;

    @Setter
    @Getter
    private Date maxDate = new Date();

    @Setter
    @Getter
    private List<modelo> list_Modelo = new ArrayList<>();

    @Setter
    @Getter
    private List<parametro> list_ParametroResultado = new ArrayList<>();

    @Setter
    @Getter
    private List<matrizX> list_MatrizX = new ArrayList<>();

    @Inject
    private modelos modelos;

    @Inject
    private parametros parametros;

    @Inject
    private amostras amostras;

    @Inject
    private amostraService amostraService;

    @Setter
    @Getter
    String tpModelo;
    @Setter
    @Getter
    String identificaAmostra;
    @Setter
    @Getter
    Date dataAmostra;

    @Setter
    @Getter
    String espectro;

    public cargaIsoladaBean() {
        limpar();
        preencheCombo1();
    }

    public void initialize() {
//        preencheCombo1();
    }

    public boolean isIMAGEM() {
//        if (amostra.getModelo().getTpinstrumento() == null) {
//            return false;
//        }
//        return amostra.getModelo().getTpinstrumento().equals("IMG");
        return false;
    }

    private void limpar() {
        modelos = new modelos();
        modelo = new modelo();
        amostras = new amostras();
        amostra = new amostra();
        list_MatrizX.clear();
        list_ParametroResultado.clear();
    }

    public void preencheCombo1() {
        list_Modelo = modelos.findAll();
    }

    public void buscaModeloNirImg() {
        if (tpModelo == null || tpModelo == "") {
            list_Modelo.clear();
        } else {
            modelo param = new modelo();
            param.setTpinstrumento(tpModelo);
            list_Modelo = modelos.modeloPorTipoAmostra(param);
        }
//        list_ParametroResultado = parametros.findParametrosModelo(param);
    }

    public void buscaParametrosModelo() {
        parametro param = new parametro();
        param.setModelo(modelo);
        list_ParametroResultado = parametros.findParametrosModelo(param);
    }

    public void gerarAmostra() {
        Mensagens msg = new Mensagens();
        try {
            amostraService = new amostraService();

            if (modelo.getNmmodelo().equals("")) {
                msg.addError("model.validation.name", amostra);
                return;
            }

            if (amostra.getDataamostra() == null) {
//            if (amostra.getDtcoletaamostra().equals("")){
                msg.addError("amostra.validation.dataamostra", amostra);
                return;
            }

            if (amostra.getNmidentifica().equals("")) {
                msg.addError("amostra.validation.identifica", amostra);
                return;
            }

            if (amostra.getDsobservacoes().equals("")) {
                msg.addError("amostra.validation.obs", amostra);
                return;
            }

            if (modelo.getTpinstrumento().equals("NIR")) {
                if (amostra.getDsespectro().equals("")) {
                    msg.addError("amostra.valida.espectro", amostra);
                    return;
                }

                amostra.setImamostra("");
                amostra.setImagem(null);
            } else {
                if (amostra.getImamostra() == null) {
                    msg.addError("amostra.valida.imagem", amostra);
                    return;
                }
                if (amostra.getImamostra().equals("")) {
                    msg.addError("amostra.valida.imagem", amostra);
                    return;
                }

                amostra.setDsespectro("");
            }

            if (modelo.getDsmodelo().equals("")) {
                msg.addError("model.validation.descricao", modelo);
                return;
            }

            amostra.setModelo(modelo);
            amostra.setDtcoletaamostra(String.valueOf(amostra.getDataamostra().toString().replace("/", "-")));
            amostra.setListaParametro(list_ParametroResultado);
            amostra.setListaMatrizX(list_MatrizX);

            this.amostra = amostraService.salvar(amostra);
            limpar();
            msg.addInfo("saved", "");
        } catch (Exception e) {

            msg.addError(String.valueOf(e), amostra);
            e.printStackTrace();
        }
    }

    public void predicaoImagem() {
        Mensagens msg = new Mensagens();
        try {
            amostraService = new amostraService();

            if (modelo.getNmmodelo().equals("")) {
                msg.addError("model.validation.name", amostra);
                return;
            }

            if (amostra.getDataamostra() == null) {
                msg.addError("amostra.validation.dataamostra", amostra);
                return;
            }

            if (amostra.getNmidentifica().equals("")) {
                msg.addError("amostra.validation.identifica", amostra);
                return;
            }

            if (amostra.getDsobservacoes().equals("")) {
                msg.addError("amostra.validation.obs", amostra);
                return;
            }

            if (amostra.getImamostra() == null) {
                msg.addError("amostra.valida.imagem", amostra);
                return;
            }
            
            if (amostra.getImamostra().equals("")) {
                msg.addError("amostra.valida.imagem", amostra);
                return;
            }

            if (modelo.getDsmodelo().equals("")) {
                msg.addError("model.validation.descricao", modelo);
                return;
            }

            amostra.setModelo(modelo);
            amostra.setDtcoletaamostra(String.valueOf(amostra.getDataamostra().toString().replace("/", "-")));
//            amostra.setListaParametro(list_ParametroResultado);
            amostra.setListaMatrizX(list_MatrizX);

            this.amostra = amostraService.predicao(amostra);
            limpar();
            msg.addInfo("saved", "");
        } catch (Exception e) {

            msg.addError(String.valueOf(e), amostra);
            e.printStackTrace();
        }
    }

    public void converteImageRgb(FileUploadEvent event) {
        Raster raster;
        try {
            byte[] bimagem = event.getFile().getContents();

            ByteArrayInputStream bais = new ByteArrayInputStream(bimagem);
            image = ImageIO.read(bais);

            image = redimensionaImg(image, 70, 70);

            //Inclui a imagem redimensionada no Array de Byte
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(image, "jpg", baos);
            baos.flush();
            byte[] imageInByte = baos.toByteArray();
            baos.close();
            amostra.setImagem(imageInByte);
            //Tratamento para jogar em um array 64 bits
            String imgArray = Base64.getEncoder().encodeToString(amostra.getImagem());
            amostra.setImamostra(imgArray);
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        Histograma hhh = new Histograma();
        int red[] = hhh.histogramaRed(image);
        int green[] = hhh.histogramaGreen(image);
        int blue[] = hhh.histogramaBlue(image);

        list_MatrizX.clear();
        int nrsequencia = 0;
        for (int r : red) {
            nrsequencia += 1;
            //Monta a Matriz RGB
            matrizX matriz = new matrizX();
            matriz.setNrsequencia(Long.parseLong(String.valueOf(nrsequencia)));
            matriz.setNrposicaolinha(0);
            matriz.setNrposicaocoluna(1);
            matriz.setVllinhacoluna(BigDecimal.valueOf(r));
            matriz.setIdpixel(1);
            list_MatrizX.add(matriz);
        }

        for (int g : green) {
            nrsequencia += 1;
            //Monta a Matriz RGB
            matrizX matriz = new matrizX();
            matriz.setNrsequencia(Long.parseLong(String.valueOf(nrsequencia)));
            matriz.setNrposicaolinha(1);
            matriz.setNrposicaocoluna(1);
            matriz.setVllinhacoluna(BigDecimal.valueOf(g));
            matriz.setIdpixel(2);
            list_MatrizX.add(matriz);
        }

        for (int b : blue) {
            nrsequencia += 1;
            //Monta a Matriz RGB
            matrizX matriz = new matrizX();
            matriz.setNrsequencia(Long.parseLong(String.valueOf(nrsequencia)));
            matriz.setNrposicaolinha(1);
            matriz.setNrposicaocoluna(1);
            matriz.setVllinhacoluna(BigDecimal.valueOf(b));
            matriz.setIdpixel(3);
            list_MatrizX.add(matriz);
        }
//        //Percorre a Imagem pegando os RGB
//        raster = image.getRaster();
//        int cores[] = new int[256];
//        // esse vetor "cores[]" vai armazenar as cores RGB  
//        // [0] será Red(R), [1] será Green(G) e [2] será Blue(B)  
//
//        // esses laços varrem todo o objeto "imagem",   
//        // saindo do eixo 0,0 até o último pixel da imagem 
//        list_MatrizX.clear();
//        int nrsequencia = 0;
//        for (int x = 0; x < image.getWidth(); x++) {
//            for (int y = 0; y < image.getHeight(); y++) {
//                raster.getPixel(x, y, cores); // captura da combinação de cor do pixel  
//                
//                nrsequencia += 1;
//                //Monta a Matriz RGB
//                matrizX matriz = new matrizX();
//                matriz.setNrsequencia(Long.parseLong(String.valueOf(nrsequencia)));
//                matriz.setNrposicaolinha(x);
//                matriz.setNrposicaocoluna(y);
//                matriz.setVllinhacoluna(BigDecimal.valueOf(cores[0]));
//                matriz.setIdpixel(1);
//                
//                list_MatrizX.add(matriz);
//                
//                nrsequencia += 1;
//                //Monta a Matriz RGB
//                matriz = new matrizX();
//                matriz.setNrsequencia(Long.parseLong(String.valueOf(nrsequencia)));
//                matriz.setNrposicaolinha(x);
//                matriz.setNrposicaocoluna(y);
//                matriz.setVllinhacoluna(BigDecimal.valueOf(cores[1]));
//                matriz.setIdpixel(2);
//                
//                list_MatrizX.add(matriz);
//                
//                nrsequencia += 1;
//                //Monta a Matriz RGB
//                matriz = new matrizX();
//                matriz.setNrsequencia(Long.parseLong(String.valueOf(nrsequencia)));
//                matriz.setNrposicaolinha(x);
//                matriz.setNrposicaocoluna(y);
//                matriz.setVllinhacoluna(BigDecimal.valueOf(cores[2]));
//                matriz.setIdpixel(3);
//
//                list_MatrizX.add(matriz);
//                
//                System.out.println("R(" + cores[0] + ") G(" + cores[1] + ") B(" + cores[2] + ")");
//            }
//        }
    }

    public BufferedImage redimensionaImg(BufferedImage imagem, int new_w, int new_h) throws IOException {
        //BufferedImage imagem = ImageIO.read(image);
        BufferedImage new_img = new BufferedImage(new_w, new_h, BufferedImage.TYPE_INT_RGB);

        Graphics2D g = new_img.createGraphics();
        g.drawImage(imagem, 0, 0, new_w, new_h, null);
        g.dispose();

        return new_img;
    }

}
