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
  int N = int.parse(input());
  print('${(N/100).ceil()}');
}
