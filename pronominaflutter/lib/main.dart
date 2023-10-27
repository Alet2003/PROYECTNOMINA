import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

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
          child: Text("PAGAR NOMINA",
              style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
        ),
        SizedBox(
          height: 10,
        ),
        Container(
          width: 300,
          height: 50,
          alignment: Alignment.topCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child: Text("Aquí puedes pagar a tus empleados",
              style: TextStyle(fontSize: 12)),
        ),
        SizedBox(
          height: 10,
        ),
        Container(
          width: 300,
          height: 180,
          decoration: BoxDecoration(
            color: Colors.transparent,
            border: Border.all(
              color: Color(0xFF39c545),
              width: 5.0,
            ),
            borderRadius: BorderRadius.circular(8.0),
          ),
          child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                IconButton(
                  onPressed: () {},
                  icon: Icon(Icons.monetization_on,
                      size: 100, color: Color(0xFF39c545)),
                ),
                Container(
                  margin: EdgeInsets.fromLTRB(95, 20, 10, 30),
                  child: Text(
                    "IR A PAGAR",
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                )
              ]),
        ),
        SizedBox(
          height: 30,
        ),
        Container(
          width: 300,
          height: 80,
          alignment: Alignment.bottomCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child: Text("PRESTAMOS",
              style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
        ),
        SizedBox(
          height: 10,
        ),
        Container(
          width: 300,
          height: 50,
          alignment: Alignment.topCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child: Text("VERIFICA Y SOLICITA UN CREDITO",
              style: TextStyle(fontSize: 10)),
        ),
        SizedBox(
          height: 15,
        ),
        Container(
          width: 300,
          height: 50,
          alignment: Alignment.topCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child: Text("SOLICITA CUALQUIERA DE LOS DIFERENTES TIPOS DE CREDITOS",
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 10.5,
              )),
        ),
        Container(
          margin: EdgeInsets.fromLTRB(0, 20, 0, 15),
          width: 300,
          height: 250,
          decoration: BoxDecoration(
            color: Colors.transparent,
            border: Border.all(
              color: Color(0xFF39c545),
              width: 5.0,
            ),
            borderRadius: BorderRadius.circular(8.0),
          ),
          child: MyCarousel(),
        ),
        SizedBox(
          height: 20,
        ),
        Container(
          width: 300,
          height: 80,
          alignment: Alignment.bottomCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child: Text("HISTORIAL DE PAGOS",
              style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
        ),
        SizedBox(
          height: 10,
        ),
        Container(
          width: 300,
          height: 50,
          alignment: Alignment.topCenter,
          //padding: EdgeInsetsDirectional.symmetric(vertical: 30, horizontal: 80),
          child: Text(
              "Aqui podras ver el historial de todos los pagos hechos a tus empleados anteriormente",
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 10.5,
              )),
        ),
        SizedBox(
          height: 10,
        ),
        Container(
          width: 300,
          height: 180,
          decoration: BoxDecoration(
            color: Colors.transparent,
            border: Border.all(
              color: Color(0xFF39c545),
              width: 5.0,
            ),
            borderRadius: BorderRadius.circular(8.0),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Container(
                width: 100, // Ancho del círculo
                height: 100, // Alto del círculo
                margin: EdgeInsets.fromLTRB(20, 10, 20, 10),
                decoration: BoxDecoration(
                  color: Color(0xFF39c545), // Color de fondo del círculo
                  shape: BoxShape.circle, // Establece la forma como un círculo
                ),
                child: IconButton(
                  onPressed: () {},
                  icon: Icon(Icons.h_mobiledata_rounded,
                      size: 70, color: Colors.white),
                ),
              ),
              Container(
                margin: EdgeInsets.fromLTRB(80, 0, 10, 20),
                child: Text(
                  "VER HISTORIAL",
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
        ),
        SizedBox(
          height: 40,
        ),
        SizedBox(
          height: 30,
        ),
        SizedBox(
          height: 30,
        ),
        Container(
          width: 500,
          height: 800,
          color: Color(0xFF212529),
          child: Stack(
            children: [
              Positioned(
                top: 80,
                left: 90,
                child: Text(
                  "CONTACTANOS",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Positioned(
                top: 130,
                left: 20,
                width: 350,
                child: Text(
                  "Llena Los siguientes datos y envianos un mensaje ya sea tu opinion, sugerencia o inquietud",
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 15,
                  ),
                ),
              ),
              Positioned(
                top: 160,
                left: 20,
                width: 350,
                child: Container(
                  margin: EdgeInsets.fromLTRB(0, 20, 0, 15),
                  width: 300,
                  height: 450,
                  decoration: BoxDecoration(
                    color: Colors.transparent,
                    border: Border.all(
                      color: Color(0xFF39c545),
                      width: 5.0,
                    ),
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                  child: Column(
                    children: [
                      Container(
                          margin: EdgeInsets.fromLTRB(20, 20, 10, 20),
                          width: 300,
                          child:     TextField(
                        style: TextStyle(
                          fontSize: 20.0, // Tamaño de texto deseado
                          fontFamily: 'Open Sans',
                          color: Colors.white, // Color de texto blanco
                        ),
                        enableInteractiveSelection: false,
                        //autofocus: true,
                        decoration: InputDecoration(
                          hintText: 'Nombre completo',
                          hintStyle: TextStyle(
                            color: Color(0xFF212529),
                            fontFamily: 'Open Sans',
                            fontWeight: FontWeight.bold,
                          ),
                          filled: true,
                          fillColor: Colors.white,
                          border: OutlineInputBorder(
                            borderSide: BorderSide.none,
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.white),
                          ),
                        ),
                      )
                      ),
                      Container(
                          margin: EdgeInsets.fromLTRB(20, 0, 10, 20),
                          width: 300,
                          child:     TextField(
                            style: TextStyle(
                              fontSize: 20.0, // Tamaño de texto deseado
                              fontFamily: 'Open Sans',
                              color: Colors.white, // Color de texto blanco
                            ),
                            enableInteractiveSelection: false,
                            //autofocus: true,
                            decoration: InputDecoration(
                              hintText: 'Email',
                              hintStyle: TextStyle(
                                color: Color(0xFF212529),
                                fontFamily: 'Open Sans',
                                fontWeight: FontWeight.bold,
                              ),
                              filled: true,
                              fillColor: Colors.white,
                              border: OutlineInputBorder(
                                borderSide: BorderSide.none,
                              ),
                              focusedBorder: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.white),
                              ),
                            ),
                          )
                      ),
                      Container(
                          margin: EdgeInsets.fromLTRB(20, 0, 10, 20),
                          width: 300,
                          child:     TextField(
                            style: TextStyle(
                              fontSize: 20.0, // Tamaño de texto deseado
                              fontFamily: 'Open Sans',
                              color: Colors.white, // Color de texto blanco
                            ),
                            enableInteractiveSelection: false,
                            //autofocus: true,
                            decoration: InputDecoration(
                              hintText: 'Numero de telefono',
                              hintStyle: TextStyle(
                                color: Color(0xFF212529),
                                fontFamily: 'Open Sans',
                                fontWeight: FontWeight.bold,
                              ),
                              filled: true,
                              fillColor: Colors.white,
                              border: OutlineInputBorder(
                                borderSide: BorderSide.none,
                              ),
                              focusedBorder: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.white),
                              ),
                            ),
                          )
                      ),
                      Container(
                          margin: EdgeInsets.fromLTRB(20, 0, 10, 20),
                          width: 500,
                          height: 150,
                          color: Colors.white,
                          child:     TextField(
                            style: TextStyle(
                              fontSize: 20.0, // Tamaño de texto deseado
                              fontFamily: 'Open Sans',
                              color: Colors.white, // Color de texto blanco
                            ),
                            enableInteractiveSelection: false,
                            //autofocus: true,
                            decoration: InputDecoration(
                              hintText: 'Escribe tu mensaje aqui',
                              hintStyle: TextStyle(
                                color: Color(0xFF212529),
                                fontFamily: 'Open Sans',
                                fontWeight: FontWeight.bold,
                              ),
                              filled: true,
                              fillColor: Colors.white,
                              border: OutlineInputBorder(
                                borderSide: BorderSide.none,
                              ),
                              focusedBorder: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.white),
                              ),
                            ),
                          )
                      )
                    ],
                  ),
                ),
              ),
              Positioned(
                top: 680,
                left: 65,
                width: 250,
                height: 60,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(primary: Color(0xFF39c545)),
                  child: Text("ENVIAR MENSAJE"),
                  onPressed: () {},
                ),
              ),
            ],
          ),
        ),
      ]),
    );
  }
}

class MyCarousel extends StatelessWidget {
  final List<Map<String, String>> creditData = [
    {
      'image': 'assets/img/imagen-blog-credito-libre-inversion-400x300.jpg',
      'text': 'CREDITO LIBRE INVERSIÓN',
    },
    {
      'image':
          'assets/img/Crédito-educativo-para-continuar-tus-estudios (1).jpg',
      'text': 'CREDITO EDUCATIVO',
    },
    {
      'image': 'assets/img/beneficios-credito-hipotecario.jpg',
      'text': 'CREDITO HIPOTECARIO',
    },
  ];

  @override
  Widget build(BuildContext context) {
    return CarouselSlider(
      items: creditData.map((credit) {
        return Container(
          margin: EdgeInsets.all(15),
          child: Column(
            children: [
              Image.asset(
                credit['image']!,
                fit: BoxFit.cover,
                height: 150, // Alto de la imagen
              ),
              SizedBox(height: 10),
              Text(
                credit['text']!,
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
        );
      }).toList(),
      options: CarouselOptions(
        height: 250.0, // Altura del carrusel
        enlargeCenterPage: true,
        autoPlay: true, // Reproducción automática
        aspectRatio: 16 / 9,
        viewportFraction: 0.8,
      ),
    );
  }
}
