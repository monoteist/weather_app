from db_connector import db_connector, execute_query


def get_city(city_name):
    db_connector.connect()
    query = f"SELECT * FROM weather_city WHERE name = '{city_name}';"
    city = execute_query(query, fetch_all=False)
    db_connector.disconnect()
    return city
