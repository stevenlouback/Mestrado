package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.predicao;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.repository.predicoes;
import com.mf2solucoes.application.service.parametroService;
import com.mf2solucoes.application.service.predicaoService;
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
@Named("predicaoB")
@ViewScoped
public class PredicaoBean implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private predicao predicao;

    @Inject
    private predicoes predicoes;

    @Inject
    private predicaoService predicaoService;

    @Setter
    @Getter
    private List<predicao> list_Predicao = new ArrayList<>();

    @Setter
    @Getter
    private List<modelo> list_Modelo = new ArrayList<>();

    @Inject
    private modelos modelos;

    public PredicaoBean() {
        limpar();
    }

    public void initialize() {
        preencheComboModelos();
    }

    private void limpar() {
        predicao = new predicao();
        //this.list_Predicao = new ArrayList<>(); 
    }

    public predicao predicaoPorAmostra(predicao predicao) {
        return predicoes.predicaoPorAmostra(predicao);
    }

    public void pesquisar() {
        try {
            predicaoService = new predicaoService();
            
            preencheComboModelos();

            if (predicao.getIdamostra() != null) {
                this.list_Predicao = new ArrayList<>();
                this.predicao = predicaoService.pesquisar(predicao);
                System.out.println(predicao.toString());
                this.list_Predicao.add(predicao);
                salvar();
            }

            limpar();
        } catch (Exception e) {
            Mensagens msg = new Mensagens();
            msg.addError(String.valueOf(e), predicao);
            e.printStackTrace();
        }
    }

    public void salvar() {
        Mensagens msg = new Mensagens();
        try {
            predicaoService = new predicaoService();
            this.predicao = predicaoService.salvar(predicao);
            limpar();
            msg.addInfo("saved", "");
        } catch (Exception e) {
            msg.addError(String.valueOf(e), predicao);
            e.printStackTrace();
        }
    }

    //    @PostConstruct
    public void preencheComboModelos() {
        list_Modelo = modelos.findAll();
    }

}
