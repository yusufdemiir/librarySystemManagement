CREATE TABLE borrowed_books(
	borrow_id INT PRIMARY KEY AUTO_INCREMENT,
    borrowed_book_id int,
    CONSTRAINT fk_borrowed_book FOREIGN KEY (borrowed_book_id) REFERENCES book_pool(book_id),
    borrowed_user_id varchar(7),
    CONSTRAINT fk_borrowed_user FOREIGN KEY (borrowed_user_id) REFERENCES users(user_id),
    borrowed_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP
);