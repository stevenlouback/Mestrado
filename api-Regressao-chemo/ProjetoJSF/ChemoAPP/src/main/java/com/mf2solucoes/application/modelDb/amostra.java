package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
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
public class amostra implements Serializable {

    private static final long serialVersionUID = 1L;

    @Setter
    @Getter
    @Id
    private Long idamostra;
    @Setter
    @Getter
    private amostra amostra;
    @Setter
    @Getter
    private String tpamostra; //Nome da Amostra
    @Setter
    @Getter
    private String dsobservacoes;
    @Setter
    @Getter
    private String dtcoletaamostra;
    @Setter
    @Getter
    @Lob
    @Column(columnDefinition = "mediumblob")
    private byte[] imamostra;

    
    
    /**
     * Constructor
     */
    public amostra() {
    }

}
