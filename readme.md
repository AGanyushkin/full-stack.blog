
# Build and deploy

```shell
# Generate content
make clean html

# Deploy
aws.exe s3 rm --recursive s3://full-stack.blog/ --endpoint-url=https://storage.yandexcloud.net/ --profile YC
aws.exe s3 cp --recursive ./output/ s3://full-stack.blog/ --endpoint-url=https://storage.yandexcloud.net/ --profile YC

```


# Some additional links

[markdownguide](https://www.markdownguide.org/basic-syntax/)

[pelican docs](https://docs.getpelican.com/en/latest/index.html)

[pelican content](https://docs.getpelican.com/en/3.6.3/content.html)
