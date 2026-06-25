programa {
  funcao inicio() {
    real valor, soma = 0

    enquanto (verdadeiro) {
      escreva("Informe valor do produto: ")
      leia(valor)
      se (valor <= 0)
        pare
      soma = soma + valor
    }

    escreva("O total de produtos é: ", soma)
  }
}
