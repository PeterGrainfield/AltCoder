import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> xyz = inputIntList();
  print(xyz[2].toString() + " " + xyz[0].toString() + " " + xyz[1].toString());
}
