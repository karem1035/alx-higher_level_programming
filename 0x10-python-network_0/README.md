- What a URL is

  - Uniform Resource Locator (URL)

- What HTTP is

  - it is a protocol that defines how data is going to be transmitted between web servers and clients

- How to read a URL

  - There are 4 parts in a URL
  - _protocol_://_hostname_:_port_/_path-and-file-name_

  1. _Protocol_: The application-level protocol used by the client and server, e.g., HTTP, FTP, and telnet.
  2. _Hostname_: The DNS domain name (e.g., `www.nowhere123.com`) or IP address (e.g., 192.128.1.2) of the server.
  3. _Port_: The TCP port number that the server is listening for incoming requests from the clients.
  4. _Path-and-file-name_: The name and location of the requested resource, under the server document base directory.

- The scheme for a HTTP URL

  - `http://`

- What a domain name is

  - it is an alternative readable name to the IP address of the server hosting the website

- What a sub-domain is

  - it is a prefix attached to a domain name, forming a new domain within the larger parent domain. It allows for the organization and segmentation of website content or services

- How to define a port number in a URL

  - `protocol://domain:port/path`

- What a query string is

  - it is a part of the URL comes after the ? character contains a key, value pair of the data has been sent from the web server. each key, value pair separated with &

- What an HTTP request is

  - A request sent from the browser after the TCP connection to the data

- What an HTTP response is

  - A response from the web server to the browser sent the request with the data request or the error messaeg

- What HTTP headers are

  - it is a meta data sent with the http request or response contains more data about the HTTP itself

- What the HTTP message body is

  - The body of the http request or response that contains that caries the actual data

- What an HTTP request method is

  - Each HTTP request contains a method that specifies the action the client want to perform on the web serve Ex. GET POST PUT DELETE

- What an HTTP response status code is

  - it is a three digit code number returned by the server in the HTTP response to the HTTP request made by the client, it indicates the outcome of the request has been sent

- What an HTTP Cookie is

  - it is a data that gets stored at the browser's local storage by the web server, it is used to enhance the overall experience of the client on the website via remembering preferences like language, location...

- How to make a request with URL

  - `response = requests.get(url)`
