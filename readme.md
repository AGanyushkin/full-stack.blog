
# Local

```bash
make devserver
```

# Build and deploy

```shell
# Generate content
make clean html

# Deploy
aws.exe s3 rm --recursive s3://full-stack.blog/ --endpoint-url=https://storage.yandexcloud.net/ --profile YC
aws.exe s3 cp --recursive ./output/ s3://full-stack.blog/ --endpoint-url=https://storage.yandexcloud.net/ --profile YC

```

# Docker

```shell
# build image
docker build -t pelican:v1 .

# use image
docker run --rm -v G:/full-stack.blog:/data -p 9999:9999 -e SITEURL=http://127.0.0.1:9999 -e PORT=9999 -it pelican:v1 make devserver
docker run --rm -v G:/full-stack.blog:/data -it pelican:v1 make clean html
```

# Some additional links

[markdownguide](https://www.markdownguide.org/basic-syntax/)

[pelican docs](https://docs.getpelican.com/en/latest/index.html)

[pelican content](https://docs.getpelican.com/en/3.6.3/content.html)
