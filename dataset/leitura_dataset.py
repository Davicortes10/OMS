import pandas as pd

class LeitorDataset:
    """
    Classe para leitura e análise exploratória de datasets CSV.

    Esta classe permite a leitura de um arquivo CSV e fornece métodos para análise
    inicial dos dados, incluindo:
    
    - Exibição de informações estruturais do dataset (número de linhas, colunas e tipos de dados).
    - Geração de estatísticas descritivas das colunas numéricas.
    - Identificação de valores ausentes.
    - Visualização das primeiras linhas do dataset para uma inspeção rápida.

    Attributes:
        caminho (str): Caminho do arquivo CSV.
        df (pd.DataFrame): DataFrame Pandas contendo os dados carregados.

    Methods:
        __init__(caminho): Inicializa a classe e carrega o arquivo CSV.
        informacoes(): Exibe detalhes sobre o número de linhas, colunas e tipos de dados do dataset.
        estatisticas(): Retorna estatísticas descritivas das colunas numéricas.
        registros_faltantes(): Identifica valores ausentes no dataset.
        primeiras_linhas(linhas=5): Exibe as primeiras linhas do dataset para uma visualização inicial.
    """

    def __init__(self, caminho: str) -> None:
        """
        Inicializa a classe e carrega um arquivo CSV em um DataFrame do Pandas.

        Este método tenta carregar o arquivo CSV fornecido no parâmetro `file_path`
        e armazená-lo em um DataFrame (`self.df`). Se a leitura for bem-sucedida, uma
        mensagem de confirmação é exibida. Caso ocorra um erro, a exceção é capturada
        e uma mensagem de erro é exibida.

        Args:
            caminho (str): Caminho do arquivo CSV que será carregado.

        Returns:
            None: O método apenas inicializa a instância da classe.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
            pd.errors.EmptyDataError: Se o arquivo CSV estiver vazio.
            pd.errors.ParserError: Se houver erro ao interpretar o arquivo CSV.
            Exception: Para qualquer outro erro inesperado.

        Example:
            >>> leitor = LeitorDataset("dados.csv")
            ✅ Arquivo 'dados.csv' carregado com sucesso!

        Se o arquivo não for encontrado:

            >>> leitor = CSVReader("arquivo_inexistente.csv")
            ❌ Erro ao carregar o arquivo: [Errno 2] No such file or directory: 'arquivo_inexistente.csv'
        """
        self.caminho = caminho
        try:
            self.df = pd.read_csv(caminho)
            print(f"✅ Arquivo '{caminho}' carregado com sucesso!")
        except FileNotFoundError:
            print(f"❌ Erro: O arquivo '{caminho}' não foi encontrado.")
        except pd.errors.EmptyDataError:
            print(f"❌ Erro: O arquivo '{caminho}' está vazio.")
        except pd.errors.ParserError:
            print(f"❌ Erro: O arquivo '{caminho}' não pôde ser interpretado corretamente.")
        except Exception as e:
            print(f"❌ Erro ao carregar o arquivo: {e}")

    def informacoes(self) -> None:
        """
        Exibe informações gerais sobre o dataset, incluindo número de linhas, colunas e tipos de dados.

        Este método imprime detalhes estruturais do DataFrame, como:
        - O número total de entradas (linhas).
        - O número de colunas e seus respectivos tipos de dados.
        - A contagem de valores não nulos em cada coluna.
        - O uso de memória do dataset.

        Returns:
            None: A função apenas imprime as informações, sem retornar valores.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.

        Example:
            >>> leitor = LeitorDataset("dados.csv")
            >>> leitor.informacoes()

            📌 Informações do Dataset:
            <class 'pandas.core.frame.DataFrame'>
            RangeIndex: 1000 entries, 0 to 999
            Data columns (total 5 columns):
            #   Column   Non-Null Count  Dtype  
            ---  ------   --------------  -----  
            0   Nome     1000 non-null   object 
            1   Idade    980 non-null    float64
            2   Cidade   1000 non-null   object 
            3   Renda    950 non-null    float64
            4   Status   1000 non-null   object 
            dtypes: float64(2), object(3)
            memory usage: 39.2+ KB
        """
        # Verifica se o DataFrame foi carregado corretamente
        if not hasattr(self, 'df') or self.df is None:
            raise AttributeError("❌ O DataFrame não foi carregado. Certifique-se de que o arquivo CSV foi lido corretamente.")

        print("\n📌 Informações do Dataset:")
        print(self.df.info())

    def estatisticas(self) -> None:
        """
        Exibe estatísticas descritivas das colunas numéricas do dataset.

        Este método gera uma análise estatística detalhada das colunas numéricas do DataFrame.
        Ele fornece métricas como média, desvio padrão, mínimo, máximo e quartis (25%, 50%, 75%).
        
        Se o dataset não contiver colunas numéricas, uma mensagem apropriada será exibida.

        Returns:
            None: A função imprime as estatísticas, mas não retorna um valor.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.

        Example:
            >>> leitor = LeitorDataset("dados.csv")
            >>> leitor.estatisticas()

            📊 Estatísticas Descritivas:
                    Idade       Salario
            count   1000.000000  950.000000
            mean      35.467000  3200.800000
            std        8.900000   980.500000
            min       18.000000   800.000000
            25%       28.000000  2500.000000
            50%       35.000000  3200.000000
            75%       42.000000  4000.000000
            max       65.000000  9200.000000

        Se o dataset não tiver colunas numéricas:

            📊 Estatísticas Descritivas:
            ❌ Nenhuma coluna numérica encontrada no dataset.
        """
        # Verifica se o DataFrame foi carregado corretamente
        if not hasattr(self, 'df') or self.df is None:
            raise AttributeError("❌ O DataFrame não foi carregado. Certifique-se de que o arquivo CSV foi lido corretamente.")

        print("\n📊 Estatísticas Descritivas:")

        # Filtra apenas colunas numéricas
        df_numerico = self.df.select_dtypes(include=['number'])

        if df_numerico.empty:
            print("❌ Nenhuma coluna numérica encontrada no dataset.")
        else:
            print(df_numerico.describe())

    def registros_faltantes(self) -> None:
        """
        Identifica e exibe a contagem de valores ausentes em cada coluna do dataset.

        Este método analisa o DataFrame carregado e exibe a quantidade de valores ausentes
        (NaN) para cada coluna. Se todas as colunas estiverem completas, uma mensagem
        indicando que não há valores ausentes será exibida.

        Returns:
            None: A função apenas imprime a contagem de valores ausentes, sem retornar dados.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.

        Example:
            >>> leitor = LeitorDataset("dados.csv")
            >>> leitor.registros_faltantes()
            
            🔍 Valores Ausentes:
            Idade      3
            Salario   10
            Estado     1
            dtype: int64

        Se não houver valores ausentes:

            🔍 Valores Ausentes:
            ✅ Nenhum valor ausente encontrado!
        """
        # Verifica se o DataFrame foi carregado corretamente
        if not hasattr(self, 'df') or self.df is None:
            raise AttributeError("❌ O DataFrame não foi carregado. Certifique-se de que o arquivo CSV foi lido corretamente.")

        print("\n🔍 Valores Ausentes:")
        missing = self.df.isnull().sum()

        # Exibe apenas colunas que possuem valores ausentes
        if missing.any():
            print(missing[missing > 0])
        else:
            print("✅ Nenhum valor ausente encontrado!")

    def primeiras_linhas(self, linhas: int = 5) -> None:
        """
        Exibe as primeiras linhas do dataset para uma análise inicial.

        Este método imprime as primeiras linhas do DataFrame carregado, permitindo que o usuário
        tenha uma visão preliminar da estrutura dos dados, incluindo os valores e possíveis padrões.

        Args:
            linhas (int, opcional): Número de linhas a serem exibidas. 
                O valor padrão é 5.

        Returns:
            None: A função imprime as primeiras linhas do dataset, mas não retorna nenhum valor.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.
            ValueError: Se o número de linhas solicitado for menor que 1.

        Example:
            >>> leitor = LeitorDataset("dados.csv")
            >>> leitor.primeiras_linhas(3)
            Visualização das 3 primeiras linhas do dataset:
            Nome  Idade    Cidade  Salario
            0  João     28       SP   4000.0
            1  Maria    34       RJ   3500.0
            2  Pedro    45       MG   5000.0
        """
        # Verifica se o DataFrame foi carregado corretamente
        if not hasattr(self, 'df') or self.df is None:
            raise AttributeError("❌ O DataFrame não foi carregado. Certifique-se de que o arquivo CSV foi lido corretamente.")

        # Valida se o número de linhas solicitado é positivo
        if linhas < 1:
            raise ValueError("❌ O número de linhas deve ser pelo menos 1.")

        print(f"\n Visualização das {linhas} primeiras linhas do dataset:")
        print(self.df.head(linhas))

    def executar_leitura(self) -> None:
        """
        Executa um pipeline de leitura e análise do dataset.

        Este método encapsula a execução sequencial de outras funções da classe,
        proporcionando uma visão geral do dataset sem a necessidade de chamar
        cada método individualmente. Ele realiza as seguintes operações:

        1. Exibe informações gerais do dataset (`informacoes()`).
        2. Mostra estatísticas descritivas das colunas numéricas (`estatisticas()`).
        3. Identifica e exibe valores ausentes (`registros_faltantes()`).
        4. Apresenta uma amostra inicial do dataset (`primeiras_linhas()`).

        Returns:
            None: O método apenas exibe as informações no console.

        Raises:
            AttributeError: Se o DataFrame (`self.df`) não estiver carregado corretamente.

        Example:
            >>> leitor = LeitorDataset("dados.csv")
            >>> leitor.executar_leitura()

            📌 Informações do Dataset:
            <class 'pandas.core.frame.DataFrame'>
            RangeIndex: 1000 entries, 0 to 999
            Data columns (total 5 columns):
            ...

            📊 Estatísticas Descritivas:
                    Idade       Salario
            count   1000.000000  950.000000
            mean      35.467000  3200.800000
            ...

            🔍 Valores Ausentes:
            Idade      3
            Salario   10

            👀 Visualização das 5 primeiras linhas do dataset:
            Nome  Idade    Cidade  Salario
            0  João     28       SP   4000.0
            1  Maria    34       RJ   3500.0
        """
        # Verifica se o DataFrame foi carregado corretamente antes de executar os métodos
        if not hasattr(self, 'df') or self.df is None:
            raise AttributeError("❌ O DataFrame não foi carregado. Certifique-se de que o arquivo CSV foi lido corretamente.")

        self.informacoes()
        self.estatisticas()
        self.registros_faltantes()
        self.primeiras_linhas()




