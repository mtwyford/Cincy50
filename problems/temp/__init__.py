import check50
import check50.c

@check50.check()
def exists():
    """temp.c exists"""
    check50.exists("temp.c")

@check50.check(exists)
def compiles():
    """temp.c compiles"""
    check50.c.compile("temp.c", lcs50=True)

@check50.check(compiles)

def mum():
    """responds to input 22"""
    check50.run("./temp").stdin(22).stdout(71.6).exit()
@check50.check(mum)
      
def body():
    """responds to input 37"""
    check50.run("./temp").stdin(37).stdout(98.6).exit()
@check50.check(body)

