python3 -m http.server -b 0.0.0.0 9999 -d .

---------------------------------

docker build -t phonebook-ui-service:v1 .

docker rm -f PHONEBOOK-UI

docker run -d -p 8888:9999 --name PHONEBOOK-UI phonebook-ui-service:v1