package com.mf2solucoes.application.repository;

import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.modelo;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import static com.mf2solucoes.tools.Constants.modeloADD;
import static com.mf2solucoes.tools.Constants.modeloGetALL;
import com.mf2solucoes.tools.DateDeserializer;
import com.mf2solucoes.tools.genericoWS;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.WebResource;
import java.io.Serializable;
import java.util.Date;
import java.util.List;

/**
 *
 * @author Marlons
 */
public class modelos implements Serializable {

    private static final long serialVersionUID = 1L;

    public modelo guardar(modelo modelo) {

        if (modelo.getDtcriacao() == null) {

        } else {
            modelo.setDtcriacao(modelo.getDtcriacao().replace("/", "-"));
        }

        
        genericoWS ws = new genericoWS();
        ws.insertObject(modelo, BASE_URI, modeloADD, "POST");

        return null;
    }

    public List<modelo> findAll() {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(modeloGetALL);
        String json = wr.get(String.class);
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<modelo>>() {
        }.getType());
    }

    public List<modelo> findLogin(String login) {
        return null;
    }

    public List<modelo> findBloqueio(boolean bloqueio) {
        return null;
    }
}
