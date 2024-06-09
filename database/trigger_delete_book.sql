DELIMITER //

CREATE TRIGGER delete_book 
BEFORE DELETE ON book_pool
FOR EACH ROW

BEGIN

	DELETE FROM reservations
    WHERE reserved_book_id = OLD.book_id;

	DELETE FROM borrowed_books
    WHERE borrowed_book_id = OLD.book_id;
    
END//

DELIMITER ;