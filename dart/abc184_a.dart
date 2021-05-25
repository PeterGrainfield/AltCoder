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
  var ab = input().split(' ').map(int.parse).toList();
  var cd = input().split(' ').map(int.parse).toList();
  print(ab[0]*cd[1]-ab[1]*cd[0]);
}
