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
        title: Text('PAGO NOMINA', style: TextStyle(color: Color(0xFFFFC800))),
        backgroundColor: Colors.black,
        actions: [],
      ),
      endDrawer: MyCustomDrawer(), // Usa tu cajón personalizado aquí
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
            width: 400, // Personaliza el ancho de tu cajón
            color: Colors.black, // Personaliza el color de fondo
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                ListTile(
                  title: Text('PAGAR NOMINA',
                      style: TextStyle(color: Color(0xFFFFC800))),
                  onTap: () {
                    Navigator.pop(context); // Cierra el cajón
                    // Navegar a la página de inicio
                    Navigator.pushNamed(context, "/");
                  },
                ),
                ListTile(
                  title: Text('PRESTAMOS',
                      style: TextStyle(color: Color(0xFFFFC800))),
                  onTap: () {
                    Navigator.pop(context); // Cierra el cajón
                    // Navegar a la página de carrito
                    Navigator.pushNamed(context, "/");
                  },
                ),
                ListTile(
                  title: Text('HISTORIAL DE PAGOS',
                      style: TextStyle(color: Color(0xFFFFC800))),
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
      child: Container(
        child: Stack(
          children: [
            Image(
              image: AssetImage(
                  'assets/img/primer-plano-manos-contador-contando-calculadora.jpg'),
              width: double.infinity,
              fit: BoxFit.cover, // Ajusta la imagen al tamaño del contenedor
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
              left: 80,
              width: 300,
              height: 80,
              child: FloatingActionButton(
              child: Text("PAGAR NOMINA"),
                onPressed: () {

              },
                backgroundColor: Color(0xFFFFC800), 
                ),
              ),

          ],
        ),
      ),
    );
  }
}