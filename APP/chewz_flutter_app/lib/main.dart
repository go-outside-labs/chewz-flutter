import 'package:chewz/SwipeAnimation/index.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';


void main() => runApp(new Chewz());

class Chewz extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return new MaterialApp(

      debugShowCheckedModeBanner: false,
      home: MyStatefulWidget(),

    );
  }
}


class MyStatefulWidget extends StatefulWidget {
  MyStatefulWidget({Key key}) : super(key: key);

  @override
  _MyStatefulWidgetState createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  int _selectedIndex = 0;

  static List<Widget> _widgetOptions = <Widget>[
    new CardDemo(),
    new CardDemo(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(
                backgroundColor: Colors.lime,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Image.asset(
                    'assets/chewz_logo.png',
                      fit: BoxFit.contain,
                      color: Colors.white,
                      height: 30,
                  ),
          ],
        ),

        leading:  IconButton(
          icon: Icon(Icons.reorder,
          size: 30,
          color: Colors.white),
          onPressed: () {},
          highlightColor:Colors.lime,
          color: Colors.white,
        ),

      ),

      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),

      /*
      bottomNavigationBar: BottomNavigationBar(
        items:  <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.fastfood, size: 25,
            ),
            title: Text(''),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.group, size: 25,
            ),
            title: Text(''),
          ),

        ],
        currentIndex: _selectedIndex,
        backgroundColor: Colors.lime,
        selectedItemColor: Colors.grey[600],
        onTap: _onItemTapped,
      ),
      */

    );
  }
}


