import pandas as pd
import plotly.express as px


class TendenciaVariasVariaveis:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será visualizado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        # Verifica se as colunas necessárias existem
        required_columns = {'Year', 'Country'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"❌ O DataFrame deve conter as colunas {required_columns} para a visualização.")

        self.df = df.copy()  # Mantém os dados originais intactos
        self.cols_to_inspect = [
            'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 
            'Life expectancy ', 'Schooling', 'Income composition of resources', 
            'GDP', 'Population'
        ]
    
    def visualizar_tendencias(self) -> None:
        
        # Verifica se todas as colunas necessárias existem no DataFrame
        missing_cols = [col for col in self.cols_to_inspect if col not in self.df.columns]
        if missing_cols:
            raise KeyError(f"❌ As seguintes colunas estão ausentes no DataFrame: {missing_cols}")

        # Geração dos gráficos
        for col in self.cols_to_inspect:
            df_ordenado = self.df.sort_values(by='Year')

            fig = px.line(df_ordenado, 
                          x='Year', 
                          y=col, 
                          color='Country', 
                          title=f'Trend of {col} Over the Years')

            fig.show()