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
    
    def executar_analise_duplicatas(self) -> None:
        """
        Executa um pipeline de análise para identificar registros duplicados e contar valores únicos.

        Este método encapsula a execução sequencial das seguintes operações:
        
        1. Verifica a quantidade de registros duplicados considerando as colunas 'Country' e 'Year'.
        2. Conta a quantidade de valores únicos nas colunas categóricas (excluindo colunas numéricas).
        
        Este método facilita a análise de duplicatas e distribuição de valores categóricos sem a 
        necessidade de chamar cada método individualmente.

        Returns:
            None: O método apenas imprime os resultados no console.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.
            ValueError: Se as colunas `['Country', 'Year']` não existirem no DataFrame.

        Example:
            >>> bot = Duplicatas(df)
            >>> bot.executar_analise_duplicatas()
            
            🔍 Total de registros duplicados considerando ['Country', 'Year']: 10

            📊 Contagem de valores únicos por coluna categórica:
            Country     50
            Continent    6
            Category    12
            dtype: int64
        """
        # Verifica se o DataFrame foi carregado corretamente antes de executar os métodos
        if not hasattr(self, 'df') or self.df is None:
            raise AttributeError("❌ O DataFrame não foi carregado. Certifique-se de que o arquivo CSV foi lido corretamente.")

        self.verificar_duplicatas(['Country', 'Year'])
        self.contar_valores_unicos()


    
