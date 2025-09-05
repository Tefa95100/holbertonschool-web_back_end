const http = require('http');

// Create the server
const app = http.createServer((request, response) => {
  // send response
  response.statusCode = 200;
  response.setHeader('Content-type', 'text/html');
  response.end('Hello Holberton School!');
});
// Port to listen
app.listen(1245);

module.exports = app;
