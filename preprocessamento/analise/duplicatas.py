import pandas as pd

class Duplicatas:
    """
    Classe para análise e tratamento de registros duplicados em um DataFrame do Pandas.

    Esta classe permite identificar duplicatas e contar valores únicos em colunas categóricas,
    auxiliando na limpeza e organização de dados.

    Funcionalidades:
        - Verificar a existência de registros duplicados em colunas específicas.
        - Contar valores únicos em colunas categóricas (excluindo colunas numéricas).

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
    
    def verificar_duplicatas(self, subset: list) -> int:
        """
        Verifica a quantidade de registros duplicados em um subconjunto de colunas.

        Este método identifica e conta registros duplicados considerando as colunas
        especificadas no parâmetro `subset`. Ele retorna a contagem total de duplicatas
        e imprime o resultado.

        Args:
            subset (list): Lista de colunas a serem verificadas para duplicação.

        Returns:
            int: Número total de registros duplicados encontrados.

        Raises:
            ValueError: Se `subset` não for uma lista válida de colunas do DataFrame.

        Example:
            >>> bot = Duplicatas(df)
            >>> bot.verificar_duplicatas(['Country', 'Year'])
            🔍 Total de registros duplicados considerando ['Country', 'Year']: 10
            10
        """

        if not isinstance(subset, list) or not all(col in self.df.columns for col in subset):
            raise ValueError("❌ O argumento 'subset' deve ser uma lista contendo colunas válidas do DataFrame.")

        duplicatas = self.df.duplicated(subset=subset).sum()
        print(f"🔍 Total de registros duplicados considerando {subset}: {duplicatas}")
        return duplicatas
    
    def contar_valores_unicos(self) -> pd.Series:
        """
        Conta quantos valores únicos existem nas colunas categóricas do DataFrame.

        Este método exclui colunas numéricas (`float` e `int`) e calcula a quantidade de valores
        únicos em cada coluna categórica, fornecendo uma visão útil para análise de dados.

        Returns:
            pd.Series: Contagem de valores únicos para cada coluna categórica.

        Example:
            >>> bot = Duplicatas(df)
            >>> bot.contar_valores_unicos()
            
            📊 Contagem de valores únicos por coluna categórica:
            Country     50
            Continent    6
            Category    12
            dtype: int64
        """
        
        valores_unicos = self.df.select_dtypes(exclude=['float', 'int']).nunique()
        print("\n📊 Contagem de valores únicos por coluna categórica:")
        print(valores_unicos)
        return valores_unicos

    
