from yidetector import darknet
import os
import operator

MODULE_REAL_DIR = os.path.dirname(os.path.realpath(__file__))


class Detector(object):
    def __init__(self, net_cfg_file=None, net_weights_file=None, meta_file=None):
        # file name in unicode
        if net_cfg_file is None:
            net_cfg_file = MODULE_REAL_DIR + '/yolov3-voc.cfg'
        if net_weights_file is None:
            net_weights_file = MODULE_REAL_DIR + '/yolov3-voc.weights'
        if meta_file is None:
            meta_file = MODULE_REAL_DIR + '/voc.data'
        self.net = darknet.load_net(net_cfg_file.encode('utf8'), net_weights_file.encode('utf8'), 0)
        self.meta = darknet.load_meta(meta_file.encode('utf8'))

    def detect(self, img_pth):
        # img_pth in unicode
        res = darknet.detect(self.net, self.meta, img_pth.encode('utf8'))
        resr = {}

        def trans(cord):
                x = cord[0]
                y = cord[1]
                w = cord[2]
                h = cord[3]
                x1 = round(x - w/2)
                x2 = round(x + w/2)
                y1 = round(y - h/2)
                y2 = round(y + h/2)
                cord = [x1, x2, y1, y2]
                return cord

        for i in res:
                cls, p, cord = i
                cls = bytes.decode(cls)
                if cls not in resr:
                        resr[cls] = []
                resr[cls].append([p]+trans(cord))
        for cls in resr:
                resr[cls].sort(key=operator.itemgetter(0), reverse=True)
        return resr
