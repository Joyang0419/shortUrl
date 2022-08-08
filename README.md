# shortUrl

## Deploy
```
git clone https://github.com/Joyang0419/shortUrl.git

# 請先修改.env內的DB_HOST -> 變更為你自己的IP.

cd ./docker

# 請先安裝Docker 和 docker-compose

docker-compose up -d database
docker-compose up -d api
```

## 要在本地端跑Unit test
```
pip install -r requirements.txt
pytest tests
```

swagger doc url: http://0.0.0.0:9000/docs