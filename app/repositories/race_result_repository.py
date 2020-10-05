from db.run_sql import run_sql

from models.race_result import Race_result

from models.race import Race
import repositories.race_repository as race_repository

from models.runner import Runner
import repositories.runner_repository as runner_repository

def save(race_result):
    sql = "INSERT INTO race_results (race_id, runner_id, time) VALUES (%s, %s, %s) RETURNING id"
    values = [race_result.race.id, race_result.runner.id, race_result.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    race_result.id = id


def select_all():
    race_result = []
    sql = "SELECT * FROM race_results"
    results = run_sql(sql)
    for result in results:
        race = race_repository.select(result["race_id"])
        runner = runner_repository.select(result["runner_id"])
        race_result = Race_result(race, runner, time, result["id"])
        race_result.append(time)

def select(id):
    sql = "SELECT * FROM race_results WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    race = race_repository.select(result["race_id"])
    runner = runner_repository.select(result["runner_id"])
    race_result = Race_result(race, runner, time, result["id"])
    return race_result

def update(race_result):
    sql = "UPDATE race_results SET (race_id, runner_id, time) = (%s, %s, %s) WHERE id is = %s"
    values = [race_result.race.id, race_result.runner.id, race_result.time ]
    results = run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM race_results"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM race_results WHERE id = %s"
    values = [id]
    run_sql(sql, values)


