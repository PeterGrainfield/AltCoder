import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  int N = int.parse(input());
  N = N % 10;
  if (N == 2 || N == 4 || N == 5 || N == 7 || N == 9) {
    print("hon");
  } else if (N == 0 || N == 1 || N == 6 || N == 8) {
    print("pon");
  } else {
    print("bon");
  }
}
