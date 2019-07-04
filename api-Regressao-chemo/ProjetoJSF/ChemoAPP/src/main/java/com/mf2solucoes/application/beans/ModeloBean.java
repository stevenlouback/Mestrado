/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.beans;

//import com.mf2solucoes.application.modelDb.modelo;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.service.modeloService;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import javax.annotation.PostConstruct;
import javax.faces.bean.ViewScoped;
//import javax.faces.view.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import lombok.Getter;
import lombok.Setter;
//import org.omnifaces.cdi.ViewScoped;

/**
 *
 * @author Marlons
 */
@Named("modeloB")
@ViewScoped
public class ModeloBean implements Serializable {

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
    
    
    
    public ModeloBean() {
        limpar();
    }

    private void limpar() {
//        modelos = new modelos();
//        modeloService = new modeloService();
        modelo = new modelo();
    }
    
    public boolean isEditando() {
        return this.modelo.getIdmodelo()!= null;
    }

    public void salvar(){
        try {
            this.modelo = modeloService.salvar(modelo);
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }
    }
    
    @SuppressWarnings("unchecked")
    public void listarTodos() {
        list_Modelo = modelos.findAll();
    }

    
    
    
}
