from flask import Flask, render_template
from database import load_menu_using_category_and_id

app = Flask(__name__)


@app.route('/')
def main_menu():
  return render_template('mainpage.html')


# When user clicks the fork-knife symbol on the main page, it goes to recipeindex.html page. recipeindex.html inturn calls menulist.html page to list the menu, where it shows the recipes in dropdown boxes
@app.route('/recipeindex')
def show_recipe_index():
  return render_template("recipeindex.html")


# Once user clicks on any of the recipes, it goes to menupage.html to show the ingredients and method to cook
@app.route('/<category>/<recipeid>')
def show_recipes(category, recipeid):
  recipes = load_menu_using_category_and_id(category, recipeid)
  if not recipes:
    return "Not Found", 404
  return render_template("menupage.html", recipe=recipes)


# When user clicks on the gender symbol on the main page, it goes to aboutme.html page where it shows my history :)
@app.route('/aboutme')
def about_me():
  return render_template("aboutme.html")


# When user clicks on the writepad symbol on the main page, it goes to tamilpoems.html where you can find some of my tamil poems :)
@app.route('/tamilpoems')
def tamil_poems():
  return render_template("tamilpoems.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
