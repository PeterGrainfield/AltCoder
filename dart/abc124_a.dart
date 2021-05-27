import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> ab = inputIntList();
  int ans = 0;
  for (int i = 0; i < 2; i++) {
    if (ab[0] < ab[1]) {
      ans += ab[1]--;
    } else {
      ans += ab[0]--;
    }
  }
  print(ans);
}
