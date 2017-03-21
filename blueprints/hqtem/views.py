
from hqlf.blueprints.hqtem import hqteam

@hqteam.route("/info", methods=['GET'])
def info():
    page = request.args.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    return render_template('HQteam_%d.html'%(page))