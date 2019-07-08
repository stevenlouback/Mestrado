package com.mf2solucoes.application.repository;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import static com.mf2solucoes.tools.Constants.modeloADD;
import static com.mf2solucoes.tools.Constants.modeloGetALL;
import static com.mf2solucoes.tools.Constants.modeloGetId;
import static com.mf2solucoes.tools.Constants.modeloGetTpAmostra;
import com.mf2solucoes.tools.DateDeserializer;
import com.mf2solucoes.tools.Mensagens;
import com.mf2solucoes.tools.genericoWS;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.WebResource;
import java.io.IOException;
import java.io.Serializable;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.codehaus.jackson.map.ObjectMapper;
import org.omnifaces.util.Json;

/**
 *
 * @author Marlons
 */
public class modelos implements Serializable {

    private static final long serialVersionUID = 1L;

    public modelo guardar(modelo modelo) {

        if (modelo.getDtcriacao() == null) {
            if (modelo.getIdmodelo() == null) {
                SimpleDateFormat formato = new SimpleDateFormat("dd-MM-yyyy");
                modelo.setDtcriacao(formato.format(new Date()));
            }
        } else {
            modelo.setDtcriacao(modelo.getDtcriacao().replace("/", "-"));
        }

        if (modelo.getIdmodelo() == null) {
            Long x = Long.parseLong("0");
            modelo.setIdmodelo(x);
        }

//        Incluido Marlons até resolver o Converter do Tipo Instrumento
        if (modelo.getTpinstrumento() == null) {
            modelo.setTpinstrumento("IMG");
        }

        genericoWS ws = new genericoWS();
        ws.insertObject(modelo, BASE_URI, modeloADD, "POST");

        Mensagens msg = new Mensagens();

        return null;
    }

    public List<modelo> findAll() {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(modeloGetALL);
        String json = wr.get(String.class);
        return retornaListaJson(json);
//        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
//        return gson.create().fromJson(json, new TypeToken<List<modelo>>() {
//        }.getType());
    }

    public List<modelo> retornaListaJson(String json) {
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<modelo>>() {
        }.getType());
    }

    public modelo modeloPorId(modelo modelo) {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(modeloGetId).path(String.valueOf(modelo.getIdmodelo()));
        String json = wr.get(String.class);

        ObjectMapper mapper = new ObjectMapper();
        try {
            modelo = mapper.readValue(json, modelo.class);
        } catch (IOException ex) {
            Logger.getLogger(modelos.class.getName()).log(Level.SEVERE, null, ex);
        }
        return modelo;
    }
    
    public List<modelo> modeloPorTipoAmostra(modelo modelo) {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(modeloGetTpAmostra).path(String.valueOf(modelo.getTpinstrumento()));
        String json = wr.get(String.class);
        return retornaListaJson(json);
    }

    public List<modelo> findLogin(String login) {
        return null;
    }

    public List<modelo> findBloqueio(boolean bloqueio) {
        return null;
    }
}
