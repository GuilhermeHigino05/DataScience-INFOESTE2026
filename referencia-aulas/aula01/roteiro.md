# Roteiro — Aula 1 — Fundamentos de Ciência de Dados e Machine Learning

> **Curso:** Introdução à Ciência de Dados e IA — INFOESTE
> **Encontro:** 1 de 2 (~4h presenciais)
> **Blocos cobertos:** Bloco 1 (Introdução à Ciência de Dados) e Bloco 2 (Regressão Linear + Gradient Descent)
> **Instrutores:** Bruno (condução técnica) e Guilherme (co-instrutor / facilitação)
> **Artefato do dia:** o **primeiro modelo de Machine Learning** do aluno (regressão linear do zero)
> **Cadeia de produção:** este roteiro → slides → células de markdown → notebook `aula01.ipynb` → fala.

---

## 0. Como usar este roteiro

Este documento é a **fonte primária** da Aula 1. A partir dele produzimos, nesta ordem:

1. **os slides** (esboço na seção 7);
2. **as células de markdown** do notebook (que espelham os slides);
3. **o notebook** `referencia-aulas/aula01/aula01.ipynb` (guiado, ao vivo);
4. **a fala** do instrutor (blocos "O que falar").

Regras de leitura:

- Cada tópico traz **Tempo**, **Objetivo**, **Slide**, **Notebook**, **O que falar** e **Pergunta ao aluno**.
- Os tempos são **nominais**; o instrutor ajusta ao ritmo da turma. Em conflito, **priorize a atividade** (princípio "menos conteúdo, mais experiência").
- Quando algo for **simplificação pedagógica**, o roteiro marca explicitamente — não inventar precisão que não temos.
- Matemática aparece quando **resolve uma necessidade concreta** — nunca como disciplina isolada.

---

## 1. Visão geral

### 1.1 Onde estamos na narrativa do curso

A Aula 1 é o **começo da espiral**:

```
Dados -> Ciência de Dados -> Machine Learning -> Regressão -> (Classificação -> Redes Neurais -> ...)
```

Hoje paramos em **Regressão**. A Aula 2 retoma exatamente daqui (classificação → redes neurais → IA).

### 1.2 Objetivos da Aula 1

Ao final do encontro, o aluno deve ser capaz de:

- explicar o que é Ciência de Dados e diferenciá-la de Data Analysis e Data Engineering;
- situar IA ⊃ Machine Learning ⊃ Deep Learning;
- descrever o fluxo de um projeto de dados (coleta → limpeza → EDA → features → modelo);
- entender por que **nem toda relação é linear** e o que é uma relação linear;
- escrever o modelo de regressão linear $\hat{y} = wx + b$;
- explicar a função de custo (MSE) e por que minimizá-la;
- entender a intuição de derivada e de gradiente;
- implementar e treinar uma regressão linear **do zero em NumPy** com **Gradient Descent**;
- avaliar e diagnosticar o modelo (MSE, MAE, R², resíduos).

### 1.3 Artefatos do dia

- o aluno com o notebook rodando e **seu primeiro modelo treinado**;
- notebook preenchido durante a aula, com apoio dos instrutores;
- dataset já pronto para os alunos usarem: `dataset_olist_price_adj.csv` (alvo transformado).

### 1.4 Materiais e arquivos

| Papel | Arquivo |
| --- | --- |
| Notebook da aula | `referencia-aulas/aula01/aula01.ipynb` |
| Notebook de apoio (linearidade) | `referencia-aulas/aula01/linearidade.ipynb` |
| Dataset dos alunos (Olist + price ajustado) | `referencia-aulas/aula01/dataset_olist_price_adj.csv` |
| Dataset de apoio (antropometria) | `pratica/datasets/NHANES-2017-2018-height-weight.csv` |
| Slides | `material-auxiliar/slides/slides-aula1.pdf` (a produzir) |

> **Nota:** o dataset dos alunos é gerado ao final do próprio notebook — a coluna `price` transformada por **Yeo-Johnson** (ver seção 5.13).

### 1.5 Reparto entre instrutores

- **Abertura, contexto e técnica matemática:** Bruno.
- **Ementa, repositório, combinados e facilitação:** Guilherme.
- **Bloco 1 (mapa da área):** conduzido em dupla; Guilherme apoia com exemplos do curso/ADS.
- **Bloco 2 (modelo):** Bruno conduz; Guilherme circula pela sala na hora da implementação.
- **Ambos:** suporte individual nas células de prática e no diagnóstico.

---

## 2. Cronograma (~4h)

| Momento | Duração | Conteúdo |
| --- | --- | --- |
| Abertura | 15 min | boas-vindas, instrutores, promessa e combinados |
| **Bloco 1** | ~95 min | mapa da área + mão na massa (Olist: EDA, cleaning, features) |
| *Intervalo* | 15 min | — |
| **Bloco 2** | ~95 min | linearidade → regressão → MSE → gradiente → GD → avaliação |
| Encerramento | 15 min | síntese, exercícios, próximos passos e dúvidas |
| **Total** | ~3h35–4h | |

---

## 3. Bloco 1 — Introdução à Ciência de Dados (~95 min)

> **Função do bloco:** construir o **mapa mental** da área antes de modelar. **Não aprofundar** nenhum tópico — o objetivo é dar contexto para o Bloco 2.

Sub-cronograma (nominal):

| # | Tópico | Tempo |
| --- | --- | --- |
| 3.0 | Abertura e boas-vindas | 4 |
| 3.1 | Apresentação dos instrutores | 4 |
| 3.2 | O curso: proposta e combinados | 6 |
| 3.3 | Ementa, repositório e material | 5 |
| 3.4 | O que é Ciência de Dados | 6 |
| 3.5 | Data Analysis vs Data Engineering vs Data Science | 6 |
| 3.6 | IA vs Machine Learning vs Deep Learning | 6 |
| 3.7 | O que são dados? | 4 |
| 3.8 | O fluxo de um projeto de dados | 6 |
| 3.9 | ETL/ELT | 5 |
| 3.10 | Data Cleaning | 5 |
| 3.11 | EDA e visualização | 6 |
| 3.12 | Feature Engineering | 5 |
| 3.13 | Introdução ao Machine Learning | 7 |
| 3.14 | Ferramentas do ecossistema | 3 |
| 3.15 | Mão na massa: o dataset Olist no notebook | 18 |
| | **Total** | **~96** |

### 3.0 Abertura e boas-vindas — 4 min

- **Objetivo:** quebrar o gelo, criar clima, alinhar a expectativa do dia.
- **Slide:** título do encontro + "hoje você vai treinar seu primeiro modelo".
- **O que falar:**
  - agradecer a presença e o interesse pela área;
  - dizer que o curso é **"de aluno para aluno"** e que **não é preciso saber nada avançado**;
  - prometer o artefato: *"ao final do dia, cada um sai com um modelo treinado"*;
  - reforçar o combinado: **perguntar a qualquer momento**; errar faz parte.
- **Fechamento:** "dúvida travada? chama a gente, não fica parado."

### 3.1 Apresentação dos instrutores — 4 min

- **Objetivo:** dar credibilidade e deixar claro que **são dois professores**.
- **O que falar:**
  - **Bruno** — experiência profissional e acadêmica em Ciência de Dados/ML/IA; conduz a parte técnica.
  - **Guilherme** — estudante de ADS, organiza o curso e é **co-instrutor** (não assistente); conduz blocos e apoia os exercícios.
- **Nota pedagógica:** o roteiro reserva blocos reais para os dois; evitar que Guilherme só "passe o microfone".

### 3.2 O curso: proposta e combinados — 6 min

- **Objetivo:** alinhar expectativas e criar o contrato de aprendizagem.
- **Slide:** "o que este curso é / o que este curso não é".
- **O que falar:**
  - **É:** introdução conceitual e **muito prática**; "mão na massa"; vamos **construir versões simples** dos modelos para entender o que há por baixo.
  - **Não é:** tentar ensinar toda a Ciência de Dados/ML/IA em 8h. Seremos **honestos** sobre o escopo.
  - Combinados: 2 encontros de ~4h; intervalo no meio; notebook aberto; o ritmo da turma manda.
  - **Incentivo:** ao final há um projeto e um **sorteio do livro** *Mãos à Obra: Aprendizado de Máquina* (Géron) para quem participar.
- **Pergunta ao aluno:** "o que vocês esperam conseguir fazer ao final?" (ler o clima; ajustar exemplos).

### 3.3 Ementa, repositório e material — 5 min

- **Objetivo:** orientar o aluno sobre **onde está o quê** e como acompanhar.
- **Slide:** mapa do repositório.
- **O que falar:**
  - as **2 aulas / 4 blocos** do curso (usar o mapa da seção 1.1);
  - estrutura: `aulas/` (notebooks), `material-auxiliar/` (aprofundamento + slides), `pratica/` (datasets e projetos);
  - **como usar o notebook:** acompanhar **célula a célula**; há células de exemplo, parcialmente preenchidas e vazias; os instrutores ajudam, sobretudo no Python;
  - o notebook **depende da aula presencial** para render tudo — mas fica no repo para revisar depois.
- **Nota:** explique que o repo é público no GitHub (fork/PR vêm no fim do curso).

### 3.4 O que é Ciência de Dados — 6 min

- **Objetivo:** definir a área em uma frase e desmontar o mito do "vou só usar um modelo".
- **Slide:** definição + 3 ingredientes.
- **Notebook:** célula `### O que é Ciência de Dados?`.
- **O que falar:**
  - Ciência de Dados = **extrair conhecimento e decisões a partir de dados**;
  - combina **programação** + **estatística/matemática** + **conhecimento do domínio**;
  - **conceito-chave:** fazer Ciência de Dados é **resolver um problema**, não "apertar o botão de um modelo".
- **Pergunta ao aluno:** "onde você já viu dados servindo para tomar uma decisão?"

### 3.5 Data Analysis vs Data Engineering vs Data Science — 6 min

- **Objetivo:** mostrar que "dados" é um conjunto de papéis complementares.
- **Slide:** tabela (área → foco → pergunta típica).
- **Notebook:** célula `### Não é só Ciência de Dados`.
- **O que falar (usar a tabela):**
  - **Data Analysis:** interpretar dados já organizados — *"o que aconteceu e por quê?"*;
  - **Data Engineering:** construir o caminho dos dados — *"como os dados chegam limpos e no lugar certo?"*;
  - **Data Science:** modelar e prever — *"o que vai acontecer / qual a melhor decisão?"*;
  - **enfatizar:** na prática os papéis **se misturam**; hoje passamos por todos.
- **Pergunta ao aluno:** "num e-commerce como o Olist, quem faz o quê?"

### 3.6 IA vs Machine Learning vs Deep Learning — 6 min

- **Objetivo:** desfazer a confusão dos três termos (todos usam "IA" como sinônimo).
- **Slide:** diagrama de camadas IA ⊃ ML ⊃ DL.
- **Notebook:** célula `### IA, Machine Learning e Deep Learning`.
- **O que falar:**
  - **IA:** qualquer sistema que executa tarefas "inteligentes";
  - **Machine Learning:** **aprende padrões a partir de dados** em vez de ser programado regra por regra;
  - **Deep Learning:** ML com **redes neurais profundas**;
  - **simplificação (dizer em voz alta):** "no ML nós **não escrevemos a regra**; damos exemplos e o modelo **descobre a regra**".
- **Pergunta ao aluno:** "por que treinar em vez de escrever regras? quando isso **falha**?"

### 3.7 O que são dados? — 4 min

- **Objetivo:** fixar o vocabulário (linha/coluna) que será reutilizado o dia inteiro.
- **Slide:** exemplo de tabela com destaque de uma linha e uma coluna.
- **O que falar:**
  - **tabela:** cada **linha** é um exemplo (um pedido, um cliente); cada **coluna** é uma característica (*feature*);
  - tipos comuns: numérico, categórico, texto, data/hora;
  - amarração: "o **alvo** é a coluna que queremos prever; as **features** são o que temos para prever".
- **Pergunta ao aluno:** "que tabela você já produziu sem perceber? (planilha de gastos, notas, treino...)"

### 3.8 O fluxo de um projeto de dados — 6 min

- **Objetivo:** instalar o "mapa de processo" que vamos seguir na prática.
- **Slide:** diagrama do fluxo.
- **Notebook:** célula `### O que são dados? E o que fazemos com eles?`.
- **O que falar (fluxo):**
  ```
  coleta -> limpeza (cleaning) -> ETL/ELT -> EDA -> feature engineering -> modelo
  ```
  - **garbage in, garbage out:** "um modelo só é tão bom quanto os dados que recebe"; por isso limpamos e exploramos **antes** de modelar;
  - deixar claro: hoje vamos **percorrer esse fluxo** de ponta a ponta, ainda que de forma simples.
- **Pergunta ao aluno:** "onde nesse fluxo vocês acham que se gasta **mais tempo** na vida real?"

### 3.9 ETL/ELT — 5 min

- **Objetivo:** entender como os dados chegam "no lugar certo".
- **Slide:** ETL vs ELT (uma linha cada).
- **O que falar:**
  - **Extract, Transform, Load** — mover e padronizar dados entre sistemas;
  - **ETL** transforma antes de carregar; **ELT** carrega antes de transformar;
  - no nosso caso, "transformar" inclui **juntar tabelas** (JOIN) por uma chave.
- **Pergunta ao aluno:** "por que precisamos juntar várias tabelas antes de modelar?"

### 3.10 Data Cleaning — 5 min

- **Objetivo:** saber reconhecer os "sujeitos" dos dados reais.
- **Slide:** missing / duplicados / tipos / outliers.
- **O que falar:**
  - **valores ausentes**, **duplicados**, **tipos errados**, **outliers**;
  - **conceito (outlier):** valor muito distante do padrão — pode "puxar" o modelo;
  - decisão é sempre um **juízo** (remover? imputar? manter?) — não há resposta única.
- **Pergunta ao aluno:** "o que você faria com um produto que pesa 200 kg e foi vendido como 'leve'?"

### 3.11 EDA e visualização — 6 min

- **Objetivo:** "plotar é pensar" — a EDA precede a modelagem.
- **Slide:** collage de gráficos (histograma, dispersão, boxplot, heatmap).
- **Notebook:** seção `### EDA: entendendo os dados antes de modelar`.
- **O que falar:**
  - EDA = fazer perguntas **simples** (mínimo, máximo, média, formato da distribuição) antes de investir em modelagem;
  - **histograma** → forma da distribuição (assimetria!);
  - **dispersão** → relação entre duas variáveis;
  - **heatmap de correlação** → relações lineares entre várias colunas;
  - **boxplot** → distribuição por categoria.
- **Pergunta ao aluno:** "o que um histograma conta que a **média** esconde?"

### 3.12 Feature Engineering — 5 min

- **Objetivo:** entender que "preparar a entrada" é parte central do trabalho.
- **Slide:** antes/depois de uma tabela com feature criada.
- **O que falar:**
  - **criar/transformar** colunas para ajudar o modelo a aprender;
  - **escala importa:** variáveis em ordens de grandeza muito diferentes atrapalham o treino (vamos ver isso no Bloco 2);
  - transformar o **alvo** também é uma escolha de engenharia (faremos com o `price` no Bloco 2).
- **Pergunta ao aluno:** "que feature você criaria a partir de uma data de compra?"

### 3.13 Introdução ao Machine Learning — 7 min

- **Objetivo:** dar o vocabulário mínimo para o Bloco 2.
- **Slide:** features/alvo, treino/teste, generalização.
- **O que falar:**
  - **supervisionado** (temos o alvo) vs **não supervisionado** (procuramos estrutura) — citar bem rápido;
  - **$X$ (features)** e **$y$ (alvo)**;
  - **treino vs teste:** nunca avaliar nos dados em que treinou; queremos **generalização**;
  - **overfitting (simplificado):** "decorar" o treino e ir mal no novo.
- **Pergunta ao aluno:** "por que o modelo pode ir bem no treino e mal no teste?"

### 3.14 Ferramentas do ecossistema — 3 min

- **Objetivo:** situar o "kit" que vamos usar.
- **Slide:** logos/links curtos.
- **O que falar:**
  - **Python** + **pandas/numpy** (dados e matemática), **matplotlib/seaborn** (gráficos), **scikit-learn** (modelos prontos), **Jupyter** (notebooks); **Git/GitHub** para versionar e portfólio.
  - Frase de ouro: "hoje escrevemos o modelo **na mão**, mas com essas ferramentas no ecossistema".

### 3.15 Mão na massa — o dataset Olist no notebook — 18 min

- **Objetivo:** percorrer o fluxo de um projeto de dados **no código**, com a turma acompanhando célula a célula.
- **Notebook:** toda a parte final do Bloco 1 do `aula01.ipynb` (setup → carregamento → JOIN → EDA → cleaning → features).
- **Formato:** instrutor projeta e roda; **Guilherme circula pela sala**; pausas para "rode aí na sua máquina".

**Sequência no notebook (o que dizer em cada passo):**

1. **Preparando o ambiente** (célula de imports)
   - "Poucas dependências de propósito: pandas, numpy, matplotlib, seaborn".
2. **Carregando os dados** (Olist, 4 arquivos)
   - mostrar a busca **robusta** da pasta `archive` (funciona rodando de várias pastas);
   - imprimir os `.shape` de cada tabela → "dados vêm em pedaços".
3. **O dataset: e-commerce Olist** (markdown)
   - contextualizar: pedidos reais de uma loja brasileira; cada arquivo tem uma **chave**.
4. **Juntando as tabelas (JOIN)**
   - destacar o detalhe de **Data Engineering**: pagamentos podem ter **várias linhas por pedido** → **agregamos** por `order_id` antes do merge;
   - resultado: `df` (base única) → imprimir `df.shape` e `df.head()`.
5. **`df.info()` e `df.describe()`**
   - tipos, valores não nulos, escala das variáveis.
6. **EDA**
   - histogramas (`price`, `freight_value`, `product_weight_g`, `payment_value`) → **assimetria** e cauda longa;
   - heatmap de correlação → primeiras suspeitas de relação.
7. **Data Cleaning**
   - contar valores ausentes; `dropna` nas colunas de interesse;
   - remover **outliers de peso** (percentil 99) → "cortando os 1% mais extremos".
8. **Feature Engineering e divisão treino/teste**
   - definir o problema: **"dado o peso, quanto custa?"** → feature $x$ = `product_weight_g`, alvo $y$ = `price`;
   - **split** treino/teste (80/20) e **por que** não avaliar no treino.
9. **Transformando o alvo (Yeo-Johnson)** — ver seção 5.13
   - aplicar `PowerTransformer(method="yeo-johnson", standardize=True)` sobre `price` → **`price_adj`**;
   - mostrar o histograma **antes/depois** (assimétrico → simétrico);
   - **aviso explícito à turma:** "essa transformação é **puramente para simplificar a aula**".

- **Perguntas ao aluno (durante o demo):**
  - "por que o `price` tem essa cauda longa?"
  - "o que muda no modelo se usarmos o `price` cru vs `price_adj`?"
  - "esse `dropna` está removendo muita coisa? importa?"

> **Fechamento do Bloco 1:** "Temos um problema formulado, dados limpos e um alvo preparado. Agora falta **o modelo**."

---

## 4. Intervalo — 15 min

- Avisar o horário exato de retorno (cronometrar).
- **Guilherme** confere se alguém travou no notebook e deixa o ambiente pronto para o Bloco 2.
- Deixar a frase-gancho: "quando voltarmos, vamos **construir a reta** e **descobrir** como ela aprende".

---

## 5. Bloco 2 — Linearidade, Regressão Linear e Gradient Descent (~95 min)

> **Função do bloco:** fazer o aluno **construir e treinar** uma regressão linear do zero, entendendo o **mecanismo de aprendizado**. **Não** é uma derivação matemática completa.

Sub-cronograma (nominal):

| # | Tópico | Tempo |
| --- | --- | --- |
| 5.0 | Reconexão | 3 |
| 5.1 | Linearidade (não-linear → linear) | 14 |
| 5.2 | O modelo: uma reta | 6 |
| 5.3 | Resíduo, erro e função de custo (MSE) | 8 |
| 5.4 | Intuição de derivada | 6 |
| 5.5 | Gradiente | 4 |
| 5.6 | Gradient Descent | 10 |
| 5.7 | Cálculo na lousa | 8 |
| 5.8 | Feature scaling | 5 |
| 5.9 | Implementação em NumPy | 11 |
| 5.10 | Treinamento e convergência | 5 |
| 5.11 | O mesmo modelo com Scikit-Learn | 4 |
| 5.12 | Avaliação e diagnóstico | 8 |
| 5.13 | Recap do alvo transformado e dataset dos alunos | 4 |
| 5.14 | Síntese | 3 |
| | **Total** | **~99** |

### 5.0 Reconexão — 3 min

- **Objetivo:** retomar o fio e a motivação.
- **O que falar:**
  - "Temos dados limpos e um alvo (`price_adj`). Agora: **como um modelo 'aprende'?**"
  - anunciar a jornada: reta → erro → derivada → gradiente → descida → modelo treinado.

### 5.1 Linearidade — 14 min

- **Objetivo:** entender **o que é** uma relação linear e **por que** isso importa **antes** de usar uma reta. Começar pelo **contraexemplo** (não-linear) e só então o caso linear.
- **Slide:** "Nem tudo é uma reta" → "Quando é uma reta?".
- **Notebook de apoio:** `referencia-aulas/aula01/linearidade.ipynb` (dataset `NHANES-2017-2018-height-weight.csv`: colunas `age`, `weight`, `height`).
- **Notebook principal:** seção `### Linearidade` (scatter peso × `price_adj`).

**Passo 1 — Exemplo NÃO-LINEAR (idade × altura) — ~6 min**

- Abrir `linearidade.ipynb` e mostrar o **scatter `age` × `height`** (com a reta tracejada do `regplot`).
- **O que falar:**
  - a altura **sobe rápido** na infância e **estabiliza** por volta dos 18–20 anos (curva de crescimento);
  - a reta tracejada **erra sistematicamente**: subestima as crianças, superestima os adultos;
  - **mensagem:** "uma reta é um **modelo ruim** quando a relação não é linear".
- **Pergunta ao aluno:** "se eu te pedisse para prever a altura de alguém de 40 anos, a reta do gráfico ajudaria? por quê?"
- **Conceito (dizer em voz alta):** *linearidade é uma **suposição** do modelo — e, como toda suposição, pode ser violada.*

**Passo 2 — E quando é LINEAR? — ~4 min**

- **O que falar:**
  - uma relação é **linear** quando dá para aproximá-la por uma **reta**: aumentar $x$ faz $y$ variar de forma **aproximadamente proporcional**;
  - nem tudo é linear, mas **muita coisa é aproximadamente linear** — e é aí que a regressão linear brilha.
- **Exemplo LINEAR (sugestão principal):** no mesmo `linearidade.ipynb`, restringir aos **adultos** (`age >= 20`) e olhar **altura × peso** — a relação fica aproximadamente reta (pessoas mais altas tendem a pesar mais).
  - alternativa: usar o próprio Olist (`product_weight_g` × `price_adj`), que retomamos no passo seguinte.
- **Frase-chave:** "o modelo linear é uma **aproximação útil**, não uma lei da natureza".

**Passo 3 — Ponte para o nosso problema — ~4 min**

- Voltar ao **notebook principal** e mostrar o scatter **peso × `price_adj`** com a "reta no chute".
- **O que falar:** "no nosso caso, existe uma tendência crescente, mas bem **espalhada** — já um indício de que o peso **sozinho** não explicará tudo (veremos no diagnóstico)".
- **Gancho:** "qual reta é a **melhor**? é isso que o Bloco 2 resolve."

```text
NÃO-LINEAR: idade x altura   -> uma reta erra (curva de crescimento)
LINEAR:     altura x peso     -> uma reta aproxima bem
NOSSO CASO: peso x price_adj  -> tendência crescente, mas espalhada
```

### 5.2 O modelo: uma reta — 6 min

- **Objetivo:** escrever o modelo e dar significado a cada parâmetro.
- **Slide:** reta com destaque de $w$ (inclinação) e $b$ (intercepto).
- **Notebook:** célula `### O modelo: uma reta`.
- **O que falar:**
  - o modelo é uma reta: $\hat{y} = w\,x + b$;
  - $w$ = **peso**/coeficiente angular → "quanto $y$ muda quando $x$ muda";
  - $b$ = **viés**/intercepto → "valor de $y$ quando $x = 0$";
  - $\hat{y}$ ("y chapéu") = **previsão**.
- **Pergunta ao aluno:** "mudando só o $w$, a reta **gira** ou **sobe**? e mudando só o $b$?"

### 5.3 Resíduo, erro e função de custo (MSE) — 8 min

- **Objetivo:** transformar "reta boa" em uma **medida** que dá para minimizar.
- **Slide:** resíduos como segmentos verticais + fórmula do MSE.
- **Notebook:** células `### Erro, resíduo e a função de custo (MSE)` e `### Implementando a previsão e o custo`.
- **O que falar:**
  - **resíduo:** $r_i = \hat{y}_i - y_i$ (previsão − real);
  - somar resíduos crus não funciona (positivos e negativos **se cancelam**) → **elevar ao quadrado**;
  - **MSE:** $J(w,b) = \frac{1}{n}\sum_{i=1}^{n}\big(\hat{y}_i - y_i\big)^2$;
  - **ideia central:** *treinar = minimizar a função de custo*.
  - implementar no notebook `predict()` e `compute_mse()`; mostrar a referência "prever sempre a média" (MSE ≈ 1, pois o alvo foi padronizado).
- **Perguntas ao aluno:**
  - "por que ao quadrado e não o erro absoluto?" (pune mais os erros grandes);
  - "a MSE está sempre ≥ 0? quando vale 0?"

### 5.4 Intuição de derivada — 6 min

- **Objetivo:** entender **como** minimizar, sem formalismo pesado.
- **Slide:** parábola do custo com tangentes em vários pontos.
- **Notebook:** célula `### Como minimizar? A intuição de derivada`.
- **O que falar:**
  - a **derivada** mede a **inclinação** da função naquele ponto;
  - derivada **negativa** → aumentar $w$ faz o custo **descer** → **aumente** $w$;
  - derivada **positiva** → aumentar $w$ faz o custo **subir** → **diminua** $w$;
  - no **mínimo**, a derivada é **0** (a reta tangente é horizontal).
- **Pergunta ao aluno:** "se a derivada é negativa, eu devo **aumentar** ou **diminuir** o parâmetro?"

### 5.5 Gradiente — 4 min

- **Objetivo:** generalizar a derivada para vários parâmetros.
- **Slide:** "derivada → gradiente".
- **Notebook:** callout "Conceito (gradiente)" na seção da derivada.
- **O que falar:**
  - com vários parâmetros, o **gradiente** é o **vetor das derivadas parciais**;
  - ele aponta na direção de **maior crescimento** da função;
  - para **minimizar**, andamos na direção **oposta** ao gradiente.
- **Frase-chave:** "derivada é o caso de uma variável; gradiente é o caso de várias."

### 5.6 Gradient Descent — 10 min

- **Objetivo:** juntar tudo no **algoritmo de aprendizado**.
- **Slide:** os 4 passos + regra de atualização.
- **Notebook:** célula `### Gradient Descent`.
- **O que falar (algoritmo iterativo):**
  1. chute valores iniciais para $w$ e $b$;
  2. calcule o **gradiente** da função de custo;
  3. dê um **passo** na direção **oposta** ao gradiente;
  4. **repita** por várias iterações.
  - regra: $\theta \leftarrow \theta - \alpha\,\nabla_\theta J(\theta)$, onde $\alpha$ é o **learning rate** (tamanho do passo);
  - derivadas parciais do MSE:
    $$\frac{\partial J}{\partial w} = \frac{2}{n}\sum_{i=1}^{n}\big(\hat{y}_i - y_i\big)x_i, \qquad \frac{\partial J}{\partial b} = \frac{2}{n}\sum_{i=1}^{n}\big(\hat{y}_i - y_i\big)$$
- **Perguntas ao aluno:**
  - "o que acontece se o `learning_rate` for **grande demais**? e **pequeno demais**?"
  - "por que começamos de um 'chute' e não já no valor certo?"

### 5.7 Cálculo na lousa — 8 min

- **Objetivo:** desmistificar a matemática com um exemplo minúsculo, **passo a passo**.
- **Slide:** exemplo numérico (o mesmo da lousa).
- **O que escrever/falar na lousa (exemplo):**

  Dados: $(x,y) = (1, 2)$ e $(2, 4)$. Modelo simplificado $\hat{y} = wx$ (sem $b$, para focar).
  Custo: $J(w) = \frac{1}{n}\sum(\hat{y}_i - y_i)^2$, com $n = 2$.
  Gradiente: $\frac{dJ}{dw} = \frac{2}{n}\sum(\hat{y}_i - y_i)x_i$.

  1. **Chute** $w = 0$: previsões $0, 0$ → $J = \frac{(0-2)^2 + (0-4)^2}{2} = 10$;
  2. **Gradiente**: $\frac{dJ}{dw} = \frac{2}{2}\big[(0-2)(1) + (0-4)(2)\big] = -10$;
  3. **Passo** ($\alpha = 0{,}1$): $w \leftarrow 0 - 0{,}1\cdot(-10) = 1{,}0$;
  4. **Repetir**: com $w=1$, $J = \frac{(1-2)^2 + (2-4)^2}{2} = 2{,}5$; próximo passo leva $w$ para $\approx 1{,}3$...
  - **observação:** $J$ está **caindo** (10 → 2,5 → ...) e $w$ se aproxima de **2** (a inclinação "certa" da relação $y = 2x$).
- **Pergunta ao aluno:** "nesse exemplo, o que seria a resposta perfeita para $w$?"
- **Nota:** se sobrar tempo, refazer com $b$ incluído. Se faltar, deixar o exemplo como está.

### 5.8 Feature scaling — 5 min

- **Objetivo:** explicar por que padronizamos a entrada.
- **Slide:** "por que escalar?".
- **Notebook:** célula `### Um detalhe prático: escalar a feature`.
- **O que falar:**
  - `product_weight_g` vai de centenas a milhares, enquanto `price_adj` está na ordem de unidades → escalas muito diferentes fazem o GD "tropeçar" (passos gigantes numa direção, minúsculos na outra);
  - **solução:** padronizar $x_{\text{norm}} = \frac{x - \mu}{\sigma}$ (média 0, desvio 1);
  - **regra de ouro:** calcular $\mu$ e $\sigma$ **no treino** e aplicar a **mesma** transformação no teste.
- **Pergunta ao aluno:** "se eu calcular a média usando o **teste**, o que pode dar errado?" (vazamento).

### 5.9 Implementação em NumPy — 11 min

- **Objetivo:** escrever o modelo **na mão**, sem esconder a lógica.
- **Slide:** pseudocódigo das 4 funções.
- **Notebook:** `### Implementando o Gradient Descent`.
- **O que implementar (em ordem):**
  1. `predict(x, w, b)`;
  2. `compute_mse(y_true, y_pred)`;
  3. `compute_gradients(x, y_true, y_pred)`;
  4. `gradient_descent(x, y, learning_rate, epochs)` → devolve $w$, $b$ e o **histórico** de custo.
- **Formato:** Bruno digita ao vivo; **Guilherme circula**; pausa para os alunos digitarem.
- **Nota:** deixar claro que `np.dot(error, x)` é só o $\sum_i \text{erro}_i \cdot x_i$ (produto interno) — nada de mágico.
- **Pergunta ao aluno:** "por que guardamos o **histórico** de custo?" (para ver a convergência).

### 5.10 Treinamento e convergência — 5 min

- **Objetivo:** rodar o treino e **ver** o aprendizado acontecendo.
- **Slide:** gráfico de convergência.
- **Notebook:** células de treino (`learning_rate = 0.1`, `epochs = 100`) e `### Visualizando a convergência`.
- **O que falar:**
  - "rodamos o GD e o custo **cai** a cada época e depois **estabiliza**";
  - leitura esperada (com `random_state = 42`): $w \approx 0{,}38$, $b \approx 0$, MSE de **1,00 → ~0,85**;
  - mostrar também a **reta aprendida** sobre o scatter.
- **Pergunta ao aluno:** "se eu aumentar o número de épocas, o custo vai a zero? por quê?"

### 5.11 O mesmo modelo com Scikit-Learn — 4 min

- **Objetivo:** mostrar que a biblioteca **esconde** exatamente o que fizemos.
- **Slide:** 2 linhas de `LinearRegression` vs. nosso código.
- **Notebook:** célula `### O mesmo modelo com Scikit-Learn`.
- **O que falar:**
  - `model.fit(X, y)` devolve praticamente os **mesmos** $w$ e $b$ do nosso GD (~0,38 e ~0);
  - mensagem: **não é** "a biblioteca é melhor"; é entender **o que existe por trás do `fit`**.
- **Pergunta ao aluno:** "por que os números batem mesmo com métodos diferentes?"

### 5.12 Avaliação e diagnóstico — 8 min

- **Objetivo:** medir no **teste** e **interpretar** — treinar não basta.
- **Slide:** métricas explicadas + gráfico de resíduos.
- **Notebook:** `### Avaliação e diagnóstico do modelo` e `### Diagnóstico pelos resíduos`.
- **O que falar (métricas):**
  - **MSE** — pune erros grandes;
  - **MAE** — erro médio em R$ (após **inverter** a transformação);
  - **R²** — fração da variação de $y$ explicada pelo modelo (1 = perfeito; 0 = "prever sempre a média").
  - resultados esperados: MSE ≈ 0,84; MAE ≈ 0,72 (em `price_adj`); **R² ≈ 0,14**; MAE ≈ **R$ 70** na escala original;
  - **diagnóstico:** R² baixo → o peso **sozinho** explica só ~14% do preço; resíduos com padrão indicam que a reta não captura tudo (faltam variáveis).
- **Perguntas ao aluno:**
  - "R² de 0,14 é 'ruim'? depende do objetivo — o que o peso **não** captura no preço?"
  - "por que o MAE em R$ é bem maior que o MAE em `price_adj`?"

### 5.13 Recap do alvo transformado e dataset dos alunos — 4 min

- **Objetivo:** consolidar por que o alvo virou `price_adj` e entregar o dataset final.
- **Slide:** histograma antes/depois (Yeo-Johnson).
- **Notebook:** célula final do notebook (a que salva o dataset).
- **O que falar:**
  - o `price` é **muito assimétrico** (cauda longa); aplicamos **Yeo-Johnson** (+ padronização) → `price_adj`;
  - **aviso repetido:** transformação **puramente para simplificar a aula** — não é a única abordagem;
  - a **última célula** salva o dataset **original com a coluna `price` transformada**, que será o dataset usado pelos alunos em `dataset_olist_price_adj.csv`.
- **Pergunta ao aluno:** "a transformação **melhora** o modelo ou só facilita o nosso estudo? ela mudou o **R²**?"

### 5.14 Síntese — 3 min

- **Objetivo:** fechar o Bloco 2 amarrando a narrativa.
- **Slide:** checklist "o que construímos hoje".
- **O que falar (bullets):**
  - percorremos o fluxo de um projeto de dados (coleta → limpeza → EDA → features → modelo);
  - entendemos **linearidade** (com o contraexemplo idade × altura) e escrevemos $\hat{y} = wx + b$;
  - definimos a função de custo **MSE**;
  - usamos **derivada/gradiente** para aprender com **Gradient Descent**;
  - implementamos **do zero em NumPy** e comparamos com **Scikit-Learn**;
  - **avaliamos e diagnosticamos** (MSE, MAE, R², resíduos).

---

## 6. Encerramento, exercícios e próximos passos — 15 min

- **Objetivo:** sair com dever de casa claro e ponte para a Aula 2.
- **O que falar:**
  - recapitular as **perguntas para casa** (no notebook): learning rate alto/baixo, por que o peso explica pouco, por que escalamos, efeito da transformação;
  - indicar o **notebook de exercícios** da Aula 1 (praticar outros cenários);
  - mostrar o `material-auxiliar/` (Cálculo, Álgebra Linear, Estatística) para quem quiser **aprofundar**;
  - **gancho para a Aula 2:** "hoje **previmos valores**; na próxima, vamos **decidir classes** e, a partir daí, entrar em **redes neurais e IA**";
  - mencionar o **projeto pós-curso** e o **sorteio** do livro.
- **Fechamento:** agradecer, pedir **feedback rápido** (o que travou / o que gostaram) e liberar dúvidas.

---

## 7. Esboço de slides (por bloco)

**Bloco 1 — Introdução (~16 slides):**
1. Capa: curso + encontro 1.
2. "Hoje você vai treinar seu primeiro modelo".
3. Instrutores (Bruno e Guilherme — co-instrutores).
4. O que **é** / o que **não é** este curso.
5. Mapa do curso: 4 blocos / 2 aulas.
6. Estrutura do repositório.
7. O que é Ciência de Dados (+ 3 ingredientes).
8. Data Analysis × Data Engineering × Data Science (tabela).
9. IA ⊃ Machine Learning ⊃ Deep Learning.
10. O que são dados (linha × coluna).
11. O fluxo de um projeto de dados.
12. ETL vs ELT.
13. Data Cleaning (missing/duplicados/tipos/outliers).
14. EDA e visualização (collage de gráficos).
15. Feature Engineering (antes/depois).
16. Introdução ao ML (X, y, treino/teste) + Ferramentas do ecossistema.
- *A partir daqui, o slide dá lugar ao **notebook ao vivo** (seção 3.15).*

**Bloco 2 — Regressão (~18 slides):**
17. Divisor: "Bloco 2 — como um modelo aprende".
18. **Nem tudo é uma reta** (idade × altura).
19. **Quando é uma reta** (exemplo linear).
20. O modelo: $\hat{y} = wx + b$ (o que $w$ e $b$ fazem).
21. Resíduo.
22. MSE.
23. Intuição de derivada (tangentes).
24. Gradiente.
25. Gradient Descent (os 4 passos).
26. Exemplo numérico (o da lousa).
27. Feature scaling.
28. Pseudocódigo das 4 funções.
29. Convergência (gráfico).
30. Scikit-Learn (2 linhas).
31. MSE / MAE / R².
32. Resíduos (diagnóstico).
33. `price_adj` (Yeo-Johnson antes/depois).
34. Síntese + próximos passos.

> **Regra dos slides:** cada slide de conceito deve ter **1 ideia** e **1 imagem**; o texto do slide é **mínimo** (o detalhe vai na fala).

---

## 8. Roteiro de lousa (quadro)

**Bloco 2 — usar o quadro para (nesta ordem):**

1. **Linear vs não-linear** (desenho rápido):
   - esquerda: curva de idade × altura com uma reta por cima (mostrar o erro);
   - direita: nuvem de pontos com tendência reta.
2. **O modelo:** reta com $w$ e $b$ anotados; escrever $\hat{y} = wx + b$.
3. **MSE:** escrever a fórmula e desenhar 3 resíduos como segmentos.
4. **Derivada:** parábola com tangente mostrando o sinal da derivada em cada lado do mínimo.
5. **Exemplo numérico da seção 5.7:** escrever os 4 passos (chute → gradiente → passo → repetir) e recalcular na frente da turma.
6. **(Se couber) as derivadas parciais** do MSE (quadro, sem pressa).

> **Dica:** deixe o **exemplo numérico** escrito no quadro até o fim da aula — os alunos consultam durante a implementação.

---

## 9. Perguntas frequentes, objeções e armadilhas

**Perguntas prováveis da turma (e respostas curtas):**

- *"Mas isso é IA?"* → Machine Learning é uma parte da IA; hoje estamos no ML "clássico" (que sustenta boa parte da IA moderna).
- *"Preciso saber cálculo/álgebra linear?"* → **Não** para acompanhar a aula. Damos a **intuição**; o formal fica em `material-auxiliar/`.
- *"Por que começar com $w=0$ e $b=0$?"* → é só um ponto de partida; o GD funciona de qualquer ponto razoável e converge para o mínimo.
- *"Por que o erro não vai a zero?"* → porque ruído e variáveis que não estão no modelo (o peso não determina o preço inteiro).
- *"Por que o R² é baixo?"* → o peso **sozinho** explica pouca variação; modelos reais usam várias features.
- *"Por que transformar o `price`?"* → distribuição muito assimétrica; Yeo-Johnson deixa o problema mais "redondo" — e é **só para simplificar a aula**.
- *"Isso não é 'regressão linear de verdade'?"* → é: uma reta com MSE e GD. Na Aula 2 vamos ver a forma fechada como curiosidade, se der tempo.

**Armadilhas para os instrutores (evitar):**

- **Aprofundar demais** no Bloco 1 (é mapa mental, não disciplina de Engenharia de Dados).
- **Derivar a matemática completa** — o objetivo é o **mecanismo**, não a prova.
- **Estourar o tempo** na implementação: use o intervalo e o Guilherme para o socorro de Python.
- **Prometer precisão que o modelo não tem** (ex.: "vamos prever preço com precisão").
- **Usar jargão sem definir** (feature, alvo, treino/teste, loss...).
- **Deixar o notebook sem executar** — sempre rodar antes da aula em **máquina limpa**.

---

## 10. Encaixe roteiro ↔ notebook (`aula01.ipynb`)

| Roteiro | Seção / célula no notebook |
| --- | --- |
| 3.4–3.6 | `### O que é Ciência de Dados?`, `### Não é só Ciência de Dados`, `### IA, Machine Learning e Deep Learning` |
| 3.7–3.8 | `### O que são dados? E o que fazemos com eles?` |
| 3.15 (setup) | `### Preparando o ambiente` + imports |
| 3.15 (dados) | `### Carregando os dados` + `### O dataset: e-commerce Olist` |
| 3.15 (join) | `### Juntando as tabelas (JOIN)` |
| 3.11 (EDA) | `### EDA: entendendo os dados antes de modelar` |
| 3.10 (cleaning) | `### Data Cleaning: valores ausentes e outliers` |
| 3.12 / 3.13 | `### Feature Engineering e divisão treino/teste` |
| 5.13 (Yeo-Johnson) | `### Por que transformar o price? (Yeo-Johnson)` |
| 5.1 | `### Linearidade` |
| 5.2 | `### O modelo: uma reta` |
| 5.3 | `### Erro, resíduo e a função de custo (MSE)` + `### Implementando a previsão e o custo` |
| 5.4–5.5 | `### Como minimizar? A intuição de derivada` |
| 5.6 | `### Gradient Descent` |
| 5.8 | `### Um detalhe prático: escalar a feature` |
| 5.9 | `### Implementando o Gradient Descent` |
| 5.10 | `### Visualizando a convergência` + `### A reta aprendida` |
| 5.11 | `### O mesmo modelo com Scikit-Learn` |
| 5.12 | `### Avaliação e diagnóstico do modelo` + `### Diagnóstico pelos resíduos` |
| 5.13 (dataset) | última célula (salva `dataset_olist_price_adj.csv`) |
| 5.14 / 6 | `### Síntese da Aula 1` + `### Próximos passos` |

> **Nota:** o notebook é a **implementação** deste roteiro; se um tópico do roteiro não couber na aula, **corte do roteiro** — não adicione ao notebook.

---

## 11. Checklist pré-aula

**Conteúdo:**

- [ ] Notebook `aula01.ipynb` **executa do início ao fim** em máquina limpa.
- [ ] Notebook de apoio `linearidade.ipynb` roda (dataset NHANES presente).
- [ ] Slides do Bloco 1 e do Bloco 2 exportados.
- [ ] Exemplo numérico da lousa (seção 5.7) revisado.
- [ ] Exercícios da Aula 1 disponíveis.
- [ ] `dataset_olist_price_adj.csv` gerado/atualizado.

**Ambiente/evento:**

- [ ] Datasets disponíveis **offline** (backup) + links testados.
- [ ] `requirements.txt` atualizado.
- [ ] Projetor, tomadas, Wi-Fi e credenciais conferidos.
- [ ] Repositório do curso acessível (fork/PR explicados no encerramento).
- [ ] Material do **sorteio** (livro) separado.

**Pessoas:**

- [ ] Divisão Bruno/Guilherme confirmada (quem conduz cada bloco).
- [ ] Guilherme pronto para **circular** na parte de implementação.
- [ ] Cronômetro/cronograma à vista para não estourar os blocos.

---

## 12. Anexos

### 12.1 Datasets usados

| Dataset | Colunas principais | Uso |
| --- | --- | --- |
| Olist (4 CSVs em `aulas/aula01/archive/`) | `price`, `freight_value`, `product_weight_g`, `payment_value`, ... | demo + modelo da aula |
| `dataset_olist_price_adj.csv` | idem, com `price` transformado (Yeo-Johnson) | **dataset dos alunos** |
| `NHANES-2017-2018-height-weight.csv` | `age`, `weight`, `height` | exemplo de **não-linearidade** (linearidade.ipynb) |

### 12.2 Convenções de notação (usar igual no slide, na lousa e no notebook)

| Símbolo | Significado |
| --- | --- |
| $x$ | feature de entrada |
| $y$ | valor real (alvo) |
| $\hat{y}$ | previsão do modelo |
| $w$, $b$ | parâmetros (peso e viés) |
| $J(w,b)$ | função de custo |
| $\alpha$ | learning rate |
| $\nabla_\theta J$ | gradiente |

> **Lembrete de formatação:** matemática vai **solta** com `$`; **nunca** dentro de crases (isso quebra o LaTeX no Jupyter).

### 12.3 Bibliografia de apoio

- Géron — *Hands-On Machine Learning* (workflow, implementação, avaliação).
- James et al. — *An Introduction to Statistical Learning* (fundamentos estatísticos).
- Materiais auxiliares do curso: Cálculo, Álgebra Linear, Estatística (em `material-auxiliar/`).

### 12.4 Pontos a decidir (TODOs dos instrutores)

- [ ] Confirmar o **exemplo linear** da seção 5.1 (altura × peso em adultos **ou** peso × `price_adj` do Olist).
- [ ] Definir se a **forma fechada** da regressão aparece (curiosidade) ou fica só no aprofundamento.
- [ ] Escrever o **notebook de exercícios** da Aula 1.
- [ ] Produzir os **slides** a partir do esboço da seção 7.
- [ ] Sync do `aula01.ipynb` com este roteiro (o notebook pode ter evoluído).











