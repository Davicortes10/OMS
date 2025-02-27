import pandas as pd
import plotly.express as px

class VisualizadorExpectativaVida:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será visualizado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        # Verifica se as colunas necessárias existem
        required_columns = {'Year', 'Life expectancy ', 'Country'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"❌ O DataFrame deve conter as colunas {required_columns} para a visualização.")

        self.df = df.copy()  # Mantém os dados originais intactos