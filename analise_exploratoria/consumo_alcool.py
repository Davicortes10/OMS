import pandas as pd
import plotly.express as px

class ConsumoAlcool:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será visualizado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        # Verifica se as colunas necessárias existem
        required_columns = {'Alcohol', 'Status'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"❌ O DataFrame deve conter as colunas {required_columns} para a visualização.")

        self.df = df.copy()  # Mantém os dados originais intactos

    def visualizar_distribuicao_alcool(self, nbins: int = 30) -> None:
        # Criação do histograma empilhado
        fig = px.histogram(self.df, 
                           x='Alcohol', 
                           color='Status', 
                           barmode='stack', 
                           nbins=nbins)

        # Personalização do layout
        fig.update_layout(
            xaxis_title='Alcohol', 
            yaxis_title='Count', 
            title='Stacked Histogram of Alcohol by Status'
        )

        # Exibe o gráfico interativo
        fig.show()

    def executar_visualizacao_consumo_alcool(self) -> None:
        """
        Executa a visualização interativa da distribuição do consumo de álcool por status socioeconômico.

        Este método encapsula a chamada do método `visualizar_distribuicao_alcool()`, garantindo 
        uma interface mais intuitiva para exibição do histograma empilhado.

        Returns:
            None: Apenas exibe o gráfico interativo na interface do Plotly.

        Example:
            >>> visualizer = ConsumoAlcool(df)
            >>> visualizer.executar_visualizacao_consumo_alcool()
        """
        self.visualizar_distribuicao_alcool()
