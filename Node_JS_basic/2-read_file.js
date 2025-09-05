const fs = require('fs');

function countStudents(file) {
  let studentCount = 0;

  // Try read file
  try {
    const data = fs.readFileSync(file, { encoding: 'utf-8', flag: 'r' });

    // catch only no empty line
    const dataLine = data.split('\n')
      .map((line) => line.trim())
      .filter((line) => line.length > 0);

    // See if file have more one line
    if (dataLine <= 1) {
      console.log('Number of students: 0');
    }

    const roles = [];
    // Browse Csv for extract fields
    dataLine.slice(1).forEach((line) => {
      const word = line.split(',');
      const field = word[3];
      if (field && !roles.includes(field)) {
        roles.push(field);
      }
    });

    // Create array foreach roles
    const roleMember = {};
    roles.forEach((field) => {
      roleMember[field] = [];
    });

    // Add first name in array of role and count number of student
    dataLine.slice(1).forEach((line) => {
      const word = line.split(',');
      const firstname = word[0];
      const field = word[3];
      if (field && firstname) {
        roleMember[field].push(firstname);
        studentCount += 1;
      }
    });

    // Display result
    console.log(`Number of students: ${studentCount}`);
    roles.forEach((field) => {
      console.log(`Number of students in ${field}: ${roleMember[field].length}. List: ${roleMember[field].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
