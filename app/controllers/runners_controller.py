from flask import Blueprint, Flask, redirect, render_template, request

from models.runner import Runner
import repositories.runner_repository as runner_repository

runners_blueprint = Blueprint("runners", __name__)

# INDEX
@runners_blueprint.route("/runners")
def runners():
    runners = runner_repository.select_all()
    return render_template("runners/index.html", all_runners=runners)

# NEW
@runners_blueprint.route("/runners/new")
def new_runner():
    return render_template("/runners/new.html")
# tested and working in browser
# formatting required

# CREATE
@runners_blueprint.route("/runners/new", methods=["POST"])
def create_runner():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_runner = Runner(first_name, last_name, id)
    runner_repository.save(new_runner)
    return redirect("/runners")


# EDIT

@runners_blueprint.route('/runners/<id>/edit')
def edit_runner(id):
    runner = runner_repository.select(id)
    return render_template("runner/edit.html, runner=runner")

# UPDATE

@runners_blueprint.route("runners/<id>", methods=["POST"])
def update_runner(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_runner = Runner(first_name, last_name, id)
    runner_repository.save(new_runner)
    return redirect("/runners")

# DELETE

@runners_blueprint.route("runners/<id>/delete", methods = ["POST"])
def delete_runner(id):
    runner_repository.delete(id)
    return redirect ("/runners")
