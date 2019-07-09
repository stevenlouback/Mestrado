/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.tools;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.BasicHttpParams;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;

/**
 *
 * @author Marlons
 */
public class genericoWS {

    // default tempo de conexao para longa duracao!
    private static int TIMEOUT_CONEXAO = 20000; // 20 segundos
    private static int TIMEOUT_SOCKET = 30000; // 30 segundos
    public Gson gson;
    private GsonBuilder gsonBuilder = new GsonBuilder();
    public StringBuilder result = new StringBuilder();

    public genericoWS() {
        gsonBuilder.setDateFormat("yyyy-MM-dd'T'HH:mm:ss");
        gson = gsonBuilder.create();
    }

    public String toString(InputStream is) throws IOException {

        byte[] bytes = new byte[3145728];

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        int lidos;
        while ((lidos = is.read(bytes)) > 0) {
            baos.write(bytes, 0, lidos);
        }
        return new String(baos.toByteArray());
    }

    public String getRESTFileContent(String url) {

        System.out.println("Url solicitada : " + url);

        HttpParams httpParameters = new BasicHttpParams();

        // Configura o timeout da conexao em milisegundos ate que a conexao
        // seja estabelecida
        HttpConnectionParams.setConnectionTimeout(httpParameters,
                TIMEOUT_CONEXAO);

        // Configura o timeout do socket em milisegundos do tempo
        // que sera utilizado para aguardar os dados
        HttpConnectionParams.setSoTimeout(httpParameters, TIMEOUT_SOCKET);

        // passa os parametros para a conexao
        HttpClient httpclient = new DefaultHttpClient(httpParameters);
        HttpGet httpget = new HttpGet(url);
        InputStream instream = null;

        try {
            HttpResponse response = httpclient.execute(httpget);

            instream = response.getEntity().getContent();

            return toString(instream);

        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } finally {
            try {
                instream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    public String insertObject(Object object, String caminhoWS, String path, String method) {
        setTimeShort();
        try {
            
//            URL url = new URL(CaminhoWebService.getParam().getUrlWebService(path, method));
            URL url = new URL(caminhoWS+path);
            System.out.println(url);
            HttpURLConnection conexao = (HttpURLConnection) url
                    .openConnection();

            conexao.setRequestMethod("POST");
            conexao.addRequestProperty("Content-type", "application/json");

            conexao.setDoOutput(true);

            conexao.connect();

            OutputStream ops = conexao.getOutputStream();

//            System.out.println("JSON: " + gson.toJson(object));

            ops.write(gson.toJson(object).getBytes());
            ops.flush();

            InputStream is = conexao.getInputStream();

            String resut = toString(is);

            conexao.disconnect();

            return resut;

        } catch (Exception e) {
            e.printStackTrace();
            return "-1";
        }
    }

    public void setTimeShort() {
        TIMEOUT_CONEXAO = 10000; // 10 segundos
        TIMEOUT_SOCKET = 10000; // 10 segundos

    }

    public void setTimeLong() {
        TIMEOUT_CONEXAO = 50000; // 50 segundos
        TIMEOUT_SOCKET = 60000; // 60 segundos
    }


}
