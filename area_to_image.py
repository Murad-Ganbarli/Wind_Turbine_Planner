import urllib
from PIL import Image
from io import BytesIO
from API import api_key
import pytesseract
from os import getcwd
LAT_MAX=1000
LON_MAX=1000
import geopy.distance
EARTH_RADIUS=6378137
import math
A=4*math.pi*EARTH_RADIUS**2

def no_imagery(image_path=getcwd()+ '/images/area.png' , keys=['no imagery' , 'imagenery' , "Sony, we hava no imagery"]):
    img = Image.open(image_path).convert('RGB') 
    text = pytesseract.image_to_string(img)
    for key in keys:
        if(key in text):
            return True
    return False
def area_to_image(n, s, w,e,      view='satellite', ZOOM_MAX=20 , LAT_MAX=LAT_MAX, LON_MAX=LON_MAX):
    center= ((s+n)/2 , (w+ e)/2 )
    latdif =geopy.distance.geodesic( (s ,0   ), (   n , 0)).km
    longdif=geopy.distance.geodesic( ( 0, w) ,   (0 ,  e)) .km
    def dif_to_float_pixel(latdif, longdif):
        ratio=latdif/longdif
        global side
        if(ratio <1):
            side=longdif
            return LON_MAX*ratio, LON_MAX
        else:
            side=latdif
            return LAT_MAX , LAT_MAX/ratio

    pixels_y, pixels_x=dif_to_float_pixel(latdif , longdif)
    area=latdif*longdif
    zoom=min( ZOOM_MAX ,int(math.log2(A/area)))

    #print(zoom)
    url='http://maps.google.com/maps/api/staticmap?'+'center='+str(float(center[0]))+'%2C'+str(float(center[1]))+'&zoom='+str(zoom)+'&size='+str(int(pixels_y))+'x'+str(int(pixels_x))+"&maptype="
    url = url+view+'&sensor=false&scale=1'+'&key='+api_key
    print(url)
    f=urllib.request.urlopen(url)
    img=Image.open(BytesIO(f.read()))
    img.save(getcwd()+'/images/area.png')
    if(no_imagery(getcwd()+'/images/area.png')):
        area_to_image(n,s,w,e, ZOOM_MAX=ZOOM_MAX-1)
if __name__=='__main__':
    s , n= 39.7 , 39.8074
    w, e= 46.7 , 46.7930
    area_to_image(n, s, w, e , ZOOM_MAX=20)