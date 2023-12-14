import cv2
import cv2.aruco as aruco

import numpy as np
import os
import pickle
import csv
import time
import math
from datetime import datetime
from urllib import request
from flask import Flask, request
from flask_restx import Api, Resource
from werkzeug.utils import secure_filename
import markerdetection_nyong_0802

cap = cv2.VideoCapture(0)
# Video
# cap = cv2.VideoCapture(0)
#
# print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
#
# while(True):
#     ret, frame = cap.read()    # Read 결과와 frame
#     VideoCap = True
#     if(ret) :
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # 입력 받은 화면 Gray로 변환
#
#         cv2.imshow('frame_color', frame)    # 컬러 화면 출력
#         if cv2.waitKey(1) == ord('q'):
#             break
app = Flask(__name__)
api=Api(app)

#
# @api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
# class HelloWorld(Resource):
#     def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
#         return {"hello": "world!"}



@api.route('/upload', methods=['POST'])
class uploadging(Resource):
    def post(self):
        global f
        f=request.files['files']
        f.save("./video/"+secure_filename(str(f.filename)))
        return {"isUploadingSuccess":"success"}


@api.route('/marker', methods=['GET'])
class markers(Resource):
    def get(self):
        # await uploadging()
        file_name = request.args.get('file')
        print(file_name)
        print(("./video/"+file_name+".mp4"))

        id = markerdetection_nyong_0802.markerDetection(file_name)
        # id = markerdetection_nyong_0802.markerDetection("2023-12-06_102112")
        print(id)
        return id
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

