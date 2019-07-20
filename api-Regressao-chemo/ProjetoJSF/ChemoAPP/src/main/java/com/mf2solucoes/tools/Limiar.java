/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.tools;


import java.awt.Color;
import java.awt.image.BufferedImage;

/**
 *
 * @author Marlons
 */
public class Limiar {

    /**
     * ****************************************************************************************************************************************
     */
    /*
     * lIMIARIAZACAO BASICA com LIMIAR passado por parametro
     */
    //limiariazaçao utilizadas no threshold
    public static BufferedImage limiarizacao(BufferedImage img, int limiar) {
        //image de saida
        BufferedImage imgOut = new BufferedImage(
                img.getWidth(), img.getHeight(), BufferedImage.TYPE_INT_RGB);
        int cor;
        // atribuido valores a imagem dos pixels
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                cor = (Color.getColor("red", img.getRGB(x, y)).getRed() + Color.getColor("green", img.getRGB(x, y)).getGreen() + Color.getColor("blue", img.getRGB(x, y)).getBlue()) / 3;
                if (cor >= limiar) {
                    //maior que o limiar fundo
                    imgOut.setRGB(x, y, Color.WHITE.getRGB());
                } else {
                    imgOut.setRGB(x, y, Color.BLACK.getRGB());
                }
            }
        }
        // retorna a imagem binarizada
        return imgOut;
    }

    public static boolean[][] limiarizacaoBool(BufferedImage img, int limiar) {
        //vetor de boolean para saida da funcao
        //valores true sao obejto de interesse
        boolean[][] boolImg = new boolean[img.getWidth()][img.getHeight()];

        int cor;
        // atribuido valores a imagem dos pixels
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                cor = (Color.getColor("red", img.getRGB(x, y)).getRed() + Color.getColor("green", img.getRGB(x, y)).getGreen() + Color.getColor("blue", img.getRGB(x, y)).getBlue()) / 3;
                if (cor >= limiar) {
                    boolImg[x][y] = false;
                } else {
                    boolImg[x][y] = true;

                }
            }
        }
        // retorna a imagem binarizada
        return boolImg;
    }
    // limiarização basica com valor já pré-definido (valores atrivuidos a uma
    // matriz) com liminar por parametro,
    // retornando uma matriz com os valores booleanos true para borda; false
    // para fundo

    public static boolean[][] limiarizacao(int[][] img, int liminar) {
        // cria uma matriz de booleanos com o mesmo tamanho da matriz recebida
        // como parametro
        boolean[][] borda = new boolean[img.length][img[0].length];

        // atribuido caso o pixel seja uma borda recebe true
        // linhas
        for (int x = 0; x < img.length; x++) {
            // colunas
            for (int y = 0; y < img[0].length; y++) {
                if (img[x][y] >= liminar) {
                    //o valor gerado pelo dtector de bordas for maior que o limiar eh considerado uma borda
                    borda[x][y] = true;//BLACK
                } else {
                    borda[x][y] = false;
                }
            }
        }
        // retorna a matriz de boolean
        return borda;
    }

    // limiarização basica com valor já pré-definido (valores atribuidos a uma
    // matriz) com liminar por parametro, que retona uma imagem
    public static BufferedImage limiarizacao(BufferedImage img, int[][] g, int limiar) {
        //Imagem de saida
        BufferedImage imgOut = new BufferedImage(
                img.getWidth(), img.getHeight(), BufferedImage.TYPE_INT_RGB);

        // atribuido valores a imagem dos pixels
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                if (g[x][y] >= limiar) {
                    //TRUE
                    imgOut.setRGB(x, y, Color.BLACK.getRGB());
                } else {
                    imgOut.setRGB(x, y, Color.WHITE.getRGB());
                }
            }
        }
        // retorna a imagem binarizada
        return imgOut;
    }

    /**
     * ****************************************************************************************************************************************
     */
    /**
     *
     * Liminar Automático Por Maxima Entropia da imagem
     *
     */
// calcular o liminar pelo maximo de entropia da imagem
    public static int maxentropia(int histograma[], double totalpixels) {
        // variaveis
        double h0, h1, p0, p1, max = 0;
        int t, i, limiar = 0;

        for (t = 0; t < 256; t++) {
            p0 = 0;
            p1 = 0;
            for (i = 0; i <= t; i++) {
                p0 += (histograma[i] / totalpixels);
            }
            for (i = t + 1; i < 256; i++) {
                p1 += (histograma[i] / totalpixels);
            }

            h0 = 0;
            h1 = 0;
            for (i = 0; i <= t; i++) {
                h0 += entropia((histograma[i] / totalpixels) / p0);
            }
            for (i = t + 1; i < 256; i++) {
                h1 += entropia((histograma[i] / totalpixels) / p1);
            }

            if (h0 + h1 > max) {
                max = h0 + h1;
                limiar = t;
            }
        }
        return limiar;
    }

    // calcula a entropia
    private static double entropia(double x) {
        double e;

        if (x > 0) {
            e = -(x * Math.log(x));
        } else {
            e = 0;
        }
        return e;
    }

    public static int otsuTreshold(int[] histogramOriginal, int total) {
        /* Implementado de acordo com o artigo proposto por Otsu: 
         * @article{otsu1975threshold,
         * title={A threshold selection method from gray-level histograms},
         * author={Otsu, Nobuyuki},
         * journal={Automatica},
         * volume={11},
         * number={285-296},
         * pages={23--27},
         * year={1975}
         * }
         * 
         * 
         */
        float histogram[] = new float[histogramOriginal.length];
        for (int i = 0; i < histogramOriginal.length; i++) {
            histogram[i] = (float) histogramOriginal[i] / (float) total;
        }

        double n, miT, S2b, S2t, w0, w1, u0, u1, ut, pi;

        int TOtsu = 0;
        double VOtsu = 0;


        miT = 0;
        pi = 0;
        for (int i = 0; i < 256; i++) {
            pi = histogram[i];
            miT += i * pi; //Total mean level of original picture;
        }

        S2t = 0;
        for (int i = 0; i < 256; i++) {
            pi = histogram[i];
            S2t += ((i - miT) * (i - miT)) * pi; //Total Variance of levels;
        }

        pi = 0;
        w1 = 0;
        for (int t = 0; t < 256; t++) {
            w0 = 0;
            ut = 0;

            for (int i = 0; i < t; i++) {
                pi = histogram[i];
                w0 += pi; //Probabilities of class occurrence
                ut += (double) i * pi;
            }

            w1 = 1 - w0; // Probabilities of class occurrence

            if (w1 != 0 && w1 != 1) {
                u1 = (miT - ut) / (1 - w1);
            } else {
                u1 = 0;
            }

            if (w0 != 0) { //Class Mean levels
                u0 = ut / w0;
            } else {
                u0 = 0;
            }

            S2b = w0 * w1 * ((u1 - u0) * (u1 - u0));

            n = (S2b / S2t);

            double S2bt = ((miT * w0 - ut) * (miT * w0 - ut)) / (w0 * (1 - w0));

            if (VOtsu < S2bt) {
                VOtsu = S2bt;
                TOtsu = t;
            }
        }
        return TOtsu;
    }

    
}
