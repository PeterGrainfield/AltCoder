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
  String slot = input();
  if (slot[0] == slot[1] && slot[1] == slot[2]) {
    print("Won");
  } else {
    print("Lost");
  }
}
