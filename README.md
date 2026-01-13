# 📘 Estudos de Python com Téo Calvo

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Progresso](https://img.shields.io/badge/Progresso-Pandas-orange)

Este repositório reúne os códigos desenvolvidos durante os estudos do **canal do Téo Calvo** no YouTube:  
➡️ [Python do básico ao Data Science](https://www.youtube.com/@teomewhy)

---

## 📑 Índice

- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Objetivo](#-objetivo)
- [Pré-requisitos](#-pré-requisitos)
- [Estrutura do Repositório](#️-estrutura-do-repositório)
- [Conteúdo](#-conteúdo)
  - [Introdução ao Python](#-introdução-ao-python)
  - [Pandas](#-pandas)
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
├── .gitignore
├── LICENSE 
└── README.md
```

### 🧭 Conforme o curso avança, novas pastas serão adicionadas, como:

```bash
Estatística/
MachineLearning/
VisualizaçãoDeDados/
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

***📍 Momento atual do estudo***

Nesta parte estão os estudos da biblioteca Pandas, focando em análise e manipulação de dados.

**Organização da pasta:**
- **data/**: Datasets utilizados nos exercícios
- **Dia\*/**: Seguindo a mesma lógica explicada em "Introdução ao Python"
- **exercicios\*/**: Exercícios disponibilizados pelo Téo, junto com o case_homicidios do ipea

---

### 🧩 Expansão Futura

Conforme os estudos avançam, novas seções serão adicionadas:

- 📊 **Estatística** → Conceitos estatísticos aplicados a dados reais
- 🤖 **Machine Learning** → Fundamentos e primeiros modelos com Scikit-learn
- 🎯 **Projeto Final** → Integração de todo o conhecimento adquirido

---

## 📊 Progresso dos Estudos

| Módulo | Status | Conclusão | Observações |
|--------|--------|-----------|-------------|
| 📘 Introdução ao Python | ✅ Concluído | 100% | Fundamentos consolidados |
| 🐼 Pandas | ✅ Concluído | 100% | Fundamentos consolidados |
| 📊 Estatística | ⏳ Não iniciado | 0% | Aguardando conclusão do Pandas |
| 🤖 Machine Learning | ⏳ Não iniciado | 0% | Próxima etapa |
| 📈 Visualização de Dados | ⏳ Não iniciado | 0% | A definir |

**Legenda:**
- ✅ Concluído
- 🔄 Em andamento
- ⏳ Não iniciado

**Última atualização:** Outubro/2025

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
