DELIMITER //

CREATE TRIGGER open_fk_check_again
AFTER UPDATE ON users
FOR EACH ROW

BEGIN
    SET FOREIGN_KEY_CHECKS = 1;
END//

DELIMITER ;