# DLCV-YOLOv7-EXPERIMENTS

```
python train.py --data ../datasets/pipe/data.yaml --cfg ../datasets/pipe/yolov7-tiny-ecanet-redux.yaml --weights weights/yolov7_training.pt --name pipe-eca-redux --device 0

python3 train.py --data ../datasets/pipe/data.yaml --cfg ../datasets/neudet/yolov7-tiny-ecanet-cbam-n.yaml --weights weights/yolov7_training.pt --hyp data/hyp.scratch.tiny.yaml --name pipe-eca-cbam --device 0 --epoch 200

https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-seg.pt

python segment/train.py --data coco.yaml --batch 16 --weights '' --cfg yolov7-seg.yaml --epochs 300 --name yolov7-seg --img 640 --hyp hyp.scratch-high.yaml

python3 train.py --data ../datasets/breast-1/data.yaml --weights yolov7-seg.pt --cfg models/segment/yolov7-tiny-ecanet-cbam-seg.yaml --epochs 200 --device 0 --name breast-yolo-ecacbam-seg --img 640 --hyp data/hyps/hyp.scratch-high.yaml


python3 train.py --data ../datasets/weld-porosity/data.yaml --cfg cfg/training/yolov7-tiny.yaml --weights weights/yolov7_training.pt --hyp data/hyp.scratch.tiny.yaml --name weld-porosity-yolov7-tiny --device 0 --epoch 200

python3 train.py --data ../datasets/weld-porosity/data.yaml --cfg ../datasets/breast-1/yolov7-tiny-ecanet-cbam2.yaml --weights weights/yolov7_training.pt --hyp data/hyp.scratch.tiny.yaml --name weld-porosity-yolov7-tiny-ecanet-cbam --device 0 --epoch 200
```