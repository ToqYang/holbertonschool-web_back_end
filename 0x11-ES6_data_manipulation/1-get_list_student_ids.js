// List students

const getListStudentIds = (ids) => {
  if (typeof ids !== 'object') {
    return [];
  }
  const meids = ids.map((item) => item.id);

  return meids;
};

export default getListStudentIds;
