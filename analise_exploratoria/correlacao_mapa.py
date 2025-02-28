import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class MatrizRelacao:
    """
    Classe para análise de correlação entre variáveis numéricas.

    Esta classe calcula a matriz de correlação, identifica correlações significativas
    e exibe um heatmap para facilitar a visualização.

    Funcionalidades:
    - Calcular a matriz de correlação de Pearson para variáveis numéricas.
    - Filtrar apenas as correlações significativas (>0.5 ou <-0.5).
    - Exibir um heatmap das correlações relevantes.

    Attributes:
        df (pd.DataFrame): O DataFrame contendo os dados a serem analisados.
    """

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
        """
        Calcula a matriz de correlação entre as variáveis numéricas.

        Returns:
            pd.DataFrame: Matriz de correlação.

        Example:
            >>> analyzer = MatrizRelacao(df)
            >>> correlation_matrix = analyzer.calcular_correlacoes()
        """

        correlation_matrix = self.df.select_dtypes(include=['float', 'int']).corr()
        print("\n📊 Matriz de Correlação Calculada:")
        return correlation_matrix
    
    def obter_correlacoes_significativas(self, limiar: float = 0.5) -> pd.DataFrame:
        """
        Filtra as correlações mais significativas com base em um limiar.

        Args:
            limiar (float, opcional): Valor mínimo absoluto para considerar uma correlação significativa.
                O padrão é 0.5.

        Returns:
            pd.DataFrame: Matriz contendo apenas as correlações fortes.

        Example:
            >>> analyzer = MatrizRelacao(df)
            >>> high_corr = analyzer.obter_correlacoes_significativas(limiar=0.6)
        """

        correlation_matrix = self.calcular_correlacoes()
        high_correlations = correlation_matrix[np.abs(correlation_matrix) > limiar]
        high_correlations = high_correlations[high_correlations < 1.0].dropna(how='all', axis=1).dropna(how='all', axis=0)

        print("\n🔥 Correlações Significativas (>|{:.2f}|):".format(limiar))
        return high_correlations
    
    def visualizar_heatmap_correlacoes(self, limiar: float = 0.5) -> None:
        """
        Gera um heatmap com as correlações mais relevantes.

        Args:
            limiar (float, opcional): Valor mínimo absoluto para considerar uma correlação significativa.
                O padrão é 0.5.

        Returns:
            None: Apenas exibe o gráfico.

        Example:
            >>> analyzer = MatrizRelacao(df)
            >>> analyzer.visualizar_heatmap_correlacoes()
        """

        high_correlations = self.obter_correlacoes_significativas(limiar)

        if high_correlations.empty:
            print("✅ Nenhuma correlação significativa encontrada para o limiar definido.")
            return

        plt.figure(figsize=(10, 8))
        sns.heatmap(high_correlations, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title(f"Heatmap das Correlações Significativas (> |{limiar}|)")
        plt.show()
    
    def executar_matriz_relacao(self, limiar: float = 0.5) -> None:
        """
        Executa o pipeline completo para análise da matriz de correlação.

        Este método encapsula a execução das seguintes etapas:
        1. Cálculo da matriz de correlação entre variáveis numéricas.
        2. Filtragem das correlações mais significativas com base em um limiar.
        3. Geração e exibição de um heatmap para visualização das relações encontradas.

        Args:
            limiar (float, opcional): Valor mínimo absoluto para considerar uma correlação significativa.
                O padrão é 0.5.

        Returns:
            None: Apenas exibe os resultados das análises.

        Example:
            >>> analyzer = MatrizRelacao(df)
            >>> analyzer.executar_matriz_relacao(limiar=0.6)
        """
        self.calcular_correlacoes()
        self.obter_correlacoes_significativas(limiar)
        self.visualizar_heatmap_correlacoes(limiar)
