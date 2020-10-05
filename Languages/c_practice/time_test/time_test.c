#include <stdio.h>  // printf()
#include <time.h>   // clock_t, clock()

int main(void)
{
    clock_t clk1, clk2; // Data type that stores clock counts
    int sum = 0;
    
    clk1 = clock(); // Record current clock count (the moment before beginning the task)
    
    for (int ii = 0; ii < 100000000; ii++)
    {
        sum += ii;  // Do a repetitive task to spend enough time
    }
    clk2 = clock();  // Record current clock count (the moment after finishing the task)

    printf("clk1: %5d\nclk2: %5d\nElapsed Time: %2.3f\n",
            (int)clk1, (int)clk2, (float)(clk2 - clk1) / CLOCKS_PER_SEC);
                    
    return 0;
}
