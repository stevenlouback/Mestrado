package com.mf2solucoes.tools;

import Jama.Matrix;
import Jama.SingularValueDecomposition;

/**
 * Estrategias para se usar imagens na analise de dados
 * @author MFSantos
 */
public class MinimoQuadradoParcialPLS {

    private double[][] T;

    public double[][] getT() {
        return T;
    }
    private double[][] U;

    public double[][] getU() {
        return U;
    }
    private double[][] P;

    public double[][] getP() {
        return P;
    }
    private double[][] C;

    public double[][] getC() {
        return C;
    }
    private double[][] W;

    public double[][] getW() {
        return W;
    }
    private double[] B;

    public double[] getB() {
        return B;
    }
    private double[][] Wstar;

    public double[][] getWstar() {
        return Wstar;
    }

//    Algoritmo:
//Seja X a matriz de entrada,
//            Deixe Y ser a matriz de saída,
//            Seja P a matriz de carregamento para X , e digamos a iésima coluna de P;
//    Seja Q a matriz de carregamentos para Y e deixe qi indicar a iésima coluna de Q;
//    Seja T a matriz de pontuação para X, e dê a iésima coluna de T;
//    Deixe U ser a matriz de pontuação para Y , e ui denotar a iésima coluna de U;
//    Seja W a matriz de peso PLS , e d wi denotar a iésima coluna de W;
//    e Seja B uma matriz diagonal de coeficientes diagonais bi
//    Então:
//Para cada fator i a ser calculado:
//Inicialmente , escolha ui como o maior vetor de colunas em X(tendo a maior soma de quadrados),
//    mas você também pode escolher a primeira coluna.
//Enquanto (ti não convergeu para uma precisão desejada)
//Wi α X'ui (estimativa X pesos)
//Ti α Xwi (estimativa do fator X)
//Qi α Y'ti (estimativa de pesos Y)
//Ui = Yqi (pontuação Y estimada)
//Bi = t'u (coeficiente de previsão de cálculo b)
//Pi = X't (estimativa de carga de fator X)
//X = X - tp '(deflação X)
    
    
    // Nipals
    public MinimoQuadradoParcialPLS(final double[][] X, final double[][] Y, int factors) {
        // Initialize and prepare the data
        // Inicializar e preparar os dados
        int rows = X.length;
        int xcols = X[0].length;
        int ycols = Y[0].length;

        double[][] E = new double[rows][xcols];
        E = X;
        double[][] F = new double[rows][ycols];
        F = Y;

        T = new double[rows][factors];
        U = new double[rows][factors];
        P = new double[xcols][factors];
        C = new double[ycols][factors];
        W = new double[xcols][factors];
        B = new double[factors];

        double[] varX = new double[factors];
        double[] varY = new double[factors];

        // Initialize the algorith
        // Inicializa o Algoritmo
        boolean stop = false;
        //  dlg.setVisible(true);
        for (int factor = 0; factor < factors && !stop; factor++) {
            // Select t as the largest column from X,
            // Seleciona T como a maior coluna de X
            int lE = largest(E);
            double[] t = new double[rows];
            for (int i = 0; i < rows; i++) {
                t[i] = E[i][lE];
            }
            //double[] t = E[largest(E)];
            // Select u as the largest column from Y.
            // Seleciona U maior coluna de Y
            int lF = largest(F);
            double[] u = new double[rows];
            for (int i = 0; i < rows; i++) {
                u[i] = F[i][lF];
            }
            //double[] u = F[largest(F)];
            // Will store weights for X and Y
            // Armazena Pesos para X e Y
            double[] w = new double[xcols];
            double[] c = new double[ycols];

            double norm_t = Euclidean(t);

            // Iteration region
            // Região de Iteração
            while (norm_t > 1e-14) {
                // Store initial t to check convergence
                // Armazena inicial t para verificar convergência
                //  double[] t0 = (double[])t.Clone();
                double[] t0 = t;

                // Passo 1. Estimativa w (pesos X): w α E '* u 
                // (no papel de Abdi, X é referido como E).
                // 1.1. Calcule w = E '* u; 
                w = new double[xcols];
                for (int j = 0; j < w.length; j++) {
                    for (int i = 0; i < u.length; i++) {
                        w[j] = w[j] + E[i][j] * u[i];
                    }
                }
                // 1.2. Normalize w (w = w/norm(w))
                double Ew = Euclidean(w);
                for (int i = 0; i < w.length; i++) {
                    w[i] = w[i] / Ew;
                }
                // Step 2. Estimate t (X factor scores): t ∝ E*w
                //   (in Abdi's paper, X is referred as E).
                // 2.1. Compute t = E*w

                // Passo 2. Estimativa t (pontuações factor X): t α E * w 
                // (no papel de Abdi, X é referido como E). 
                t = new double[rows];
                for (int i = 0; i < t.length; i++) {
                    for (int j = 0; j < w.length; j++) {
                        t[i] = t[i] + E[i][j] * w[j];
                    }
                }
                // 2.2. Normalize t: t = t/norm(t)
                double Et = Euclidean(t);
                for (int i = 0; i < t.length; i++) {
                    t[i] = t[i] / Et;
                }
                // Step 3. Estimate c (Y weights): c ∝ F't
                //   (in Abdi's paper, Y is referred as F).
                // 3.1. Compute c = F'*t0;

                // Passo 3. Estimativa c (peso Y): c α F't 
                // (no papel de Abdi, Y é referida como F). 
                // 3.1. Calcule c = F '* t0; 
                c = new double[ycols];
                for (int j = 0; j < c.length; j++) {
                    for (int i = 0; i < t.length; i++) {
                        c[j] = c[j] + F[i][j] * t[i];
                    }
                }
                // 3.2. Normalize q: c = c/norm(q)
                double Ec = Euclidean(c);
                for (int i = 0; i < c.length; i++) {
                    c[i] = c[i] / Ec;
                }
                // Step 4. Estimate u (Y scores): u = F*q
                //   (in Abdi's paper, Y is referred as F).
                // 4.1. Compute u = F*q;

                // Etapa 4. Estime você (pontuação Y): u = F * q 
                // (em O artigo de Abdi, Y é referido como F). 
                // 4.1. Calcule u = F * q; 
                u = new double[rows];
                for (int i = 0; i < u.length; i++) {
                    for (int j = 0; j < c.length; j++) {
                        u[i] = u[i] + F[i][j] * c[j];
                    }
                }

                // Recalculate norm of the difference
                // Recalcula a norma da diferença 
                norm_t = 0.0;
                for (int i = 0; i < t.length; i++) {
                    double d = (t0[i] - t[i]);
                    norm_t += d * d;
                }
                norm_t = Math.sqrt(norm_t);
            }
            // End iteration
            // Fim da Iteração

            // Compute the value of b which is used to
            // predict Y from t as b = t'u [Abdi, 2010]
            // calcular o valor de b, que é usado para 
            // Y prever a partir de t como b = t'u [Abdi, 2010] U 
            double b = 0;
            for (int i = 0; i < t.length; i++) {
                b = b + t[i] * u[i];
            }
            // Compute factor loadings for X as p = E'*t [Abdi, 2010]
            // Calcula as cargas de fator para X como p = E '* t [Abdi, 2010]
            double[] p = new double[xcols];
            for (int j = 0; j < p.length; j++) {
                for (int i = 0; i < rows; i++) {
                    p[j] = p[j] + E[i][j] * t[i];
                }
            }
            // Perform deflaction of X and Y
            // Efetuar a deflação de X e Y 
            for (int i = 0; i < t.length; i++) {
                // Deflate X as X = X - t*p';
                // Desflocar X como X = X - t * p ';
                for (int j = 0; j < p.length; j++) {
                    E[i][j] = E[i][j] - t[i] * p[j];
                }
                // Deflate Y as Y = Y - b*t*q';
                // Desflate Y como Y = Y - b * t * q '; 
                for (int j = 0; j < c.length; j++) {
                    F[i][j] = F[i][j] - b * t[i] * c[j];
                }
            }
            // Calculate explained variances
            // Calcula as variações explicadas
            varY[factor] = b * b;
            double temp = 0;
            for (int i = 0; i < p.length; i++) {
                temp = temp + p[i] * p[i];
            }
            varX[factor] = temp;
            // Save iteration results
            // Salva os Resultados
            for (int i = 0; i < t.length; i++) {
                T[i][factor] = t[i];
            }
            for (int i = 0; i < p.length; i++) {
                P[i][factor] = p[i];
            }
            for (int i = 0; i < u.length; i++) {
                U[i][factor] = u[i];
            }
            for (int i = 0; i < c.length; i++) {
                C[i][factor] = c[i];
            }
            for (int i = 0; i < w.length; i++) {
                W[i][factor] = w[i];
            }
            B[factor] = b;

        }

        // Calculate the coefficient vector
        // Calcula o Vetor de Coeficiente
        Matrix Wmat = new Matrix(W);
        Matrix Pmat = new Matrix(P);
        double[][] tempB = new double[B.length][B.length];
        for (int i = 0; i < B.length; i++) {
            tempB[i][i] = B[i];
        }
        Matrix Bmat = new Matrix(tempB);
        Matrix PmatI = pinv(Pmat.transpose());
        PmatI = PmatI.times(Bmat);
        Matrix Cmat = new Matrix(C);
        PmatI = PmatI.times(Cmat.transpose());

        Wstar = PmatI.getArray();

    }

    private double Euclidean(double[] vect) {
        double result = 0;
        for (int i = 0; i < vect.length; i++) {
            result = result + Math.pow(vect[i], 2);
        }
        result = Math.sqrt(result);
        return result;
    }

    private int largest(double[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int index = 0;
        double max = 0;
        for (int i = 0; i < cols; i++) {
            double squareSum = 0.0;
            for (int j = 0; j < rows; j++) {
                squareSum = squareSum + matrix[j][i] * matrix[j][i];
            }
            if (squareSum > max) {
                max = squareSum;
                index = i;
            }
        }
        return index;
    }

    public static double MACHEPS = 2E-16;
    //algoritmo usando um cálculo inverso Pseudo Moore-Penrose ( função pinv ).

    public static Matrix pinv(Matrix x) {
        if (x.rank() < 1) {
            return null;
        }
        if (x.getColumnDimension() > x.getRowDimension()) {
            return pinv(x.transpose()).transpose();
        }
        SingularValueDecomposition svdX = new SingularValueDecomposition(x);
        double[] singularValues = svdX.getSingularValues();
        double tol = Math.max(x.getColumnDimension(),
                x.getRowDimension()) * singularValues[0] * MACHEPS;
        double[] singularValueRecip = new double[singularValues.length];
        for (int i = 0; i < singularValues.length; i++) {
            singularValueRecip[i] = Math.abs(singularValues[i]) < tol ? 0 : (1.0 / singularValues[i]);
        }
        double[][] u = svdX.getU().getArray();
        double[][] v = svdX.getV().getArray();
        int min = Math.min(x.getColumnDimension(), u[0].length);
        double[][] inverse = new double[x.getColumnDimension()][x.getRowDimension()];
        for (int i = 0; i < x.getColumnDimension(); i++) {
            for (int j = 0; j < u.length; j++) {
                for (int k = 0; k < min; k++) {
                    inverse[i][j] += v[i][k] * singularValueRecip[k] * u[j][k];
                }
            }
        }
        return new Matrix(inverse);
    }

}
