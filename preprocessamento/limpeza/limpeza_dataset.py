import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class PreenchendoKNN:
    """
    Classe para imputação de valores ausentes usando K-Nearest Neighbors (KNN).

    Este método preenche os valores ausentes com base nos k vizinhos mais próximos, 
    garantindo que as substituições sejam feitas com base em padrões de dados reais, 
    evitando viés estatístico e perda de informações.

    Funcionalidades:
    - Aplicar KNN Imputer para preencher valores ausentes em colunas numéricas.
    - Manter a estrutura original do DataFrame.
    - Evitar a imputação de colunas categóricas.

    Attributes:
        df (pd.DataFrame): O DataFrame original contendo valores ausentes.
        n_neighbors (int): Número de vizinhos considerados no algoritmo KNN.
    """

    def __init__(self, df: pd.DataFrame, n_neighbors: int = 20):
        """
        Inicializa a classe com um DataFrame e configura o KNN Imputer.

        Args:
            df (pd.DataFrame): O DataFrame que será processado.
            n_neighbors (int, opcional): Número de vizinhos considerados para imputação.
                O padrão é 20.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")
        if not isinstance(n_neighbors, int) or n_neighbors <= 0:
            raise ValueError("❌ O número de vizinhos deve ser um inteiro positivo.")

        self.df = df.copy()  # Mantém os dados originais intactos
        self.n_neighbors = n_neighbors
        self.imputer = KNNImputer(n_neighbors=self.n_neighbors)
    
    def imputar_valores(self) -> pd.DataFrame:
        """
        Aplica o KNN Imputer para preencher valores ausentes nas colunas numéricas.

        Retorna um novo DataFrame onde os valores ausentes foram imputados.

        Returns:
            pd.DataFrame: DataFrame com valores ausentes preenchidos.

        Raises:
            ValueError: Se não houver colunas numéricas para imputação.

        Example:
            >>> bot = KNNMissingValueImputer(df)
            >>> df_imputado = bot.imputar_valores()
        """

        # Seleciona apenas colunas numéricas
        colunas_numericas = self.df.select_dtypes(exclude='object').columns
        if colunas_numericas.empty:
            raise ValueError("❌ O DataFrame não possui colunas numéricas para imputação.")

        df_imputado = self.df.copy()
        df_imputado.loc[:, colunas_numericas] = self.imputer.fit_transform(self.df[colunas_numericas])

        print(f"✅ Imputação KNN aplicada com sucesso utilizando {self.n_neighbors} vizinhos.")
        return df_imputado
    
    def executar_limpeza_dados(self) -> pd.DataFrame:
        """
        Executa o pipeline de imputação de valores ausentes no dataset.

        Este método encapsula a execução do processo de preenchimento de valores ausentes
        utilizando o algoritmo K-Nearest Neighbors (KNN), garantindo que os dados sejam tratados
        de forma consistente e preservando a estrutura original do DataFrame.

        Returns:
            pd.DataFrame: DataFrame processado com valores ausentes preenchidos.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.
            ValueError: Se não houver colunas numéricas para imputação.

        Example:
            >>> bot = KNNMissingValueImputer(df)
            >>> df_limpo = bot.executar_limpeza_dados()
        """
        return self.imputar_valores()
