# Enviroments no Python
- Usado quando temos ***mais de um projeto*** em uma mesma máquina e cada projeto pode ter uma ***necessidade diferente de mesmas bibliotecas***
- Pense que teremos pythons diferentes para cada ambiente
- Um python não sabe da existência do outro, então baixar uma biblioteca em um ambiente não significa que estará baixado no outro
- Podemos ter um ambiente para desenvolvimento, outro para produção, outro para testes, etc
- No vscode, para criar um ambiente com o conda, basta abrir o terminal e digitar:
```bash
conda create --name env-name python=3.
y
conda info--envs
conda activate env-name
```
> Usar "3." para pegar a última versão do python 3
- Depois de ativar o ambiente, podemos instalar as bibliotecas que quisermos, sem interferir em outros ambientes