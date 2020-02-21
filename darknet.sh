#!/bin/bash
module load gcc/8.3.0
module load cuda/10.1.168
ip addr
./darknet detector train ENSTA/voc.data ENSTA/yolov3-tiny.cfg ENSTA/darknet53.conv.74 --gpus 0,1 -dont_show -mjpeg_port 8090 -map
echo fin
