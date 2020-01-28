# Chewz IG Downloader

## Install


```
$ python setup.py install
```


## Running


To scrape a user's media:
```bash
instagram-scraper <username> -u <your username> -p <your password>
```

To use Chewz's restaurant list locally:

```
ig_scrapper -t image --destination ./pictures --filename ./restaurant_list.txt --media-metadata --profile-metadata --retain-username
```

To upload to S3:
