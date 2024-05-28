CREATE TABLE book_pool(
	book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_name varchar(100) NOT NULL,
    author varchar(50),
    genre VARCHAR(50),
    publisher VARCHAR(50),
    isbn VARCHAR(13),
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    added_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    summary VARCHAR(500)
);