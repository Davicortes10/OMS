from dataset.leitura_dataset import LeitorDataset
from modelos.modelagaem_expectativa_vida import ExpectativaVidaMLP
from analise_exploratoria.consumo_alcool import ConsumoAlcool
from analise_exploratoria.correlacao_mapa import MatrizRelacao
from analise_exploratoria.expectativa_scaterplot import VisualizacaoScaterPlot
from analise_exploratoria.tendencia_varias_variaveis import TendenciaVariasVariaveis
from analise_exploratoria.visualizacao_expectativa_vida import VisualizadorExpectativaVida
from preprocessamento.analise.dataframe_final import DataFrameFinal
from preprocessamento.analise.duplicatas import Duplicatas
from preprocessamento.analise.valores_ausentes import AnaliseValoresAusentes
from preprocessamento.limpeza.colunas_redundantes import RemovendoColunas
from preprocessamento.limpeza.limpeza_dataset import PreenchendoKNN
from preprocessamento.outliers.outliers import Outlier



class Principal:
    def __init__(self):
        leitor_df = LeitorDataset("OMS/dataset/dataset_LE.csv")
        self.df = leitor_df.executar_leitura()
    
    def duplicatas(self):
        dupli = Duplicatas(self.df)
        dupli.executar_analise_duplicatas()
    
    def valores_nulos(self):
        valor_n = AnaliseValoresAusentes(self.df)
        valor_n.executar_analise_valores_ausentes()

    def outliers(self):
        outli = Outlier(self.df)
        self.df = outli.executar_outliers()
    
    def preencher_valor_ausente(self):
        valor_ause = PreenchendoKNN(self.df)
        self.df = valor_ause.executar_limpeza_dados()
    
    def dataframefinal(self):
        final = DataFrameFinal(self.df)
        self.df = final.executar_analise_dataframe_final()

    def visualizar_expectativa_vida(self):
        visualizar = VisualizadorExpectativaVida(self.df)
        visualizar.executar_visualizacao_tendencia_vida()
    
    def tendencia_variavel(self):
        tendencia = TendenciaVariasVariaveis(self.df)
        tendencia.executar_visualizacao_varias_variaveis()
    
    def consumo_alcool(self):
        alcool = ConsumoAlcool(self.df)
        alcool.executar_visualizacao_consumo_alcool()
    
    def scatter_plot(self):
        scatter = VisualizacaoScaterPlot(self.df)
        scatter.executar_visualizar_correlacao_bmi_vida()
    
    def matriz_relacao(self):
        matriz = MatrizRelacao(self.df)
        matriz.executar_matriz_relacao()
    
    def colunas_redundantes(self):
        colunas = RemovendoColunas(self.df)
        self.df = colunas.executar_remover_colunas()
    
    def rede_neural(self):
        rede = ExpectativaVidaMLP(self.df)
        rede.executar_pipeline()

    def executar_tudo(self):
        """
        Executa todo o pipeline de processamento, análise e modelagem da expectativa de vida,
        permitindo que o usuário pressione ENTER para avançar para cada etapa.

        Este método encapsula todas as etapas do pipeline, incluindo:
        1. Leitura e carregamento do dataset.
        2. Análise de duplicatas e valores ausentes.
        3. Detecção e tratamento de outliers.
        4. Preenchimento de valores ausentes usando KNN.
        5. Análise do DataFrame final após a limpeza.
        6. Visualizações exploratórias da expectativa de vida e outras variáveis.
        7. Análise do consumo de álcool e sua relação com expectativa de vida.
        8. Geração de scatter plots e análise de correlação.
        9. Remoção de colunas redundantes.
        10. Treinamento e avaliação da rede neural.

        Returns:
            None: Apenas exibe os resultados das análises e modelagens.

        Example:
            >>> pipeline = Principal()
            >>> pipeline.executar_tudo()
        """

        def aguardar_usuario():
            input("\n🔹 Pressione ENTER para continuar...")

        print("\n📌 **Iniciando Pipeline Completo...**")
        
        print("\n🔍 1. Analisando duplicatas...")
        self.duplicatas()
        aguardar_usuario()

        print("\n📊 2. Analisando valores nulos...")
        self.valores_nulos()
        aguardar_usuario()

        print("\n🚀 3. Detectando e tratando outliers...")
        self.outliers()
        aguardar_usuario()

        print("\n🛠️ 4. Preenchendo valores ausentes com KNN...")
        self.preencher_valor_ausente()
        aguardar_usuario()

        print("\n✅ 5. Exibindo análise final do DataFrame...")
        self.dataframefinal()
        aguardar_usuario()

        print("\n📈 6. Visualizando tendência da expectativa de vida...")
        self.visualizar_expectativa_vida()
        aguardar_usuario()

        print("\n📊 7. Analisando tendências de múltiplas variáveis...")
        self.tendencia_variavel()
        aguardar_usuario()

        print("\n🥂 8. Visualizando consumo de álcool e impacto na expectativa de vida...")
        self.consumo_alcool()
        aguardar_usuario()

        print("\n📉 9. Gerando Scatter Plot (Correlação BMI vs Expectativa de Vida)...")
        self.scatter_plot()
        aguardar_usuario()

        print("\n📊 10. Criando Matriz de Correlação...")
        self.matriz_relacao()
        aguardar_usuario()

        print("\n🗑️ 11. Removendo colunas redundantes...")
        self.colunas_redundantes()
        aguardar_usuario()

        print("\n🤖 12. Iniciando treinamento da Rede Neural para previsão de Expectativa de Vida...")
        self.rede_neural()
        aguardar_usuario()

        print("\n🎉 **Pipeline Finalizado com Sucesso!** ✅")

