/*
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
*/
#include <stdio.h>
#include <stdlib.h> // For exit() function
int main()
{
    int c;
    FILE *file;
    file = fopen("input.txt", "r");
    if (file)
    {
        while ((c = getc(file)) != EOF)
            putchar(c);
        fclose(file);
    }

    return 0;
}
