CREATE TABLE book_pool(
	book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_name varchar(100) NOT NULL,
    author varchar(100),
    genre VARCHAR(50),
    publisher VARCHAR(50),
    isbn VARCHAR(13),
    UNIQUE(isbn),
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    added_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    summary VARCHAR(500)
);