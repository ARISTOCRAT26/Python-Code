#include<iostream>

int main()
{
    int x;
    int y;
    int sum;
    std::cout << "Hello World!";
    std::cout << "Enter any two numbers: ";
    std::cin >> x >> y;
    std::cout << std::endl;
    sum = x + y;
    std::cout << "Sum is: " <<sum;
    return 0;
}