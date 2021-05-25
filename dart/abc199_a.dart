import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  if (str != null) {
    return str;
  } else {
    return '';
  }
}

void main() {
  final abc = input().split(' ').map((e) => int.parse(e)).toList();
  int a = abc[0];
  int b = abc[1];
  int c = abc[2];
  if (a*a+b*b < c*c){
    print('Yes');
  } else {
    print('No');
  }

}
