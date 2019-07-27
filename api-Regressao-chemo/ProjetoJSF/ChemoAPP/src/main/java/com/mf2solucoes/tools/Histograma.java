
package com.mf2solucoes.tools;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.*;
import java.util.logging.Logger;
/**
 *
 * @author Marlons
 */
public class Histograma {
 


    /**
     * ****************************************************************************************************************************************
     */
    /**
     *
     * Histogramas Por tom de cinza e os 3 canais RGB
     *
     *
     */
    public  int[] histogramaRed(BufferedImage img) {
        // Histogramas
        int red[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            red[i] = 0;
        }

        // pegando os valores RGB
        int largura = img.getWidth();
        int altura = img.getHeight();

        for (int x = 0; x < largura; x++) {
            for (int y = 0; y < altura; y++) {

                red[Color.getColor("red", img.getRGB(x, y)).getRed()]++;
            }
        }
        return red;
    }

    public int[] histogramaRed(BufferedImage img, boolean[][] imgBool) {
        // Histogramas
        int red[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            red[i] = 0;
        }

        // pegando os valores RGB
        int largura = img.getWidth();
        int altura = img.getHeight();

        for (int x = 0; x < largura; x++) {
            for (int y = 0; y < altura; y++) {
                if (imgBool[x][y]) {
                    red[Color.getColor("red", img.getRGB(x, y)).getRed()]++;
                }
            }
        }
        return red;
    }

    public int[] histogramaGreen(BufferedImage img) {
        // Histogramas
        int green[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            green[i] = 0;
        }

        // pegando os valores RGB
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                green[Color.getColor("green", img.getRGB(x, y)).getGreen()]++;
            }
        }
        return green;
    }

    public int[] histogramaGreen(BufferedImage img, boolean[][] imgBool) {
        // Histogramas
        int green[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            green[i] = 0;
        }

        // pegando os valores RGB
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                if (imgBool[x][y]) {
                    green[Color.getColor("green", img.getRGB(x, y)).getGreen()]++;
                }
            }
        }
        return green;
    }

    public int[] histogramaBlue(BufferedImage img) {
        // Histogramas
        int blue[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            blue[i] = 0;
        }

        // pegando os valores RGB
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                blue[Color.getColor("blue", img.getRGB(x, y)).getBlue()]++;
            }
        }
        return blue;
    }

    public int[] histogramaBlue(BufferedImage img, boolean[][] imgBool) {
        // Histogramas
        int blue[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            blue[i] = 0;
        }

        // pegando os valores RGB
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                if (imgBool[x][y]) {
                    blue[Color.getColor("blue", img.getRGB(x, y)).getBlue()]++;
                }
            }
        }
        return blue;
    }

    public int[] histogramaGray(BufferedImage img) {
        // Histogramas
        int h[] = new int[256];

        // Inicialização dos vetores
        for (int i = 0; i <= 255; i++) {
            h[i] = 0;
        }

        // Recebe a media das cores Red, Green e Blue que é o tom de cinza do
        // pixel
        int media;

        // pegando os valores RGB
        for (int x = 0; x < img.getWidth(); x++) {
            for (int y = 0; y < img.getHeight(); y++) {
                media = (Color.getColor("red", img.getRGB(x, y)).getRed() + Color.getColor("green", img.getRGB(x, y)).getGreen() + Color.getColor("blue", img.getRGB(x, y)).getBlue()) / 3;
                h[media]++;
            }
        }
        return h;
    }

    //calcula o histograma medio de um array de imagens recebido por parametro
    public int[] histogramaMedioRed(BufferedImage[] imagens, boolean threshold) {
        //histograma
        int[] histogramaOut = new int[256];

        try {
            //percorre as fotos
            int cont = 0;
            for (BufferedImage image : imagens) {
                int[] histograma;
                //calcula o histograma individual de cada foto
                //se verdadeiro o threshold esta ligado
                if (threshold) {
                    histograma = histogramaRed(image, Limiar.limiarizacaoBool(image, Limiar.otsuTreshold(histogramaGray(image), image.getWidth() * image.getHeight())));
                } else {
                    histograma = histogramaRed(image);
                }

                for (int i = 0; i < 256; i++) {
                    //agrega o valor a cada posicao no histograma geral
                    histogramaOut[i] += histograma[i];
                }
            }
            //obtendo a media para cada tonalidade de cor
            for (int i = 0; i < 256; i++) {
                //dividir o valor agregado pelo numero de imagens
                histogramaOut[i] /= imagens.length;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return histogramaOut;
    }

    //funcao que calcula o desvio padrao de um array de imagens e seu respectivo histograma meedio
    public int[] histogramaDesvioPadraoRed(BufferedImage[] imagens, int[] hMedioRed, boolean threshold) {
        //histograma
        int[] histogramaOut = new int[256];

        try {
            //percorre as fotos
            for (BufferedImage image : imagens) {
                int[] histograma;
                //calcula o histograma individual de cada foto
                //se verdadeiro o threshold esta ligado
                if (threshold) {
                    histograma = histogramaRed(image, Limiar.limiarizacaoBool(image, Limiar.otsuTreshold(histogramaGray(image), image.getWidth() * image.getHeight())));
                } else {
                    histograma = histogramaRed(image);
                }
                for (int i = 0; i < 256; i++) {
                    //calcula o desvio quadratico de cada tonalidade
                    histogramaOut[i] += Math.pow(hMedioRed[i] - histograma[i], 2);
                }
            }
            //obtendo o desvio padrão
            for (int i = 0; i < 256; i++) {
                //divindo os desvios quadraticos de cada tonalidade, obtem a variância
                //Atraves da raiz quadrada de cada variancia se obtem o desvio padrão
                histogramaOut[i] = (int) Math.sqrt(histogramaOut[i] / imagens.length);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        //retorna o array com os valores do desvio padrão
        return histogramaOut;
    }

    //calcula o histograma medio de um array de imagens
    public int[] histogramaMedioGreen(BufferedImage[] imagens, boolean threshold) {
        //histograma
        int[] histogramaOut = new int[256];

        try {
            //percorre as fotos
            for (BufferedImage image : imagens) {
                int[] histograma;
                //calcula o histograma individual de cada foto
                //se verdadeiro o threshold esta ligado
                if (threshold) {
                    histograma = histogramaGreen(image, Limiar.limiarizacaoBool(image, Limiar.otsuTreshold(histogramaGray(image), image.getWidth() * image.getHeight())));
                } else {
                    histograma = histogramaGreen(image);
                }
                for (int i = 0; i < 256; i++) {
                    //agrega o valor a cada posicao no histograma geral
                    histogramaOut[i] += histograma[i];
                }
            }
            for (int i = 0; i < 256; i++) {
                //dividir o valor agregado pelo numero de imagens
                histogramaOut[i] /= imagens.length;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return histogramaOut;
    }

    public int[] histogramaDesvioPadraoGreen(BufferedImage[] imagens, int[] hMedioGreen, boolean threshold) {
        //histograma
        int[] histogramaOut = new int[256];

        try {
            //percorre as fotos
            for (BufferedImage image : imagens) {
                int[] histograma;
                //calcula o histograma individual de cada foto
                //se verdadeiro o threshold esta ligado
                if (threshold) {
                    histograma = histogramaGreen(image, Limiar.limiarizacaoBool(image, Limiar.otsuTreshold(histogramaGray(image), image.getWidth() * image.getHeight())));
                } else {
                    histograma = histogramaGreen(image);
                }
                for (int i = 0; i < 256; i++) {
                    //calcula o desvio quadratico de cada tonalidade
                    histogramaOut[i] += Math.pow(hMedioGreen[i] - histograma[i], 2);
                }
            }
            //obtendo o desvio padrão
            for (int i = 0; i < 256; i++) {
                //divindo os desvios quadraticos de cada tonalidade, obtem a variância
                //Atraves da raiz quadrada de cada variancia se obtem o desvio padrão
                histogramaOut[i] = (int) Math.sqrt(histogramaOut[i] / imagens.length);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        //retorna o array com os valores do desvio padrão
        return histogramaOut;
    }

    //calcula o histograma medio de um array de imagens
    public int[] histogramaMedioBlue(BufferedImage[] imagens, boolean threshold) {
        //histograma
        int[] histogramaOut = new int[256];

        try {
            //percorre as fotos
            for (BufferedImage image : imagens) {
                int[] histograma;
                //calcula o histograma individual de cada foto
                //se verdadeiro o threshold esta ligado
                if (threshold) {
                    histograma = histogramaBlue(image, Limiar.limiarizacaoBool(image, Limiar.otsuTreshold(histogramaGray(image), image.getWidth() * image.getHeight())));
                } else {
                    histograma = histogramaBlue(image);
                }
                for (int i = 0; i < 256; i++) {
                    //agrega o valor a cada posicao no histograma geral
                    histogramaOut[i] += histograma[i];
                }
            }
            for (int i = 0; i < 256; i++) {
                //dividir o valor agregado pelo numero de imagens
                histogramaOut[i] /= imagens.length;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return histogramaOut;
    }

    public int[] histogramaDesvioPadraoBlue(BufferedImage[] imagens, int[] hMedioBlue, boolean threshold) {
        //histograma
        int[] histogramaOut = new int[256];

        try {
            //percorre as fotos
            for (BufferedImage image : imagens) {
                int[] histograma;
                //calcula o histograma individual de cada foto
                //se verdadeiro o threshold esta ligado
                if (threshold) {
                    histograma = histogramaBlue(image, Limiar.limiarizacaoBool(image, Limiar.otsuTreshold(histogramaGray(image), image.getWidth() * image.getHeight())));
                } else {
                    histograma = histogramaBlue(image);
                }
                for (int i = 0; i < 256; i++) {
                    //calcula o desvio quadratico de cada tonalidade
                    histogramaOut[i] += Math.pow(hMedioBlue[i] - histograma[i], 2);
                }
            }
            //obtendo o desvio padrão
            for (int i = 0; i < 256; i++) {
                //divindo os desvios quadraticos de cada tonalidade, obtem a variância
                //Atraves da raiz quadrada de cada variancia se obtem o desvio padrão
                histogramaOut[i] = (int) Math.sqrt(histogramaOut[i] / imagens.length);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        //retorna o array com os valores do desvio padrão
        return histogramaOut;
    }
    //normalização de histograma por scala
    //normalization by scaling between 0 and 1
    public double[] normalizacao(double[] histograma) {

        //Armazena a frequencia max e min do histograma
        double max = histograma[0];
        double min = histograma[0];

        double[] hist = new double[histograma.length];

        //identifica a frequencia maxima e minima existente no histograma
        for (int i = 1; i < histograma.length; i++) {
            if (histograma[i] > max) {
                max = histograma[i];
            } else if (histograma[i] < min) {
                min = histograma[i];
            }
        }
        //calcula os valores do no histograma
        for (int i = 0; i < histograma.length; i++) {
            hist[i] = (histograma[i] - min) / (max - min);
        }

        //retorna o histograma 
        return hist;
    }

    //funcao que cria um txt com os dados de um histograma
    public void criarTxtHistograma(String caminhoNome, int[] histograma) {
        try {
            FileWriter arquivo = new FileWriter(caminhoNome + ".txt");
            BufferedWriter buffer = new BufferedWriter(arquivo);
            for (int i : histograma) {
                buffer.write(i + "");
                buffer.newLine();
            }
            buffer.flush();
            buffer.close();
        } catch (IOException ex) {
            Logger.getLogger(String.valueOf(ex));
        }
    }

    //funcao que pega um txt de inteiros e converte em histograma
    public int[] lerTxtHistograma(String caminhoNome) {
        int[] histograma = new int[256];
        try {
            FileReader reader = new FileReader(caminhoNome);
            BufferedReader buffer = new BufferedReader(reader);
            for (int i = 0; i < 256; i++) {
                histograma[i] = Integer.parseInt(buffer.readLine());
            }
            buffer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return histograma;
    }

    public BufferedImage equalizaRGB(BufferedImage img, int[] hRed, int[] hGreen, int[] hBlue) {
        BufferedImage imgOut = new BufferedImage(
                img.getWidth(), img.getHeight(), BufferedImage.TYPE_INT_RGB);

        int x, y;

        float totalpixels = img.getWidth() * img.getHeight();

        float acumuloRed = 0;
        float acumuloGreen = 0;
        float acumuloBlue = 0;

        float[] hacumuladoRed = new float[256];
        float[] hacumuladoGreen = new float[256];
        float[] hacumuladoBlue = new float[256];


        for (x = 0; x < 256; x++) {
            hacumuladoRed[x] = hacumuladoGreen[x] = hacumuladoGreen[x] = 0;
        }

        for (x = 0; x < 256; x++) {
            //canal RED
            acumuloRed = acumuloRed + hRed[x] / totalpixels;
            hacumuladoRed[x] = acumuloRed;
            //canal GREEN
            acumuloGreen = acumuloGreen + hGreen[x] / totalpixels;
            hacumuladoGreen[x] = acumuloGreen;
            //canal BLUE
            acumuloBlue = acumuloBlue + hBlue[x] / totalpixels;
            hacumuladoBlue[x] = acumuloBlue;
        }

        for (y = 0; y < img.getHeight(); y++) {
            for (x = 0; x < img.getWidth(); x++) {
                int red = (int) ((hacumuladoRed[Color.getColor("red", img.getRGB(x, y)).getRed()]) * 255);
                int green = (int) ((hacumuladoGreen[Color.getColor("green", img.getRGB(x, y)).getGreen()]) * 255);
                int blue = (int) ((hacumuladoBlue[Color.getColor("blue", img.getRGB(x, y)).getBlue()]) * 255);

                imgOut.setRGB(x, y, new Color(red, green, blue).getRGB());
            }
        }

        return imgOut;
    }
   
}
