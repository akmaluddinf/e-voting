from flask import Flask, jsonify, request, json, make_response, abort
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from models import Voter, Presiden, Dpr
from random import randint
from flask_cors import CORS
from functools import wraps

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

def verifyLogin(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(403)
        # isTrue = False
        # if (isTrue) :
            # return "login gagal"
        # tokennya ditaro di headers dgn keyword "Bearer" spasi token makanya di bawah di-slice
        # token = request.headers["Authorization"][7:]
        # data = (decode(token))
        # username = decrypt(data["data"])
        # g.username = username
        return  f(*args, **kwargs)
    return decoratedFunction


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


# =======================================================LOGIN============================
@app.route('/login', methods=['POST'])
def login():
    body = request.json

    no_ktp = body['no_ktp']
    password = body['password']
    
    isLogin = False

    response = {}
    errorCode = 404

    try:
        all_voter = get_all_voter().json
        for voter in all_voter:
            # print(no_ktp, voter['no_ktp'], password, voter['password'])
            # print((no_ktp, voter['no_ktp'], no_ktp == voter['no_ktp']))
            # print(password == voter['password'])
            
            if no_ktp == voter['no_ktp'] and password == voter['password']:
                dataVoter = voter
                isLogin = True
                break

    except Exception as e:
        return str(e), 400
    
    if isLogin:
        response['data'] = dataVoter
        response['pesan'] = "Berhasil login"
        response['error'] = False
        errorCode = 200

    else:
        response['error'] = True
        response['pesan'] = "Gagal login"
        errorCode = 403
    
    return jsonify(response), errorCode


@app.route("/addVoter", methods=['POST'])
def add_voter():
    body = request.json

    no_ktp = body['no_ktp']
    nama = body['nama']
    password = body['password']
    alamat = body['alamat']

    try:
        voter = Voter(
            no_ktp = no_ktp,
            nama = nama,
            password = password,
            alamat = alamat
            )
        db.session.add(voter)
        db.session.commit()
        return "Voter added. user id={}".format(voter.no_ktp),200

    except Exception as e:
        return (str(e)),400


# ========================================================Presiden=============================================
@app.route("/getAllPresiden", methods=['GET'])
@verifyLogin
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


@app.route('/addPresiden', methods=["POST"])
def add_presiden():

        body = request.json
        
        no_urut = body['no_urut']
        nama = body['nama']

        try:
                presiden = Presiden(
                no_urut = no_urut,
                nama = nama
                )

                db.session.add(presiden)
                db.session.commit()
                return "Calon Presiden bertambah. No. Urut={}".format(presiden.no_urut), 200

        except Exception as e:
                return(str(e)), 400


@app.route('/pilihPresiden', methods=['POST'])
@verifyLogin
def pilihPresiden():
    body = request.json
    no_ktp = body['no_ktp']
    response = {}
    
    try:
        voter = get_voter_by(no_ktp).json

        if voter['pilihan_presiden'] is None:
            pesan = "Berhasil memilih Capres, Suara Sah!"
            pilihan_presiden = {
                'pilihan_presiden' : body['pilihan_presiden']
            }
            db.session.query(Voter).filter_by(no_ktp = no_ktp).update(pilihan_presiden)
            db.session.commit()
            response['status'] = "Berhasil"
        else:
            pesan = "Anda sudah melakukan voting Capres sebelumnya, Suara Tidak Sah!"
            response['status'] = "Gagal"

        response['pesan'] = pesan
        
        return jsonify(response), 200
    except Exception as e:
        
        return str(e), 400


@app.route('/hasilVotingPresiden', methods=['GET'])
def hasilVotingPresiden():
    response = {}
    data = []

    try: 
        semuaCapres = Presiden.query.all()
        for pilihan_presiden in semuaCapres:
            calon = {}
            suara = Voter.query.filter_by(pilihan_presiden = pilihan_presiden.no_urut).all()
            calon['nama'] = pilihan_presiden.nama
            calon['jumlah_suara'] = len(suara)
            data.append(calon)

        response['data'] = data
        return jsonify(response), 200
        
    except Exception as e:
        return str(e), 400



# ========================================================DPR=============================================
@app.route("/getAllDpr", methods=['GET'])
@verifyLogin
def get_all_dpr():
    try:
        dpr = Dpr.query.order_by(Dpr.no_urut).all()
        return jsonify([dpr.serialize() for dpr in dpr])
    except Exception as e:
        return (str(e))

@app.route("/getDpr/<id_>", methods=['GET'])
def get_dpr_by(id_):
    try:
        dpr = Dpr.query.filter_by(no_urut=id_).first()
        return jsonify(dpr.serialize())
    except Exception as e:
        return(str(e))


@app.route('/addDpr', methods=["POST"])
def add_dpr():

        body = request.json
        
        no_urut = body['no_urut']
        nama = body['nama']

        try:
                dpr = Dpr(
                no_urut = no_urut,
                nama = nama
                )

                db.session.add(dpr)
                db.session.commit()
                return "Calon DPR bertambah. No. Urut={}".format(dpr.no_urut), 200

        except Exception as e:
                return(str(e)), 400


@app.route('/pilihDPR', methods=['POST'])
@verifyLogin
def pilihDPR():
    body = request.json
    no_ktp = body['no_ktp']
    response = {}

    try:
        voter = get_voter_by(no_ktp).json

        if voter['pilihan_dpr'] is None:
            pesan = "Berhasil memilih DPR, suara sah!"
            dpr = {
                'pilihan_dpr' : body['pilihan_dpr']
            }
            db.session.query(Voter).filter_by(no_ktp = no_ktp).update(dpr)
            db.session.commit()
            response['status'] = "Berhasil"
        else:
            pesan = "Anda sudah melakukan voting DPR sebelumnya, suara tidak sah!"
            response['status'] = "Gagal"

        response['pesan'] = pesan

        return jsonify(response), 200
    except Exception as e:
        
        return str(e), 400

@app.route('/hasilVotingDPR', methods=['GET'])
def hasilVotingDPR():
    response = {}
    data = []

    try: 
        semuaCalonDpr = Dpr.query.all()
        for pilihan_dpr in semuaCalonDpr:
            calon = {}
            suara = Voter.query.filter_by(pilihan_dpr = pilihan_dpr.no_urut).all()
            calon['nama'] = pilihan_dpr.nama
            calon['jumlah_suara'] = len(suara)
            data.append(calon)

        response['data'] = data
        return jsonify(response), 200
    except Exception as e:
        return str(e), 400
