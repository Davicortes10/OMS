# Expectativa de Vida WHO - Mineração de Dados e Aplicações à Engenharia

Este projeto realiza análises preditivas e mineração de dados na expectativa de vida global, utilizando dados da Organização Mundial da Saúde (WHO).

## Objetivo
Explorar e modelar a expectativa de vida com aprendizado de máquina, redes neurais e visualização de dados.

## Tecnologias Utilizadas
O projeto foi desenvolvido utilizando as seguintes tecnologias e bibliotecas:

- **Python 3.12+**
- **Pandas** → Manipulação e análise de dados
- **NumPy** → Cálculos numéricos eficientes
- **Matplotlib & Seaborn** → Visualização de dados
- **Scikit-Learn** → Algoritmos de aprendizado de máquina
- **TensorFlow & Keras** → Implementação de Redes Neurais Artificiais (RNA)
- **KerasTuner** → Otimização de hiperparâmetros
- **Plotly** → Gráficos interativos

## Pré-requisitos
Antes de rodar o projeto, certifique-se de ter instalado:

- **Python 3.12+**
- **pip** (gerenciador de pacotes do Python)
- **Virtualenv** (opcional, mas recomendado)

Para instalar os pacotes necessários:

```bash
pip install -r requirements.txt
```

## Instalação

1️⃣ Clone este repositório:

```bash
git clone https://github.com/Davicortes10/OMS.git
cd OMS
```

2️⃣ Crie e ative um ambiente virtual (recomendado):

```bash
# Criando o ambiente virtual
python -m venv venv

# Ativando no Windows
venv\Scripts\activate

# Ativando no macOS/Linux
source venv/bin/activate
```

3️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução do Código

Após configurar o ambiente, execute o pipeline completo:

```bash
python main.py
```

Caso queira rodar cada etapa separadamente, utilize:

```python
from principal import Principal
pipeline = Principal()
pipeline.executar_tudo()
```



## Principais Funcionalidades

### Análise Exploratória:
- Identificação de outliers 
- Tratamento de valores ausentes
- Correlação entre variáveis 

### Modelagem de Aprendizado de Máquina:
- Regressão Linear e Árvores de Decisão
- Redes Neurais (Sequential, Keras)
- Otimização com KerasTuner

### Visualização Interativa:
- Gráficos de dispersão e histogramas
- Tendência temporal da expectativa de vida
- Matriz de correlação entre variáveis

## Exemplo de Uso

### Rodando a Modelagem com Redes Neurais

```python
from modelos.model import LifeExpectancyNN
modelo = LifeExpectancyNN(df)
modelo.executar_pipeline(epochs=500, batch_size=32)
```

### Executando a Avaliação do Modelo

```python
from modelos.avaliacao_modelo import ModelEvaluator
avaliacao = ModelEvaluator(y_test, predictions, model.history.history)
avaliacao.executar_avaliacao_completa()
```

## Referências

- 📄 [WHO Life Expectancy Dataset](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)
- 📘 [Documentação do Pandas](https://pandas.pydata.org/)
- 📘 [TensorFlow & Keras](https://www.tensorflow.org/)

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório
2. Crie uma branch (`git checkout -b feature-nova`)
3. Commit suas alterações (`git commit -m 'Adicionando nova funcionalidade'`)
4. Envie para análise (`git push origin feature-nova`)
5. Abra um Pull Request

## Reconhecimentos e Direitos Autorais

### Autores:
- Davi Oliveira Cortes MAT: 2020034190

### Contato:
- Email: davi.cortes@discente.ufma.br
- GitHub: https://github.com/Davicortes10

### Última versão: 28/02/2025
### Versão: 1.0

### Agradecimentos:
Este trabalho foi desenvolvido no curso **Engenharia da Computação** na **Universidade Federal do Maranhão (UFMA)**, sob a orientação do **Professor Doutor Thales Levi Azevedo Valente**. Agradecemos a todos os colegas que contribuíram para a construção deste projeto.

## Licença

### Sobre este projeto
Este material é resultado de um trabalho acadêmico para a disciplina **Mineração de Dados e Aplicações a Engenharia**, orientado pelo professor **Dr. Thales Levi Azevedo Valente**, semestre letivo **2024.2**, curso **Engenharia da Computação** na **Universidade Federal do Maranhão (UFMA)**.

### Licença MIT
Este projeto está licenciado sob a **Licença MIT**.

 [Mais informações sobre a Licença MIT](https://opensource.org/licenses/MIT)

 Desenvolvido por Davi Oliveira Cortes e colaboradores 

