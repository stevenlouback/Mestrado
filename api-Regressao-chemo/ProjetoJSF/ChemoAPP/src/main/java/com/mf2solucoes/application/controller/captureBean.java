/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.controller;

import com.mf2solucoes.tools.tratamentoImagem;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.faces.FacesException;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ViewScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import javax.imageio.ImageIO;
import javax.imageio.stream.FileImageOutputStream;
import javax.inject.Named;
import org.primefaces.event.CaptureEvent;

/**
 *
 * @author MFSantos
 */
@ManagedBean
@ViewScoped
public class captureBean {

    private String filename;

    private String getRandomImageName() {
        int i = (int) (Math.random() * 10000000);

        return String.valueOf(i);
    }

    public String getFilename() {
        return filename;
    }

    public void oncapture(CaptureEvent captureEvent) {
        filename = getRandomImageName();
        byte[] data = captureEvent.getData();

        ExternalContext externalContext = FacesContext.getCurrentInstance().getExternalContext();
        String newFileName = externalContext.getRealPath("") + File.separator + "resources" + File.separator + "primefaces-bootstrap"
                + File.separator + "images" + File.separator + filename + ".jpeg";

        FileImageOutputStream imageOutput;
        try {
            imageOutput = new FileImageOutputStream(new File(newFileName));
            imageOutput.write(data, 0, data.length);
            imageOutput.close();
        } catch (IOException e) {
            throw new FacesException("Erro na Captura da Imagem.", e);
        }
    }

    public void conversaoRGB() {
        System.out.println("entrou");
        ExternalContext externalContext = FacesContext.getCurrentInstance().getExternalContext();
        BufferedImage image;
        tratamentoImagem trata = new tratamentoImagem();

        try {
            image = ImageIO.read(new File(externalContext.getRealPath("") + File.separator
                    + "resources" + File.separator + "primefaces-bootstrap"
                    + File.separator + "images" + File.separator + filename + ".jpeg"));
            trata.leituraPixelsRGB(image);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
