import 'dart:io';
import 'dart:core';
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
  List<String> listAB = input().split(" ");
  String A = listAB[0];
  String B = listAB[1];
  int sa = 0;
  int sb = 0;
  for (int i = 0; i < A.length; i++) {
    sa += int.parse(A[i]);
  }
  for (int i = 0; i < B.length; i++) {
    sb += int.parse(B[i]);
  }
  print([sa, sb].reduce(max));
}
