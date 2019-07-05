/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mf2solucoes.tools;

import com.mf2solucoes.infraestrutura.utils.MessageSource;
import org.omnifaces.util.Messages;

/**
 *
 * @author Marlons
 */
public class Mensagens {
 
    public Mensagens(){
        
    }
    
    public String translate(String i18nKey) {
        return MessageSource.get(i18nKey);
    }

  
    public void addInfo(String message, Object... parameters) {
        Messages.addInfo(null, this.translate(message), parameters);
    }
    
    public void addError(String message, Object... parameters) {
        Messages.addError(null, this.translate(message), parameters);
    }
}
