import 'dart:io';

String input() {
  var str = stdin.readLineSync();
  return str == null ? "" : str;
}

List<int> inputIntList() {
  return input().split(' ').map(int.parse).toList();
}

void main() {
  List<int> abc = inputIntList();
  int a = abc[0];
  int b = abc[1];
  int c = abc[2];
  int N = a+b+1;
  bool turn = c == 0 ? true : false;
  for (int i = 0; i < N; i++) {
    turn ? a-- : b--;
    //print("${a} ${b}");
    if (a < 0) {
      print("Aoki");
      return;
    } else if (b < 0) {
      print("Takahashi");
      return;
    }
    turn = !turn;
  }
}
