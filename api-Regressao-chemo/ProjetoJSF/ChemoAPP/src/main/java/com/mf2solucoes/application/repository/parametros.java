package com.mf2solucoes.application.repository;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.tools.Constants;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import static com.mf2solucoes.tools.Constants.parametroADD;
import static com.mf2solucoes.tools.Constants.parametroGetALL;
import com.mf2solucoes.tools.DateDeserializer;
import com.mf2solucoes.tools.Mensagens;
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
public class parametros implements Serializable {

    private static final long serialVersionUID = 1L;

    public parametro guardar(parametro parametro) {

//        Gson gson = new Gson();
//        String json = gson.toJson(parametro);
//        
//        Client c = Client.create();
//        WebResource wr = c.resource(BASE_URI).path("/parametros/add/param="+json);
//        json = wr.get(String.class);
//        
        if (parametro.getIdparametroref() == null) {
            Long x = Long.parseLong("0");
            parametro.setIdparametroref(x);
        }

        genericoWS ws = new genericoWS();
        ws.insertObject(parametro, BASE_URI, parametroADD, "POST");

        Mensagens msg = new Mensagens();
        msg.addInfo("saved", "");
        return null;
    }

    public List<parametro> findAll() {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(parametroGetALL);
        String json = wr.get(String.class);
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<parametro>>() {
        }.getType());
    }

    public List<parametro> findLogin(String login) {
        return null;
    }

    public List<parametro> findBloqueio(boolean bloqueio) {
        return null;
    }
}
