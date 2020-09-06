# Docker for PHP

Let's make an apache server for php and mysql database.
Following [this tutorial](https://youtu.be/_mwWxgfZ7Zc)

### php-apache

Here is `docker-compose.yml` file:

```yml
version: '3.8'
services:
  web:
    image: php:7.4-apache
    container_name: php74
    volumes:
      - ./php:/var/www/html/
    ports:
      - 8000:80
```

Then run `docker-compose up` command.
The php files go into `./php` directory.


### Set up MYSQL

Update `docker-compose.yml` to include MySQL.

```yml
version: '3.8'
services:
  web:
    build:
      context: ./php
      dockerfile: Dockerfile
    container_name: php74
    depends_on:
      - db
    env_file: .env
    volumes:
      - ./php:/var/www/html/
    ports:
      - 8000:80
  db:
    container_name: mysql8
    image: mysql:8.0
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    env_file: .env
    ports:
      - 6033:3306
```

Now use `Dockerfile` to install mysqli to use mysql in php.
The `Dockerfile` goes to `./php` directory:

    FROM php:7.4-apache
    RUN apt-get update && apt-get upgrade -y
    RUN docker-php-ext-install mysqli
    EXPOSE 80

The MYSQL User name, password and etc goes into `.env` file.
Put the `.env` into `.gitignore` if you are using `git`.
An example of `.env` would be following:

```shell
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=test_db
MYSQL_USER=devuser
MYSQL_PASSWORD=devpass
```

Use the mysql in php like this: (example of `./php/index.php` file):

```php
<?php

$host = 'db'; // service name from docker-compose.yml
$user = getenv("MYSQL_USER");
$password = getenv("MYSQL_PASSWORD");
$db = getenv("MYSQL_DATABASE");

$conn = new mysqli($host, $user,$password, $db);
if($conn->connect_error) {
    echo 'connection failed' . $conn->connect_error;
}
echo 'Sucessfully connected to MYSQL';

?>
```
