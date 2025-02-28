import pandas as pd

class RemovendoColunas:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será processado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        self.df = df.copy()  # Mantém os dados originais intactos
        self.cols_to_remove = [' thinness 5-9 years', 'percentage expenditure', 
                               'under-five deaths ', 'Diphtheria ', 
                               'Income composition of resources']
    
    def remover_colunas(self) -> pd.DataFrame:
        
        colunas_presentes = [col for col in self.cols_to_remove if col in self.df.columns]
        if not colunas_presentes:
            print("⚠️ Nenhuma das colunas a serem removidas está presente no DataFrame.")
            return self.df
        
        df_processado = self.df.drop(colunas_presentes, axis=1)
        print(f"✅ Removidas as colunas: {colunas_presentes}")
        return df_processado
    
