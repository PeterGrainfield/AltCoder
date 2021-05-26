import 'dart:io';
import 'dart:core';
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
  List<int> xy = inputIntList();
  if ((xy[0] - xy[1]).abs() < 3) {
    print("Yes");
  } else {
    print("No");
  }
}
