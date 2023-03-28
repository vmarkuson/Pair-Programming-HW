from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friends_dict = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        tname = form["tname"]
        aname = form["aname"]
        pname = form["pname"]
        classification = form["read"]
        activities = form.getlist("activities")  # this is a PYthon list
        acquisition = form["Acquisition"]

        print(tname)
        print(aname)
        print(pname)
        print(classification)
        print(activities)
        print(acquisition)

        activities_string = ", ".join(activities)  # make the Python list into a string

        friend_dict = {
            "tname": tname,
            "aname": aname,
            "pname": pname,
            "classification": classification,
            "activities": activities_string,
            "acquisition": acquisition,
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)