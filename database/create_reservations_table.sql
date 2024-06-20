CREATE TABLE reservations(
	reserve_id INT PRIMARY KEY AUTO_INCREMENT,
    reserved_user_id VARCHAR(15),
    CONSTRAINT fk_reserved_user FOREIGN KEY (reserved_user_id) REFERENCES users(user_id),
    reserved_book_id INT,
    CONSTRAINT fk_reserved_book FOREIGN KEY (reserved_book_id) REFERENCES book_pool(book_id),
    reserve_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status_ ENUM("Beklemede", "Uygun") NOT NULL DEFAULT "Beklemede",
    queue_no INT
);