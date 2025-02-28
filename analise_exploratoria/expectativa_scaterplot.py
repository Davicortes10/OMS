import pandas as pd
import plotly.express as px

class VisualizacaoScaterPlot:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será visualizado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        # Verifica se as colunas necessárias existem
        required_columns = {' BMI ', 'Life expectancy ', 'Status'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"❌ O DataFrame deve conter as colunas {required_columns} para a visualização.")

        self.df = df.copy()  # Mantém os dados originais intactos
    
    def visualizar_correlacao_bmi_vida(self) -> None:
        # Criando o gráfico de dispersão
        fig = px.scatter(self.df, 
                         x=' BMI ', 
                         y='Life expectancy ', 
                         color='Status', 
                         title='Life Expectancy vs BMI')

        # Personalizando o layout
        fig.update_layout(
            xaxis_title='BMI', 
            yaxis_title='Life Expectancy'
        )

        # Exibe o gráfico interativo
        fig.show()