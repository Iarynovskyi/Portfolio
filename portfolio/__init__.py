from flask import Flask, render_template, abort
app = Flask(__name__)
projects = [
    {
        "name": "Habit tracking app",
        "img": "img/clear-habit-journal_gallery_hi-res_03.jpg",
        "hero": "",
        "categories": ["python", "flask", "render"],
        "slug": "habit-tracking",
    },
    {
        "name": "Portfolio app",
        "img": "img/screenshot-2023-08-24-at-7.40.44-pm-tmc7W3.webp",
        "hero": "",
        "categories": ["python", "jinja2", "html/css"],
        "slug": "portfolio",
    },
    {
        "name": "Resume Web-pog",
        "img": "img/skill-based-resume-template.png",
        "hero": "",
        "categories": ["html/css", "AJAX", "javascript"],
        "slug": "resume-web-pog",
    }
]
slug_to_project = {projects['slug']: project for project in projects}
@app.route('/')
def home():
    return render_template("home.html", projects=projects)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/projects/<string:slug>')
def projects(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])
