from config.db import db, app, ma

class HorasExtras(db.Model):
    __tablename__ = "horasextras"

    IDRegistroHorasExtras = db.Column(db.Integer, primary_key=True)
    FechaRegistro = db.Column(db.Date)
    HoraInicioHorasExtras = db.Column(db.Time)
    HoraFinHorasExtras = db.Column(db.Time)
    TotalHorasExtras = db.Column(db.Numeric(5, 2))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, FechaRegistro, HoraInicioHorasExtras, HoraFinHorasExtras, TotalHorasExtras, IDEmpleado):
        self.FechaRegistro = FechaRegistro
        self.HoraInicioHorasExtras = HoraInicioHorasExtras
        self.HoraFinHorasExtras = HoraFinHorasExtras
        self.TotalHorasExtras = TotalHorasExtras
        self.IDEmpleado = IDEmpleado

with app.app_context():
    db.create_all()

class HorasExtrasSchema(ma.Schema):
    class Meta:
        fields = ('IDRegistroHorasExtras',  'FechaRegistro', 'HoraInicioHorasExtras', 'HoraFinHorasExtras', 'TotalHorasExtras','IDEmpleado')
