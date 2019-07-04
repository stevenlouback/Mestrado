package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.repository.parametros;
import com.mf2solucoes.application.service.parametroService;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import javax.annotation.PostConstruct;
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
@ViewScoped
public class ParametroBean implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private parametro parametro;

    @Setter
    @Getter
    private List<parametro> list_Parametro = new ArrayList<>();
    
    @Setter
    @Getter
    private List<modelo> list_Modelo = new ArrayList<>();

    @Inject
    private parametros parametros;
    
    @Inject
    private modelos modelos;

    @Inject
    private parametroService parametroService;

    public ParametroBean() {
//        limpar();
    }

    public void initialize() {
        limpar();
        listarTodos();
    }

    private void limpar() {
        parametro = new parametro();
    }

    public boolean isEditando() {
        return this.parametro.getIdparametroref() != null;
    }

    public void salvar() {
        try {
            this.parametro = parametroService.salvar(parametro);
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }
    }

    @SuppressWarnings("unchecked")
    public void listarTodos() {
        parametros = new parametros();
        list_Parametro = parametros.findAll();
    }
    
    @PostConstruct
    public void preencheCombo1() {
        list_Modelo = modelos.findAll();
    }

}
