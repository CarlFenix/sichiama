from flask import Flask  ,jsonify ,request
from flask_cors import CORS      
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app) 


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/sichiama'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)

class Postulante(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    edad=db.Column(db.Integer)
    email=db.Column(db.String(100))
    def __init__(self,nombre,edad,email):
        self.nombre=nombre
        self.edad=edad
        self.email=email

with app.app_context():
    db.create_all()

class PostulanteSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','edad','email')

Postulante_schema=PostulanteSchema()
Postulantes_schema=PostulanteSchema(many=True)


@app.route('/Postulantes',methods=['GET'])
def get_Postulantes():
    all_Postulantes=Postulante.query.all()
    result=Postulantes_schema.dump(all_Postulantes)

    return jsonify(result)


@app.route('/Postulantes/<id>',methods=['GET'])
def get_Postulante(id):
    Postulante=Postulante.query.get(id)
    return Postulante_schema.jsonify(Postulante)


@app.route('/Postulantes/<id>',methods=['DELETE'])
def delete_Postulante(id):
    Postulante=Postulante.query.get(id)
    db.session.delete(Postulante)
    db.session.commit()
    return Postulante_schema.jsonify(Postulante)

@app.route('/Postulantes', methods=['POST'])
def create_Postulante():
    nombre=request.json['nombre']
    edad=request.json['edad']
    email=request.json['email']
    new_Postulante=Postulante(nombre,edad,email)
    db.session.add(new_Postulante)
    db.session.commit()
    return Postulante_schema.jsonify(new_Postulante)

@app.route('/Postulantes/<id>' ,methods=['PUT'])
def update_Postulante(id):
    Postulante=Postulante.query.get(id)
    Postulante.nombre=request.json['nombre']
    Postulante.edad=request.json['edad']
    Postulante.email=request.json['email']

    db.session.commit()
    return Postulante_schema.jsonify(Postulante)
 

if __name__=='__main__':  
    app.run(debug=True, port=5000)
