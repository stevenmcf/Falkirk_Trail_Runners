from flask import Blueprint, Flask, render_template, redirect, request

from models.race import Race
import repositories.race_repository as race_repository

races_blueprint = Blueprint("races", __name__)

# INDEX

# HTML to be written and tested
@races_blueprint.route("/races")
def races():
    races = race_repository.select_all()
    return render_template("races/index.html", all_races=races)

# NEW

# HTML to be written and tested
@races_blueprint.route("/races/new")
def new_race():
    return render_template("/races/new.html")

# CREATE

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

