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