from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__perfil__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Perfil|(db.Model)

    biblio = db.Column(db.String(1000))
    
    def __init__(self,foto,bibliografia,**kwargs):
        super(perfil, self).__init__(**kwargs)
        self.foto = foto
        self.biblio = bibliografia

    def get_foto(self):
        return self.foto
    def set_foto(self, nova_foto):
        self.foto = nova_foto

    def get_biblio(self):
        return self.biblio
    def set_biblio(self, nova_biblio):
        self.biblio = nova_biblio
        
db.create_all()
db.session.add()
