import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

class LifeExpectancyNN:
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
        
        le = LabelEncoder()
        mm = MinMaxScaler()

        df[self.scale_cols] = mm.fit_transform(df[self.scale_cols])
        df[self.label_cols] = df[self.label_cols].apply(le.fit_transform)

        return df
    
    def build_model(self, input_shape: tuple) -> Sequential:
        
        model = Sequential([
            Dense(128, activation='relu', input_shape=input_shape),
            Dense(64, activation='relu'),
            Dense(1, activation='linear')
        ])
        return model