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
    
    