package com.mf2solucoes.application.service;

import com.mf2solucoes.application.modelDb.parametro;
import com.mf2solucoes.application.repository.parametros;
import java.io.Serializable;
import javax.inject.Inject;
import javax.transaction.Transactional;

/**
 *
 * @author Mfsantos
 */
public class parametroService implements Serializable {

    private static final long serialVersionUID = 1L;

    @Inject
    private parametros parametros;

    @Transactional
    public parametro salvar(parametro parametro) {
        return parametros.guardar(parametro);
    }
}