from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    """ Starting state of the webpage """
    return render_template("index.html")


@app.route("/choose_page", methods = ['POST'])
def page_handler():
    """
    Choose the template of the page
    """

    switcher = request.form.get("info")
    
    if switcher == "Про скло":
        return render_template("template1.html", sorting_image1 = "paper1.jpg", sorting_image2 = "paper2.jpg")

    elif switcher == "Про папір":
        return render_template("template1.html", sorting_image1 = "glass1.jpg", sorting_image2 = "glass2.jpg")

    elif switcher == "Пластик":
        return render_template("template1.html", sorting_image1 = "plastic1.jpg", sorting_image2 = "plastic2.jpg")

    else:
        return render_template("template1.html", sorting_image1 = "metal1.jpg", sorting_image2 = "metal2.jpg")



if __name__ == "__main__":
    app.run(debug=False)