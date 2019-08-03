package com.mf2solucoes.application.beans;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.modelDb.predicao;
import com.mf2solucoes.application.repository.modelos;
import com.mf2solucoes.application.repository.predicoes;
import com.mf2solucoes.application.service.parametroService;
import com.mf2solucoes.application.service.predicaoService;
import com.mf2solucoes.tools.Mensagens;
import java.io.Serializable;
import java.math.BigDecimal;
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
import org.primefaces.model.chart.BarChartModel;
import org.primefaces.model.chart.BarChartSeries;
import org.primefaces.model.chart.ChartSeries;

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
        //preencheComboModelos();
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

            //preencheComboModelos();
            if (predicao.getIdamostra() != null) {

                this.list_Predicao = new ArrayList<>();
                this.predicao = predicaoService.pesquisar(predicao);
                System.out.println(predicao.toString());
                this.list_Predicao.add(predicao);
                salvar();
                //graficoBarras();
            }

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
            //limpar();
//            msg.addInfo("saved", "");
            
            if (predicao.getValorreferencia() != null) {
                BigDecimal referencia = new BigDecimal(predicao.getValorreferencia());
                BigDecimal predito = new BigDecimal(predicao.getValorpredito());
                BigDecimal diferenca = referencia.subtract(predito);
                diferenca = diferenca.abs();
                BigDecimal rmsec = new BigDecimal(predicao.getRmsec());
                rmsec = rmsec.add(new BigDecimal(10));

                if (diferenca.compareTo(rmsec) == 1) {
                    msg.addInfo("amostra.outlier", "");
                }
            }
        } catch (Exception e) {
            msg.addError(String.valueOf(e), predicao);
            e.printStackTrace();
        }
    }

    //    @PostConstruct
    public void preencheComboModelos() {
        list_Modelo = modelos.findAll();
    }

    public BarChartModel graficoBarras() {
        BarChartModel categoryModel = new BarChartModel();
        ChartSeries barraReferencia = new BarChartSeries();
        ChartSeries barraPredito = new BarChartSeries();

        if (this.predicao.getIdamostra() != null) {
            barraReferencia.setLabel("Valor Referência");
            barraReferencia.set("", Double.parseDouble(this.predicao.getValorreferencia()));
            barraPredito.setLabel("Valor Predito");
            barraPredito.set("", Double.parseDouble(this.predicao.getValorpredito()));

            categoryModel.addSeries(barraReferencia);
            categoryModel.addSeries(barraPredito);

            categoryModel.setTitle("Referência X Predito");
            categoryModel.setLegendPosition("w");
            categoryModel.setShowPointLabels(true);
            return categoryModel;
        }

        return categoryModel;
    }

//    public BarChartModel graficoBarras() {
//        BarChartModel model = new BarChartModel();
//        BarChartSeries barra = new BarChartSeries();
//
//        if (this.predicao.getIdamostra() != null) {
//            barra.setLabel("Predição");
//            barra.set("Valor de Referência", Double.parseDouble(this.predicao.getValorreferencia()));
//            barra.set("Valor de Predito", Double.parseDouble(this.predicao.getValorpredito()));
//
//            model.addSeries(barra);
//            return model;
//        }
//
//        return model;
//    }
}
