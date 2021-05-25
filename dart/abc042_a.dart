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
  List<int> listA = inputIntList();
  listA.sort();
  print(listA);
  if (listA[0]==5 && listA[1]==5 && listA[2]==7) {
    print("YES");
  } else {
    print("NO");
  }
}
