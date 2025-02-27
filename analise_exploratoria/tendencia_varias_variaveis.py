class TendenciaVariasVariaveis:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe com um DataFrame.

        Args:
            df (pd.DataFrame): O DataFrame que será visualizado.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ O argumento fornecido deve ser um DataFrame do Pandas.")

        # Verifica se as colunas necessárias existem
        required_columns = {'Year', 'Country'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"❌ O DataFrame deve conter as colunas {required_columns} para a visualização.")

        self.df = df.copy()  # Mantém os dados originais intactos
        self.cols_to_inspect = [
            'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 
            'Life expectancy ', 'Schooling', 'Income composition of resources', 
            'GDP', 'Population'
        ]