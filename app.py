from flask import Flask, render_template

app = Flask(__name__)

dashboard1 = "https://public.tableau.com/app/profile/om.lakde/viz/Global_AI_Adoption_EducationDashboard1/Dashboard1"
dashboard2 ="https://public.tableau.com/app/profile/om.lakde/viz/Global_AI_Adoption_EducationDashboard2/Dashboard"
story ="https://public.tableau.com/app/profile/om.lakde/viz/Global_AI_Adoption_EducationDashboard2/Story1"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard1")
def dashboard1_page():
    return render_template(
        "dashboard1.html",
        tableau_url=dashboard1
    )


@app.route("/dashboard2")
def dashboard2_page():
    return render_template(
        "dashboard2.html",
        tableau_url=dashboard2
    )


@app.route("/story")
def story_page():
    return render_template(
        "story.html",
        tableau_url=story
    )


if __name__=="__main__":
    app.run(debug=True)