## Start:
```
docker image pull dzakriev/shorturl-service
docker run -d -p 8000:80 -v app/data dzakriev/shorturl-service:latest
```