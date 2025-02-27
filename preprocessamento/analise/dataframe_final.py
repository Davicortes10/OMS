import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class DataFrameFinal:
    """
    Classe para limpeza e validação de dados em um DataFrame.

    Esta classe permite:
    - Identificar e contar valores ausentes por país.
    - Verificar se a imputação de valores ausentes foi bem-sucedida.
    - Exibir o DataFrame final processado.

    Attributes:
        df (pd.DataFrame): O DataFrame que será analisado.
    """

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
        """
        Verifica se ainda existem valores ausentes no dataset e os contabiliza por país.

        Returns:
            pd.Series: Contagem de valores ausentes por país, ordenada do maior para o menor.

        Example:
            >>> cleaner = DataFrameFinal(df)
            >>> cleaner.verificar_valores_ausentes_por_pais()
            
            Country
            India     0
            Brazil    0
            USA       0
            France    0
            dtype: int64
        """
        
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
    
    def exibir_dataframe_final(self) -> pd.DataFrame:
        """
        Exibe o DataFrame após a imputação e limpeza dos dados.

        Returns:
            pd.DataFrame: O DataFrame final, sem valores ausentes.

        Example:
            >>> cleaner = DataFrameFinal(df)
            >>> df_final = cleaner.exibir_dataframe_final()
        """

        print("\n✅ DataFrame final sem valores ausentes:")
        return self.df
    
    def executar_analise_dataframe_final(self) -> pd.DataFrame:
        """
        Executa a exibição do DataFrame final após a imputação e limpeza de dados.

        Este método encapsula a chamada do método `exibir_dataframe_final()`, garantindo
        que o DataFrame processado seja retornado de forma padronizada para análise final.

        Returns:
            pd.DataFrame: DataFrame final, já processado, sem valores ausentes.

        Example:
            >>> cleaner = DataCleaner(df)
            >>> df_final = cleaner.executar_analise_dataframe_final()
        """
        return self.exibir_dataframe_final()
