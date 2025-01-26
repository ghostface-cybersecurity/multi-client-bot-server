import socketserver
import sys

containsfile = False

try:
    FILE = sys.argv[1]
    print(f'\n--Filename: {FILE}--\n')
    containsfile = True
except IndexError:
    print('\n--File not specified:--\nExample run: python3 multi-client-bor-server.py <filename>\n')

class BotHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f'Bot with IP {self.client_address[0]} sent data:')
        print(self.data)

        if containsfile:
            try:
                with open(FILE) as f:
                    commands = f.read()
                    print(f'Commands {FILE}:\n\n {commands}\n')
                self.request.sendall(commands.encode('utf-8'))
            except FileNotFoundError:
                print('File not found error')
                self.request.sendall(self.data.upper())

        else:
            self.request.sendall(self.data.upper())

if __name__ == '__main__':
    HOST, PORT = "", 8000
    tcpServ = socketserver.TCPServer((HOST,PORT), BotHandler)
    try:
        tcpServ.serve_forever()
    except:
        print('\n\nERROR')
