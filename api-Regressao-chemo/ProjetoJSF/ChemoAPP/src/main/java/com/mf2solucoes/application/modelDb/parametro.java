/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import java.util.Date;
import java.util.Objects;
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
public class parametro  implements Serializable {

    private static final long serialVersionUID = 1L;
    
    @Id
    @Setter
    @Getter
    private Long idparametroref;
    @Setter
    @Getter
    private modelo modelo;
    @Setter
    @Getter
    private String nmparametroref;
    @Setter
    @Getter
    private Long idmodelo;

    /**
     * Constructor
     */
    public parametro() {
    }
}
