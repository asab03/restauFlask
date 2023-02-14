from flask import Flask, render_template, request, redirect, url_for
#from livereload import server, shell
#import json
pizza ="pizza "
kebab = "kebab "
galette = "galette "
listeplat =[]
listeaservir = []

app = Flask(__name__)



@app.route('/')
def page_index():
    return render_template('index.html')

@app.route('/commande')
def page_commande():
    plats10 = listeplat[-10:]

    plats10simple = []
    if len(listeplat) > 0:
        premier = len(listeplat) - 10

        if premier < 0:
           premier = 0

        for i in range(premier, len(listeplat)):
            plats10simple.append(listeplat[i])

    print(plats10simple)
    return render_template('commande.html', plats=plats10simple)

@app.route('/datacommande', methods=['GET', 'POST'])
def page_datacommande():
    if request.method == "POST":
        data = request.form.to_dict()

        if'btn_pizza' in data:
            listeplat.append(pizza)
        elif'btn_kebab' in data:
            listeplat.append(kebab)
        elif'btn_galette' in data:
            listeplat.append(galette)
        return redirect(url_for('page_commande'))

    return ('aie ca marche pas')


@app.route('/cuisine')
def page_cuisine():
    plat_todo=None
    plat_waiting =[]
    if len(listeplat)>0:

        plat_todo=listeplat[0]
        for i in range(1, 10):
            if i < len(listeplat):
                plat_waiting.append(listeplat[i])
            elif 'btn-terminer' in plat_todo:
                listeaservir.append(plat_todo)
    return render_template('Cuisine.html', todo=plat_todo, waiting=plat_waiting)

@app.route('/datacuisine', methods=['GET', 'POST'])
def page_datacuisine():
    if request.method == 'POST':
        data = request.form.to_dict ()
        if 'button_terminer' in data:
            if len(listeplat) > 0:
                listeaservir.append(listeplat.pop(0))

        return redirect (url_for ('page_cuisine'))

    return "aie il y a un probleme"

@app.route('/service')
def page_service():
    plat_aservir = None
    plat_waiting2 = []
    if len(listeaservir) > 0:

        plat_aservir = listeaservir[0]
        for i in range(1, 10):
            if i < len(listeaservir):
                plat_waiting2.append(listeaservir[i])
    return render_template('service.html', aservir=plat_aservir, enattente=plat_waiting2)


@app.route('/dataservice', methods=['GET', 'POST'])
def page_dataservice():
    if request.method == 'POST':
        data = request.form.to_dict()
        if 'button_termine' in data:
            if len(listeaservir) > 0:
                listeaservir.pop(0)

        return redirect(url_for('page_service'))

    return "aie il y a un probleme"


