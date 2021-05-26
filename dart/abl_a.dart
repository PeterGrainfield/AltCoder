import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  int K = int.parse(input());
  String ans = "";
  for (int i = 0; i < K; i++) {
    ans += "ACL";
  }
  print(ans);
}
