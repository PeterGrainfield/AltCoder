import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> lrd = inputIntList();
  int ans = 0;
  for (int i = lrd[0]; i <= lrd[1]; i++) {
    if (i % lrd[2] == 0) {
      ans++;
    }
  }
  print(ans);
}
