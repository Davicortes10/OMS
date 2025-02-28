import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class MatrizRelacao:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será analisado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()  # Mantém os dados originais intactos
    
    def calcular_correlacoes(self) -> pd.DataFrame:
        correlation_matrix = self.df.select_dtypes(include=['float', 'int']).corr()
        print("\n📊 Matriz de Correlação Calculada:")
        return correlation_matrix