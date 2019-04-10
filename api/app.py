from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from models import Voter, Presiden, Dpr
from random import randint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user' : 'postgres',
    'pw' : 'lupalagi',
    'db' : 'evoting',
    'host' : 'localhost',
    'port' : '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# postgresql://username:password@localhost:5432/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES 

db.init_app(app)

# ========================================================USER=============================================
@app.route("/getAllVoter", methods=['GET'])
def get_all_voter():
    try:
        voter = Voter.query.order_by(Voter.no_ktp).all()
        return jsonify([vtr.serialize() for vtr in voter])
    except Exception as e:
        return (str(e))

@app.route("/getVoter/<id_>", methods=['GET'])
def get_voter_by(id_):
    try:
        voter = Voter.query.filter_by(no_ktp=id_).first()
        return jsonify(voter.serialize())
    except Exception as e:
        return(str(e))


@app.route("/addVoter", methods=['POST'])
def add_voter():
    body = request.json

    no_ktp = body['no_ktp']
    nama = body['nama']
    password = body['password']
    address = body['address']

    try:
        voter = Voter(
            no_ktp = no_ktp,
            nama = nama,
            password = password,
            address = address
            )
        db.session.add(voter)
        db.session.commit()
        return "Voter added. user id={}".format(voter.no_ktp),200

    except Exception as e:
        return (str(e)),400

@app.route("/removeVoter/<id_>", methods=['DELETE'])
def remove_voter(id_):
    try:
        voter = Voter.query.filter_by(no_ktp=id_).first()
        db.session.delete(voter)
        db.session.commit()
        return "Voter id = " + str(id_) + " deleted."
    except Exception as e:
        return (str(e))
    finally:
        db.session.close()


# ========================================================Presiden=============================================
@app.route("/getAllPresiden", methods=['GET'])
def get_all_presiden():
    try:
        presiden = Presiden.query.order_by(Presiden.no_urut).all()
        return jsonify([pres.serialize() for pres in presiden])
    except Exception as e:
        return (str(e))

@app.route("/getPresiden/<id_>", methods=['GET'])
def get_presiden_by(id_):
    try:
        presiden = Presiden.query.filter_by(no_urut=id_).first()
        return jsonify(presiden.serialize())
    except Exception as e:
        return(str(e))

# ========================================================DPR=============================================
@app.route("/getAllDpr", methods=['GET'])
def get_all_dpr():
    try:
        dpr = Dpr.query.order_by(Dpr.no_urut).all()
        return jsonify([dpr.serialize() for dpr in dpr])
    except Exception as e:
        return (str(e))

@app.route("/getPresiden/<id_>", methods=['GET'])
def get_dpr_by(id_):
    try:
        dpr = Dpr.query.filter_by(no_urut=id_).first()
        return jsonify(dpr.serialize())
    except Exception as e:
        return(str(e))

# =============================================================LOGIN=======================================
@app.route('/login', methods=['POST'])
def login():
    response = {}
    body = request.json
    no_ktp = body['no_ktp']
    password = body['password']
    isLogin = False

    try:
        voters = get_all_voter().json
        for voter in voters:
            if no_ktp == voter['no_ktp']:
                if password == voter['password']:
                    isLogin = True
                    
    except Exception as e:
        response['Error'] = str(e)
        # return str(e)
    
    if isLogin:
        response['message'] = 'Login success{}'.format(no_ktp)
        # response['token'] = 'generateToken(username)'
        code = 200

    else:
        response['message'] = 'Login failed'
        code = 400
        
    return jsonify(response), code

