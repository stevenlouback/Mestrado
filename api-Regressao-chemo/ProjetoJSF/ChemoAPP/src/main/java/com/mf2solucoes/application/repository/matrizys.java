package com.mf2solucoes.application.repository;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.mf2solucoes.application.modelDb.matrizY;
import com.mf2solucoes.tools.Constants;
import static com.mf2solucoes.tools.Constants.BASE_URI;
import static com.mf2solucoes.tools.Constants.matrizyGetALL;
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
public class matrizys implements Serializable {

    private static final long serialVersionUID = 1L;



    public List<matrizY> matrizYPorModelo(matrizY matrizy) {
        Client c = Client.create();
        WebResource wr = c.resource(BASE_URI).path(matrizyGetALL).path(String.valueOf(matrizy.getModelo().getIdmodelo()));
        String json = wr.get(String.class);
        return retornaListaJson(json);
    }

    public List<matrizY> findLogin(String login) {
        return null;
    }

    public List<matrizY> findBloqueio(boolean bloqueio) {
        return null;
    }

    public List<matrizY> retornaListaJson(String json) {
        GsonBuilder gson = new GsonBuilder().registerTypeAdapter(Date.class, new DateDeserializer());
        return gson.create().fromJson(json, new TypeToken<List<matrizY>>() {
        }.getType());
    }

    public static void main(String[] args) {
        matrizys mat = new matrizys();
        matrizY m = new matrizY();
        m.setIdmodelo(1);

        List<matrizY> lista = mat.matrizYPorModelo(m);
        
    }
}
