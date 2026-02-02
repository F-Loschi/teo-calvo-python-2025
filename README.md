# 📘 Estudos de Python com Téo Calvo

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Progresso](https://img.shields.io/badge/Progresso-MachineLearning-orange)

Este repositório reúne os códigos desenvolvidos durante os estudos do **canal do Téo Calvo** no YouTube:  
➡️ [Python do básico ao Data Science](https://www.youtube.com/@teomewhy)

---

## 📑 Índice

- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Objetivo](#-objetivo)
- [Pré-requisitos](#-pré-requisitos)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Conteúdo](#-conteúdo)
  - [Introdução ao Python](#-introdução-ao-python)
  - [Pandas](#-pandas)
  - [Estatística](#-estatística)
  - [Machine Learning](#-machine-learning)
- [Progresso dos Estudos](#-progresso-dos-estudos)
- [Como Utilizar](#-como-utilizar)
- [Recursos Úteis](#-recursos-úteis)
- [Créditos](#-créditos)
- [Licença](#-licença)

---

## 🚀 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- Bibliotecas principais:
  - `pandas`
  - `numpy`
  - `matplotlib`

---

## 🎯 Objetivo

- Consolidar os conhecimentos de Python do **nível básico ao avançado**
- Criar uma base sólida para trabalhar com **Data Science**
- Ter um repositório de fácil consulta e revisão dos conteúdos estudados

---

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- **Python 3.8 ou superior** → [Download aqui](https://www.python.org/downloads/)
- **Anaconda** (recomendado) → [Download aqui](https://www.anaconda.com/download)
- **Editor de código** (recomendado):
  - [VS Code](https://code.visualstudio.com/)
  - [PyCharm](https://www.jetbrains.com/pycharm/)
  - [Jupyter Notebook](https://jupyter.org/) (já incluso no Anaconda)
- **Git** → [Download aqui](https://git-scm.com/)

### 📦 Instalação das Dependências

Após clonar o repositório, instale as bibliotecas necessárias:

**💡 Usando Anaconda (recomendado):**

```bash
# Criar ambiente conda
conda create -n teo-python python=3.11

# Ativar ambiente
conda activate teo-python

# Instalar dependências
conda install pandas numpy matplotlib
```

**Ou usando pip padrão:**

```bash
pip install pandas numpy matplotlib
```

**Ou usando um ambiente virtual (venv):**

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install pandas numpy matplotlib
```

---

## 🗂️ Estrutura do Repositório

A organização do repositório segue a progressão natural do curso, indo do **básico de Python** até **Data Science, Estatística e Machine Learning**.

Cada pasta principal representa um módulo de aprendizado, e dentro de cada módulo há subdivisões por **dia de estudo** ou **tema específico**.

### 🌳 Estrutura Atual

```bash
CURSOPYTHON2025/
├── Introdução ao Python/
│   ├── Desafio/
│   ├── Dia*/
│   └── Exercicios/
│ 
├── Pandas/
│   ├── data/
│   ├── Dia*/ 
│   └── Exercicios/
│
├── Estatistica/
│    └── Téo_Stats.pdf
│
├── Machine Learning/
│    ├── data/
│    ├── Dia*/
│    ├── Teoria/ 
│
├── .gitignore
├── LICENSE 
└── README.md
```

---

## 📚 Conteúdo

### 📘 Introdução ao Python

**[Playlist no YouTube](https://www.youtube.com/watch?v=OeKzVjiiRm4&list=PLvlkVRRKOYFSpRkqnR0p2A-eaVlpLnN3D)**

Esta pasta contém os primeiros passos com a linguagem, baseados no material introdutório do curso do Téo Calvo.

**Tópicos abordados:**
- Sintaxe básica
- Tipos de dados
- Estruturas condicionais e de repetição
- Manipulação de listas e dicionários
- Criação de funções
- Manipulação de arquivos
- Como consumir APIs
- O que são os Environments e para que servem
- Dict Comprehension

**Organização da pasta:**
- **Desafio/**: Exercício de desafio da Loteria da Babilônia
- **Dia\*/**: A playlist é gravada pelas lives que o Téo faz na Twitch. Os vídeos, mesmo que separados por tópicos, são postados por cada dia de live. Cada dia não necessariamente é uma matéria diferente, mas sim um dia de live diferente.
- **Exercícios/**: Exercícios feitos ao longo dos dias

---

### 🐼 Pandas

**[Playlist no YouTube](https://www.youtube.com/watch?v=9Cw7iIjFlBc&list=PLvlkVRRKOYFQHnDhjTmXLEz3HU5WTgOcF)**

Nesta parte estão os estudos da biblioteca Pandas, focando em análise e manipulação de dados.

**Organização da pasta:**
- **data/**: Datasets utilizados nos exercícios
- **Dia\*/**: Seguindo a mesma lógica explicada em "Introdução ao Python"
- **exercicios\*/**: Exercícios disponibilizados pelo Téo, junto com o case_homicidios do ipea

---

### 📊 Estatística

**[Playlist no YouTube](https://www.youtube.com/watch?v=4CcgZXXIl7o&list=PLvlkVRRKOYFQGIZdz7BycJet9OncyXlbq)**

Nesta pasta, encontram-se os estudos voltados para a análise estatística de dados, fundamentais para a tomada de decisão e modelagem preditiva.

**Destaque do Material:**

📝 Téo_Stats.pdf: Este arquivo é o coração desta seção. Ele contém as anotações detalhadas da matéria, incluindo fórmulas explicadas, conceitos teóricos e a base necessária para aplicar estatística em Python.

Tópicos abordados:

**Estatística Descritiva (Medidas de tendência central e dispersão)**

**Distribuições de Probabilidade**

**Testes de Hipóteses**

---

### 🤖 Machine Learning

***📍 Momento atual do estudo***

**[Playlist no YouTube](https://www.youtube.com/playlist?list=PLvlkVRRKOYFR6_LmNcJliicNan2TYeFO2)**

Nesta seção encontram-se os estudos sobre modelos preditivos e algoritmos de aprendizado de máquina, utilizando principalmente a biblioteca Scikit-Learn.

Organização da pasta:

 - data/: Conjuntos de dados utilizados para treinamento e teste dos modelos.

 - semana01/: Notebooks e scripts desenvolvidos durante as lives, seguindo a cronologia dos estudos.

 - Teoria/: Documentação, conceitos fundamentais (como viés, variância, overfitting e métricas de avaliação) e a base matemática dos algoritmos.

---

### 🧩 Expansão Futura

Conforme os estudos avançam, novas seções serão adicionadas:

- 🎯 **Projeto Final** → Integração de todo o conhecimento adquirido

---

## 📊 Progresso dos Estudos

| Módulo | Status | Conclusão | Observações |
|--------|--------|-----------|-------------|
| 📘 Introdução ao Python | ✅ Concluído | 100% | Fundamentos consolidados |
| 🐼 Pandas | ✅ Concluído | 100% | Fundamentos consolidados |
| 📊 Estatística | ✅ Concluído | 100% | Fundamentos consolidados |
| 🤖 Machine Learning | 🔄 Em andamento | 48% | Naive Bayes |
| 📈 Visualização de Dados | ⏳ Não iniciado | 0% | A definir |

**Legenda:**
- ✅ Concluído
- 🔄 Em andamento
- ⏳ Não iniciado

**Última atualização:** Janeiro/2026

---

## 📌 Como Utilizar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/F-Loschi/teo-calvo-python-2025.git
   ```

2. **Entre na pasta do projeto:**
   ```bash
   cd teo-calvo-python-2025
   ```

3. **Execute os scripts Python:**
   ```bash
   python nome_do_arquivo.py
   ```

---

## 🙌 Créditos

Todo o conteúdo de estudo foi baseado no canal do [Téo Calvo](https://www.youtube.com/@teomewhy).

Este repositório serve apenas como material de estudo pessoal.

---

## 🔗 Recursos Úteis

### 📚 Documentação Oficial
- [Python 3 Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

### 🎓 Materiais Complementares
- [Real Python](https://realpython.com/) - Tutoriais e artigos sobre Python
- [Kaggle Learn](https://www.kaggle.com/learn) - Cursos práticos de Data Science
- [Python Tutor](https://pythontutor.com/) - Visualização de execução de código
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - Comunidade para dúvidas

### 🎥 Outros Canais Recomendados
- [Téo Me Why](https://www.youtube.com/@teomewhy) - Canal principal
- [Téo Me Why - Lives](https://www.twitch.tv/teomewhy) - Lives na Twitch
- [Kaggle](https://www.youtube.com/@Kaggle) - Data Science e ML

### 🛠️ Ferramentas Úteis
- [Anaconda Navigator](https://www.anaconda.com/) - Gerenciador de ambientes e pacotes Python
- [Google Colab](https://colab.research.google.com/) - Notebooks Python na nuvem
- [Jupyter](https://jupyter.org/) - Ambiente interativo para Python
- [DBeaver](https://dbeaver.io/) - Gerenciador de bancos de dados

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar como referência nos seus estudos!
