import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

# ========================================================Voter=============================================
class Voter(db.Model):
    __tablename__ = 'voter'

    no_ktp = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())
    password = db.Column(db.String())
    address = db.Column(db.String())
    
    def __init__(self, no_ktp, nama, password, address):
        self.no_ktp = no_ktp
        self.nama = nama
        self.password = password
        self.address = address

    def __repr__(self):
        return '<no ktp {}>'.format(self.no_ktp)
    
    def serialize(self):
        return{
            'no_ktp': self.no_ktp,
            'nama': self.nama,
            'password': self.password,
            'address': self.address
        }

# ========================================================Presiden=============================================
class Presiden(db.Model):
    __tablename__ = 'presiden'

    no_urut = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())
    
    def __init__(self, no_urut, nama):
        self.no_urut = no_urut
        self.nama = nama

    def __repr__(self):
        return '<no urut {}>'.format(self.no_urut)
    
    def serialize(self):
        return{
            'no_urut': self.no_urut,
            'nama': self.nama
        }

# ========================================================DPR=============================================
class Dpr(db.Model):
    __tablename__ = 'dpr'

    no_urut = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())
    
    def __init__(self, no_urut, nama):
        self.no_urut = no_urut
        self.nama = nama

    def __repr__(self):
        return '<no urut {}>'.format(self.no_urut)
    
    def serialize(self):
        return{
            'no_urut': self.no_urut,
            'nama': self.nama
        }