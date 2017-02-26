# coding=utf-8
from __future__ import print_function
import threading
import math
from resources import QueueResources, DictResources

locatingMessageQueue = QueueResources.locatingMessageQueue
spectrumDict = DictResources.spectrumDict
locationDict = DictResources.locationDict


# 定位线程类
class Locator(object):
    def getLoacatingMessage(self, muMac='B4:0B:44:2F:C8:A2'):
        global locatingMessageQueue
        global locationDict
        messageDict = locatingMessageQueue.get()

        message = messageDict.get(muMac, -1)
        print(message)
        res = [-1, -1]

        if message != -1:
            # print message
            locationID = self.getLocation(message)
            cord = locationDict[locationID]
            res[0] = round(cord['X'],2)
            res[1] = round(cord['Y'],2)
        return res

    # 使用NN(Nearest Neighbour)方法计算定位结果
    def getLocation(self, message):
        # print 'locating start'
        self.minDist = 1000.
        self.locationID = 0
        global spectrumDict
        for location in spectrumDict.keys():
            spectrumItem = spectrumDict[location]
            rssiPairList = []
            # 由于指纹库中对于缺失数值填的是-100，对于实际采样缺失的数值，也应该填补-100
            for ap in spectrumItem.keys():
                if ap in message.keys():
                    rssiPairList.append((message[ap][0], spectrumItem[ap][0]))
                else:
                    rssiPairList.append((-100, spectrumItem[ap][0]))
            dist = self.euclidDist(rssiPairList)
            # print dist, '\n'
            if dist < self.minDist:
                self.locationID = location
                self.minDist = dist
        locationID = self.locationID
        self.locationID = 0
        self.minDist = 1000.
        return locationID

    # 计算信号强度向量之间的欧几里德距离
    def euclidDist(self, rssiPairList):
        powSum = 0.
        for pair in rssiPairList:
            x, y = pair
            powSum += pow((int(x) - int(y)), 2)
        return math.sqrt(powSum)
