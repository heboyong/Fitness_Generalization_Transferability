_base_ = [
    '../../_base_/models/faster-rcnn_diff_fpn_2.1.py',
    '../../_base_/dg_setting/dg_20k.py',
    '../../_base_/datasets/cityscapes/cityscapes_aug.py'
]

detector = _base_.model
detector.roi_head.bbox_head.num_classes = 8
