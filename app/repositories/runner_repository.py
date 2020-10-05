from db.run_sql import run_sql

from models.runner import Runner
from models.race import Race

def save(runner):
    sql = "INSERT INTO runners (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [runner.first_name, runner.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    runner.id = id
    return runner

def select_all():
    runners = []

    sql = "SELECT * from runners"
    results = run_sql(sql)

    for row in results:
        runner = Runner(row['first_name'], row['last_name'], row['id'])
        runners.append(runner)
    return runners

def select(id):
    sql = "SELECT * from runners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    # if result is not None:
    runner = Runner(result['first_name'], result['last_name'], result['id'])
    return runner

# Tested and works in python3 debugger

def update(runner):
    sql = "UPDATE runners SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [runner.first_name, runner.last_name, runner.id]
    print(values)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM runners"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM runners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def races(runner):
    races = []
    sql = "SELECT * from races WHERE runner_id = %s"
    values = [runner.id]
    results = run_sql(sql, values)

    for row in results:
        race = Race(row['title'], row['distance'], row['elevation'], row['runner_id'], row['id'])
        races.append(race)
    return races
