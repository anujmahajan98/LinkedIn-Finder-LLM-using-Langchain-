from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["post"])
def process():
    name = request.form["name"]
    person_info, person_profile_pic = ice_break(name=name)

    return jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.topics_of_interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breakers,
            "picture_url": person_profile_pic,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080, debug=True)
