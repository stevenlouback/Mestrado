package com.mf2solucoes.application.repository;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.predicao;
import com.mf2solucoes.tools.Constants;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import static com.mf2solucoes.tools.Constants.predicaoADD;
import static com.mf2solucoes.tools.Constants.predicaoGetId;
import com.mf2solucoes.tools.DateDeserializer;
import com.mf2solucoes.tools.Mensagens;
import com.mf2solucoes.tools.genericoWS;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.WebResource;
import java.io.IOException;
import java.io.Serializable;
import java.util.Date;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.codehaus.jackson.map.ObjectMapper;

/**
 *
 * @author Marlons
 */
public class predicoes implements Serializable {

    private static final long serialVersionUID = 1L;

    public predicao guardar(predicao predicao) {

        genericoWS ws = new genericoWS();
        ws.insertObject(predicao, BASE_URI, predicaoADD, "POST");

        return null;
    }

    public predicao predicaoPorAmostra(predicao predicao) {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(predicaoGetId).path(String.valueOf(predicao.getModelo().getIdmodelo())).path(String.valueOf(predicao.getIdamostra()));
        String json = wr.get(String.class);
        ObjectMapper mapper = new ObjectMapper();
        try {
            predicao = mapper.readValue(json, predicao.class);
        } catch (IOException ex) {
            Logger.getLogger(modelos.class.getName()).log(Level.SEVERE, null, ex);
        }
        return predicao;
    }

    public List<predicao> predicaoListPorAmostra(predicao predicao) {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(predicaoGetId).path(String.valueOf(predicao.getModelo().getIdmodelo())).path(String.valueOf(predicao.getIdamostra()));
        String json = wr.get(String.class);
        return retornaListaJson(json);
    }

    public List<predicao> findLogin(String login) {
        return null;
    }

    public List<predicao> findBloqueio(boolean bloqueio) {
        return null;
    }

    public List<predicao> retornaListaJson(String json) {
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<predicao>>() {
        }.getType());
    }

    public static void main(String[] args) {
        predicoes predicoes = new predicoes();
        predicao p = new predicao();
        p.setIdamostra("348");

        p = predicoes.predicaoPorAmostra(p);
        System.out.println(p.toString());
    }
}
