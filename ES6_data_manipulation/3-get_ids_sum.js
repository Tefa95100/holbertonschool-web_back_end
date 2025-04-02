export default function getStudentIdsSum(studentList) {
  if (!Array.isArray(studentList)) {
    return [];
  }
  return studentList.reduce((acc, studentList) => acc + studentList.id, 0);
}
