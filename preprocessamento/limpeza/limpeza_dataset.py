import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class KNNMissingValueImputer:
    def __init__(self, df: pd.DataFrame, n_neighbors: int = 20):
        """
        Inicializa a classe com um DataFrame e configura o KNN Imputer.

        Args:
            df (pd.DataFrame): O DataFrame que será processado.
            n_neighbors (int, opcional): Número de vizinhos considerados para imputação.
                O padrão é 20.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")
        if not isinstance(n_neighbors, int) or n_neighbors <= 0:
            raise ValueError("❌ O número de vizinhos deve ser um inteiro positivo.")

        self.df = df.copy()  # Mantém os dados originais intactos
        self.n_neighbors = n_neighbors
        self.imputer = KNNImputer(n_neighbors=self.n_neighbors)
    
    def imputar_valores(self) -> pd.DataFrame:
        # Seleciona apenas colunas numéricas
        colunas_numericas = self.df.select_dtypes(exclude='object').columns
        if colunas_numericas.empty:
            raise ValueError("❌ O DataFrame não possui colunas numéricas para imputação.")

        df_imputado = self.df.copy()
        df_imputado.loc[:, colunas_numericas] = self.imputer.fit_transform(self.df[colunas_numericas])

        print(f"✅ Imputação KNN aplicada com sucesso utilizando {self.n_neighbors} vizinhos.")
        return df_imputado