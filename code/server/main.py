from vscode import Server

server = Server()

server.run_forever(host="localhost", port=4005)
