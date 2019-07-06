/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.service.modeloService;
import java.io.Serializable;
import java.util.ArrayList;
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
    private List<modelo> list_Modelo = new ArrayList<>();
    
    @Inject
    private modelos modelos;
    
    @Inject
    private modeloService modeloService;
    
    @Setter
    @Getter
    String tpModelo;
    
    @Setter
    @Getter
    String espectro;
    
    public cargaIsoladaBean() {
        limpar();
        preencheCombo1();
    }
    
    public void initialize() {
        preencheCombo1();
    }
    
    public boolean isIMAGEM() {
        if (tpModelo == null){
            return false;
        }
        return tpModelo.equals("IMG");
    }
    
    public boolean isNIR() {
        if (tpModelo == null){
            return false;
        }
        return tpModelo.equals("NIR");
    }

    private void limpar() {
        modelos = new modelos();
        modeloService = new modeloService();
        modelo = new modelo();
    }
    
    public void preencheCombo1() {
        list_Modelo = modelos.findAll();
    }
    
}
