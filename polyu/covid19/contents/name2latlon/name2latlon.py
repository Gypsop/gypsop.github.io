# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:27:26 2020

@author: Gypsop
"""
import geocoder
import time

request_result = []
location_list = open("深圳_14天以上.txt", "r", encoding='UTF-8').read().split("\n")#["香港理工大学", "红磡站", "旺角"]#
for each_location in location_list:
    print("Currently processing " + each_location + ", waiting for 1 second(s) for a long-term using...")
    time.sleep(1)
    print("End waiting, go on processing!")
    latlon = geocoder.google(each_location, key = "AIzaSyDHHFp4x6vKyYcyf_GKiJ8c2E9ygpsklds").latlng
    print("Resuest result:", latlon)
    if latlon == None:
        request_result.append([])
    else:
        request_result.append([each_location] + latlon)