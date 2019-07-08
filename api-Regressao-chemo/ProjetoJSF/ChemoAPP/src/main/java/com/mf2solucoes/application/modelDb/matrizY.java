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


@EqualsAndHashCode
@Entity
public class matrizY implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    @Id
    private amostra amostra;
    @Setter
    @Getter
    private String dtpredicao;
    @Setter
    @Getter
    private int idcalibracao;
    @Setter
    @Getter
    private int idparametroref;
    @Setter
    @Getter
    private int idmodelo;    
    @Setter
    @Getter
    private String vlresultado;
    @Setter
    @Getter
    private String vlreferencia;    

    public matrizY() {
    }

}
