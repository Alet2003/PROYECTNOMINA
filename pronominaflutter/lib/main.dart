import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('PAGO NOMINA', style: TextStyle(color: Color(0xFF39c545))),
        backgroundColor: Colors.black,
        actions: [],
      ),
      endDrawer: MyCustomDrawer(),
      body: MyPage(),
    );
  }
}

class MyCustomDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        Align(
          child: Container(
            margin:
                EdgeInsetsDirectional.symmetric(horizontal: 0, vertical: 45),
            width: 400,
            color: Colors.black,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                ListTile(
                  title: Text('PAGAR NOMINA',
                      style: TextStyle(color: Color(0xFF39c545))),
                  onTap: () {
                    Navigator.pop(context); // Cierra el cajón
                    // Navegar a la página de inicio
                    Navigator.pushNamed(context, "/");
                  },
                ),
                ListTile(
                  title: Text('PRESTAMOS',
                      style: TextStyle(color: Color(0xFF39c545))),
                  onTap: () {
                    Navigator.pop(context); // Cierra el cajón
                    // Navegar a la página de carrito
                    Navigator.pushNamed(context, "/");
                  },
                ),
                ListTile(
                  title: Text('HISTORIAL DE PAGOS',
                      style: TextStyle(color: Color(0xFF39c545))),
                  onTap: () {
                    Navigator.pop(context); // Cierra el cajón
                    // Navegar a la página de carrito
                    Navigator.pushNamed(context, "/");
                  },
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}

class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Column(children: [
        Stack(
          children: [
            Image(
              image: AssetImage(
                  'assets/img/primer-plano-manos-contador-contando-calculadora.jpg'),
              width: double.infinity,
              fit: BoxFit.cover, // Ajusta la imagen al tamaño del contenedor
            ),
            Positioned(
              top: 0,
              left: 0,
              width: 500,
              height: 300,
              child: Container(
                width: 500,
                height: 200,
                decoration: BoxDecoration(color: Colors.black.withOpacity(0.3)),
              ),
            ),
            Positioned(
              top: 40, // Ajusta la posición vertical del texto
              left: 80, // Ajusta la posición horizontal del texto
              child: Text(
                "BIENVENIDO",
                textAlign: TextAlign.start,
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 40,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Positioned(
              top: 100, // Ajusta la posición vertical del texto
              left: 40, // Ajusta la posición horizontal del texto
              child: Text(
                "¿QUÉ LE GUSTARÍA HACER?",
                textAlign: TextAlign.start,
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 25,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Positioned(
              top: 140,
              left: 135,
              width: 150,
              height: 50,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(primary: Color(0xFF39c545)),
                child: Text("PAGAR NOMINA"),
                onPressed: () {},
              ),
            ),
          ],
        ),
        Container(
          width: 300,
            height: 80,

            alignment: Alignment.bottomCenter,
            //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
            child:
            Text("PAGAR NOMINA", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
        ),
        SizedBox(
          height: 3,
        ),
        Container(
          width: 300,
          height: 50,
          alignment: Alignment.topCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child:
          Text("Aquí puedes pagar a tus empleados", style: TextStyle(fontSize: 15)),
        ),
      ]),
    );
  }
}
