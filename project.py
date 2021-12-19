from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'Name':'Rahul',
        'Contact':'6739828660',
        'done':False,
    },
    {
        'id':2,
        'Name':'Rohit',
        'Contact':'8114411798',
        'done':False,
    }
]
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })
@app.route('/add-data',methods=['POST'])
def add_taks():
    if not request.json:
        return jsonify({
            'status':'Error',
            'message':'Please provide the data',
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',''),
        'done':False,
    }
    tasks.append(task)
    return jsonify({
        'status':'Success',
        'message':'Task added successfully',
    },200)
if __name__=='__main__':
    app.run(debug=True)