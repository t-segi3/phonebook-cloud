docker build -t phonebook-api-service:v1 .

docker rm -f PHONEBOOK-API

docker run -d -p 32000:32000 --name PHONEBOOK-API phonebook-api-service:v1