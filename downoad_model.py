#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
url="https://googledrive.com/host/0B046sNk0DhCDUk9YeklwOFczc0E/fast_rcnn_vgg_voc.model"
filename="fast_rcnn_vgg_voc.model"
#python3方法不在原来的路径了,修改为 urllib.request.urlretrieve
urllib.urlretrieve(url,filename)