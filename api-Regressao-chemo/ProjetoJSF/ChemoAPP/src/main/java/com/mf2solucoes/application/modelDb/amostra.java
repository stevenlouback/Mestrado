package com.mf2solucoes.application.modelDb;

import java.io.Serializable;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.Transient;
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
    private modelo modelo;
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
    @Transient
    @Column(columnDefinition = "mediumblob")
    private byte[] imagem;
    @Setter
    @Getter
    private String imamostra;
    @Setter
    @Getter
    private String dsespectro;

    /**
     * Constructor
     */
    public amostra() {
    }

}
