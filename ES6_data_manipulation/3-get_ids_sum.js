export default function getStudentIdsSum(studentList) {
  if (!Array.isArray(studentList)) {
    return [];
  }
  return studentList.map((studentList) => studentList.id).reduce(
    (acc, current) => acc + current, 0,
  );
}
