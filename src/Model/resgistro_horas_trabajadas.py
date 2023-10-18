from config.db import db, app, ma

class RegistroHorasTrabajadas(db.Model):
    __tablename__ = "registrohorastrabajadas"

    IDRegistro = db.Column(db.Integer, primary_key=True)
    FechaRegistro = db.Column(db.Date)
    HoraEntrada = db.Column(db.Time)
    HoraSalida = db.Column(db.Time)
    TotalHorasTrabajadas = db.Column(db.Numeric(5, 2))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, FechaRegistro, HoraEntrada, HoraSalida, TotalHorasTrabajadas, IDEmpleado):
        self.FechaRegistro = FechaRegistro
        self.HoraEntrada = HoraEntrada
        self.HoraSalida = HoraSalida
        self.TotalHorasTrabajadas = TotalHorasTrabajadas
        self.IDEmpleado = IDEmpleado

with app.app_context():
    db.create_all()

class RegistroHorasTrabajadasSchema(ma.Schema):
    class Meta:
        fields = ('IDRegistro', 'FechaRegistro', 'HoraEntrada', 'HoraSalida', 'TotalHorasTrabajadas', 'IDEmpleado')
