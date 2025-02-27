import pandas as pd

class Duplicatas:

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): DataFrame que será analisado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")
        
        self.df = df
    
    def verificar_duplicatas(self, subset: list) -> int:
        
        if not isinstance(subset, list) or not all(col in self.df.columns for col in subset):
            raise ValueError("❌ O argumento 'subset' deve ser uma lista contendo colunas válidas do DataFrame.")

        duplicatas = self.df.duplicated(subset=subset).sum()
        print(f"🔍 Total de registros duplicados considerando {subset}: {duplicatas}")
        return duplicatas
    
    def contar_valores_unicos(self) -> pd.Series:
        
        valores_unicos = self.df.select_dtypes(exclude=['float', 'int']).nunique()
        print("\n📊 Contagem de valores únicos por coluna categórica:")
        print(valores_unicos)
        return valores_unicos

    
