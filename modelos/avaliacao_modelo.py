import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

class ModelEvaluator:

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
        r2 = r2_score(self.y_test, self.predictions)
        print(f"\n📊 R² Score: {r2:.4f}")
        return r2
    
    def comparar_valores_reais_preditos(self) -> None:
        df = pd.DataFrame({'Actual': self.y_test, 'Predicted': self.predictions})
        df.plot(kind='hist', alpha=0.7, bins=30, figsize=(8, 5))
        plt.title("Comparação de Valores Reais vs. Preditos")
        plt.xlabel("Expectativa de Vida")
        plt.ylabel("Frequência")
        plt.legend(["Valores Reais", "Valores Preditos"])
        plt.grid()
        plt.show()

    def visualizar_historico_perda(self) -> None:
        pd.DataFrame(self.model_history).plot(figsize=(8, 5))
        plt.title("Histórico de Treinamento - Função de Perda")
        plt.xlabel("Épocas")
        plt.ylabel("Perda")
        plt.grid()
        plt.show()