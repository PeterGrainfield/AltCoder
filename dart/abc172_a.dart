import 'dart:io';
import 'dart:math';

String input() {
  var str = stdin.readLineSync();
  if (str != null) {
    return str;
  } else {
    return '';
  }
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  int a = int.parse(input());
  print(a + a * a + a * a * a);
}
