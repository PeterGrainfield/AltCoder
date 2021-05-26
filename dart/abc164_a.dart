import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> sw = inputIntList();
  print(sw[0] <= sw[1] ? "unsafe" : "safe");
}
