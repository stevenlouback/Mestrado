/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.beans;

//import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
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
import org.apache.commons.lang3.StringUtils;

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

    @Setter
    @Getter
    private String nmparametroref;

    @Setter
    @Getter
    private parametro parametroSelecionado;

    @Setter
    @Getter
    private parametro parametroLinhaEditavel;

    public ModeloBean() {
        limpar();
    }

    private void limpar() {
//        modelos = new modelos();
//        modeloService = new modeloService();
        modelo = new modelo();
        this.modelo.adicionarItemVazio();
    }

    public boolean isEditando() {
        return this.modelo.getIdmodelo() != null;
    }

    public void salvar() {
        Mensagens msg = new Mensagens();
        try {
            modeloService = new modeloService();

            if (modelo.getNmmodelo().equals("")) {
                msg.addError("model.validation.name", modelo);
                return;
            }

            modelo.setTpinstrumento("img");
            if (modelo.getTpinstrumento().equals("")) {;
                msg.addError("model.validation.instrumento", modelo);
                return;
            }

            if (modelo.getNmmetodoreferencia().equals("")) {
                msg.addError("model.validation.metodo", modelo);
                return;
            }

            if (modelo.getDsmodelo().equals("")) {
                msg.addError("model.validation.descricao", modelo);
                return;
            }
//            this.modelo = modeloService.salvar(modelo);
            limpar();
            msg.addInfo("saved", "");
        } catch (Exception e) {

            msg.addError(String.valueOf(e), modelo);
            e.printStackTrace();
        }
    }

    public void carregarParametroLinhaEditavel() {
        Mensagens msg = new Mensagens();

        if (StringUtils.isNotEmpty(this.nmparametroref)) {
            this.parametroLinhaEditavel = new parametro();
            this.parametroLinhaEditavel.setNmparametroref(this.nmparametroref);
        }

        parametro item = this.modelo.getListaParametro().get(0);

        if (this.parametroLinhaEditavel != null) {
            if (this.existeItemComParametro(this.parametroLinhaEditavel)) {
                msg.addError("errorParametro", "");
//                return;
            } else {
                item.setIdparametroref(sequenciaParametro());
                item.setNmparametroref(this.nmparametroref);
                item.setModelo(this.getModelo());

                this.modelo.adicionarItemVazio();
                this.nmparametroref = ""; //inicializa campo
                this.parametroLinhaEditavel = null;

            }
        }
    }

    private boolean existeItemComParametro(parametro parametro) {
        boolean existeItem = false;

        for (parametro item : this.getModelo().getListaParametro()) {
            if (parametro.getNmparametroref().equals(item.getNmparametroref())) {
                existeItem = true;
                break;
            }
        }

        return existeItem;
    }

    private Long sequenciaParametro() {
        Long nrsequencia = 0L;
        for (parametro item : this.getModelo().getListaParametro()) {
            if (item.getIdparametroref() != null) {
                if (nrsequencia < item.getIdparametroref()) {
                    nrsequencia = item.getIdparametroref();
                }
            }
        }

        return nrsequencia + 1L;
    }

    @SuppressWarnings("unchecked")
    public void listarTodos() {
        modelos = new modelos();
        list_Modelo = modelos.findAll();
    }

    public modelo modeloPorId(modelo modelo) {
        return modelos.modeloPorId(modelo);
    }

//    public void calibrarModelo(Long idmodelo) {
//        Mensagens msg = new Mensagens();
//        modeloService = new modeloService();
//        this.modelo = modeloService.calibrarModelo(idmodelo);
//        limpar();
//        msg.addInfo("calibrado", "");
//    }
    public void excluirParametro() {
        List<parametro> nova = new ArrayList<parametro>();

        Long contador = 0L;
        for (parametro item : this.getModelo().getListaParametro()) {
            if (item.getIdparametroref() != null) {
                if (item.getIdparametroref() != parametroSelecionado.getIdparametroref()) {
                    contador += 1L;
                    item.setIdparametroref(contador);
                    nova.add(item);
                }
            }
        }

        this.modelo.setListaParametro(nova);

        this.modelo.adicionarItemVazio();
    }
}
