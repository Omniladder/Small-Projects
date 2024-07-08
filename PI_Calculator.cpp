#include <cmath>
#include <iostream>

int main()
{
    long long int num_of_iter = 1000000;
    double MY_PI = 0;
    double dx = 2.0/num_of_iter;
    for(long long int i = 0; i <= num_of_iter; i++)
    {
        MY_PI += dx * sqrt((-1 * ((-1 + dx * i) * (-1 + dx * i))) + 1);
        std::cout<<i<<std::endl;
        
    }
    MY_PI *= 2 ;
    std::cout<< MY_PI<<std::endl;
}