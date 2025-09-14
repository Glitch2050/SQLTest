def insert_row():
    phone_id = input("Enter phone ID (integer): ")
    country_code = input("Enter country code (integer): ")
    phone_number = input("Enter phone number (integer): ")
    phone_type = input("Enter phone type (up to 12 characters): ")

    insert_sql = f"""
    INSERT INTO phone (phone_id, country_code, phone_number, phone_type)
    VALUES ({phone_id}, {country_code}, {phone_number}, '{phone_type}');
    """
    print("\nGenerated SQL INSERT statement:")
    print(insert_sql)

def select_rows():
    select_country_code = input("Enter country code to search for phone numbers: ")
    select_sql = f"""
    SELECT phone_number
    FROM phone
    WHERE country_code = {select_country_code};
    """
    print("\nGenerated SQL SELECT statement:")
    print(select_sql)

def update_rows():
    update_sql = """
    UPDATE phone
    SET phone_type = 'MOBILE'
    WHERE phone_type = 'CELLULAR';
    """
    print("\nGenerated SQL UPDATE statement:")
    print(update_sql)

def delete_rows():
    delete_country_code = input("Enter country code to delete rows: ")
    delete_sql = f"""
    DELETE FROM phone
    WHERE country_code = '{delete_country_code}';
    """
    print("\nGenerated SQL DELETE statement:")
    print(delete_sql)

def drop_table():
    confirm = input("Are you sure you want to drop the 'phone' table? Type YES to confirm: ")
    if confirm.upper() == "YES":
        drop_sql = "DROP TABLE phone;"
        print("\nGenerated SQL DROP TABLE statement:")
        print(drop_sql)
    else:
        print("Table drop cancelled.")

# Main loop
while True:
    print("\n--- SQL Statement Generator ---")
    print("1. Insert a phone number")
    print("2. Select phone number")
    print("3. Update phone number")
    print("4. Delete phone number")
    print("5. Drop the phone number table")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        insert_row()
    elif choice == "2":
        select_rows()
    elif choice == "3":
        update_rows()
    elif choice == "4":
        delete_rows()
    elif choice == "5":
        drop_table()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 6.")
