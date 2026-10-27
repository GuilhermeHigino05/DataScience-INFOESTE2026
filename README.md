# DataScience-INFOESTE2026

Material didático da disciplina de Ciência de Dados e Inteligência Artificial.

## Estrutura

```text
aulas/
	aula01_final.ipynb
	aula02_final.ipynb
	datasets/
```

`aula01_final.ipynb` apresenta preparação e exploração de dados, regressão
linear, função de custo, derivadas, gradiente descendente e avaliação de
modelos.

`aula02_final.ipynb` continua a progressão com classificação, regressão
logística, redes neurais, embeddings, TF-IDF, Transformers, attention e uma
aplicação de classificação de sentimentos no IMDB.

## Como executar

O projeto usa Python 3.13 ou superior e pode ser executado em um ambiente
virtual. A partir da raiz do projeto:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install jupyter pandas numpy matplotlib seaborn scikit-learn torch datasets graphviz
jupyter notebook
```

No Arch Linux, a renderização do diagrama Graphviz também exige o executável
de sistema:

```bash
sudo pacman -S graphviz
```

Abra o notebook desejado dentro de `aulas/`. Os datasets usados pelos
notebooks estão em `aulas/datasets/`, e os caminhos relativos já partem dessa
localização.

## Ordem recomendada

1. `aulas/aula01_final.ipynb`
2. `aulas/aula02_final.ipynb`

