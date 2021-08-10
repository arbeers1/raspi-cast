from flask import Flask, jsonify, render_template, request
import sys
sys.path.append(sys.path[0] + '/src/')
from src.remote import Remote

remote = Remote()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/youtube')
def youtube():
    remote.youtube()
    return jsonify(result='success')

@app.route('/search')
def search():
    return render_template('netsearch.html',
            img1='', shw1='', desc1='',
            img2='', shw2='', desc2='',
            img3='', shw3='', desc3='',
            img4='', shw4='', desc4='',
            img5='', shw5='', desc5=''
            )

@app.route('/shows', methods=['POST'])
def shows():
    result = remote.search_show(request.form['search'])['results']
    images = []
    shows = []
    descriptions = []
    for x in range(len(result)):
        images.append(result[x]['img'])
        shows.append(result[x]['title'])
        descriptions.append(result[x]['synopsis'])
    while(len(images) < 5):
        images.append('')
        shows.append('')
        descriptions.append('')
    return render_template('netsearch.html',
            img1=images[0], shw1=shows[0], desc1=descriptions[0],
            img2=images[1], shw2=shows[1], desc2=descriptions[1],
            img3=images[2], shw3=shows[2], desc3=descriptions[2],
            img4=images[3], shw4=shows[3], desc4=descriptions[3],
            img5=images[4], shw5=shows[4], desc5=descriptions[4]
            )



