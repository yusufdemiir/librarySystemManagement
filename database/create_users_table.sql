CREATE TABLE users(
	user_id varchar(15) PRIMARY KEY,
    name_ varchar(50) NOT NULL,
    surname varchar(50) NOT NULL,
    password_ varchar(15) NOT NULL,
    role_ enum('Ziyaretçi','Yönetici') NOT NULL,
    tel varchar(10),
    address varchar(500),
    tc varchar(11) NOT NULL,
    UNIQUE (tc)
);