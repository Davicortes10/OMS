import pandas as pd

class RemovendoColunas:
    """
    Classe para pré-processamento de dados, removendo colunas redundantes ou altamente correlacionadas.

    Esta classe permite:
    - Identificar e remover colunas desnecessárias do DataFrame.
    - Armazenar o DataFrame processado para futuras análises.
    
    Attributes:
        df (pd.DataFrame): O DataFrame original contendo os dados antes da remoção de colunas.
        cols_to_remove (list): Lista de colunas que serão removidas.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será processado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()  # Mantém os dados originais intactos
        self.cols_to_remove = [' thinness 5-9 years', 'percentage expenditure', 
                               'under-five deaths ', 'Diphtheria ', 
                               'Income composition of resources']
    
    def remover_colunas(self) -> pd.DataFrame:
        """
        Remove colunas redundantes ou altamente correlacionadas do DataFrame.

        Returns:
            pd.DataFrame: O DataFrame atualizado sem as colunas especificadas.

        Raises:
            KeyError: Se alguma das colunas a serem removidas não estiver presente no DataFrame.

        Example:
            >>> preprocessor = RemovendoColunas(df)
            >>> df_limpo = preprocessor.remover_colunas()
        """
        
        colunas_presentes = [col for col in self.cols_to_remove if col in self.df.columns]
        if not colunas_presentes:
            print("⚠️ Nenhuma das colunas a serem removidas está presente no DataFrame.")
            return self.df
        
        df_processado = self.df.drop(colunas_presentes, axis=1)
        print(f"✅ Removidas as colunas: {colunas_presentes}")
        return df_processado
    
    def executar_remover_colunas(self) -> pd.DataFrame:
        """
        Executa a remoção de colunas redundantes ou altamente correlacionadas.

        Este método encapsula a chamada do método `remover_colunas()`, garantindo 
        uma interface mais intuitiva para a exclusão de variáveis desnecessárias.

        Returns:
            pd.DataFrame: O DataFrame atualizado sem as colunas removidas.

        Example:
            >>> preprocessor = RemovendoColunas(df)
            >>> df_processado = preprocessor.executar_remover_colunas()
        """
        return self.remover_colunas()
