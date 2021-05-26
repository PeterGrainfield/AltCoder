import 'dart:io';
import 'dart:math';

String input() {
  var str = stdin.readLineSync();
  if (str != null) {
    return str;
  } else {
    return '';
  }
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> ab = inputIntList();
  int ans = [ab[0] * 2 + 100 - ab[1], 0].reduce(max);
  print(ans);
}
