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

# Cant get to work - speak to grown up tomorrow. 


def select_all():
    race_results = []
    sql = "SELECT * FROM race_results ORDER BY time"
    results = run_sql(sql)
    for result in results:
        race = race_repository.select(result["race_id"])
        runner = runner_repository.select(result["runner_id"])
        race_result = Race_result(race, runner, result["time"], result["id"])
        race_results.append(race_result)
    return race_results

# return a race result sorting by time, displaying runners.
# def show_results_for_Races()
#     sql = "SELECT runners.* FROM races INNER JOIN race_results ON race.id = race_results.race_id INNER JOIN runners ON race_results.runner_id = runners.id


# def show_results_by_race(race_id):
#     sql = "SELECT race_results.* FROM race_results WHERE race_id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     race_result = Race_result(result["race"], result["runner"], result["time"], result["id"])
#     return race_result

#     (Pdb) race_result_repository.show_results_by_race()
#     *** AttributeError: module 'repositories.race_result_repository' has no attribute 'show_results_by_race'

# def show_results_by_runner(runner_id):
#     sql = "SELECT race_results.* FROM race_results WHERE runner_id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     race_result = Race_result(result["race"], result["runner"], result["time"], result["id"])
#     return race_result

    # (Pdb) race_result_repository.show_results_by_runner(3)
    # *** AttributeError: module 'repositories.race_result_repository' has no attribute 'show_results_by_runner'

# def select(id):
#     sql = "SELECT * FROM race_results WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     # race = race_repository.select(result["race_id"])
#     # runner = runner_repository.select(result["runner_id"])
#     race_result = Race_result(result["race_id"], result["runner_id"], result["time"], result["id"])
#     return race_result

#   race_result_repository.select(2)
#   returns the following in Pdb
#     # *** KeyError: 'race'

# def update(race_result):
#     sql = "UPDATE race_results SET (race_id, runner_id, time) = (%s, %s, %s) WHERE id is = %s"
#     values = [race_result.race.id, race_result.runner.id, race_result.time ]
#     results = run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM race_results"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM race_results WHERE id = %s"
    values = [id]
    run_sql(sql, values)


