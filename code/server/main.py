from clashofclans import Server

server = Server()

server.debug = True
server.run_forever(host="localhost", port=4005)
