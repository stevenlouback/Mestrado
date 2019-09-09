package com.mf2solucoes.application.beans;

//import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.calibracao;
import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.application.repository.calibracaos;
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
@ManagedBean(name = "calibracaoBean")
@ViewScoped
public class CalibracaoBean implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    private calibracao calibracao;

    @Setter
    @Getter
    private modelo modelo;

    @Setter
    @Getter
    private List<calibracao> list_Calibracao = new ArrayList<>();

    @Inject
    private calibracaos calibracaos;

    public CalibracaoBean() {
        limpar();
    }

    private void limpar() {
        calibracao = new calibracao();
    }

    public boolean isEditando() {
        return this.calibracao.getIdcalibracao() != null;
    }

    public boolean isOutlier() {
        if (calibracao.getOutlier() == null) {
            return false;
        }

        System.out.println(calibracao.getOutlier() > 0);

        return calibracao.getOutlier() > 0;
    }

    @SuppressWarnings("unchecked")
    public void listarTodos() {
        calibracaos = new calibracaos();

        List<calibracao> list_AuxParam = new ArrayList<>();
//        list_Parametro = parametros.findAll();
        calibracao calibracao = new calibracao();
        calibracao.setIdmodelo(Long.valueOf("2"));
        calibracao = calibracaos.findCalibrado(calibracao);
        list_AuxParam.add(calibracao);
        list_Calibracao.clear();//inicializa a lista
//        Para não mexer no WS resolvi tratar aqui, depois nós vemos o que fazemos
        for (int i = 0; i < list_AuxParam.size(); i++) {
            calibracao novoParametro = new calibracao();
            novoParametro.setIdmodelo(list_AuxParam.get(i).getIdmodelo());
            novoParametro.setIdcalibracao(list_AuxParam.get(i).getIdcalibracao());
            novoParametro.setInativo(list_AuxParam.get(i).getInativo());
            novoParametro.setDtcalibracao(list_AuxParam.get(i).getDtcalibracao());
            novoParametro.setRmsec(list_AuxParam.get(i).getRmsec());
            novoParametro.setRmsep(list_AuxParam.get(i).getRmsep());
            novoParametro.setCoeficiente(list_AuxParam.get(i).getCoeficiente());
            novoParametro.setSensibilidade(list_AuxParam.get(i).getSensibilidade());
            novoParametro.setLimitedetecta(list_AuxParam.get(i).getLimitedetecta());
            novoParametro.setQuantificacao(list_AuxParam.get(i).getQuantificacao());

            modelo modelo = new modelo();
            modelo.setIdmodelo(novoParametro.getIdmodelo());

            modelos modelos = new modelos();
            modelo = modelos.modeloPorId(modelo);

            novoParametro.setModelo(modelo);

            list_Calibracao.add(novoParametro);
        }

    }

    public void calibracaoModelo() {
        Mensagens msg = new Mensagens();
        modeloService modeloService = new modeloService();

        if (calibracao.getModelo().getIdmodelo() == null) {
            msg.addError("idmodeloinfo", "");
            return;
        }

        if (calibracao.getLatente() == null) {
            msg.addError("latenteinfo", "");
            return;
        }

        if (calibracao.getOutlier() == null) {
            msg.addError("outlierinfo", "");
            return;
        }

        this.modelo = modeloService.calibrarModelo(
                calibracao.getModelo().getIdmodelo(),
                calibracao.getLatente(),
                calibracao.getOutlier(),
                calibracao.getCorteOutlier());
        limpar();
        msg.addInfo("calibrado", "");
    }

}
