package com.mf2solucoes.application.service;

import com.mf2solucoes.application.modelDb.amostra;
import com.mf2solucoes.application.repository.amostras;
import java.io.Serializable;
import javax.inject.Inject;
import javax.transaction.Transactional;

/**
 *
 * @author Mfsantos
 */
public class amostraService implements Serializable {

    private static final long serialVersionUID = 1L;

    
    private amostras amostras;

    @Transactional
    public amostra salvar(amostra amostra) {
        amostras = new amostras();
        return amostras.guardar(amostra);
    }
}