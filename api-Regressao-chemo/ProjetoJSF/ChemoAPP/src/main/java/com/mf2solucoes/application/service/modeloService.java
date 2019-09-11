package com.mf2solucoes.application.service;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.repository.modelos;
import java.io.Serializable;
import java.math.BigDecimal;
import javax.inject.Inject;
import javax.transaction.Transactional;

/**
 *
 * @author Mfsantos
 */
public class modeloService implements Serializable {

    private static final long serialVersionUID = 1L;

    
    private modelos modelos;

    @Transactional
    public modelo salvar(modelo modelo) {
        modelos = new modelos();
        return modelos.guardar(modelo);
    }
    
    @Transactional
    public modelo calibrarModelo(Long idmodelo, Long latente, Long outlier, BigDecimal corte) {
        modelos = new modelos();
        return modelos.calibrarModelo(idmodelo, latente, outlier, corte);
    }
}