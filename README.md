# DLCV-YOLOv7-EXPERIMENTS

```
python train.py --data ../datasets/pipe/data.yaml --cfg ../datasets/pipe/yolov7-tiny-ecanet-redux.yaml --weights weights/yolov7_training.pt --name pipe-eca-redux --device 0

python3 train.py --data ../datasets/pipe/data.yaml --cfg ../datasets/neudet/yolov7-tiny-ecanet-cbam-n.yaml --weights weights/yolov7_training.pt --hyp data/hyp.scratch.tiny.yaml --name pipe-eca-cbam --device 0 --epoch 200

```