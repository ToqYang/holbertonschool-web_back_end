//

const updateStudentGradeByCity = (students, city, newGrades) => {
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    return [];
  }

  const studentByCity = students.filter((student) => student.location === city);

  const studentByGrade = studentByCity.map((student) => {
    const grades = newGrades.filter((note) => student.id === note.studentId);
    let grade = 'N/A';

    if (grades[0]) {
      grade = grades[0].grade;
    }

    return { ...student, grade };
  });

  return studentByGrade;
};

export default updateStudentGradeByCity;
