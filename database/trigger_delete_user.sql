DELIMITER //

CREATE TRIGGER delete_user 
BEFORE DELETE ON users
FOR EACH ROW

BEGIN

	DELETE FROM reservations
    WHERE reserved_user_id = OLD.user_id;

	DELETE FROM borrowed_books
    WHERE borrowed_user_id = OLD.user_id;
    
END//

DELIMITER ;