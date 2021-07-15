#include "solution.hpp"
#include <string>
#include <iostream>
#include <vector>
#include <regex>

using namespace ::std;

regex tag_regex("@([\\w\\d-_]+)");

string GetRecipient(string message, int position)
{
    cout << "start: " << message << endl;

    auto tag_begin = sregex_iterator(message.begin(), message.end(), tag_regex);
    auto tag_end = sregex_iterator();

    uint i = 1;
    for (std::sregex_iterator regexIterator = tag_begin; regexIterator != tag_end; ++regexIterator) {
        std::smatch match = *regexIterator;
        std::string match_str = match.str(1);
        if (i == position) return match_str;
        i++;
    }

    return "";
}