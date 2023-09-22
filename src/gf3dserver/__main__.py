from . import create_app

app = create_app()

# # run app in debug mode on port 5000
app.run(debug=True, port=5000, threaded=False)