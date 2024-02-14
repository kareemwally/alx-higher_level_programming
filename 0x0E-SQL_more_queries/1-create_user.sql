-- that script to create a USER with grants
CREATE USER IF NOT EXISTS
'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- giving grants
GRANT ALL
ON  *.*
TO user_0d_1@localhost;
