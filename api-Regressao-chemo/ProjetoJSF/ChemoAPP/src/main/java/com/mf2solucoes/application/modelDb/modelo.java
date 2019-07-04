/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import java.util.Objects;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Id;
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
    private String nmmodelo;
    @Setter
    @Getter
    private String nmmetodoreferencia;
    @Setter
    @Getter
    private String tpinstrumento;
    @Setter
    @Getter
    private String dsmodelo;
    @Setter
    @Getter
    private String dtcriacao;

    /**
     * Constructor
     */
    public modelo() {
    }

}
