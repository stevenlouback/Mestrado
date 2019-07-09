package com.mf2solucoes.application.service;


import com.mf2solucoes.application.modelDb.matrizY;
import com.mf2solucoes.application.repository.matrizys;
import java.io.Serializable;
import java.util.List;
import javax.inject.Inject;
import javax.transaction.Transactional;

/**
 *
 * @author sklcarvalho
 */
public class matrizyservice implements Serializable {

    private static final long serialVersionUID = 1L;

    @Inject
    private matrizys matrizys;

    @Transactional
    public List<matrizY> pesquisar(matrizY matrizy) {
        matrizys = new matrizys();
        return matrizys.matrizYPorModelo(matrizy);
    }
    

}