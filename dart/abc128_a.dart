import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> ap = inputIntList();
  int pieces = ap[0] * 3 + ap[1];
  print(pieces~/2);
}
