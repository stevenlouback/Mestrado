package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.matrizY;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.repository.matrizys;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.service.matrizyservice;
import com.mf2solucoes.tools.Mensagens;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import javax.faces.bean.ManagedBean;
//import javax.faces.bean.ManagedBean;
//import javax.faces.bean.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import lombok.Getter;
import lombok.Setter;
import org.omnifaces.cdi.ViewScoped;

/**
 *
 * @author sklcarvalho
 */
@Named("resultadosB")
@ViewScoped
public class ResultadosBean implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private matrizY matrizY;

    @Inject
    private matrizys matrizys;

    @Inject
    private matrizyservice matrizyService;

    @Setter
    @Getter
    private List<matrizY> list_matrizY = new ArrayList<>();

    @Setter
    @Getter
    private List<modelo> list_Modelo = new ArrayList<>();

    @Inject
    private modelos modelos;

    public ResultadosBean() {
        limpar();
    }

    public void initialize() {
        preencheComboModelos();
    }

    private void limpar() {
        matrizY = new matrizY();
        //this.list_Predicao = new ArrayList<>(); 
    }

    public void pesquisar() {
        try {
            matrizyService = new matrizyservice();

            preencheComboModelos();

            if (this.matrizY.getModelo() != null) {
                this.list_matrizY = new ArrayList<>();
                this.list_matrizY = matrizyService.pesquisar(matrizY);
            }

            limpar();
        } catch (Exception e) {
            Mensagens msg = new Mensagens();
            msg.addError(String.valueOf(e), matrizY);
            e.printStackTrace();
        }
    }

    //    @PostConstruct
    public void preencheComboModelos() {
        list_Modelo = modelos.findAll();
    }

}
