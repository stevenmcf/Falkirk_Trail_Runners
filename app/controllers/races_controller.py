from flask import Blueprint, Flask, render_template, redirect, request

from models.race import Race
import repositories.race_repository as race_repository

races_blueprint = Blueprint("races", __name__)

# # INDEX
# @races_blueprint.route("/races")
# def races():
#     races = race_repository.select_all()
#     return render_template("/races/index.html")

@races_blueprint.route("/races")
def race():
    races = race_repository.select_all()
    return render_template("races/index.html", all_races=races)

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

# HTML to be written and tested

@races_blueprint.route('/races/<id>/edit')
def edit_race(id):
    race = race_repository.select(id)
    return render_template("race/edit.html", race=race)


# UPDATE



# DELETE

# HTML to be written and tested

@races_blueprint.route("/races/<id>/delete", methods = ["POST"])
def delete_runner(id):
    races_repository.delete(id)
    return redirect ("/races")

