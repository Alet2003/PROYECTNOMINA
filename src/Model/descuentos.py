from config.db import db, app, ma

class Descuentos(db.Model):
    __tablename__ = "descuentos"

    IDDescuento = db.Column(db.Integer, primary_key=True)
    FechaAplicacionDescuento = db.Column(db.Date)
    TipoDescuento = db.Column(db.String(255))
    MontoDescuento = db.Column(db.Numeric(10, 2))
    DescripcionDescuento = db.Column(db.Text)
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, FechaAplicacionDescuento, TipoDescuento, MontoDescuento, DescripcionDescuento, IDEmpleado):
        self.FechaAplicacionDescuento = FechaAplicacionDescuento
        self.TipoDescuento = TipoDescuento
        self.MontoDescuento = MontoDescuento
        self.DescripcionDescuento = DescripcionDescuento
        self.IDEmpleado = IDEmpleado

class DescuentosSchema(ma.Schema):
    class Meta:
        fields = ('IDDescuento', 'FechaAplicacionDescuento', 'TipoDescuento', 'MontoDescuento', 'DescripcionDescuento', 'IDEmpleado')
