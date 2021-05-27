import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  String S = input();
  if (S[2] == S[3] && S[4] == S[5]) {
    print("Yes");
  } else {
    print("No");
  }
}
