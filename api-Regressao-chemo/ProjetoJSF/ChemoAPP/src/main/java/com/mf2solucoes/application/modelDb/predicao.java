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
 * @author sklcarvalho
 */
@EqualsAndHashCode
@Entity
public class predicao implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @Setter
    @Getter
    private String idamostra;
    @Setter
    @Getter
    private String valorpredito;
    @Setter
    @Getter
    private String rmsec;
    @Setter
    @Getter
    private String rmsep;
    @Setter
    @Getter
    private String dtcalibracao;
    @Setter
    @Getter
    private String idmodelo;

    @Setter
    @Getter
    private String valorreferencia;
    @Setter
    @Getter
    private String coeficiente;
    @Setter
    @Getter
    private modelo modelo;    

    /**
     * Constructor
     */
    public predicao() {
    }

    @Override
    public String toString() {
        return "predicao{" + "idamostra=" + idamostra + ", valorpredito=" + valorpredito + ", rmsec=" + rmsec + ", idmodelo=" + idmodelo + ", valorreferencia=" + valorreferencia + ", coeficiente=" + coeficiente + '}';
    }
    
    
}
