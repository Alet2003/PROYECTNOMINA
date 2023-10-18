from config.db import db, app, ma

class Pagos(db.Model):
    __tablename__ = "pagos"

    IDPago = db.Column(db.Integer, primary_key=True)
    FechaPago = db.Column(db.Date)
    TipoPago = db.Column(db.String(255))
    MontoPago = db.Column(db.Numeric(10, 2))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, FechaPago, TipoPago, MontoPago, IDEmpleado):
        self.FechaPago = FechaPago
        self.TipoPago = TipoPago
        self.MontoPago = MontoPago
        self.IDEmpleado = IDEmpleado

with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('IDPago' ,'FechaPago', 'TipoPago', 'MontoPago', 'IDEmpleado')
