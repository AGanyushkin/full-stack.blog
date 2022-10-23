
https://docs.getpelican.com/en/latest/index.html

https://www.markdownguide.org/basic-syntax/

https://docs.getpelican.com/en/3.6.3/content.html



pelican content

pelican --listen

```bash
pelican -r -l -t ./theme
```

```bash
pelican content -t ./theme
aws s3 rm --recursive s3://full-stack.blog/ --endpoint-url=https://storage.yandexcloud.net/
aws s3 cp --recursive ./output/ s3://full-stack.blog/ --endpoint-url=https://storage.yandexcloud.net/
```
