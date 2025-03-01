import pandas as pd
import plotly.express as px

class VisualizacaoScaterPlot:
    """
    Classe para visualização da relação entre Índice de Massa Corporal (BMI) e Expectativa de Vida.

    Esta classe gera um gráfico de dispersão interativo usando Plotly, permitindo analisar 
    a correlação entre BMI e Expectativa de Vida em países desenvolvidos e em desenvolvimento.

    Funcionalidades:
    - Criar um gráfico de dispersão para visualizar a correlação entre BMI e Expectativa de Vida.
    - Diferenciar os países pelo status socioeconômico.
    - Permitir análise visual detalhada da distribuição dos dados.

    Attributes:
        df (pd.DataFrame): O DataFrame contendo os dados a serem analisados.
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
        required_columns = {' BMI ', 'Life expectancy ', 'Status'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"❌ O DataFrame deve conter as colunas {required_columns} para a visualização.")

        self.df = df.copy()  # Mantém os dados originais intactos
    
    def visualizar_correlacao_bmi_vida(self) -> None:
        """
        Gera um gráfico de dispersão mostrando a correlação entre BMI e Expectativa de Vida.

        Returns:
            None: Apenas exibe o gráfico interativo.

        Example:
            >>> visualizer = VisualizacaoScaterPlot(df)
            >>> visualizer.visualizar_correlacao_bmi_vida()
        """
        # Criando o gráfico de dispersão
        fig = px.scatter(self.df, 
                         x=' BMI ', 
                         y='Expectativa de vida', 
                         color='Status', 
                         title='Expectativa de vida vs BMI')

        # Personalizando o layout
        fig.update_layout(
            xaxis_title='BMI', 
            yaxis_title='Expectativa de vida'
        )

        # Exibe o gráfico interativo
        fig.show()
    
    def executar_visualizar_correlacao_bmi_vida(self) -> None:
        """
        Executa a visualização interativa da correlação entre Índice de Massa Corporal (BMI) e Expectativa de Vida.

        Este método encapsula a chamada do método `visualizar_correlacao_bmi_vida()`, garantindo 
        uma interface mais intuitiva para exibição do gráfico de dispersão.

        Returns:
            None: Apenas exibe o gráfico interativo na interface do Plotly.

        Example:
            >>> visualizer = VisualizacaoScaterPlot(df)
            >>> visualizer.executar_visualizar_correlacao_bmi_vida()
        """
        self.visualizar_correlacao_bmi_vida()
