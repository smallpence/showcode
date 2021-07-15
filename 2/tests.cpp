#include "solution.hpp"
#include <vector>

using namespace ::std;

int main() {
    string message = "@JoeBloggs yo";
    int position = 1;
    string expected = "JoeBloggs";
    cout << GetRecipient(message, position) << " " << expected << endl;

    message = "Hey @Joe_Bloggs what time are we meeting @FredBloggs?";
    position = 3;
    expected = "FredBloggs";
    cout << GetRecipient(message, position) << " " << expected << endl;
}