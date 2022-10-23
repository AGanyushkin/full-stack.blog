Title: CV labelling tools
Date: 2022-09-01 00:01
Category: machine_learning
Tags: computer vision, dataset, object detection, segmentation
Author: Andrey G
Status: published
---

It’s a quick note about tools which I’m using for creation datasets.

The goal: I would like to have a tool or tools to create datasets for computer vision models.

My requirements for these tools:

1. Should support object detection and segmentation problems
2. Should work offline on my PC (windows, possible mac)
3. The ability to create databases for Mask R-CNN, U-Net, YoloX models
4. Will be great to avoid payments 🙂

# Which tools acceptable for me:

- [https://github.com/wkentaro/labelme](https://github.com/wkentaro/labelme)
   Nice offline tool. Can be installed
```shell
conda create --name=labelme python=3
conda activate labelme
pip install labelme

labelme --help
```
   Export to COCO & Masks
   [https://github.com/wkentaro/labelme/tree/main/examples/instance_segmentation](https://github.com/wkentaro/labelme/tree/main/examples/instance_segmentation)

- [https://supervise.ly/](https://supervise.ly/)
   It is online service and not so intuitive to use but has free plan and can be used for quick prototyping. Can export dataset as COCO or masks.

- [https://labelbox.com/](https://labelbox.com/)
   Online, but flexible labelling editor which can be configured for any purposes. Has free plan. Not so easy export procedure.

- still in search

   🙂

# Other tools:
A list of awesome data labelling tools

[https://github.com/heartexlabs/awesome-data-labeling](https://github.com/heartexlabs/awesome-data-labeling)
