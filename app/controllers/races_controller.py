from flask import Blueprint, Flask, render_template, redirect, request

from models.race import Race
import repositories.race_repository as race_repository
from models.race_result import Race_result
import repositories.race_result_repository as race_result_repository
import repositories.runner_repository as runner_repository

races_blueprint = Blueprint("races", __name__)

# # INDEX

@races_blueprint.route("/races")
def race():
    races = race_repository.select_all()
    return render_template("races/index.html", all_races=races)

    # create your show route that triggers the race repo select - render the template which will pass in the race object and the list of runner objects

# NEW
@races_blueprint.route("/races/new")
def new_race():
    return render_template("/races/new.html")

# now working in browser

# CREATE

@races_blueprint.route("/races", methods=["POST"])
def create_race():
    title = request.form["title"]
    date = request.form["date"]
    distance = request.form["distance"]
    elevation = request.form["elevation"]
    new_race = Race(title, date, distance, elevation, id)
    race_repository.save(new_race)
    return redirect("/races")

# EDIT

@races_blueprint.route('/races/<id>/edit')
def edit_race(id):
    race = race_repository.select(id)
    return render_template("races/edit.html", race=race)


# UPDATE

# doesnt save the update to browser/database ??? Why not !

@races_blueprint.route("/races/<id>", methods=["POST"])
def update_race(id):
    title = request.form["title"]
    date = request.form["date"]
    distance = request.form["distance"]
    elevation = request.form["elevation"]
    new_race = Race(title, date, distance, elevation, id)
    race_repository.update(new_race)
    return redirect("/races")

# SHOW RESULTS 
@races_blueprint.route("/races/<id>")
def show_results(id):
    race = race_repository.select(id)
    runners = race_repository.select_runners_by_race(id)
    results = race_result_repository.select_all()
    counter = 1
    # print(results)
    # sorted_results = results.sort()
    return render_template("/races/show.html", race=race, runners=runners, race_results=results, counter=counter)

# SHOW ALL RESULTS

@races_blueprint.route("/results")
def results():
    results = race_result_repository.select_all()
    races = race_repository.select_all()
    runners = runner_repository.select_all()
    return render_template("races/results.html", all_results=results, races=races, runners=runners)

# DELETE
# functionality in browser

@races_blueprint.route("/races/<id>/delete", methods=["POST"])
def delete_race(id):
    race_repository.delete(id)
    return redirect ("/races")

