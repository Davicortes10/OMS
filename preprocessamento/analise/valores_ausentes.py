import pandas as pd

class AnaliseValoresAusentes:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): DataFrame que será analisado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df
    
    def contar_valores_ausentes(self) -> pd.Series:
        valores_ausentes = self.df.isnull().sum()
        print("\n📉 Contagem de valores ausentes por coluna:")
        print(valores_ausentes)
        return valores_ausentes
    
    def paises_com_valores_ausentes(self) -> list:
        paises_faltantes = self.df[self.df.isnull().any(axis=1)]['Country'].unique().tolist()
        print("\n🌍 Países com valores ausentes:", paises_faltantes)
        return paises_faltantes
    
    def valores_ausentes_por_pais(self) -> pd.Series:
        valores_por_pais = self.df.isnull().groupby(self.df['Country']).sum().sum(axis=1).sort_values(ascending=False)
        print("\n📊 Valores ausentes por país (ordenados):")
        print(valores_por_pais)
        return valores_por_pais