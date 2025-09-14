# SQL to create the table
create_table_sql = """
CREATE TABLE phone (
    phone_id INT,
    country_code INT NOT NULL,
    phone_number INT NOT NULL,
    phone_type VARCHAR(12),
    PRIMARY KEY(phone_id)
);
"""

# SQL to select rows where country_code is 'US'
select_sql = """
SELECT phone_number
FROM phone
WHERE country_code = 'US';
"""

# SQL to update rows where phone_type is 'CELLULAR'
update_sql = """
UPDATE phone
SET phone_type = 'MOBILE'
WHERE phone_type = 'CELLULAR';
"""

# SQL to delete rows where country_code is 'XX'
delete_sql = """
DELETE FROM phone
WHERE country_code = 'XX';
"""

# SQL to drop the table
drop_table_sql = "DROP TABLE phone;"

# Print all SQL statements
print(create_table_sql)
print(select_sql)
print(update_sql)
print(delete_sql)
print(drop_table_sql)
