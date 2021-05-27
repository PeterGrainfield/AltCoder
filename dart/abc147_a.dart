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
  List<int> abc = inputIntList();
  if (abc[0] + abc[1] + abc[2] > 21) {
    print("bust");
  } else {
    print("win");
  }
}
