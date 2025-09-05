const http = require("node:http");

//Create the server
http.createServer((request, response) => {
	//Reception of the request
	let body = [];
	request.on("data", chunk => {
		body.push(chunk);
	}).on("end", () => {
		body = Buffer.concat(body).toString();
		//response
		response.end("Hello Holberton School!");
	});
})
//Port to listen
.listen(1245);
