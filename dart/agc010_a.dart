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
  int N = int.parse(input());
  List<int> listA = inputIntList();

  int cnt = 0;
  for (int i = 0; i < listA.length; i++) {
    if (listA[i].isOdd) {
      cnt++;
    }
  }
  if (cnt.isOdd) {
    print("NO");
  } else {
    print("YES");
  }
}
