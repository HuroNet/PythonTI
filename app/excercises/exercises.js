function getAverage(scores) {
  const tam = scores.length;
  let suma = 0;
  for (let i = 0; i < tam; i++) {
    suma += scores[i];
  }
  const resultado = suma / tam;
  return resultado;
}
console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
// console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));

function getGrade(score) {
  let grade = "";
  if (score === 100) {
    grade = "A++";
  } else if (score >= 90 && score < 100) {
    grade = "A";
  } else if (score >= 80 && score < 90) {
    grade = "B";
  } else if (score >= 70 && score < 80) {
    grade = "C";
  } else if (score >= 60 && score < 70) {
    grade = "D";
  } else {
    grade = "F";
  }
  return grade;
}

console.log(getGrade(96));
console.log(getGrade(82));
console.log(getGrade(56));
