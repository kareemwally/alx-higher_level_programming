-- that script to get description of table
-- without using `DESCRIPTION` command
SELECT column_name, data_type, character_maximum_length, is_nullable
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0 '
AND table_name = 'first_table';
