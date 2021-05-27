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
  String T = input();
  print(S == "Y" ? T.toUpperCase() : T);
}
