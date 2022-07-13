#include <string>

std::string bool_to_word(bool value)
{
  if (value == true)
    return "Yes";
  else
    return "No";
}