import pandas as pd
import plotly.express as px

class VisualizadorExpectativaVida:
    """
    Classe para visualização da tendência da expectativa de vida ao longo dos anos.

    Esta classe gera gráficos interativos usando Plotly para mostrar a evolução da expectativa de vida
    por país ao longo do tempo, facilitando a análise de tendências e padrões.

    Funcionalidades:
    - Criar um gráfico de linha para visualizar a tendência da expectativa de vida.
    - Ordenar os dados corretamente para exibição precisa.
    - Diferenciar os países por cores para facilitar a análise.

    Attributes:
        df (pd.DataFrame): O DataFrame contendo os dados de expectativa de vida.
    """

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

    def visualizar_tendencia_vida(self) -> None:
        """
        Gera um gráfico de linha interativo mostrando a tendência da expectativa de vida ao longo dos anos.

        O gráfico exibe a expectativa de vida no eixo Y, o ano no eixo X e diferencia os países por cores.

        Returns:
            None: Apenas exibe o gráfico interativo.

        Example:
            >>> visualizer = VisualizadorExpectativaVida(df)
            >>> visualizer.visualizar_tendencia_vida()
        """
        # Ordena os dados pelo ano para uma visualização correta
        df_ordenado = self.df.sort_values(by='Year')

        # Criação do gráfico de linha
        fig = px.line(df_ordenado, 
                      x='Year', 
                      y='Life expectancy ', 
                      color='Country', 
                      title='Trend of Life Expectancy Over the Years')

        # Exibe o gráfico interativo
        fig.show()
    
    def executar_visualizacao_tendencia_vida(self) -> None:
        """
        Executa a visualização interativa da tendência da expectativa de vida.

        Este método encapsula a chamada do método `visualizar_tendencia_vida()`, 
        garantindo uma interface mais intuitiva para exibição do gráfico.

        Returns:
            None: Apenas exibe o gráfico interativo na interface do Plotly.

        Example:
            >>> visualizer = LifeExpectancyVisualizer(df)
            >>> visualizer.executar_visualizacao_tendencia_vida()
        """
        self.visualizar_tendencia_vida()
