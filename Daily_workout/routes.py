from Daily_workout.models import WorkoutPlan, get_unique_elements
from flask import (
    current_app,
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def home():
    # Retrieve the list of warm-up exercises from the session
    warmups_to_do = session.get("warmups_to_do", None)
    if warmups_to_do is None:
        warmups_to_do = []  # Set a default value if it was not found in the session

    # Retrieve the list of skill exercises from the session
    skills_to_do = session.get("skills_to_do", None)
    if skills_to_do is None:
        skills_to_do = []  # Set a default value if it was not found in the session

    # Retrieve the list of skill exercise links from the session
    skills_to_do_links = session.get("skills_to_do_links", None)
    if skills_to_do_links is None:
        skills_to_do_links = []  # Set a default value if it was not found in the session

    # Combine skills_to_do and skills_to_do_links before passing to the template
    skills_combined = zip(skills_to_do, skills_to_do_links)
    
    # Retrieve the list of strength exercises from the session
    workout_to_do = session.get("workout_to_do", None)
    if workout_to_do is None:
        workout_to_do = []  # Set a default value if it was not found in the session

    return render_template(
        "home.html",
        title="Daily Workout - Generator",
        warmups_to_do=warmups_to_do,
        skills_combined=skills_combined,
        workout_to_do=workout_to_do,
    )


@pages.route("/gen_warmup")
def generate_warmup():
    # Create an instance of the WorkoutPlan class
    workout_plan = WorkoutPlan()

    # Get a list of unique warm-up exercises
    warmups_to_do = get_unique_elements(workout_plan.warmup_exercices, 3)
    print(warmups_to_do)
    # Store the list of warm-up exercises in the session
    session["warmups_to_do"] = warmups_to_do

    # Mark the session as modified
    session.modified = True

    # Redirect to the home page
    return redirect(url_for("pages.home"))


@pages.route("/gen_skill")
def generate_skill():
    # Create an instance of the WorkoutPlan class
    workout_plan = WorkoutPlan()

    # Get a list of unique skill exercises
    skills_to_do = get_unique_elements(workout_plan.skill_exercices_list, 3)

    # Create a list to store the links corresponding to the selected skill exercises
    skills_to_do_links = []

    # Iterate over the selected skill exercises and retrieve their links from the dictionary
    for skill in skills_to_do:
        skills_to_do_links.append(workout_plan.skill_exercices.get(skill))

    # Store the lists in the session
    session["skills_to_do"] = skills_to_do
    session["skills_to_do_links"] = skills_to_do_links
    session.modified = True

    # Redirect to the home page
    return redirect(url_for("pages.home"))


@pages.route("/gen_strength")
def generate_strength():
    # Create an instance of the WorkoutPlan class
    workout_plan = WorkoutPlan()

    # Get a list with a randomly selected set of strength exercises
    workout_to_do = get_unique_elements(workout_plan.strength_fundamentals, 1)

    # Store the selected set of strength exercises in the session
    session["workout_to_do"] = workout_to_do

    # Mark the session as modified
    session.modified = True

    # Redirect to the home page
    return redirect(url_for("pages.home"))

@pages.route("/refresh")
def refresh():
    session.pop("warmups_to_do", None)

    skills_to_do = session.pop("skills_to_do", None)

    skills_to_do_links = session.pop("skills_to_do_links", None)

    workout_to_do = session.pop("workout_to_do", None)

    # Redirect to the home page
    return redirect(url_for("pages.home"))