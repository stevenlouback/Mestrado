package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Date;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Lob;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;

/**
 *
 * @author Marlons
 */
@EqualsAndHashCode
@Entity
public class matrizX implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    @Id
    private Long nrsequencia;
    @Setter
    @Getter
    private amostra amostra;
    @Setter
    @Getter
    private int nrposicaolinha;
    @Setter
    @Getter
    private int nrposicaocoluna;
    @Setter
    @Getter
    private int idpixel;
    @Setter
    @Getter
    @Column(precision = 13, scale = 8)
    private BigDecimal vllinhacoluna = BigDecimal.ZERO;

    /**
     * Constructor
     */
    public matrizX() {
    }

}
