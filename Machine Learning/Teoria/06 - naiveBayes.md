# Naive Bayes
Técnica paramétrica em que assumimos que cada variável do dataset segue uma distribuição de probabilidade e esperamos que a variável resposta desloque.

Teorema:
$$P(y \mid X) = \frac{P(y)\,P(X \mid y)}{P(X)}$$


Exemplo:
Qual a probabilidade de ser diabético, dado algumas informações?
- y = Diabetes(1 = Sim; 0 = Não)
- x1 = Histórico Familiar(1 = Sim; 0 = Não)
- x2 = Acima do peso(1 = Sim; 0 = Não)
- x3 = Atividade física(1 = Sim; 0 = Não)

Usa-se o dataset para obter as respostas usando o teorema de Bayes.
