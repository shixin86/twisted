from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

root=File("/home/shixin")
root.putChild("workspace", File("/home/shixin/workspace"))
root.putChild("download", File("/home/shixin/Downloads"))

factory=Site(root)

reactor.listenTCP(8000, factory)
reactor.run()
