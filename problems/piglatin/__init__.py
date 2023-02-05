import check50
import check50.c

@check50.check()
def exists():
    """piglatin.c exists"""
    check50.exists("piglatin.c")

@check50.check(exists)
def compiles():
    """piglatin.c compiles"""
    check50.c.compile("piglatin.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()
