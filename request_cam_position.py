import requests
import time
class Camera_requestor:
    def __init__(self):
        self.url = "http://192.168.0.110:5000/yz_json"
        self.y = 0
        self.z = 0
    def request_yz_data(self):
        r = requests.get(self.url)
        tmp = r.text.split(',')
        self.y =  int(tmp[0])
        self.z = int(tmp[1])
        print("Y: ", self.y,"Z: ", self.z)
        
    def get_Y(self):
        return self.y
    
    def get_Z(self):
        return self.z
    
