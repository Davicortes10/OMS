import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class DataFrameFinal:

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será processado e analisado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()  # Mantém os dados originais intactos
    
    def verificar_valores_ausentes_por_pais(self) -> pd.Series:
        
        if 'Country' not in self.df.columns:
            raise KeyError("❌ O DataFrame deve conter a coluna 'Country' para segmentação dos dados.")

        valores_faltantes = (
            self.df.isnull()
            .groupby(self.df['Country'])
            .sum()
            .sum(axis=1)
            .sort_values(ascending=False)
        )

        print("\n📉 Contagem de valores ausentes por país:")
        print(valores_faltantes)
        return valores_faltantes