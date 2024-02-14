-- ALTER DB TO CHANGE CHARACTER SET
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 
DEFAULT CHARACTER SET = utf8mb4
DEFAULT COLLATE = utf8mb4_unicode_ci;
-- ALTER THE TABLE character set ITSELF
USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE  utf8mb4_unicode_ci;
-- alter a column
USE hbtn_0c_0;
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
