DELIMITER //

CREATE PROCEDURE delete_book(IN deleted_book_id INT)
BEGIN
    DELETE FROM book_pool
    WHERE book_id = deleted_book_id;
END//

DELIMITER ;