package com.mf2solucoes.application.controller;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.io.Serializable;
import javax.faces.bean.ManagedBean;
import javax.faces.view.ViewScoped;
import javax.imageio.ImageIO;
import javax.inject.Named;
import javax.swing.ImageIcon;
import lombok.Getter;
import lombok.Setter;
import org.primefaces.event.FileUploadEvent;
import org.primefaces.model.UploadedFile;

/**
 *
 *
 *
 * @author MFSantos
 */
@ManagedBean
@ViewScoped
public class imageBean implements Serializable {

    @Setter
    @Getter
    private BufferedImage image;

    public imageBean() {

    }

    public void converteImageRgb(FileUploadEvent event) {

        Raster raster; // se precisar alterar os pixels ao invés de só captura-los,  
        // use WritableRaster no lugar de Raster...  
        try {
            UploadedFile uploadedFile = event.getFile();

            byte[] bimagem = event.getFile().getContents();
            System.out.println(uploadedFile.getFileName());

//            image = ImageIO.read(new File(uploadedFile.getFileName()));
            ByteArrayInputStream bais = new ByteArrayInputStream(bimagem);
            image = ImageIO.read(bais);

            image = redimensionaImg(image, 15, 15);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        raster = image.getRaster();
        int cores[] = new int[255];
        // esse vetor "cores[]" vai armazenar as cores RGB  
        // [0] será Red(R), [1] será Green(G) e [2] será Blue(B)  
        for (int x = 0; x < image.getWidth(); x++) {
            for (int y = 0; y < image.getHeight(); y++) {
                raster.getPixel(x, y, cores); // captura da combinação de cor do pixel  
                System.out.println("R(" + cores[0] + ") G(" + cores[1] + ") B(" + cores[2] + ")");
            }
        }
        // esses laços varrem todo o objeto "imagem",   
        // saindo do eixo 0,0 até o último pixel da mesma 
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
