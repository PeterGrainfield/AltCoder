import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> abcd = inputIntList();
  int L = abcd[0] + abcd[1];
  int R = abcd[2] + abcd[3];
  if (L == R) {
    print("Balanced");
  } else {
    print(L < R ? "Right" : "Left");
  }
}
