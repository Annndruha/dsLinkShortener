from web import app
from flask import redirect, abort, request, make_response, render_template

from db_mngr import GetLink, GetUser, SetLink, linkErrors

@app.route('/')
def index():
    return redirect(location = 'http://your_domain/')

@app.route('/<alias>', methods=['GET'])
def goto(alias):
    link = GetLink(alias)
    if link != None:
        link['visits'] += 1
        return redirect(location = link['link'])
    else: 
        abort(404)

@app.route('/make/<token>', methods=['GET', 'POST'])
def make(token):
    user = GetUser(token)
    if user == None:
        abort(404)
        

    if request.method == 'POST':
        try:
            link = request.form.get('link')
        except Exception as e:
            abort(404, e)
        
        alias = request.form.get('alias')

        try:
            alias = SetLink(link,user['id'],alias)
            return render_template('make.html', link = link, alias = alias, status = 'ok')
        except linkErrors.DuplicateAliasesError:
            return render_template('make.html', link = link, alias = alias, status = 'err_already_created')
            

    elif request.method == 'GET':
        link = request.values.get('link')
        alias = request.values.get('alias')                
        return render_template('make.html', link = link, alias = alias)
            

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('error.html'), 404)     