import 'dart:io';

class Instruction<String, int> {
  final String cmd;
  final int value;

  Instruction(this.cmd, this.value);
}

List<Instruction<String, int>> PreProcess(String data) {
  List<String> datasplit = data.split('\n');
  List<Instruction<String, int>> dataList = new List.empty(growable: true);
  for (var item in datasplit) {
    dataList.add(Instruction(item.split(' ')[0], int.parse(item.split(' ')[1])));
  }
  return dataList;
}

void Process(List<Instruction<String, int>> dataList) {
  int aim = 0;
  int depth = 0;
  int horizontal = 0;

  for (var item in dataList) {
    if (item.cmd == 'forward') {
      horizontal += item.value;
      depth += aim * item.value;
    } else if (item.cmd == 'up') {
      aim -= item.value;
    } else if (item.cmd == 'down') {
      aim += item.value;
    }
  }
  print("Horizontal: $horizontal\nDepth: $depth\nSolution: ${horizontal * depth}");
}


void main(List<String> args) {
  String input = File('./Input-1.txt').readAsStringSync();  // Input is same as Problem 1
  Process(PreProcess(input));
}
