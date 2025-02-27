import pandas as pd

class AnaliseValoresAusentes:
    """
    Classe para análise de valores ausentes em um DataFrame do Pandas.

    Funcionalidades:
    - Contar a quantidade de valores ausentes por coluna.
    - Identificar quais países possuem valores ausentes.
    - Contar a quantidade total de valores ausentes por país e ordená-los.

    Attributes:
        df (pd.DataFrame): O DataFrame que será analisado.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): DataFrame que será analisado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df
    
    def contar_valores_ausentes(self) -> pd.Series:
        """
        Conta a quantidade de valores ausentes (NaN) em cada coluna.

        Returns:
            pd.Series: Contagem de valores ausentes para cada coluna.

        Example:
            >>> bot = AnaliseValoresAusentes(df)
            >>> bot.contar_valores_ausentes()
            Country       0
            Year          0
            Population   12
            GDP           8
            dtype: int64
        """

        valores_ausentes = self.df.isnull().sum()
        print("\n📉 Contagem de valores ausentes por coluna:")
        print(valores_ausentes)
        return valores_ausentes
    
    def paises_com_valores_ausentes(self) -> list:
        """
        Identifica os países que possuem pelo menos um valor ausente.

        Returns:
            list: Lista de países com valores ausentes.

        Example:
            >>> bot = AnaliseValoresAusentes(df)
            >>> bot.paises_com_valores_ausentes()
            ['Brazil', 'India', 'USA']
        """

        paises_faltantes = self.df[self.df.isnull().any(axis=1)]['Country'].unique().tolist()
        print("\n🌍 Países com valores ausentes:", paises_faltantes)
        return paises_faltantes
    
    def valores_ausentes_por_pais(self) -> pd.Series:
        """
        Conta a quantidade total de valores ausentes por país e os ordena em ordem decrescente.

        Returns:
            pd.Series: Contagem total de valores ausentes por país, ordenados do maior para o menor.

        Example:
            >>> bot = AnaliseValoresAusentes(df)
            >>> bot.valores_ausentes_por_pais()
            India     10
            Brazil     8
            USA        6
            France     4
            dtype: int64
        """
        
        valores_por_pais = self.df.isnull().groupby(self.df['Country']).sum().sum(axis=1).sort_values(ascending=False)
        print("\n📊 Valores ausentes por país (ordenados):")
        print(valores_por_pais)
        return valores_por_pais