package com.mf2solucoes.tools;

import com.mf2solucoes.domain.misc.ex.InternalServiceError;
import java.awt.image.BufferedImage;
import java.awt.image.Raster;

/**
 *
 * @author MFSantos
 */
public class tratamentoImagem {

    //Coluna 1 guarda o número
    //Coluna 2 guarda quantidade
    private int[][] frequenciaR = new int[255][2];
    private int[][] frequenciaG = new int[255][2];
    private int[][] frequenciaB = new int[255][2];

    private int qtdeR = 0;
    private int qtdeG = 0;
    private int qtdeB = 0;
//    monta a matriz de RGB

    public Object leituraPixelsRGB(BufferedImage image) {

        Raster raster = image.getRaster();
        int cores[] = new int[255];
        // esse vetor "cores[]" vai armazenar as cores RGB  
        // [0] será Red(R), [1] será Green(G) e [2] será Blue(B)
        System.out.println("============================================");
        System.out.println("Quantidade de Linhas: " + image.getWidth());
        System.out.println("Quantidade de Colunas: " + image.getHeight());
        System.out.println("============================================");

        Object[][] matrizX = new Object[image.getWidth()][image.getHeight()];

        for (int linha = 0; linha < image.getWidth(); linha++) {
            for (int coluna = 0; coluna < image.getHeight(); coluna++) {
                raster.getPixel(linha, coluna, cores); // captura da combinação de cor do pixel  
//                System.out.println("Linha: " + linha+1);
//                System.out.println("Coluna: " + coluna+1);
                int total = cores[0] + cores[1] + cores[2];
                System.out.println("R(" + cores[0] + ") G(" + cores[1] + ") B(" + cores[2] + ")");
                System.out.println("=====================");
                System.out.println("Pixel: " + total);
                System.out.println("=====================");
                System.out.println(image.getRGB(linha, coluna));

//                matrizX [linha][coluna] = image.getRGB(linha, coluna);
                matrizX[linha][coluna] = cores;
            }
        }

        return matrizX;

    }

    //Determina a frequencia de vezes que o número aparece
    public void determinaFrequencia(int valorR, int valorG, int valorB) {

        if (valorR < 0) {
            throw new InternalServiceError("error.rgb.r.negativo");
        }

        if (valorG < 0) {
            throw new InternalServiceError("error.rgb.G.negativo");
        }

        if (valorB < 0) {
            throw new InternalServiceError("error.rgb.B.negativo");
        }

        boolean encontradoMatriz = false;

        if (qtdeR == 0) {
            qtdeR++;
            frequenciaR[0][1] = valorR;
            frequenciaR[0][2] = frequenciaR[1][2] + 1;
        } else {

            if (!encontradoMatriz) {

            }
            encontradoMatriz = false;
        }

        if (qtdeG == 0) {
            qtdeG++;
            frequenciaG[0][1] = valorG;
            frequenciaG[0][2] = frequenciaG[1][2] + 1;
        } else {
            for (int i = 0; i < qtdeG; i++) {
                if (frequenciaG[i][1] == valorG) {
                    frequenciaG[i][1] = valorG;
                    frequenciaG[i][2] = frequenciaG[i][2] + 1;
                    encontradoMatriz = true;
                    break;
                }
            }

            if (!encontradoMatriz) {

            }
            encontradoMatriz = false;
        }

        if (qtdeB == 0) {
            qtdeB++;
            frequenciaB[0][1] = valorB;
            frequenciaB[0][2] = frequenciaB[1][2] + 1;
        } else {
            if (!encontradoMatriz) {

            }
            
        }
    }

//    public void leituraPixelsRGB(BufferedImage image) {
//
//        
//        Raster raster = image.getRaster();
//        int cores[] = new int[255];
//        // esse vetor "cores[]" vai armazenar as cores RGB  
//        // [0] será Red(R), [1] será Green(G) e [2] será Blue(B)
//        System.out.println("============================================");
//        System.out.println("Quantidade de Linhas: " + image.getWidth());
//        System.out.println("Quantidade de Colunas: " + image.getHeight());
//        System.out.println("============================================");
//        
//        Object [] [] matrizX = new Object [image.getWidth()][image.getHeight()];
//        
//        for (int linha = 0; linha < image.getWidth(); linha++) {
//            for (int coluna = 0; coluna < image.getHeight(); coluna++) {
//                raster.getPixel(linha, coluna, cores); // captura da combinação de cor do pixel  
//                System.out.println("Linha: " + linha+1);
//                System.out.println("Coluna: " + coluna+1);
//                System.out.println("R(" + cores[0] + ") G(" + cores[1] + ") B(" + cores[2] + ")");
//                
//            }
//        }
//        
//    }
    public int[][] getFrequenciaR() {
        return frequenciaR;
    }

    public void setFrequenciaR(int[][] frequenciaR) {
        this.frequenciaR = frequenciaR;
    }

    public int[][] getFrequenciaG() {
        return frequenciaG;
    }

    public void setFrequenciaG(int[][] frequenciaG) {
        this.frequenciaG = frequenciaG;
    }

    public int[][] getFrequenciaB() {
        return frequenciaB;
    }

    public void setFrequenciaB(int[][] frequenciaB) {
        this.frequenciaB = frequenciaB;
    }

    public int getQtdeR() {
        return qtdeR;
    }

    public void setQtdeR(int qtdeR) {
        this.qtdeR = qtdeR;
    }

    public int getQtdeG() {
        return qtdeG;
    }

    public void setQtdeG(int qtdeG) {
        this.qtdeG = qtdeG;
    }

    public int getQtdeB() {
        return qtdeB;
    }

    public void setQtdeB(int qtdeB) {
        this.qtdeB = qtdeB;
    }

}
