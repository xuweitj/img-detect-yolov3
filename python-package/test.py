import yidetector
if __name__ == '__main__':
    dec = yidetector.Detector()
    res = dec.detect('20171001_11189_376633_15068333852542.jpg')
    print(res)
