import os

class Larry():
    def __init__(self):
        """
        This should have something, right?
        """
        
    def rename(self, path, old, new):
        try:
            for file in os.listdir(path):
                oldfile = os.path.join(path, file)
                newfile = os.path.join(path, file.replace(old, new))
                os.rename(oldfile, newfile)
        except Exception as e:
            self.exceptionHendler(e)

    def exceptionHendler(self, exceptioncatch):
        print("Even a pro has a his limits: {0}".format(exceptioncatch))

if '__main__' == __name__:
    larry = Larry()
    path = r""
    old = ""
    new = ""
    larry.rename(path, old, new)


