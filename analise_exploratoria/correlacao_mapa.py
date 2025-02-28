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
    
    def obter_correlacoes_significativas(self, limiar: float = 0.5) -> pd.DataFrame:
        correlation_matrix = self.calcular_correlacoes()
        high_correlations = correlation_matrix[np.abs(correlation_matrix) > limiar]
        high_correlations = high_correlations[high_correlations < 1.0].dropna(how='all', axis=1).dropna(how='all', axis=0)

        print("\n🔥 Correlações Significativas (>|{:.2f}|):".format(limiar))
        return high_correlations
    
    def visualizar_heatmap_correlacoes(self, limiar: float = 0.5) -> None:
        
        high_correlations = self.obter_correlacoes_significativas(limiar)

        if high_correlations.empty:
            print("✅ Nenhuma correlação significativa encontrada para o limiar definido.")
            return

        plt.figure(figsize=(10, 8))
        sns.heatmap(high_correlations, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title(f"Heatmap das Correlações Significativas (> |{limiar}|)")
        plt.show()