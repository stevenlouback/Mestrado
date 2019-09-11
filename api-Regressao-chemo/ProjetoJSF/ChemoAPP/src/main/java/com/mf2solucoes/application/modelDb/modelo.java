/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.validation.constraints.NotBlank;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;

/**
 *
 * @author Marlons
 */
@EqualsAndHashCode
@Entity
public class modelo implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    @Id
    private Long idmodelo;
    @Setter
    @Getter
    @NotBlank(message = "{model.name}")
    private String nmmodelo;
    @Setter
    @Getter
    @NotBlank(message = "{model.metodo}")
    private String nmmetodoreferencia;
    @Setter
    @Getter
    @NotBlank(message = "{model.instrumento}")
    private String tpinstrumento;
    @Setter
    @Getter
    @NotBlank(message = "{'model.descricao'}")
    private String dsmodelo;
    @Setter
    @Getter
    private String dtcriacao;

    @Setter
    @Getter
    private List<parametro> listaParametro = new ArrayList<>();

    /**
     * Constructor
     */
    public modelo() {
    }

    public void adicionarItemVazio() {
        if (this.getListaParametro().size() > 1) {
            ordenaPorNumero(listaParametro);
        }

        parametro parametro = new parametro();
        this.getListaParametro().add(0, parametro);
    }

// Para ordenar por numeros
    private static void ordenaPorNumero(List<parametro> lista) {
        Collections.sort(lista, new Comparator<parametro>() {
            @Override
            public int compare(parametro o1, parametro o2) {
                return o1.getIdparametroref().compareTo(o2.getIdparametroref());
            }

        });

    }
}
