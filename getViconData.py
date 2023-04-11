from pyvicon.pyvicon import PyVicon
from enum import Enum




class StreamMode(Enum):
    ClientPull = 0
    ClientPullPreFetch = 1
    ServerPush = 2

viconClient = PyVicon()
viconClient.connect("192.168.2.221:801")
viconClient.enable_segment_data()
viconClient.enable_device_data()

r = viconClient.get_frame()
print(r)
# viconClient.set_stream_mode(StreamMode.ClientPull)
c = viconClient.get_subject_count()

pos = viconClient.get_segment_global_translation("klt02","klt02")
print ('pos: '+ str(pos))

while 1:
    viconClient.get_frame()
    # viconClient.get_segment_global_translation('moroKopf','moroKopf')
    # pos = viconClient.get_segment_global_translation("klt02","klt02")
    # print ('pos: '+ str(pos[0]/1000)+ ' '+ str(pos[1]/1000)+ ' '+ str(pos[2]/1000))
    pos = viconClient.get_segment_global_translation("cf99","cf99")
    print ('pos: '+ str(pos))
# latency -----------------
    l = viconClient.get_latency_total()
    print(l)
    lstr = "latency: |"
    for k in range(1,101):
        if k>l*1000:
            lstr = lstr + " "
        else:
            lstr = lstr + "#"
        if k%10==0:
            lstr = lstr + "|"
    print(lstr)
# latency end -----------------
print("count: "+ str(c))
