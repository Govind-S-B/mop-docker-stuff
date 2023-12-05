from flask import Flask, make_response, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


# Public
@app.route('/search', methods=['POST'])
def search():
    '''
    This is the function that the client should invoke when a request is received
    search - responsible for sending a request to the provider
    search requests for a list only and invokes the onsearch function remotely , it expects a list of catalogue items ( in this mulearn members )
    '''
    response = {'active': True}
    
    r = make_response(json.dumps(response))
    r.headers['Content-Type'] = 'application/json'
    return r

def onsearch():
    '''
    This is the function that the gateway should call inside the server of the provider
    onsearch - the function in the provider's which actually does the action

    ideally this functions result must be passed directly to the client who requested it and not via the gatway,
    for temporary measure we just pass this functions result back to search function and return it via there
    '''
    pass

@app.route('/select', methods=['POST'])
def select():
    '''
    This function is what actually retuns the details of a single item from a catalogue or list
    The client app invokes this and the gatway ( this script ) intercepts it and makes a onselect function call on the coressponding providers
    '''
    pass

def onselect():
    '''
    same purpose as above specificed , the explanation was getting redundant
    '''
    pass


if __name__ == '__main__':
    app.run(debug=True)