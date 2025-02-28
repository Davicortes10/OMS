import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import ace_tools as tools

class LifeExpectancyNN:
    """
    Classe para modelagem de Expectativa de Vida usando Redes Neurais Artificiais (RNA).

    Esta classe realiza:
    - Pré-processamento dos dados (normalização e encoding).
    - Construção de um modelo de rede neural `Sequential` com camadas densas.
    - Treinamento, avaliação e predição do modelo.

    Attributes:
        df (pd.DataFrame): O DataFrame contendo os dados para modelagem.
        model (Sequential): O modelo de Rede Neural criado.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe, realizando a preparação dos dados.

        Args:
            df (pd.DataFrame): O DataFrame com os dados originais.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()
        self.label_cols = ['Country', 'Status']
        self.scale_cols = [col for col in df.columns if col not in self.label_cols + ['Life expectancy ']]
        
        self.pre_processed_csv = self.preprocess_data(df)
        self.X = self.pre_processed_csv.drop('Life expectancy ', axis=1)
        self.y = self.pre_processed_csv['Life expectancy ']

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=123
        )

        self.model = self.build_model(input_shape=(self.X_train.shape[1],))
    
    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normaliza os dados numéricos e aplica Label Encoding às variáveis categóricas.

        Returns:
            pd.DataFrame: DataFrame pré-processado.
        """

        le = LabelEncoder()
        mm = MinMaxScaler()

        df[self.scale_cols] = mm.fit_transform(df[self.scale_cols])
        df[self.label_cols] = df[self.label_cols].apply(le.fit_transform)

        return df
    
    def build_model(self, input_shape: tuple) -> Sequential:
        """
        Constrói um modelo de Rede Neural `Sequential`.

        Args:
            input_shape (tuple): Shape da entrada do modelo.

        Returns:
            Sequential: Modelo de Rede Neural criado.
        """

        model = Sequential([
            Dense(128, activation='relu', input_shape=input_shape),
            Dense(64, activation='relu'),
            Dense(1, activation='linear')
        ])
        return model
    
    def compile_model(self, optimizer='adam', loss='Huber', metrics=['mae']):
        """
        Compila o modelo com otimizador e função de perda definidos.

        Args:
            optimizer (str): Algoritmo de otimização (padrão: Adam).
            loss (str): Função de perda (padrão: Huber).
            metrics (list): Lista de métricas (padrão: MAE).
        """

        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def train_model(self, epochs=1000, batch_size=32, validation_split=0.2):
        """
        Treina o modelo com os dados de treinamento.

        Args:
            epochs (int): Número de épocas.
            batch_size (int): Tamanho do batch.
            validation_split (float): Percentual dos dados usados para validação.
        """
        
        self.model.fit(self.X_train, self.y_train, epochs=epochs, batch_size=batch_size, validation_split=validation_split)
    
    def evaluate_model(self):
        """
        Avalia o desempenho do modelo treinado e exibe as métricas de desempenho em formato de tabela.

        A avaliação inclui:
        - Acurácia do modelo.
        - Relatório de classificação detalhado.
        - Matriz de confusão.

        Returns:
            None: Apenas exibe os resultados formatados.

        Example:
            >>> model = LifeExpectancyNN(df)
            >>> model.evaluate_model()
        """
        # Fazer previsões
        y_pred = self.model.predict(self.X_test).flatten()

        # Calcular métricas
        erro_absoluto = np.abs(self.y_test - y_pred)
        erro_relativo = np.abs(erro_absoluto / self.y_test)

        # Criar DataFrame de métricas
        metrics_data = {
            "Métrica": ["Erro Absoluto Médio (MAE)", "Erro Relativo Médio (MAPE)"],
            "Valor": [np.mean(erro_absoluto), np.mean(erro_relativo) * 100]  # MAPE em porcentagem
        }
        df_metrics = pd.DataFrame(metrics_data)

        # Matriz de confusão (convertida para DataFrame)
        y_pred_classes = np.round(y_pred)  # Como é um problema de regressão, arredondamos
        conf_matrix = confusion_matrix(self.y_test, y_pred_classes)
        df_conf_matrix = pd.DataFrame(conf_matrix, index=["Expectativa Baixa", "Expectativa Alta"], columns=["Previsto Baixo", "Previsto Alto"])

        # Exibir tabelas formatadas
        tools.display_dataframe_to_user(name="Métricas do Modelo", dataframe=df_metrics)
        tools.display_dataframe_to_user(name="Matriz de Confusão", dataframe=df_conf_matrix)