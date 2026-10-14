CREATE DATABASE bcknd;

CREATE USER bcknd@'localhost' IDENTIFIED BY 'bcknd';

GRANT ALL PRIVILEGES FROM bcknd.* TO bkcnd@'localhost';

FLUSH PRIVILEGES;