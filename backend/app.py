from flask import Flask
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
CORS(app)

@app.route('/api')
@cross_origin()
def hello_world():
    return 'HEELO AD'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)