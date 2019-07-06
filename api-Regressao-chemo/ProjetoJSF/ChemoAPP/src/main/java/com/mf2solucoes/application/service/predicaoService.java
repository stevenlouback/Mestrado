package com.mf2solucoes.application.service;

import com.mf2solucoes.application.modelDb.predicao;
import com.mf2solucoes.application.repository.predicoes;
import java.io.Serializable;
import java.util.List;
import javax.inject.Inject;
import javax.transaction.Transactional;

/**
 *
 * @author sklcarvalho
 */
public class predicaoService implements Serializable {

    private static final long serialVersionUID = 1L;

    @Inject
    private predicoes predicoes;

    @Transactional
    public predicao pesquisar(predicao predicao) {
        predicoes = new predicoes();
        return predicoes.predicaoPorAmostra(predicao);
    }
    
    @Transactional
    public predicao salvar(predicao predicao) {
        predicoes = new predicoes();
        return predicoes.guardar(predicao);
    }    
}