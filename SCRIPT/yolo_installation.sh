#!/bin/bash
git clone https://github.com/pjreddie/darknet
cd darknet
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/OPENMP=0/OPENMP=1/' Makefile
wget https://pjreddie.com/media/files/yolov3-tiny.weights 
./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights data/dog.jpg
make

