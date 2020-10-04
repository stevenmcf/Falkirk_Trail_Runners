from db.run_sql import run_sql

from models.race_time import Race_time

from models.race import Race
import repositories.race_repository as race_repository

from models.runner import Runner
import repositories.runner_repository as runner_repository

def save(race_time):
    sql = "INSERT INTO race_times (race_id, runner_id, time) VALUES (%s, %s, %s) RETURNING id"
    values = [race_time.race.id, race_time.runner.id, race_time.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    race_time.id = id


def select_all():
    race_time = []
    sql = "SELECT * FROM race_times"
    results = run_sql(sql)
    for result in results:
        race = race_repository.select(result["race_id"])
        runner = runner_repository.select(result["runner_id"])
        race_time = Race_time(race, runner, time, result["id"])
        race_time.append(time)

def select(id):
    sql = "SELECT * FROM race_times WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    race = race_repository.select(result["race_id"])
    runner = runner_repository.select(result["runner_id"])
    race_time = Race_time(race, runner, time, result["id"])
    return race_time

def update(race_time):
    sql = "UPDATE race_times SET (race_id, runner_id, time) = (%s, %s) WHERE id is = %s"
    values = [race_time.race.id, race_time.runner.id, race_time.time ]
    results = run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM race_times"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM race_times WHERE id = %s"
    values = [id]
    run_sql(sql, values)


