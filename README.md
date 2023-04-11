# pyvicon
Minimal python 3 wrapper over Vicon Datastream SDK. It keeps the SDK structure and naming convention
as much as possible.

### Tested with OS :
- Ubuntu 16.04 LTS

### Tested with Vicon SDK :
- 1.7.0

Download Vicon Datastream SDK [here](https://www.vicon.com/downloads/utilities-and-sdk/datastream-sdk).

put 
    ViconDataStreamSDK_CPPTest.cpp, 
    DataStreamClient.h,
    libboost_system-mt.so.1.58.0
    libboost_thread-mt.so.1.58.0
    libViconDataStreamSDK_CPP.so
in the same folder (pyvicon) where pyvicon.cpp and pyvicon.py 
#Put the .cpp and .h in pyvicon folder.
#Put the library (.so) somewhere accessible for your os #(ex: /usr/local/lib).

### Install
```
sudo python3 setup.py install

correct the path in the loadLib.sh to the folder where you added the Vicon SDK libraries.
```
### Test
run
. loadLib.sh
python3 getViconData.py

you should see the latency now.

### TODO
- Implement less "popular" functions

### Contribution
Always welcome!


