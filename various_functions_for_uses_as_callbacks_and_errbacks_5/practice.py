from twisted.internet.defer import Deferred

def callback1(result):
  print "callback1 said:", result
  return result

def callback2(result):
  print "callback2 said:", result

def callback3(result):
  raise Exception("callback 3")

def errback1(failure):
  print "errback1 had an error on", failure
  return failure

def errback2(failure):
  raise Exception("errback 2")

def errback3(failure):
  print "errback3 took care of", failure
  return "Everything is fine now."

"""
d=Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.callback("test")
"""

"""
d=Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3)
d.callback("test")
"""

"""
d=Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3)
d.addErrback(errback3)
d.callback("test")
"""

"""
d=Deferred()
d.addErrback(errback1)
d.addErrback(errback3)
d.errback("test")
"""

#未完待续
d=Deferred()
d.addErrback(errback2)
d.errback("Test")
