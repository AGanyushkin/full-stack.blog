Title: Requester Pays Buckets
Date: 2022-01-29 21:00
Category: data engineering
Tags: aws, s3, payment
Author: Andrey G
Status: published
Summary: aws s3 requester pays buckets
Lang: en
---

[TOC]

Interesting concept in AWS. You can share your data in AWS S3 but not pay for storing this data. In AWS it’s called “Requester Pays Buckets”.

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.html)

AS result for data transfer and storing will pay requester who will download these data.

It is very useful approach to store datasets in AWS S3.

# How to download data with S3 CLI

For example for arXiv.org shared data it will be:

```shell
aws s3 cp s3://arxiv/pdf/arXiv_pdf_manifest.json . --request-payer requester --profile personal
```

# Access through http

- For GET, HEAD, and POST requests, include `x-amz-request-payer : requester` in the header
- For signed URLs, include `x-amz-request-payer=requester` in the request

