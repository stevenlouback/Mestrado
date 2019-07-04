package com.mf2solucoes.application.service;

import com.mf2solucoes.application.modelDb.modelo;
import com.mf2solucoes.application.repository.modelos;
import java.io.Serializable;
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
}