import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> A = inputIntList();
  A.sort();
  print(A[2] - A[1] == A[1] - A[0] ? "Yes" : "No");
}
