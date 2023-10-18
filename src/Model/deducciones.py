from config.db import db, app, ma

class Deducciones(db.Model):
    __tablename__ = "deducciones"

    IDDeduccion = db.Column(db.Integer, primary_key=True)
    TipoDeduccion = db.Column(db.String(255))
    MontoDeduccion = db.Column(db.Numeric(10, 2))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, TipoDeduccion, MontoDeduccion, IDEmpleado):
        self.TipoDeduccion = TipoDeduccion
        self.MontoDeduccion = MontoDeduccion
        self.IDEmpleado = IDEmpleado

with app.app_context():
    db.create_all()

class DeduccionesSchema(ma.Schema):
    class Meta:
        fields = ('IDDeduccion', 'TipoDeduccion', 'MontoDeduccion', 'IDEmpleado')
