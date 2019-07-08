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
import com.mf2solucoes.tools.Mensagens;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import javax.faces.bean.ManagedBean;
import lombok.Getter;
import lombok.Setter;
import javax.inject.Inject;
import javax.faces.bean.ViewScoped;

/**
 *
 * @author Marlons
 */
//@Named("modeloB")
@ManagedBean(name = "modeloB")
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
        Mensagens msg = new Mensagens();
        try {
            modeloService = new modeloService();
            
            if (modelo.getNmmodelo().equals("")){
                msg.addError("model.validation.name", modelo);
                return;
            }
            
            if (modelo.getTpinstrumento().equals("")){
                msg.addError("model.validation.instrumento", modelo);
                return;
            }
            
            if (modelo.getNmmetodoreferencia().equals("")){
                msg.addError("model.validation.metodo", modelo);
                return;
            }
            
            if (modelo.getDsmodelo().equals("")){
                msg.addError("model.validation.descricao", modelo);
                return;
            }
            
            this.modelo = modeloService.salvar(modelo);
            limpar();
            msg.addInfo("saved", "");
        } catch (Exception e) {
            
            msg.addError(String.valueOf(e), modelo);
            e.printStackTrace();
        }
    }
    
    @SuppressWarnings("unchecked")
    public void listarTodos() {
        modelos = new modelos();
        list_Modelo = modelos.findAll();
    }
    
    public modelo modeloPorId(modelo modelo){
        return modelos.modeloPorId(modelo);
    }


    
    
    
}
