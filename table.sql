CREATE TABLE user(
    id int auto_increment primary key,

    surname varchar(255) not null,

    username varchar(255) not null,

    password varchar(255) not null,

    email varchar(255) not null
);

create table request_log(
    id         int auto_increment primary key,

    action_url varchar(600) null,

    time       int          null,

    user_agent varchar(255) null,

    user_id    int          null,

    ip         varchar(60)  null

);