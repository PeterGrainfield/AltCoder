import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> a = inputIntList();
  a.sort();
  if ((a[0] == a[1] && a[0] != a[2]) || (a[1] == a[2] && a[0] != a[1])) {
    print("Yes");
  } else {
    print("No");
  }
}
