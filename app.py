import streamlit as st
import snowflake.connector


snowflake_account = 'your_account_name'
snowflake_user = 'your_username'
snowflake_password = 'your_password'
snowflake_database = 'your_database_name'
snowflake_schema = 'your_schema_name'
snowflake_warehouse = 'your_warehouse_name'


def main():
    st.write("Bienvenue sur snowflake demo ")

if __name__ == '__main__':
    main()

