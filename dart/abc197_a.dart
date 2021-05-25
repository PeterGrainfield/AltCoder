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
  String S = input();
  print('${S[1] + S[2] + S[0]}');
}
