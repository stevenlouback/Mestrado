/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.repository.parametros;
import com.mf2solucoes.application.service.modeloService;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import javax.annotation.PostConstruct;
import javax.faces.bean.ManagedBean;
//import javax.faces.view.ViewScoped;
//import javax.faces.bean.ViewScoped;
import org.omnifaces.cdi.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import lombok.Getter;
import lombok.Setter;

/**
 *
 * @author Marlons
 */
@Named("cargaBean")
@ViewScoped
public class cargaIsoladaBean implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private modelo modelo;

    @Setter
    @Getter
    private parametro parametroResultado;

    @Setter
    @Getter
    private Date maxDate = new Date();

    @Setter
    @Getter
    private List<modelo> list_Modelo = new ArrayList<>();

    @Setter
    @Getter
    private List<parametro> list_ParametroResultado = new ArrayList<>();

    @Inject
    private modelos modelos;

    @Inject
    private parametros parametros;

    @Setter
    @Getter
    String tpModelo;

    @Setter
    @Getter
    String espectro;

    public cargaIsoladaBean() {
        limpar();
//        preencheCombo1();
    }

    public void initialize() {
//        preencheCombo1();
    }

    public boolean isIMAGEM() {
        if (tpModelo == null) {
            return false;
        }
        return tpModelo.equals("IMG");
    }

    public boolean isNIR() {
        if (tpModelo == null) {
            return false;
        }
        return tpModelo.equals("NIR");
    }

    private void limpar() {
        modelos = new modelos();
        modelo = new modelo();
    }

    public void preencheCombo1() {
        list_Modelo = modelos.findAll();
    }

    public void buscaModeloNirImg() {
        if (tpModelo == null || tpModelo == "") {
            list_Modelo.clear();
        } else {
            modelo param = new modelo();
            param.setTpinstrumento(tpModelo);
            list_Modelo = modelos.modeloPorTipoAmostra(param);
        }
//        list_ParametroResultado = parametros.findParametrosModelo(param);
    }

    public void buscaParametrosModelo() {
        parametro param = new parametro();
        param.setModelo(modelo);
        list_ParametroResultado = parametros.findParametrosModelo(param);
    }

}
