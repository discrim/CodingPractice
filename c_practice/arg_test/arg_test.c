#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("This program was called with \"%s\".\n", argv[0]);

    if (argc > 1)
    {
        for (int count = 0; count < argc; count++)
        {
            printf("argv[%d]: %s\n", count, argv[count]);
        }
    }
    else
    {
        printf("The command has no other arguments.\n");
    }
    return 0;
}
