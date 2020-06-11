# model settings
model = dict(
    type='FastRCNN',
    backbone=dict(
        type='ResNet_I3D',
        pretrained=None,
        pretrained2d=False,
        depth=50,
        num_stages=3,
        spatial_strides=(1, 2, 2),
        temporal_strides=(1, 1, 1),
        dilations=(1, 1, 1),
        out_indices=(2, ),
        frozen_stages=-1,
        inflate_freq=((1, 1, 1), (1, 0, 1, 0), (1, 0, 1, 0, 1, 0)),
        inflate_style='3x1x1',
        nonlocal_stages=(1, 2),
        # nonlocal_freq=((0,0,0), (0,1,0,1), (0,1,0,1,0,1)),
        nonlocal_cfg=dict(nonlocal_type="gaussian"),
        nonlocal_freq=((0, 0, 0), (0, 1, 0, 1), (0, 1, 0, 1, 0, 1), (0, 0, 0)),
        conv1_kernel_t=5,
        conv1_stride_t=1,
        pool1_kernel_t=1,
        pool1_stride_t=1,
        bn_eval=False,
        partial_bn=False,
        bn_frozen=True,
        style='pytorch'),
    shared_head=dict(
        type='ResI3DLayer',
        pretrained=None,
        pretrained2d=False,
        depth=50,
        stage=3,
        spatial_stride=2,
        temporal_stride=1,
        dilation=1,
        style='pytorch',
        inflate_freq=(0, 1, 0),
        inflate_style='3x1x1',
        bn_eval=False,
        bn_frozen=True),
    bbox_roi_extractor=dict(
        type='SingleRoIStraight3DExtractor',
        roi_layer=dict(type='RoIAlign', out_size=16, sample_num=2),
        out_channels=1024,
        featmap_strides=[16],
        with_temporal_pool=True),
    dropout_ratio=0.3,
    bbox_head=dict(
        type='BBoxHead',
        with_reg=False,
        with_temporal_pool=False,
        with_spatial_pool=True,
        spatial_pool_type='max',
        roi_feat_size=(1, 8, 8),
        in_channels=2048,
        num_classes=81,
        target_means=[0., 0., 0., 0.],
        target_stds=[0.1, 0.1, 0.2, 0.2],
        multilabel_classification=True,
        reg_class_agnostic=True,
        nms_class_agnostic=True))
# model training and testing settings
test_cfg = dict(
    train_detector=False,
    person_det_score_thr=0.85,
    rcnn=dict(
        score_thr=0.00,
        nms=dict(type='nms', iou_thr=1.0),
        max_per_img=100,
        action_thr=0.00))
