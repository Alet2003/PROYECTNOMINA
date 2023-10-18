from config.db import db, app, ma

class Creditos(db.Model):
    __tablename__ = "creditos"

    IDCredito = db.Column(db.Integer, primary_key=True)
    FechaOtorgamiento = db.Column(db.Date)
    MontoCredito = db.Column(db.Numeric(10, 2))
    TasaInteres = db.Column(db.Numeric(5, 2))
    PlazoCredito = db.Column(db.Integer)
    CuotasMensuales = db.Column(db.Numeric(10, 2))
    EstadoCredito = db.Column(db.String(255))
    IDEmpleado = db.Column(db.Integer, db.ForeignKey('empleados.IDEmpleado'))

    def __init__(self,  FechaOtorgamiento, MontoCredito, TasaInteres, PlazoCredito, CuotasMensuales, EstadoCredito, IDEmpleado):
        self.FechaOtorgamiento = FechaOtorgamiento
        self.MontoCredito = MontoCredito
        self.TasaInteres = TasaInteres
        self.PlazoCredito = PlazoCredito
        self.CuotasMensuales = CuotasMensuales
        self.EstadoCredito = EstadoCredito
        self.IDEmpleado = IDEmpleado

with app.app_context():
    db.create_all()

class CreditosSchema(ma.Schema):
    class Meta:
        fields = ('IDCredito', 'FechaOtorgamiento', 'MontoCredito', 'TasaInteres', 'PlazoCredito', 'CuotasMensuales', 'EstadoCredito', 'IDEmpleado')
