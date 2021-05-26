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
  List<int> nr = inputIntList();
  if (nr[0] >= 10) {
    print(nr[1]);
  } else {
    print(nr[1] + 100 * (10 - nr[0]));
  }
}
