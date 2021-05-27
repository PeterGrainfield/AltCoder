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
  int X = (ab[0] + ab[1]) ~/ 2;
  int Y = ab[0] - X;
  print('${X} ${Y}');
}
