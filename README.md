# DataScience-INFOESTE2026
Material didático do curso de Ciência de Dados e Inteligência Artificial da INFOESTE 2026.

## Estrutura

```text
aulas/
	aula01_final.ipynb
	aula02_final.ipynb
	datasets/
```

`aula01_final.ipynb` apresenta a primeira aula do curso e aborda preparação e exploração de dados, regressão
linear, função de custo, derivadas, gradiente descendente e avaliação de
modelos.

`aula02_final.ipynb` continua a progressão com classificação, regressão
logística, redes neurais, embeddings, TF-IDF, Transformers, attention e uma
aplicação de classificação de sentimentos no IMDB.

## Como executar

O projeto usa Python 3.13 ou superior. Para executar localmente, clone o
repositório, abra a pasta raiz no VS Code e instale as dependências:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
pip install -r requirements.txt
```

Os notebooks das aulas usam `pathlib` para localizar automaticamente a pasta
`aulas/datasets`. Ao executar a célula de configuração, o notebook imprime o
caminho encontrado. Se a pasta ou algum arquivo não for encontrado, confira se
o repositório foi clonado por completo e se o notebook está sendo executado
com a pasta raiz aberta no VS Code.

### Google Colab

No Colab, clone o repositório antes de executar as células dos notebooks:

```python
!git clone https://github.com/GuilhermeHigino05/DataScience-INFOESTE2026.git
%cd /content/DataScience-INFOESTE2026
```

Depois, abra o notebook dentro da pasta `aulas`. Se o caminho dos datasets
ainda não for encontrado, verifique se o clone terminou e se a pasta
`aulas/datasets` está presente. O Colab pode iniciar em outra pasta, por isso o
`%cd` é importante.

## Ordem recomendada

1. `aulas/aula01_final.ipynb`
2. `aulas/aula02_final.ipynb`

