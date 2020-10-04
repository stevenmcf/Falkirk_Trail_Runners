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

# CREATE

# EDIT

# UPDATE

# DELETE