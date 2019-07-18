package br.com.teteapi.testeimagens;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.ImageIcon;

/**
 *
 * @author Marcos F. Alves - 23/12/2016
 */
public class UtilImagem {

    public static BufferedImage redimensionaImg(BufferedImage imagem, int new_w, int new_h) throws IOException {
        BufferedImage new_img = new BufferedImage(new_w, new_h,  imagem.getType());
        Graphics2D g = new_img.createGraphics();
        g.drawImage(imagem, 0, 0, new_w, new_h, null);
        g.dispose();
        return new_img;
    }

    public static BufferedImage carregaImg(String caminho) {
        File arquivo = new File(caminho);
        
        BufferedImage imagem = null;
        try {
            imagem = ImageIO.read(arquivo);
        } catch (IOException ex) {
            System.out.println("Imagem não encontrada em: " + caminho);
        }
        return imagem;
    }

    public static byte[] converteEmByte(BufferedImage imagem) throws IOException {
        byte[] byteArray;
        try (ByteArrayOutputStream bytesImg = new ByteArrayOutputStream()) {
            ImageIO.write(imagem, "jpg", bytesImg);//seta a imagem para bytesImg
            bytesImg.flush();//limpa a variável
            byteArray = bytesImg.toByteArray(); //Converte ByteArrayOutputStream para byte[]
        }
        return byteArray;
    }
    
    public static ImageIcon converteEmIcon(byte[] byteArray) throws IOException {
        BufferedImage img = ImageIO.read(new ByteArrayInputStream(byteArray));
        return new ImageIcon(img);
    }
}
