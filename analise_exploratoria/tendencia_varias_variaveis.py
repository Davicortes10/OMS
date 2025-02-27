import pandas as pd
import plotly.express as px


class TendenciaVariasVariaveis:
    """
    Classe para visualização da evolução de indicadores socioeconômicos e de saúde ao longo dos anos.

    Esta classe gera gráficos interativos usando Plotly para analisar tendências em variáveis como 
    mortalidade, consumo de álcool, expectativa de vida, educação e população.

    Funcionalidades:
    - Criar gráficos de linha para visualizar a evolução de múltiplas variáveis.
    - Ordenar os dados corretamente para exibição precisa.
    - Diferenciar os países por cores para facilitar a análise.

    Attributes:
        df (pd.DataFrame): O DataFrame contendo os dados a serem analisados.
        cols_to_inspect (list): Lista de colunas que serão visualizadas.
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
        """
        Gera gráficos de linha interativos para cada variável socioeconômica definida.

        O gráfico exibe a variável socioeconômica no eixo Y, o ano no eixo X e diferencia os países por cores.

        Returns:
            None: Apenas exibe os gráficos interativos.

        Raises:
            KeyError: Se alguma das colunas especificadas para análise não estiver presente no DataFrame.

        Example:
            >>> visualizer = TendenciaVariasVariaveis(df)
            >>> visualizer.visualizar_tendencias()
        """

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
    
    def executar_visualizacao_varias_variaveis(self) -> None:
        """
        Executa a visualização interativa de múltiplas variáveis socioeconômicas ao longo do tempo.

        Este método encapsula a chamada do método `visualizar_tendencias()`, garantindo 
        uma interface mais intuitiva para exibição dos gráficos interativos.

        Returns:
            None: Apenas exibe os gráficos interativos na interface do Plotly.

        Example:
            >>> visualizer = TendenciaVariasVariaveis(df)
            >>> visualizer.executar_visualizacao_varias_variaveis()
        """
        self.visualizar_tendencias()

        
