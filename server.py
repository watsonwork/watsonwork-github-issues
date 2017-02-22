from github_app import app

app.run(host='0.0.0.0', port=int(app.config['PORT']), debug=True)
