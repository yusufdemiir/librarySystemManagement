DELIMITER //

CREATE TRIGGER borrow_book 
AFTER INSERT ON borrowed_books
FOR EACH ROW

BEGIN
	DECLARE eslesme BOOLEAN;
	SELECT 
		CASE 
			WHEN EXISTS (
				SELECT 1
				FROM book_pool AS bp
				WHERE bp.book_id = NEW.borrowed_book_id
                ) 
			THEN true
			ELSE false 
		END
	INTO eslesme;

	IF eslesme = true THEN
		UPDATE book_pool
		SET is_available = false
		WHERE book_id = NEW.borrowed_book_id;
	END IF;
    
END//

DELIMITER ;