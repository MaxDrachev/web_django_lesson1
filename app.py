from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    
    filename = "web.html"

    def get_web_content(self):
      """метод распаковки созданного html файла"""
        with open(self.filename, "r", encoding="utf-8") as file:
            web_cont = file.read()
            return web_cont

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  
        self.send_header("Content-type", "text/html")  
        self.end_headers()  
        self.wfile.write(bytes(self.get_web_content(), "utf-8"))  


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
       webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
