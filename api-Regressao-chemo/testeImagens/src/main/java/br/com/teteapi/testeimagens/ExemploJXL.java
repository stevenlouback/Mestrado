/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.teteapi.testeimagens;

/**
 *
 * @author Marlons
 */
import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.SQLException;
import java.util.Iterator;
import jxl.Cell;
import jxl.Sheet;
import jxl.Workbook;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ExemploJXL {

    private Workbook planilha; // objeto que receberá um instancia da planilha estudada
    private Sheet aba; // objeto que será a aba
    private File arquivo; // arquivo .xls que será lido

    public void leituraArquivo(String fileName, String caminho) throws IOException, SQLException, ClassNotFoundException {
        int nmAmostra = 0;
        int idAmostra = 0;
        double vlAmostra = 0;
        try {
            FileInputStream arquivo = new FileInputStream(new File(
                    fileName));

            XSSFWorkbook workbook = new XSSFWorkbook(arquivo);

            XSSFSheet sheetAlunos = workbook.getSheetAt(0);

            Iterator<Row> rowIterator = sheetAlunos.iterator();

            int contar = 0;
            while (rowIterator.hasNext()) {
                contar += 1;
                Row row = rowIterator.next();
                Iterator<org.apache.poi.ss.usermodel.Cell> cellIterator = row.cellIterator();
                if (contar > 1) {
                    while (cellIterator.hasNext()) {
                        org.apache.poi.ss.usermodel.Cell cell = cellIterator.next();
                        switch (cell.getColumnIndex()) {
                            case 0:
                                System.out.println("================================================");
                                idAmostra = (int) cell.getNumericCellValue();
                                System.out.println(idAmostra);
                                break;
                            case 1:
                                nmAmostra = (int) cell.getNumericCellValue();
                                System.out.println(nmAmostra);
                                break;
                            case 2:
                                vlAmostra = cell.getNumericCellValue();
                                System.out.println(vlAmostra);

                                gravarImagem(nmAmostra, idAmostra, vlAmostra, caminho);

                                break;
                        }
                    }
                }
            }
            arquivo.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.out.println("Arquivo Excel não encontrado!");
        }

    }

    public void leituraArquivoDados(String fileNameX, String fileNameY, String tipoAmostra) throws IOException, SQLException, ClassNotFoundException {
        double valorY = 0;
        double valorX = 0;
        try {

            FileInputStream arquivoY = new FileInputStream(new File(
                    fileNameY));

            XSSFWorkbook workbookY = new XSSFWorkbook(arquivoY);

            XSSFSheet sheetY = workbookY.getSheetAt(0);

            Iterator<Row> rowIteratorY = sheetY.iterator();
//            UltimaSequencia ultimo = new UltimaSequencia();
//            ultimo.ultimasequencia1("idamostratestes", "amostratestes");

            IncluirDados incluir = new IncluirDados();

//            int primeiraAmostra = Integer.parseInt(ultimo.ult);
            int contaLinhaY = 0;
            while (rowIteratorY.hasNext()) {
                Row rowY = rowIteratorY.next();

                contaLinhaY++;

                System.out.println("Y:" + contaLinhaY);

                String insert = "INSERT INTO public.amostra(idmodelo, idamostra, "
                        + "tpamostra, dsobservacoes, dtcoletaamostra)"
                        + "VALUES (4, " + contaLinhaY + ", "
                        + "'" + tipoAmostra + "', '" + tipoAmostra + "_CARGA', now())";

                System.out.println(insert);

                incluir.executaInclusao(insert);

                Iterator<org.apache.poi.ss.usermodel.Cell> cellIteratorY = rowY.cellIterator();

                while (cellIteratorY.hasNext()) {
                    org.apache.poi.ss.usermodel.Cell cellY = cellIteratorY.next();
                    switch (cellY.getColumnIndex()) {
                        case 0:
                            valorY = cellY.getNumericCellValue();

//                            ultimo.ultimasequencia1("idamostratestes", "amostratestes");
//                            String insert = "INSERT INTO public.amostratestes(idamostratestes, "
//                                    + "nmamostratestes, vlresultado, tipoAmostra) "
//                                    + "VALUES (" + ultimo.ult + ", '" + tipoAmostra + "_" + contaLinhaY + "',"
//                                    + " " + valorY + ", "
//                                    + "'" + tipoAmostra + "')";
                            insert = "INSERT INTO public.matrizY(idmodelo, idamostra, "
                                    + "idparametroref, idcalibracao, vlresultado, vlreferencia, dtpredicao)"
                                    + "VALUES (4, " + contaLinhaY + ", "
                                    + "1, null, null, " + valorY + ", now())";

                            System.out.println(insert);
                            incluir.executaInclusao(insert);

                            break;
                    }
                }
                arquivoY.close();

            }

            FileInputStream arquivoX = new FileInputStream(new File(
                    fileNameX));

            XSSFWorkbook workbookX = new XSSFWorkbook(arquivoX);

            XSSFSheet sheetX = workbookX.getSheetAt(0);

            Iterator<Row> rowIteratorX = sheetX.iterator();
            int contaLinhaX = 0;
            while (rowIteratorX.hasNext()) {
                contaLinhaX++;

//                    if (contaLinhaX > contaLinhaY) {
//                        break;
//                    } else {
//                        System.out.println("X:" + contaLinhaX);
//                        if (contaLinhaX == contaLinhaY) {
                int contador = 0;
                Row row = rowIteratorX.next();
                Iterator<org.apache.poi.ss.usermodel.Cell> cellIterator = row.cellIterator();
                while (cellIterator.hasNext()) {
                    contador++;
                    org.apache.poi.ss.usermodel.Cell cell = cellIterator.next();
                    valorX = cell.getNumericCellValue();

//                    String sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
//                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) "
//                            + "VALUES (" + primeiraAmostra
//                            + "," + contador
//                            + "," + contaLinhaX
//                            + "," + contador
//                            + ", '1'"
//                            + "," + valorX
//                            + ")";
                    String sql = "INSERT INTO public.matrizX("
                            + "idmodelo, idamostra, nrsequencia, nrposicaolinha, nrposicaocoluna,"
                            + "vllinhacoluna)"
                            + " VALUES (4, "+contaLinhaX+", "+contador+", "+contaLinhaX+", "+contador+","
                            + " "+valorX+")";
                    System.out.println(sql);
                    incluir.executaInclusao(sql);
                }
//                        }
//                }
            }
            arquivoX.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.out.println("Arquivo Excel não encontrado!");
        }

    }

    public void carregaPlanilha(String caminho) {

        try {

            arquivo = new File(caminho);

            System.out.println(arquivo.getPath());

            // instancia a planilha
            planilha = Workbook.getWorkbook(arquivo);

            //Obendo as Abas da planilha
            Sheet[] abas = planilha.getSheets();

            aba = planilha.getSheet(0); // pega a primeira aba, ou seja, aba de indice 0.

            String[][] matriz = new String[aba.getRows()][aba.getColumns()];

            //matriz.length -> representa as linhas da matriz
            //matriz[0].length -> pega o tamanho da linha [0], ou seja, pega o número de colunas
            Cell[] cel; // instancia um array de cÃ©lulas que irá auxiliar no povoamento da matriz

            for (int i = 0; i < matriz.length; i++) {

                cel = aba.getRow(i);

                for (int j = 0; j < matriz[0].length; j++) {

                    // pega os dados da celula cel[j] e adiciona na matriz
                    matriz[i][j] = cel[j].getContents();

                }

            }

// imprime os dados da matriz
            for (int i = 0; i < matriz.length; i++) {
                for (int j = 0; j < matriz[0].length; j++) {
                    System.out.print(matriz[i][j] + "\t");
                }
                System.out.println("");

            }

        } catch (Exception e) {

            e.printStackTrace();

        }
    }

    public void gravarImagem(int nmAmostra, int idAmostra, double vlAmostra, String caminho)
            throws SQLException, IOException, ClassNotFoundException {

        StringBuilder sb = new StringBuilder();

        sb.append(caminho);
        sb.append(nmAmostra);
        sb.append(".jpg");

        BufferedImage image = UtilImagem.carregaImg(sb.toString());
        if (image != null) {
            if (image.getHeight() > 15) {
                image = UtilImagem.redimensionaImg(image, 15, 15);
            }

            String insert = "INSERT INTO public.amostratestes(idamostratestes, nmamostratestes, vlresultado) "
                    + "VALUES (" + idAmostra + ", " + nmAmostra + ", " + vlAmostra + ")";

            IncluirDados incluir = new IncluirDados();
            incluir.executaInclusao(insert);

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
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
                            + "," + contador
                            + "," + nrLinha
                            + "," + nrColuna
                            + ", 'R'"
                            + "," + cores[0]
                            + ")";

                    incluir.executaInclusao(sql);
                    contador += 1;
                    sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
                            + "," + contador
                            + "," + nrLinha
                            + "," + nrColuna
                            + ", 'G'"
                            + "," + cores[1]
                            + ")";

                    incluir.executaInclusao(sql);
                    contador += 1;
                    sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
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

    public void gravarDadosPlanilha(int nmAmostra, int idAmostra, double vlAmostra, String caminho)
            throws SQLException, IOException, ClassNotFoundException {

        StringBuilder sb = new StringBuilder();

        sb.append(caminho);
        sb.append(nmAmostra);
        sb.append(".jpg");

        BufferedImage image = UtilImagem.carregaImg(sb.toString());
        if (image != null) {
            if (image.getHeight() > 15) {
                image = UtilImagem.redimensionaImg(image, 15, 15);
            }

            String insert = "INSERT INTO public.amostratestes(idamostratestes, nmamostratestes, vlresultado) "
                    + "VALUES (" + idAmostra + ", " + nmAmostra + ", " + vlAmostra + ")";

            IncluirDados incluir = new IncluirDados();
            incluir.executaInclusao(insert);

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
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
                            + "," + contador
                            + "," + nrLinha
                            + "," + nrColuna
                            + ", 'R'"
                            + "," + cores[0]
                            + ")";

                    incluir.executaInclusao(sql);
                    contador += 1;
                    sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
                            + "," + contador
                            + "," + nrLinha
                            + "," + nrColuna
                            + ", 'G'"
                            + "," + cores[1]
                            + ")";

                    incluir.executaInclusao(sql);
                    contador += 1;
                    sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
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

    public void gravarPlanilhas(int nmAmostra, int idAmostra, double vlAmostra, String caminho)
            throws SQLException, IOException, ClassNotFoundException {

        StringBuilder sb = new StringBuilder();

        sb.append(caminho);
        sb.append(nmAmostra);
        sb.append(".jpg");

        BufferedImage image = UtilImagem.carregaImg(sb.toString());
        if (image != null) {
            if (image.getHeight() > 15) {
                image = UtilImagem.redimensionaImg(image, 15, 15);
            }

            String insert = "INSERT INTO public.amostratestes(idamostratestes, nmamostratestes, vlresultado) "
                    + "VALUES (" + idAmostra + ", " + nmAmostra + ", " + vlAmostra + ")";

            IncluirDados incluir = new IncluirDados();
            incluir.executaInclusao(insert);

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
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
                            + "," + contador
                            + "," + nrLinha
                            + "," + nrColuna
                            + ", 'R'"
                            + "," + cores[0]
                            + ")";

                    incluir.executaInclusao(sql);
                    contador += 1;
                    sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
                            + "," + contador
                            + "," + nrLinha
                            + "," + nrColuna
                            + ", 'G'"
                            + "," + cores[1]
                            + ")";

                    incluir.executaInclusao(sql);
                    contador += 1;
                    sql = "INSERT INTO public.matrizamostra(idamostratestes, nrsequencia, "
                            + "nrlinha, nrcoluna, dsidentifica, vlresultado) VALUES (" + idAmostra
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

}
