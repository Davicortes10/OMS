import pandas as pd
import numpy as np
from scipy import stats

class Outlier:
    """
    Classe para detecção e tratamento de outliers em um DataFrame do Pandas.

    Esta classe identifica outliers usando o Z-Score (>3 desvios padrão) e os substitui por NaN,
    aplicando interpolação linear para preencher os valores ausentes.

    Funcionalidades:
    - Identificar outliers em colunas numéricas com base no Z-Score.
    - Substituir outliers por NaN para evitar distorções na análise.
    - Aplicar interpolação linear para suavizar os dados.

    Attributes:
        df (pd.DataFrame): O DataFrame original a ser processado.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será analisado e processado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()  # Faz uma cópia do DataFrame original para evitar alterações diretas
    
    def tratar_outliers(self) -> pd.DataFrame:
        """
        Remove outliers e interpola valores ausentes em colunas numéricas.

        Para cada país no dataset:
        - Calcula o Z-Score para identificar outliers (>3 desvios padrão).
        - Substitui os outliers por NaN.
        - Aplica interpolação linear para preencher os valores ausentes.

        Returns:
            pd.DataFrame: DataFrame processado com outliers removidos e interpolação aplicada.

        Raises:
            KeyError: Se a coluna 'Country' não estiver presente no DataFrame.
            ValueError: Se não houver colunas numéricas para processar.

        Example:
            >>> bot = Outlier(df)
            >>> df_limpo = bot.tratar_outliers()
        """

        # Verifica se a coluna 'Country' existe no DataFrame
        if 'Country' not in self.df.columns:
            raise KeyError("❌ O DataFrame deve conter a coluna 'Country' para segmentação dos dados.")

        # Obtém colunas numéricas
        colunas_numericas = self.df.select_dtypes(include=['float', 'int']).columns
        if colunas_numericas.empty:
            raise ValueError("❌ O DataFrame não possui colunas numéricas para análise.")

        df_filtrado = self.df.copy()

        # Itera sobre cada país único no DataFrame
        for country in df_filtrado['Country'].unique():
            for col in colunas_numericas:
                # Calcula Z-Score para identificar outliers
                z_scores = stats.zscore(df_filtrado[df_filtrado['Country'] == country][col])
                outliers = np.abs(z_scores) > 3

                # Substitui os outliers por NaN
                df_filtrado.loc[(df_filtrado['Country'] == country) & outliers, col] = np.nan

                # Aplica interpolação linear para preencher os valores NaN
                df_filtrado.loc[df_filtrado['Country'] == country, col] = \
                    df_filtrado.loc[df_filtrado['Country'] == country, col].interpolate(method='linear')

        print("✅ Outliers removidos e interpolação aplicada com sucesso.")
        return df_filtrado
    
    def executar_outliers(self) -> pd.DataFrame:
        """
        Executa o pipeline de detecção e tratamento de outliers no dataset.

        Este método encapsula a execução da detecção e tratamento de outliers, utilizando
        o método `tratar_outliers()` para remover valores extremos e aplicar interpolação linear.
        
        Returns:
            pd.DataFrame: DataFrame processado com outliers removidos e interpolação aplicada.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.
            KeyError: Se a coluna 'Country' não estiver presente no DataFrame.
            ValueError: Se não houver colunas numéricas para processar.

        Example:
            >>> bot = Outlier(df)
            >>> df_limpo = bot.executar_outliers()
        """
        return self.tratar_outliers()
