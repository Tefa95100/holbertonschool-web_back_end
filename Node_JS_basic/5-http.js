const http = require('http');
const fs = require('fs');

const file = process.argv[2];
const header = 'This is the list of our students\n';

function countStudents(file) {
  let studentCount = 0;

  // Try read file
  return new Promise((resolve, reject) => {
    fs.readFile(file, { encoding: 'utf-8', flag: 'r' }, (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

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
      const lines = [];
      lines.push(`Number of students: ${studentCount}`);
      roles.forEach((field) => {
        lines.push(
          `Number of students in ${field}: ${roleMember[field].length}. List: ${roleMember[field].join(', ')}`,
        );
      });

      return resolve(lines.join('\n'));
    });
  });
}

const app = http.createServer((request, response) => {
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.statusCode = 200;
    response.end('Hello Holberton School!');
    return;
  }

  if (request.url === '/students') {
    if (!file) {
      response.statusCode = 200;
      response.end(`${header}Cannot load the database`);
      return;
    }

    countStudents(file).then((text) => {
      response.statusCode = 200;
      response.end(header + text);
    }).catch(() => {
      response.statusCode = 200;
      response.end(`${header}Cannot load the database`);
    });
  }
});

app.listen(1245);

module.exports = app;
