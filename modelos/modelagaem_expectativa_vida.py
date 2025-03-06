import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split,KFold
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import mean_absolute_error, r2_score
from modelos.avaliacao_modelo import Avaliacao

class ExpectativaVidaMLP:
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

    def __init__(self, df: pd.DataFrame, k_folds=5):
        """
        Inicializa a classe, realizando a preparação dos dados.

        Args:
            df (pd.DataFrame): O DataFrame com os dados originais.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()
        self.k_folds = k_folds
        self.label_cols = ['Country', 'Status']
        self.scale_cols = [col for col in df.columns if col not in self.label_cols + ['Life expectancy ']]
        
        self.pre_processed_csv = self.preprocessamento_data(df)
        self.X = self.pre_processed_csv.drop('Life expectancy ', axis=1)
        self.y = self.pre_processed_csv['Life expectancy ']

        self.X_train, self.X_temp, self.y_train, self.y_temp = train_test_split(
            self.X, self.y, test_size=0.4, random_state=123
        )
        self.X_val, self.X_test, self.y_val, self.y_test = train_test_split(
            self.X_temp, self.y_temp, test_size=0.5, random_state=123
        )

        self.normalizar_dados()

        self.model = self.modelando(input_shape=(self.X_train.shape[1],))
    
    def preprocessamento_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Aplica Label Encoding às colunas categóricas para conversão em valores numéricos.

        Args:
            df (pd.DataFrame): DataFrame contendo variáveis categóricas.

        Returns:
            pd.DataFrame: DataFrame com colunas categóricas convertidas.
        """

        le = LabelEncoder()
        
        df[self.label_cols] = df[self.label_cols].apply(le.fit_transform)

        return df
    
    def normalizar_dados(self):
        """
        Aplica normalização Min-Max apenas ao conjunto de treino e usa os mesmos parâmetros no teste.

        Args:
            None (usa os atributos da classe).

        Returns:
            None (modifica os atributos X_train e X_test in-place).
        """
        
        mm = MinMaxScaler()


        self.X_train = mm.fit_transform(self.X_train)
        self.X_val = mm.transform(self.X_val)
        self.X_test = mm.transform(self.X_test)
    
    def modelando(self, input_shape: tuple) -> Sequential:
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
    
    def compilando(self, optimizer='adam', loss='mse', metrics=['mae']):
        """
        Compila o modelo com otimizador e função de perda definidos.

        Args:
            optimizer (str): Algoritmo de otimização (padrão: Adam).
            loss (str): Função de perda (padrão: Huber).
            metrics (list): Lista de métricas (padrão: MAE).
        """

        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def treinando(self, epochs=1000, batch_size=32):
        """
        Treina o modelo utilizando validação cruzada K-Fold.
        """
        kf = KFold(n_splits=self.k_folds, shuffle=True, random_state=123)
        mae_scores = []
        r2_scores = []

        for train_index, val_index in kf.split(self.X_train):
            X_train_fold, X_val_fold = self.X_train[train_index], self.X_train[val_index]
            y_train_fold, y_val_fold = self.y_train.iloc[train_index], self.y_train.iloc[val_index]

            # Criar um novo modelo para cada iteração do K-Fold
            self.model = self.modelando(input_shape=(X_train_fold.shape[1],))
            self.compilando()

            self.model.fit(
                X_train_fold, y_train_fold,
                epochs=epochs,
                batch_size=batch_size,
                validation_data=(X_val_fold, y_val_fold),
                verbose=0  # Reduz logs durante o treino
            )

            # Previsão e avaliação do fold
            y_pred = self.model.predict(X_val_fold).flatten()
            mae = mean_absolute_error(y_val_fold, y_pred)
            r2 = r2_score(y_val_fold, y_pred)

            mae_scores.append(mae)
            r2_scores.append(r2)

        # Exibir média dos resultados da Validação Cruzada
        print(f"\n📊 **Resultados da Validação Cruzada K-Fold ({self.k_folds} folds):**")
        print(f"MAE médio: {np.mean(mae_scores):.4f}")
        print(f"R² médio: {np.mean(r2_scores):.4f}")
    
    def avaliando(self):
        """
        Avalia o desempenho do modelo treinado e exibe métricas de desempenho para regressão.

        A avaliação inclui:
        - Erro Absoluto Médio (MAE)
        - Erro Relativo Médio (MAPE)
        - R² Score (Coeficiente de Determinação)
        - Análise visual da distribuição de erros.

        Returns:
            None: Apenas exibe os resultados formatados.

        Example:
            >>> model = LifeExpectancyNN(df)
            >>> model.evaluate_model()
        """

        # Fazer previsões
        y_pred = self.model.predict(self.X_test).flatten()

        # Calcular métricas apropriadas para regressão
        erro_absoluto = np.abs(self.y_test - y_pred)
        erro_relativo = np.abs(erro_absoluto / self.y_test)
        r2 = r2_score(self.y_test, y_pred)

        # Criar DataFrame de métricas
        df_metrics = pd.DataFrame({
            "Métrica": ["Erro Absoluto Médio (MAE)", "Erro Relativo Médio (MAPE)", "R² Score"],
            "Valor": [np.mean(erro_absoluto), np.mean(erro_relativo) * 100, r2]
        })

        # Exibir métricas no console
        print("\n📊 **Métricas do Modelo:**")
        print(df_metrics)

        # Criar instância da classe ModelEvaluator para análises visuais
        avaliacao =  Avaliacao(self.y_test, y_pred, self.model.history.history)
        
        print("\n📊 **Gerando análises visuais...**")
        avaliacao.executar_avaliacao_completa()

        print("\n✅ **Avaliação do modelo finalizada!** 🚀")
    
    def executar_pipeline(self, epochs=1000, batch_size=3):
        """
        Executa o pipeline completo de modelagem da expectativa de vida.

        Este método inclui as seguintes etapas:
        1. Compilação do modelo com otimizador e função de perda.
        2. Treinamento do modelo nos dados de treinamento.
        3. Avaliação do modelo nos dados de teste.
        4. Exibição das métricas de desempenho.

        Args:
            epochs (int, opcional): Número de épocas para o treinamento (padrão: 1000).
            batch_size (int, opcional): Tamanho do batch para treinamento (padrão: 32).
            validation_split (float, opcional): Percentual dos dados de treino usados para validação (padrão: 0.2).

        Returns:
            None: Apenas exibe os resultados formatados.

        Example:
            >>> model = LifeExpectancyNN(df)
            >>> model.executar_pipeline(epochs=500, batch_size=64, validation_split=0.3)
        """
        print("\n🔄 Compilando o modelo...")
        self.compilando()

        print("\n📊 Iniciando o treinamento do modelo...")
        self.treinando(epochs=epochs, batch_size=batch_size)

        print("\n✅ Avaliando o modelo...")
        self.avaliando()
