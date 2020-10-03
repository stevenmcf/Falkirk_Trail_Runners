from db.run_sql import run_sql

from models.race import Race
from models.runner import Runner
import repositories.runner_repository as runner_repository

def save(race):
    sql = "INSERT INTO races (title, distance, elevation, runner_time, runner_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [race.title, race.distance, race.elevation, race.runner_time, race.runner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    race.id = id
    return race

def select_all():
    races = []

    sql = "SELECT * from races"
    results = run_sql(sql)

    for row in results:
        races = Race(row['title'], row['distance'],row['elevation'], row['runner_time'], runner, row['id'])
        races.append(race)
    return races

def select(id):
    race = None
    sql = "SELECT * from runners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        runner = runner_repository.select(result['runner_id'])
        race = Race(row['title'], row['distance'],row['elevation'], row['runner_time'], runner, row['id'])
    return race

def update(race):
    sql = "UPDATE races SET (title, distance, elevation, runner_time, runner_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [race.title, race.distance, race.elevation, race.runner_time, race.runner.id]
    print(values)
    run_sql(sql, values)
    
    
def delete_all():
    sql = "DELETE  FROM races"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM races WHERE id = %s"
    values = [id]
    run_sql(sql, values)



