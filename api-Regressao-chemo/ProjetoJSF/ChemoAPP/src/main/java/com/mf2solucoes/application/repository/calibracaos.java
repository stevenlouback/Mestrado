/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.repository;

import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.calibracao;
import com.mf2solucoes.application.modelDb.modelo;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import static com.mf2solucoes.tools.Constants.calibracaoGetAtivo;
import static com.mf2solucoes.tools.Constants.modeloGetALL;
import com.mf2solucoes.tools.DateDeserializer;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.WebResource;
import java.io.IOException;
import java.util.Date;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.codehaus.jackson.map.ObjectMapper;

/**
 *
 * @author Marlons
 */
public class calibracaos {

    public calibracao findCalibrado(calibracao calibracao) {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(calibracaoGetAtivo).path(String.valueOf(calibracao.getIdmodelo()));
        String json = wr.get(String.class);
        
         ObjectMapper mapper = new ObjectMapper();
        try {
            calibracao = mapper.readValue(json, calibracao.class);
        } catch (IOException ex) {
            Logger.getLogger(amostras.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        return calibracao;
//        return retornaListaJson(json);

    }
    
    public List<calibracao> retornaListaJson(String json) {
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<calibracao>>() {
        }.getType());
    }

}
