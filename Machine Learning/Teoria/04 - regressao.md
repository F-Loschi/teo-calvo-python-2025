# Regressão
Quando queremos prever um valor.

* *Relembrando*: Em *y = a + bx*:
    - y: Função
    - a: constante de deslocamento, fazendo a reta subir ou descer
    - b: constante de angulação, mexendo no ângulo da reta

Ao fazer uma regressão, tentamos encaixar uma reta em um gráfico de dispersão e ao fazer isso, não conseguiremos encaixar a reta perfeitamente ao gráfico, assim, geramos um erro.

- **Erro**: Diferença entre o que estamos estimando e o que aconteceu de verdade:
$$
Erro = y_i - \hat{y}_i
$$
- Erro quadrático:
$$
Erro\ Quadrático = (y_i - \hat{y}_i)^2
$$
- Soma do Erro Quadrático:
$$
\text{Soma do Erro Quadrático} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$
- Minímos Quadrados: Queremos minimizar a soma do erro quadrático
