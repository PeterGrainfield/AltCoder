import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> xa = inputIntList();
  if (xa[0] < xa[1]) {
    print(0);
  } else {
    print(10);
  }
}
