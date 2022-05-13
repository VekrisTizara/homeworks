from flask import Flask
from flask import render_template, request, redirect, url_for
from plant_form import PlantForm
from http import HTTPStatus
from models import Plant, db
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from os import getenv
from flask_migrate import Migrate


app = Flask(__name__)

CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJECT_PATH)


db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return render_template("home.html", text="Hello Plant!")

@app.route("/about/")
def about():
    return render_template("./about.html", text="The author of this site just loves plants")

@app.route("/add_plant/", methods=["GET", "POST"], endpoint="add_plant")
def add_plant():
    form = PlantForm()
    if request.method == "GET":
        return render_template("plants/add.html", form=form)

    if not form.validate_on_submit():
        app.logger.warning("errors found in request:", str(form.errors))
        return render_template("plants/add.html", form=form), HTTPStatus.BAD_REQUEST

    print("request if fine...")

    plant_name = form.data["name"]
    plant_type = form.data["type"]
    plant = Plant(name=plant_name, type=plant_type)

    db.session.add(plant)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"could not save plant, probably name {plant_name!r} is not unique")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save plant, unexpected error")

    plant_url = url_for("plants_list", plant_id=plant.id)
    return redirect(plant_url)

@app.get("/plants_list/", endpoint="plants_list")
def plants_list():
    plants = Plant.query.all()
    app.logger.warning(plants)
    for i in plants:
        app.logger.warning(i.name)
    return render_template("plants/plants_list.html", plants=enumerate(plants))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
