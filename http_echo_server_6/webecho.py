from twisted.internet import protocol,reactor
from twisted.protocols import basic

class HttpEchoProtocol(basic.LineReceiver):
  def __init__(self):
    self.lines=[]
  
  def lineReceived(self,line):
    self.lines.append(line)
    if not line:
      self.sendResponse()

  def sendResponse(self):
    self.sendLine("HTTP/1.1 200 OK")
    self.sendLine("")
    responseBody="You said:\r\n\r\n" + "\r\n".join(self.lines)
    self.transport.write(responseBody)
    self.transport.loseConnection()

class HTTPEchoFactory(protocol.ServerFactory):
  def buildProtocol(self, addr):
    return HttpEchoProtocol()

reactor.listenTCP(8000, HTTPEchoFactory())
reactor.run()
