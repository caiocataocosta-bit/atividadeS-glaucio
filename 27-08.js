let nomeAluno = "João Silva";
let nota1 = 6.5;
let nota2 = 7.0;

const mediaMinima = 7;

let media = (nota1 + nota2) / 2;
let notaRecuperacao = null;
let situacao = "";

if (media >= mediaMinima) {
    situacao = "APROVADO";
} else if (media >= 5 && media < mediaMinima) {
    situacao = "RECUPERAÇÃO";
    notaRecuperacao = 6;

    if (notaRecuperacao < 5) {
        situacao = "REPROVADO";
    } else {
        situacao = "APROVADO";
    }
} else {
    situacao = "REPROVADO";
}

console.log("Nome do aluno: " + nomeAluno);
console.log("Nota 1: " + nota1);
console.log("Nota 2: " + nota2);
console.log("Média: " + media);
if (notaRecuperacao !== null) {
    console.log("Nota de Recuperação: " + notaRecuperacao);
}
console.log("Situação do Aluno: " + situacao);