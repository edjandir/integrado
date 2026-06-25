programa {
  funcao inicio() {
    inteiro alunos
    real nota, soma = 0
    escreva("Quantos alunos: ")
    leia(alunos)

    para(inteiro contador=1; contador <= alunos; contador++) {
      escreva("Qual a nota do aluno (", contador, "): ")
      leia(nota)
      soma = soma + nota
    }

    escreva("A média da turma: ", (soma/alunos))
    
  }
}
