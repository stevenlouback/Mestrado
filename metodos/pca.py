import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt # NOTE: This was tested with matplotlib v. 2.1.0'''

class PCA(object):
    def testePCA(self, mat):

        data = pd.DataFrame(index=mat)
        # retorna os dados da matriz
        print(data.head())

        #retorna as dimensoes da matriz
        print(data.shape())

        # Perform PCA on the data
        # First center and scale the data
        scaled_data = preprocessing.scale(data)

        pca = PCA() # create a PCA object
        pca.fit(scaled_data) # do the math - Aqui [e feito o PCA, SCORE e LOADINGS e VARIACAO
        pca_data = pca.transform(scaled_data) # get PCA coordinates for scaled_data

        #The following code constructs the Scree plot
        #calculamos o percentual de variancia para cada componente principal
        per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)

        #Criacao dos Labels para cada Component Principal
        labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]

        plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
        plt.ylabel('Porcentagem de variação explicada')
        plt.xlabel('Componente Principal')
        plt.title('Scree Plot')
        plt.show()

        #the following code makes a fancy looking plot using PC1 and PC2 ou o código a seguir cria uma plotagem de aparência sofisticada usando PC1 e PC2
        pca_df = pd.DataFrame(pca_data, index=[*wt, *ko], columns=labels)

        plt.scatter(pca_df.PC1, pca_df.PC2)
        plt.title('My PCA Graph')
        plt.xlabel('PC1 - {0}%'.format(per_var[0]))
        plt.ylabel('PC2 - {0}%'.format(per_var[1]))

        for sample in pca_df.index:
            plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

        plt.show()

        # Determine which genes had the biggest influence on PC1

        ## get the name of the top 10 measurements (genes) that contribute
        ## most to pc1.
        ## first, get the loading scores - pca.components_[0] zero vai ser a PC1
        loading_scores = pd.Series(pca.components_[0], index=genes)
        ## now sort the loading scores based on their magnitude
        sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

        # get the names of the top 10 genes
        top_10_genes = sorted_loading_scores[0:10].index.values

        ## print the gene names and their scores (and +/- sign)
        print(loading_scores[top_10_genes])
        # <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>

