import 'dart:convert';
import 'dart:io';

void main(List<String> args) async {
  final file = File('activities/activities.json');
  final data = await file.readAsString();
  final json = jsonDecode(data) as Map;

  for (var key in json.keys) {
    json[key]["scoresheet"] = "General";
  }

  for (var key in overrides.keys) {
    for (var act in overrides[key] ?? []) {
      if (json.containsKey(act)) json[act]["scoresheet"] = key;
    }
  }

  print(jsonEncode(json));

  await file.writeAsString(jsonEncode(json));
}

Map<String, List<String>> overrides = {
  "Basketball":
      "Basketball, Basketball Skills, Wheelchair Basketball, Water Basketball"
          .split(", "),
  "Flag Football": "Flag Football, Football Skills".split(", "),
  "Soccer":
      "Soccer, Soccer Skills, Futsal, Bubble Soccer, Indoor Soccer".split(", "),
  "Softball": "Softball, Baseball, Baseball Skills, Wiffleball".split(", "),
  "Volleyball":
      "Volleyball, Beach Volleyball, Seated Volleyball, Wallyball, Water Volleyball, Mud Volleyball, Inner Tube Water Volleyball"
          .split(", "),
  "Hockey": "Ice Hockey".split(", "),
};
