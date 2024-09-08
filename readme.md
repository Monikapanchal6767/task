creating virtual environment  -
python -m venv webhook_env

activating the virtual env - 
webhook_env\Scripts\activate (command prompt)

run flask app - 
python app.py

mongodb - pip install pymongo


we will make a flask app for webhook -libs -  pip install Flask 

we will use the Dynamic Data Rendering: Based on the event's action (PUSH, PULL_REQUEST, or MERGE), the appropriate text is formatted and appended to the event-list HTML element.


testing using curl
'''

push - curl -X POST http://127.0.0.1:5000/webhook -H "Content-Type: application/json" -d "{\"author\": \"Travis\", \"action\": \"PUSH\", \"from_branch\": \"dev\", \"to_branch\": \"main\", \"request_id\": \"123abc\"}"

pull request - curl -X POST http://127.0.0.1:5000/webhook -H "Content-Type: application/json" -d "{\"author\": \"Travis\", \"action\": \"PULL_REQUEST\", \"from_branch\": \"feature\", \"to_branch\": \"main\", \"request_id\": \"456def\"}"

merge events - curl -X POST http://127.0.0.1:5000/webhook -H "Content-Type: application/json" -d "{\"author\": \"Travis\", \"action\": \"MERGE\", \"from_branch\": \"dev\", \"to_branch\": \"main\", \"request_id\": \"789ghi\"}"


'''

mongo db - start mongodb {open cmd and type ' mongod '  }  libs -  pip install pymongo

cd - C:\Program Files\MongoDB\Server\7.0\bin
then run - mongod --dbpath "C:\data\db"

mongod --dbpath "C:\data\db"


then Use curl to send webhook events push,pull,merge (testing using curl)



mongodb basic commands 
db
show dbs
use myDatabase
show collections
db.myCollection.find()
db.myCollection.insertOne({name: "John", age: 30})
