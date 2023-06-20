# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

# --------------------------------------------------------


@app.route('/get-subset')
def query_example():

    allgood = True
    # if key doesn't exist, returns None
    latitude = request.args.get('latitude')
    if latitude is None:
        allgood = False
    longitude = request.args.get('longitude')
    if longitude is None:
        allgood = False
    depth = request.args.get('depth')
    if depth is None:
        allgood = False
    radius = request.args.get('radius')
    if radius is None:
        allgood = False

    if allgood is True:
        string = '''<h1> Values from query</h1>'''
        string += '<body>'
        string += f'Latitude: {float(latitude):10.4f}<br>'
        string += f'Longitude:{float(longitude):10.4f}<br>'
        string += f'Depth:    {float(depth):10.4f}<br>'
        string += f'Radius:   {float(radius):10.4f}<br>'
        string += '</body>'
    else:
        string = '400'
    return string


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
