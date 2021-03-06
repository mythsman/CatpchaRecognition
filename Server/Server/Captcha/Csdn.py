#coding=utf-8
from Captcha import Captcha
from Cnn import Cnn
import Util
class Csdn(Captcha):
    
    def __init__(self):
        super(Csdn,self).__init__("csdn")
        self.comment='CSDN论坛'
        self.url='https://passport.csdn.net/ajax/verifyhandler.ashx'
        self.suffix=".jpg"
        self.width=32
        self.height=32
        
    def splitImage(self, img):
        img = Util.resize(img, 100, 20)
        img = Util.otsu(img)
        #img = Util.closing(img,3)
        imgT = img[0:1 ,0:1]
        img1 = img[0:20, 6:26]
        img2 = img[0:20, 26:46]
        img3 = img[0:20, 43:63]
        img4 = img[0:20, 60:80]
        img5 = img[0:20, 80:100]
        img1=Util.resize(img1,32,32)
        img2=Util.resize(img2,32,32)
        img3=Util.resize(img3,32,32)
        img4=Util.resize(img4,32,32)
        img5=Util.resize(img5,32,32)

        return [img1, img2, img3, img4,img5]
        
if  "__main__" == __name__:
    csdn = Csdn()
    csdn.preprocess()
    cnn = Cnn()
    cnn.load(csdn)
    cnn.genLmdb()
    cnn.train(4000)
    #cnn.predictDir()
