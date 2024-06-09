DELIMITER //

CREATE PROCEDURE add_return_date(IN borrowing_id INT, returned_book_id INT)
BEGIN
    UPDATE borrowed_books
    SET return_date = NOW()
    WHERE borrow_id = borrowing_id;
    
    UPDATE book_pool
    SET is_available = true
    WHERE book_id = returned_book_id;
END//

DELIMITER ;