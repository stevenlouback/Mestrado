package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.repository.parametros;
import com.mf2solucoes.application.service.parametroService;
import com.mf2solucoes.tools.Mensagens;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
//import javax.faces.bean.ManagedBean;
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
@Named("parametroB")
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
        limpar();
    }

    public void initialize() {
        listarTodos();
        preencheCombo1();
    }

    private void limpar() {
        parametro = new parametro();
    }

    public boolean isEditando() {
        return this.parametro.getIdparametroref() != null;
    }

    public void salvar() {
        Mensagens msg = new Mensagens();
        try {
            if (parametro.getModelo().getDsmodelo().equals("")){
                msg.addError("parametro.validation.modelo", parametro);
                return;
            }
            
            if (parametro.getNmparametroref().equals("")){
                msg.addError("parametro.validation.name", parametro);
                return;
            }
            
            this.parametro = parametroService.salvar(parametro);
            limpar();
            msg.addInfo("saved", "");
        } catch (Exception e) {
            msg.addError(String.valueOf(e), parametro);
            System.out.println(e);
            e.printStackTrace();
        }
    }

    @SuppressWarnings("unchecked")
    public void listarTodos() {
        parametros = new parametros();
        List<parametro> list_AuxParam = new ArrayList<>();
//        list_Parametro = parametros.findAll();
        list_AuxParam = parametros.findAll();
        list_Parametro.clear();//inicializa a lista
//        Para não mexer no WS resolvi tratar aqui, depois nós vemos o que fazemos
        for (int i = 0; i < list_AuxParam.size(); i++) {
            parametro novoParametro = new parametro();
            novoParametro.setIdmodelo(list_AuxParam.get(i).getIdmodelo());
            novoParametro.setIdparametroref(list_AuxParam.get(i).getIdparametroref());
            novoParametro.setNmparametroref(list_AuxParam.get(i).getNmparametroref());
            
            modelo modelo = new modelo();
            modelo.setIdmodelo(novoParametro.getIdmodelo());
            
            modelos modelos = new modelos();
            modelo = modelos.modeloPorId(modelo);
            
            novoParametro.setModelo(modelo);
            
            list_Parametro.add(novoParametro);
        }

    }

//    @PostConstruct
    public void preencheCombo1() {
        list_Modelo = modelos.findAll();
    }

}
