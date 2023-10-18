from config.db import db, app, ma

class VacacionesTiempoLibre(db.Model):
    __tablename__ = "vacacionestiempolibre"

    IDSolicitud = db.Column(db.Integer, primary_key=True)
    TipoSolicitud = db.Column(db.String(255))
    FechaSolicitud = db.Column(db.Date)
    FechaInicio = db.Column(db.Date)
    FechaTermino = db.Column(db.Date)
    EstadoSolicitud = db.Column(db.String(255))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self, TipoSolicitud, FechaSolicitud, FechaInicio, FechaTermino, EstadoSolicitud, IDEmpleado):
        self.TipoSolicitud = TipoSolicitud
        self.FechaSolicitud = FechaSolicitud
        self.FechaInicio = FechaInicio
        self.FechaTermino = FechaTermino
        self.EstadoSolicitud = EstadoSolicitud
        self.IDEmpleado = IDEmpleado

with app.app_context():
    db.create_all()

class VacacionesTiempoLibreSchema(ma.Schema):
    class Meta:
        fields = ('IDSolicitud', 'TipoSolicitud', 'FechaSolicitud', 'FechaInicio', 'FechaTermino', 'EstadoSolicitud', 'IDEmpleado')
