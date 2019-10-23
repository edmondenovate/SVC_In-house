from flask import Flask, render_template, request
from controllers.funcs import SVC

# create instance of a flask app
app = Flask(__name__)

# create instance of SVC
svc_init = SVC()

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form
        if data['info'] == 'init':
            result = svc_init.project_init()
            return render_template('index.html', msg=result)

        elif data['info'] == 'clean':
            res = svc_init.clean()
            return render_template("index.html", results=res)


    return render_template("index.html")


@app.route("/users", methods=['POST', 'GET'])
def branch_users():
    if request.method == 'POST':
        data = request.form
        branch_name = data['branch']

        try:
            process = svc_init.create_and_branch(branch_name)
            return render_template('users.html', results=process, branch=branch_name)

        except Exception as error:
            return (error)

    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3030)
