import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> nab = inputIntList();
  int A = nab[0] * nab[1];
  print(A < nab[2] ? A : nab[2]);
}
