import pandas as pd
import numpy as np
from scipy import stats

class Outlier:
    

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será analisado e processado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()  # Faz uma cópia do DataFrame original para evitar alterações diretas