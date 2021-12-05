import 'dart:io';

Map<String, int> PreProcess(String data) {
  List<String> datasplit = data.split('\n');
  Map<String, int> dataMap = {'x': 0, 'y': 0};
  for (var item in datasplit) {
    String cmd = item.split(' ')[0];
    int distance = int.parse(item.split(' ')[1]);
    if (cmd.trim() == 'up') {
      dataMap['y'] = dataMap['y']! + distance;
    } else if (cmd.trim() == 'down') {
      dataMap['y'] = dataMap['y']! - distance;
    } else if (cmd.trim() == 'forward') {
      dataMap['x'] = dataMap['x']! + distance;
    }
  }
  return dataMap;
}

void Process(Map<String, int> d) {
  print('Horizontal Distance × Depth: ${d["x"]! * d["y"]! * -1}');
}


void main(List<String> args) {
  String input = File('./Input-1.txt').readAsStringSync();
  Process(PreProcess(input));
}
