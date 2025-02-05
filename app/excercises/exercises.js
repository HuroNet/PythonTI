function getAverage(scores) {
  const tam = scores.length;
  let suma = 0;
  for (let i = 0; i < tam; i++) {
    suma += scores[i];
  }
  const resultado = suma / tam;
  return resultado;
}
// console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
// // console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));

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

// console.log(getGrade(96));
// console.log(getGrade(82));
// console.log(getGrade(56));

function hasPassingGrade(score) {
  const grade = getGrade(score);
  let result;
  if (grade !== "F") {
    result = true;
  } else {
    result = false;
  }
  return result;
}

// console.log(hasPassingGrade(100));
// console.log(hasPassingGrade(53));
// console.log(hasPassingGrade(87));

function studentMsg(totalScores, studentScore) {
  const average = getAverage(totalScores);
  const grade = getGrade(studentScore);
  const passed = hasPassingGrade(studentScore);

  if (passed === false) {
    return `Class average: ${average}. Your grade: ${grade}. You failed the course.`;
  } else {
    return `Class average: ${average}. Your grade: ${grade}. You passed the course.`;
  }
}
// console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89,667], 37));

const palindromo = (string) => {
  let original = string.toLowerCase().replace(/[^a-z0-9]/g, "");
  let invertida = original.split("").reverse().join("");
  if (original === invertida) {
    return "palindromo";
  } else {
    return "negado";
  }
};

console.log(palindromo("hola"));

console.log(palindromo("AmoLaPAl oma"));
console.log(palindromo("amolapaloma"));
