import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> lx = inputIntList();
  for (int i = 0; i < lx.length; i++) {
    if (lx[i] == 0) {
      print(i + 1);
      break;
    }
  }
}
