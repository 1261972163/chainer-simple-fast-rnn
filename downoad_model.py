#!/usr/bin/env python
# -*- coding: utf-8 -*-
#调试发现在云平台必须如下import才行
import urllib.request
#路径地址错误"https://googledrive.com/host/0B046sNk0DhCDUk9YeklwOFczc0E/fast_rcnn_vgg_voc.model"
url="https://drive.google.com/open?id=0B046sNk0DhCDNW5oMnVGaFdnWkU"
filename="fast_rcnn_vgg_voc.model"
#python3方法不在原来的路径了,修改为 urllib.request.urlretrieve
urllib.request.urlretrieve(url,filename)