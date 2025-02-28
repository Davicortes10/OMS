import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

class ModelEvaluator:
    """
    Classe para avaliação do desempenho de modelos de aprendizado de máquina.

    Esta classe executa:
    - Cálculo do R² Score para medir a qualidade do modelo.
    - Comparação visual entre valores reais e previstos.
    - Análise da perda ao longo do treinamento.
    - Avaliação dos erros residuais (loss).

    Attributes:
        y_test (pd.Series ou np.array): Valores reais do conjunto de teste.
        predictions (np.array): Valores previstos pelo modelo.
        model_history (dict): Histórico de treinamento do modelo.
    """

    def __init__(self, y_test, predictions, model_history):
        """
        Inicializa a classe com os valores reais, previsões e histórico do modelo.

        Args:
            y_test (pd.Series ou np.array): Valores reais do conjunto de teste.
            predictions (np.array): Valores previstos pelo modelo.
            model_history (dict): Histórico do treinamento do modelo.
        """
        self.y_test = np.array(y_test)  # Converte para numpy para evitar erros
        self.predictions = predictions.flatten()
        self.model_history = model_history
    
    def calcular_r2_score(self) -> float:
        """
        Calcula o coeficiente de determinação (R² Score) para avaliar a qualidade do modelo.

        Returns:
            float: Valor do R² Score.

        Example:
            >>> evaluator = ModelEvaluator(y_test, predictions, model.history.history)
            >>> r2 = evaluator.calcular_r2_score()
            >>> print(f"R² Score: {r2:.4f}")
        """

        r2 = r2_score(self.y_test, self.predictions)
        print(f"\n📊 R² Score: {r2:.4f}")
        return r2
    
    def comparar_valores_reais_preditos(self) -> None:
        """
        Gera um histograma comparando os valores reais e previstos.

        Returns:
            None: Apenas exibe o gráfico.

        Example:
            >>> evaluator = ModelEvaluator(y_test, predictions, model.history.history)
            >>> evaluator.comparar_valores_reais_preditos()
        """

        df = pd.DataFrame({'Actual': self.y_test, 'Predicted': self.predictions})
        df.plot(kind='hist', alpha=0.7, bins=30, figsize=(8, 5))
        plt.title("Comparação de Valores Reais vs. Preditos")
        plt.xlabel("Expectativa de Vida")
        plt.ylabel("Frequência")
        plt.legend(["Valores Reais", "Valores Preditos"])
        plt.grid()
        plt.show()
    
    def analisar_erros_residuais(self) -> None:    
        """
        Plota a distribuição dos erros residuais (diferença entre valores reais e previstos).

        Returns:
            None: Apenas exibe o gráfico.

        Example:
            >>> evaluator = ModelEvaluator(y_test, predictions, model.history.history)
            >>> evaluator.analisar_erros_residuais()
        """

        df_loss = pd.DataFrame({'loss': self.y_test - self.predictions}).reset_index(drop=True)
        df_loss.plot(figsize=(8, 5))
        plt.title("Distribuição dos Erros Residuais")
        plt.xlabel("Amostras")
        plt.ylabel("Erro (Diferença Real - Predito)")
        plt.axhline(y=0, color='r', linestyle='--')
        plt.grid()
        plt.show()
    
    def executar_avaliacao_completa(self) -> None:
        """
        Executa todas as análises do modelo de forma sequencial.

        Este método encapsula todas as etapas do processo de avaliação, incluindo:
        1. Cálculo do R² Score para medir a qualidade do modelo.
        2. Comparação visual entre valores reais e previstos.
        3. Análise do histórico da função de perda ao longo do treinamento.
        4. Visualização da distribuição dos erros residuais.

        Returns:
            None: Apenas exibe os resultados das avaliações.

        Example:
            >>> evaluator = ModelEvaluator(y_test, predictions, model.history.history)
            >>> evaluator.executar_avaliacao_completa()
        """
        print("\n📌 **Iniciando Avaliação Completa do Modelo...**")

        print("\n🔍 1. Calculando o R² Score...")
        self.calcular_r2_score()

        print("\n📊 2. Comparando valores reais vs. previstos...")
        self.comparar_valores_reais_preditos()

        print("\n📉 3. Avaliando a distribuição dos erros residuais...")
        self.analisar_erros_residuais()

        print("\n✅ **Avaliação Finalizada com Sucesso!** 🎯")