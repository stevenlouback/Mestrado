package com.mf2solucoes.application.repository;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import com.mf2solucoes.tools.DateDeserializer;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.WebResource;
import java.io.Serializable;
import java.util.Date;
import java.util.List;

/**
 *
 * @author Marlons
 */
public class parametros implements Serializable {

    private static final long serialVersionUID = 1L;


    public parametro guardar(parametro parametro) {
        
        Gson gson = new Gson();
        String json = gson.toJson(parametro);
        
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path("/parametros/add/param="+json);
        json = wr.get(String.class);
        
        return null;
    }


    public List<parametro> findAll() {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path("/parametros/getall");
        String json = wr.get(String.class);
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class , new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<parametro>>() {}.getType());
    }

    public List<parametro> findLogin(String login) {
        return null;
    }

    public List<parametro> findBloqueio(boolean bloqueio) {
        return null;
    }
}
