from flask import request, redirect, flash, url_for
from flask import Flask, render_template, request
import string
import random
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect('warhammer.db')

conn.execute('CREATE TABLE rasa (id_rasy INTEGER PRIMARY KEY, jmeno TEXT NOT NULL, pocet INTEGER NOT NULL, velikost_imperia INTEGER, planeta TEXT NOT NULL)')
conn.execute('CREATE TABLE bydliste (id INTEGER PRIMARY KEY, id_rasy INTEGER NOT NULL, planeta TEXT NOT NULL)')
conn.execute('CREATE TABLE vozidla (id_vozidla INTEGER PRIMARY KEY, nazev TEXT NOT NULL, id_rasy INTEGER not NULL, rychlost INTEGER NOT NULL, styl_boje TEXT NOT NULL)')

sql1 = """INSERT INTO rasa(id_rasy, jmeno, pocet, velikost_imperia, planeta)
    VALUES 
     (1, 'lide', 100, 1000, 'zeme'),
     (2, 'ork', 2000, 3000, 'orkhome'),
     (3, 'tyranid', 75, 50, 'tyranidhome'),
     (4, 'necron', 25, 100, 'necronhome'),
     (5, 'aeldari', 10, 50, 'aeldarihome')"""

sql2 = """INSERT INTO bydliste (id_rasy, planeta)
    VALUES 
    (1, "zeme"),
    (1, "zeme2"),
    (2, "orkhome"),
    (2, "ork2home"),
    (3, "tyranidhome"),
    (3, "tyranid2home"),
    (4, "necronhome"),
    (4, "necron2home"),
    (5, "aeldarihome"),
    (5, "aeldari2home")"""

sql3 = """INSERT INTO vozidla (id_vozidla, nazev, id_rasy, rychlost, styl_boje)
    VALUES    
   (1, "knight", 1, 75, "na_blízko"),
   (6, "dreadnought", 1, 65, "na_dálku"),
   (2, "choppa", 2, 10, "na_blízko/nadálku"),
   (7, "battlewagon", 2, 100, "na_dálku"),
   (3, "neni", 3,0, "nn"),
   (4, "canoptek", 4, 75, "reanimace"),
   (8, "ark", 4, 85, "neni"),
   (5, "hornet", 5, 125, "na_blízko"),
   (9, "falcon", 5, 85, "ná_dálku")"""

@app.route("/")
def home():
    con = sqlite3.connect("informace.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM bydliste")
    print(res)
    return render_template("warhammer.html", bydliste = res)

@app.route('//', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']

        results = (search_term)
        
        return render_template('warhammer.html', results=results, search_term=search_term)
        
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        rasa = request.form['rasa']
        bydliste = request.form['bydliste']
        vozidla = request.form['vozidla']
        secret = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
        record = {'rasa': rasa, 'bydliste': bydliste, 'vozidla': vozidla, "secret": secret}
        

        flash(f'Your recipe has been added! Your secret is {secret}')
        return redirect(url_for('form'))
    else:
        return render_template('form.html')
    

@app.route('/api/recipe1', methods=['POST'], endpoint='/api/recipe1')
def api_post_recipe():
    rasa = request.args.get('rasa')
    author = request.args.get('bydliste')
    description = request.args.get('vozidla')
    ...
    
@app.route('/api/recipes')
def api_get_recipes():
   ...

@app.route('/api/recipe3', endpoint='/api/recipe3')
def api_get_recipe():
    rasa = request.args.get('rasa')
    bydliste = request.args.get('bydliste')
    ...
    

@app.route('/api/recipe4', methods=['PUT'], endpoint='/api/recipe4')
def api_put_recipe():
    rasa = request.args.get('rasa')
    bydliste = request.args.get('bydliste')  
    vozidla = request.args.get('vozidla')
    secret = request.args.get('secret')
    ...

@app.route('/api/recipe5', methods=['DELETE'], endpoint='/api/recipe5')
def api_delete_recipe():
    rasa = request.args.get('rasa')
    bydliste = request.args.get('bydliste')
    secret = request.args.get('secret')    

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True) 