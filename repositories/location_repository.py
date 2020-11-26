from db.run_sql import run_sql
from models.location import Location
from models.user import User

def save(location):
    sql = "INSERT INTO locations(name, category) VALUES ( %s, %s ) RETURNING id"
    values = [location.name, location.category]
    results = run_sql( sql, values )
    location.id = results[0]['id']
    return location


def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['category'], row['id'])
        locations.append(location)
    return locations


def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result['name'], result['category'], result['id'] )
    return location


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)


def users(location):
    users = []
    sql = """SELECT users.* FROM users
             INNER JOIN visits ON users.id = visits.user_id
             INNER JOIN locations ON locations.id = visits.location_id
             WHERE locations.id = %s"""

    values = [location.id]
    sql_results = run_sql(sql, values)

    for row in sql_results:
        # create object of type User class
        user = User(row['name'], row['id'])
        users.append(user)
        
    return users