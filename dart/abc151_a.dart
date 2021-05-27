import 'dart:convert';
import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  String S = input();
  int c = S.codeUnitAt(0);
  print(String.fromCharCode(++c));
}
