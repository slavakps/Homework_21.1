from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        try:
            # Чтение HTML-файла
            with open('contacts.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(html_content.encode('utf-8'))

        except FileNotFoundError:
            # Если файл не найден
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("Ошибка 404: Файл index.html не найден".encode('utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен на http://{hostName}:{serverPort}")
    print("На любой GET-запрос возвращается страница из index.html")
    print("Для остановки сервера нажмите Ctrl+C")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен")