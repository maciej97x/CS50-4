CREATE TABLE "user"(
    "id" int "auto_increment" primary key,

    "surname" varchar(255) not null,

    "username" varchar(255) not null,

    password varchar(255) not null,

    "email" varchar(255) not null
);
