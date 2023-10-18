from config.db import db, app, ma

class Empleados(db.Model):
    __tablename__ = "empleados"

    IDEmpleado = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(255))
    Apellido = db.Column(db.String(255))
    FechaNacimiento = db.Column(db.Date)
    Direccion = db.Column(db.String(255))
    NumeroTelefono = db.Column(db.String(15))
    CorreoElectronico = db.Column(db.String(255))
    Departamento = db.Column(db.String(255))
    FechaContratacion = db.Column(db.Date)
    SalarioBase = db.Column(db.Numeric(10, 2))

    def __init__(self, Nombre, Apellido, FechaNacimiento, Direccion, NumeroTelefono, CorreoElectronico, Departamento, FechaContratacion, SalarioBase):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaNacimiento = FechaNacimiento
        self.Direccion = Direccion
        self.NumeroTelefono = NumeroTelefono
        self.CorreoElectronico = CorreoElectronico
        self.Departamento = Departamento
        self.FechaContratacion = FechaContratacion
        self.SalarioBase = SalarioBase

with app.app_context():
    db.create_all()

class EmpleadosSchema(ma.Schema):
    class Meta:
        fields = ('IDEmpleado', 'Nombre', 'Apellido', 'FechaNacimiento', 'Direccion', 'NumeroTelefono', 'CorreoElectronico', 'Departamento', 'FechaContratacion', 'SalarioBase')

