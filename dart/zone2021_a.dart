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
  int ans = 0;
  for (int i = 0; i < S.length - 3; i++) {
    if (S.substring(i, i + 4) == "ZONe") {
      ans += 1;
    }
  }
  print(ans);
}
