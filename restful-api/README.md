 HTTP Request & Response Structure

 GET /home HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Request Line: GET /home HTTP/1.1

GET is the method

/home is the path

HTTP/1.1 is the version

Headers: Provide metadata (e.g. User-Agent, Accept)

Body (Optional): Present in methods like POST, PUT

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>...actual webpage content...</html>

