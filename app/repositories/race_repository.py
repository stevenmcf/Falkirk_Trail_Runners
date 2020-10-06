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
    # Bring the race in
    sql = "SELECT * from races WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    race = Race(result['title'], result['date'], result['distance'], result['elevation'], result['id'])
  
    return race

def select_runners_by_race(id):
      # Bring the runners in from that race
    # sql query that selects the runners from the runners table - inner joins your race results table where the race_id = id
    sql = "SELECT runners.*, race_results.time FROM runners INNER JOIN race_results ON race_results.runner_id = runners.id WHERE race_results.race_id = %s ORDER BY race_results.time"
    # runners = loop through and create a runner object for each result coming back
    values = [id]
    results = run_sql(sql,values)
    runners = []
    for result in results:
        runner = Runner(result["first_name"], result["last_name"], result['id'])
        runners.append(runner)
    return runners

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



