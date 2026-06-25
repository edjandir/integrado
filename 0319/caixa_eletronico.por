programa {
  funcao inicio() {
    real valor, saldo = 0
    inteiro opcao

    enquanto(verdadeiro) {
      escreva("\n[1]- Ver Saldo\n[2]- Depositar\n[3]- Sair\n")
      leia(opcao)

      se (opcao == 1)
        escreva("Seu saldo é: ", saldo)
      senao
        se (opcao == 2) {
          escreva("Valor a depositar: ")
          leia(valor)
          saldo = saldo + valor
        }
        senao
          pare
    }
  }
}
