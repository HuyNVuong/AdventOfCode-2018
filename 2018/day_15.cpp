#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>  

using namespace std;

class Unit {
    public : 
        char type;
        int hitpoints;
        pair<int, int> coordinate;

        Unit(char t, int x, int y) {
            type = t;
            hitpoints = 200;
            coordinate = make_pair(x, y);
        }

        int mahatanDistance(Unit other) {
            return abs(coordinate.first - other.coordinate.first) + abs(coordinate.first - other.coordinate.second);
        }

        string toString() {
            std::ostringstream out;  
            out << "Unit : " << type << " " << hitpoints << " " << " (" << coordinate.first << ", " << coordinate.second << ")" ;
            return out.str();
        }
};

int main() {
    string line;
    vector<Unit> units;
    int y = 0;
    do {
        line = "";
        cin >> line;
        for (int x = 0; x < line.length(); x++) {
            if (line.at(x) != '#' && line.at(x) != '.') {
                Unit unit(line.at(x), x, y);
                units.push_back(unit);       
            }
        }
        y++;
    } while (!line.empty());
    for (auto u : units) {
        cout << u.toString() << endl;
    }
    return 0;
}