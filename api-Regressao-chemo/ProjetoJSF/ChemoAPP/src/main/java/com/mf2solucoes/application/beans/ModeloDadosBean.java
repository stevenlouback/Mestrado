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
import javax.faces.bean.SessionScoped;
//import javax.faces.bean.ViewScoped;
import javax.inject.Inject;
import javax.inject.Named;
import lombok.Getter;
import lombok.Setter;
import org.omnifaces.cdi.ViewScoped;

/**
 *
 * @author Marlons
 */
@Named
//@SessionScoped
@ViewScoped
public class ModeloDadosBean   implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private modelo modelo;

    public ModeloDadosBean() {
//        limpar();
    }

    @PostConstruct
    private void limpar() {
        modelo = new modelo();
    }

    @Setter
    @Getter
    private List<modelo> list_Modelo = new ArrayList<>();

    @Inject
    private modelos modelos;

    @Inject
    private modeloService modeloService;

    @SuppressWarnings("unchecked")
    public void listarTodos() {
        list_Modelo = modelos.findAll();
    }
}
