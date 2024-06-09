DELIMITER //

CREATE TRIGGER update_old_ids_saves
BEFORE UPDATE ON users
FOR EACH ROW

BEGIN
    SET FOREIGN_KEY_CHECKS = 0;

	UPDATE reservations SET reserved_user_id = NEW.user_id
	WHERE reserved_user_id = OLD.user_id;
	
	UPDATE borrowed_books SET borrowed_user_id = NEW.user_id
    WHERE borrowed_user_id = OLD.user_id;

END//

DELIMITER ;