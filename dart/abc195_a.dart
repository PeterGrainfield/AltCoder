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
  final mh = input().split(' ').map((e) => int.parse(e)).toList();
  if (mh[1]%mh[0] == 0) {
    print('Yes');
  } else {
    print('No');
  }
}
