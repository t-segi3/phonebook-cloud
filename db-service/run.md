docker compose up

----------------------------------------------------------------

docker pull mysql:8.0.1

docker run -p 3306:3306 --name phonebook-sql -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0.1

docker pull phpmyadmin/phpmyadmin:latest

docker run --name phonebook-phpmyadmin -d --link phonebook-sql:db -p 8081:80 phpmyadmin/phpmyadmin