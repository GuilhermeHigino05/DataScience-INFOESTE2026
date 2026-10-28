# Próximos passos

## O que este curso apresentou

Este curso teve como objetivo oferecer um primeiro contato com diferentes partes da Ciência de Dados. Vimos preparação e exploração de dados, regressão, classificação, redes neurais, embeddings, Transformers e modelos de linguagem. A proposta foi construir uma visão geral do fluxo de um projeto e mostrar, com exemplos em Python, como dados podem ser transformados em modelos e análises.

Esse percurso foi necessariamente introdutório. Ele deu um gostinho de várias áreas, mas não pretendeu substituir o estudo sistemático de matemática, estatística, programação, aprendizado de máquina e comunicação de resultados. Para compreender os modelos com mais profundidade, interpretar suas limitações e criar soluções próprias, é importante continuar os estudos de forma gradual.

## Bases fundamentais

### Cálculo

O Cálculo estuda variação, limites, derivadas e integrais. Em Ciência de Dados, as derivadas ajudam a entender gradientes, funções de custo e algoritmos de treinamento, como o gradiente descendente. As integrais aparecem em probabilidade, funções de densidade e algumas formulações de otimização e aprendizado.

Uma sequência inicial de estudos pode incluir:

- funções, gráficos e composição de funções;
- limites e continuidade;
- derivadas e regra da cadeia;
- derivadas parciais e gradiente;
- integrais e interpretação como acumulação;
- funções de várias variáveis e aproximações locais.

O objetivo não é decorar fórmulas. É compreender como uma função muda, como medir essa mudança e como usar essa informação para encontrar melhores parâmetros.

### Álgebra Linear

A Álgebra Linear fornece a linguagem dos dados e dos modelos. Vetores representam observações e parâmetros; matrizes organizam conjuntos de dados e transformações; produtos internos medem relações; autovalores e autovetores aparecem em redução de dimensionalidade e análise de estruturas.

Estude principalmente:

- escalares, vetores, matrizes e tensores;
- operações matriciais e sistemas lineares;
- combinação linear, espaço gerado, base e dimensão;
- independência linear e posto;
- produto interno, norma, distância e projeção;
- transformações lineares;
- autovalores, autovetores e decomposições;
- interpretação geométrica de regressão e redução de dimensionalidade.

Uma boa prática é relacionar cada conceito a uma operação em NumPy ou PyTorch e visualizar vetores e transformações em gráficos simples.

### Estatística e Probabilidade

Probabilidade oferece uma linguagem para incerteza e aleatoriedade. Estatística ajuda a resumir dados, estimar quantidades, comparar grupos e avaliar se um padrão pode ser explicado pelo acaso. Essas áreas são essenciais para não confundir correlação com causalidade e para comunicar o grau de confiança de uma análise.

Os temas mais importantes são:

- eventos, probabilidade condicional e independência;
- variáveis aleatórias e distribuições;
- esperança, variância, covariância e correlação;
- distribuições Bernoulli, binomial, normal e outras distribuições comuns;
- amostragem, viés e variabilidade;
- lei dos grandes números e teorema central do limite;
- estimação pontual e intervalos de confiança;
- testes de hipótese e valor-p;
- regressão, avaliação de modelos e validação cruzada;
- inferência bayesiana em nível introdutório.

Ao estudar, tente sempre responder: de onde vieram os dados, qual é a população de interesse, qual incerteza existe na medida e que conclusão os dados realmente sustentam?

### Otimização

Otimização trata da escolha dos melhores valores para uma função objetivo, respeitando possíveis restrições. Em aprendizado de máquina, normalmente queremos minimizar uma função de perda. O gradiente descendente, apresentado neste curso, é uma das estratégias mais importantes para isso.

Vale estudar:

- funções objetivo, restrições e pontos ótimos;
- mínimos locais e globais;
- convexidade e interpretação geométrica;
- gradiente, Hessiana e condições de otimalidade;
- gradiente descendente e suas variações;
- taxa de aprendizado, normalização e critérios de parada;
- otimização estocástica e por minibatches;
- regularização como parte da definição do problema.

Otimização conecta Cálculo, Álgebra Linear e programação. Ao acompanhar a evolução da perda durante o treinamento, você consegue observar na prática como essas áreas trabalham juntas.

## Como continuar estudando

1. **Fortaleça Python e NumPy.** Escreva funções pequenas, manipule vetores e matrizes e aprenda a testar seus resultados.
2. **Estude uma base matemática por vez.** Comece por Álgebra Linear e Estatística, avance em Cálculo e depois conecte os temas em Otimização.
3. **Reproduza os exemplos.** Primeiro execute os notebooks; depois altere dados, parâmetros e visualizações; por fim, tente reimplementar o método sem consultar o código.
4. **Compare teoria e biblioteca.** Implemente uma versão simples de regressão ou classificação e compare-a com `scikit-learn` ou PyTorch.
5. **Use dados reais com cuidado.** Documente a origem, trate ausências, separe treino e teste e registre as decisões tomadas.
6. **Leia os erros do modelo.** Métricas resumem o desempenho, mas resíduos, exemplos classificados incorretamente e matriz de confusão mostram onde o modelo falha.
7. **Faça projetos pequenos.** Um bom projeto tem uma pergunta clara, uma análise reproduzível e uma conclusão que reconhece limitações.
8. **Explique o que aprendeu.** Escrever um relatório curto ou ensinar um conceito é uma forma eficiente de encontrar lacunas no entendimento.

Não é necessário dominar toda a matemática antes de programar. É melhor alternar teoria e prática: estudar um conceito, implementá-lo em um exemplo pequeno e voltar à teoria para entender o que o código está fazendo.

## Fontes complementares e trilha de estudo

Como guia visual da progressão do conteúdo, vale consultar o roadmap em [roadmap_ciencia_dados_ia.png](roadmap_ciencia_dados_ia.png). Ele ajuda a situar os pilares de Ciência de Dados e IA e a orientar o que estudar nas próximas aulas, mantendo a ordem lógica entre fundamentos, modelos, aplicações e aprofundamento.

Além dos livros e temas já citados, duas fontes gratuitas e muito úteis podem complementar a formação:

- [OSSU Data Science](https://github.com/ossu/data-science): uma iniciativa de "faculdade" livre, em inglês, que reúne materiais e videoaulas de universidades renomadas e cobre uma grande variedade de tópicos de ciência de dados, estatística, matemática, programação, aprendizado de máquina e IA. É uma boa opção para quem quer seguir uma trilha mais ampla e estruturada, sem depender de um único curso.
- [Canal Téo Me Why — playlist de Machine Learning](https://www.youtube.com/playlist?list=PLvlkVRRKOYFTXcpttQSZmv1wDg7F3uH7o): oferece videoaulas gratuitas, bem didáticas e bastante completas sobre diversos tópicos de machine learning e aprendizado de máquina. Ela funciona muito bem como apoio prático para revisar conceitos, observar aplicações e reforçar a conexão entre teoria e implementação.

Essas fontes se encaixam bem na sequência proposta: primeiro fundamentos e ferramentas, depois modelos e avaliação, e por fim aprofundamento em IA e aprendizado profundo. A ideia não é trocar a leitura e a prática, mas complementar a formação com materiais diferentes, em níveis e estilos variados.

## Ementa de leitura

### 1. *Python para Análise de Dados* — Wes McKinney

Use este livro para consolidar Python aplicado a dados, NumPy, pandas, limpeza, transformação, agrupamento, séries temporais e visualização. Ele é uma boa continuação imediata para quem quer ganhar fluência no trabalho cotidiano de análise.

**Foco sugerido:** arrays, DataFrames, índices, seleção, dados ausentes, combinação de tabelas, agrupamentos, importação e exportação de dados.

### 2. *Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras e TensorFlow* — Aurélien Géron

Este livro apresenta um caminho prático para construir, avaliar e melhorar modelos de aprendizado de máquina. Ele ajuda a conectar preparação de dados, pipelines, validação, métricas, modelos clássicos e redes neurais.

**Foco sugerido:** projeto de aprendizado de máquina, divisão de dados, pré-processamento, regressão, classificação, validação cruzada, ajuste de hiperparâmetros, ensembles e introdução a redes neurais.

### 3. *Matemática para Machine Learning* — Marc Peter Deisenroth, A. Aldo Faisal e Cheng soon Ong

Use esta referência para estudar a matemática que sustenta os modelos. O livro conecta Álgebra Linear, Cálculo Multivariável e Probabilidade com problemas de aprendizado de máquina.

**Foco sugerido:** vetores e matrizes, decomposições, derivadas, gradientes, otimização, probabilidade e regressão.

### 4. *An Introduction to Statistical Learning with Applications in Python* — Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani e Jonathan Taylor

Esta é uma referência acessível para entender os principais métodos estatísticos de aprendizado, suas hipóteses e formas de avaliação. A versão com Python combina explicação conceitual, exemplos e exercícios.

**Foco sugerido:** regressão, classificação, reamostragem, seleção de modelos, regularização, árvores, métodos de ensemble, aprendizado não supervisionado e fundamentos de aprendizado profundo.

### 5. *Attention Is All You Need* — Ashish Vaswani e coautores

Este artigo apresenta a arquitetura Transformer e o mecanismo de atenção que se tornou central em muitos modelos modernos de linguagem. É uma leitura mais técnica e deve ser feita depois de estudar redes neurais, Álgebra Linear, probabilidade e otimização.

**Foco sugerido:** consultas, chaves e valores, atenção escalada, multi-head attention, codificação posicional, conexões residuais, normalização e treinamento paralelo.

## Ordem recomendada

Uma sequência possível é:

1. *Python para Análise de Dados* para consolidar as ferramentas;
2. revisão de Álgebra Linear, Estatística e Probabilidade;
3. *An Introduction to Statistical Learning with Applications in Python*;
4. *Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras e TensorFlow*;
5. *Matemática para Machine Learning* em paralelo aos capítulos mais matemáticos;
6. *Attention Is All You Need* depois de compreender redes neurais e atenção.

Essa ordem não é uma regra rígida. O mais importante é manter um ciclo de estudo, implementação, experimentação e revisão. A Ciência de Dados é ampla, e aprender bem significa construir conexões entre programação, matemática, dados, modelos e o problema real que se deseja resolver.
