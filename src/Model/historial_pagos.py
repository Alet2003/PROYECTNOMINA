from config.db import db, app, ma

class HistorialPagos(db.Model):
    __tablename__ = "historialpagos"

    IDRegistro = db.Column(db.Integer, primary_key=True)
    FechaPago = db.Column(db.Date)
    TipoPago = db.Column(db.String(255))
    MontoPago = db.Column(db.Numeric(10, 2))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, FechaPago, TipoPago, MontoPago, IDEmpleado):
        self.FechaPago = FechaPago
        self.TipoPago = TipoPago
        self.MontoPago = MontoPago
        self.IDEmpleado = IDEmpleado

class HistorialPagosSchema(ma.Schema):
    class Meta:
        fields = ('IDRegistro', 'FechaPago', 'TipoPago', 'MontoPago', 'IDEmpleado')
