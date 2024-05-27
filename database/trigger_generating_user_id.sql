DELIMITER //
CREATE TRIGGER generate_user_id BEFORE INSERT
ON users
FOR EACH ROW
BEGIN
	DECLARE ziyaretci_sayisi INT;
	DECLARE yonetici_sayisi INT;
    
    SELECT COUNT(*) INTO yonetici_sayisi
    FROM users
    WHERE role_ = 'Yonetici';
    
    SELECT COUNT(*) INTO ziyaretci_sayisi
    FROM users
    WHERE role_ = 'Ziyaretci';

	IF NEW.role_ = 'Ziyaretci' THEN
    SET NEW.user_id = CONCAT('Z', LPAD(ziyaretci_sayisi + 1, 6, '0'));
    ELSE
    SET NEW.user_id = CONCAT('Y', LPAD(yonetici_sayisi + 1, 6, '0'));
    END IF;
END//
DELIMITER ;