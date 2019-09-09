package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import java.math.BigDecimal;
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
public class calibracao implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    @Id
    private Long idcalibracao;
    @Setter
    @Getter
    private Long idmodelo;
    @Setter
    @Getter
    private modelo modelo;
    @Setter
    @Getter
    private String inativo;
    @Setter
    @Getter
    private String dtcalibracao;
    @Setter
    @Getter
    private BigDecimal rmsec;
    @Setter
    @Getter
    private BigDecimal rmsep;
    @Setter
    @Getter
    private BigDecimal coeficiente;
    @Setter
    @Getter
    private BigDecimal sensibilidade;
    @Setter
    @Getter
    private BigDecimal limitedetecta;
    @Setter
    @Getter
    private BigDecimal quantificacao;
    @Setter
    @Getter
    private Long latente;
    @Setter
    @Getter
    private Long outlier;
    @Setter
    @Getter
    private BigDecimal corteOutlier;

    /**
     * Constructor
     */
    public calibracao() {
    }

}
