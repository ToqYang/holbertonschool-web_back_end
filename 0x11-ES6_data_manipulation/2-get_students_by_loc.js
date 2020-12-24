// Filter based in the search of the city

const getStudentsByLocation = (students, city) => {
  const studentsLocation = students.filter(
    (student) => student.location === city,
  );

  return studentsLocation;
};

export default getStudentsByLocation;
