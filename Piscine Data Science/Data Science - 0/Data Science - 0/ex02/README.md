- https://chat.openai.com/c/44d52e00-1e63-46fb-b243-22861343a0eb
- psql -U your_username -d your_database_name
```sql
-- Create the table if it doesn't exist (you can skip this step if the table already exists)
CREATE TABLE IF NOT EXISTS event_data (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price NUMERIC,
    user_id BIGINT,
    user_session UUID
);

-- Use \copy to import the data from the CSV file into the table
\copy event_data (event_time, event_type, product_id, price, user_id, user_session)
FROM '/home/mahdi/Desktop/Python-DS-ML/Piscine Data Science/Data Science - 0/assets/customer/data_2022_oct.csv' DELIMITER ',' CSV HEADER;

```