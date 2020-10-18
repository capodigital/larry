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

    def pngtoQT(self, imgseq, outname, start):
        #ffmpeg -framerate 5 -i img-%02d.png video.avi
        try:
            os.system('cmd /c "ffmpeg -framerate 25 -start_number {2} -i {0}%04d.png {1}.mp4"'.format(imgseq, outname, start))
        except Exception as e:
            self.exceptionHendler(e)
    
    def justQT(self, video):
        #ffmpeg -framerate 5 -i img-%02d.png video.avi
        try:
            name = os.path.splitext(video)[0]+'.mp4'
            os.system('cmd /c "ffmpeg -i {0} {1}"'.format(video, name))
            print('He is worth every penny.')
        except Exception as e:
            self.exceptionHendler(e)


    def exceptionHendler(self, exceptioncatch):
        print("Even a pro has a his limits: {0}".format(exceptioncatch))

if '__main__' == __name__:
    larry = Larry()
    path = r"X:\\cloud\\Dropbox\\200918_ov_cazbha_espejismos\\vfx\\_lookdev\\hporco\\in\\octodens.webm"
    # old = "m_rai_laser_020_a"
    # new = "m_rai_laser_020_a.0"
    # larry.rename(path, old, new)
    #outname = os.path.join(path, 'elnombredelQuicktime')
    #larry.pngQT(path, outname, 1001)
    larry.justQT(path)
