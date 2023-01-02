Title: Use latex to generate layout dataset
Date: 2022-01-08 21:00
Category: Layout Analizer
Tags: latex, article layout, ml, dataset
Author: Andrey G
Status: published
Summary: latex article sources to generate layout dataset
Lang: en
---

“Extracting Scientific Figures with Distantly Supervised Neural Networks”

Interesting idea here – it is patching latex source to generate document layout dataset.

__For example:__

if we have latex sources we can inject some latex commands and set color for title or other document part. Then document will be generated we can generate images from pdf and process these images in OpenCV to find bounding box for title text entry. So simple but we can generate big dataset in this approach.


[paper link](./papers/Extracting%20Scientific%20Figures%20with%20Distantly%20Supervised%20Neural%20Network.pdf)
