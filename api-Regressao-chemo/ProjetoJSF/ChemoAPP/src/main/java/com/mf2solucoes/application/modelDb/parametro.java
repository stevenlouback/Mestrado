/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import java.math.BigDecimal;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
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
    @NotNull(message = "{model.name}")
    private modelo modelo;
    @Setter
    @Getter
    @NotBlank(message="{parametro.name}")
    private String nmparametroref;
    @Setter
    @Getter
    private Long idmodelo;
    @Setter
    @Getter
    @Column(precision = 13, scale = 8)
    private BigDecimal valorMovto = BigDecimal.ZERO;

    /**
     * Constructor
     */
    public parametro() {
    }
}
