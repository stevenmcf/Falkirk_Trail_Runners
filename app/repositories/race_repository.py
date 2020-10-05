from db.run_sql import run_sql

from models.race import Race
from models.runner import Runner
import repositories.runner_repository as runner_repository

def save(race):
    sql = "INSERT INTO races (title, date, distance, elevation) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [race.title, race.date, race.distance, race.elevation,]
    results = run_sql(sql, values)
    id = results[0]['id']
    race.id = id
    return race

def select_all():
    races = []
    sql = "SELECT * from races"

    results = run_sql(sql)

    for row in results:
        race = Race(row['title'], row['date'], row['distance'],row['elevation'], row['id'])
        races.append(race)
    return races

def select(id):
    sql = "SELECT * from races WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    race = Race(result['title'], result['date'], result['distance'], result['elevation'], result['id'])
    return race

def update(race):
    sql = "UPDATE races SET (title, date, distance, elevation) = (%s, %s, %s, %s) WHERE id = %s"
    values = [race.title, race.date, race.distance, race.elevation, race.id]
    print(values)
    run_sql(sql, values)
    
    
def delete_all():
    sql = "DELETE  FROM races"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM races WHERE id = %s"
    values = [id]
    run_sql(sql, values)



