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
  var NW = input().split(' ').map((e) => int.parse(e)).toList();
  print('${(NW[0]/NW[1]).floor()}');
}
