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
  var abc = input().split(' ').map((e) => int.parse(e)).toList();
  print('${21 - abc[0] - abc[1] - abc[2]}');
}
