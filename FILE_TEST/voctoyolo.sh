#!/bin/bash
for i in `seq 1 200`;
do
        cnee --replay -f /tmp/xnee.xns --time 2  --keep-autorepeat --force-replay
done
