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
  var ab = input().split(' ').map((e) => int.parse(e)).toList();
  if (ab[0] * ab[1] % 2 == 1) {
    print('Odd');
  } else {
    print('Even');
  }
}
