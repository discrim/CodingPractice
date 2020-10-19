#include <stdio.h>
#include <string.h>

// Future work: Can I implement a function doing this task?

int main(void) {
	char hello;
	char str[] = "This\nis\na\nsimple\nsentence";
	printf("%s\n", str);
	
	// Method 1 (my method)
	char *cptr;
	for (cptr = str; *cptr != '\0'; cptr++) {
		if (*cptr == '\n') {
			*cptr = ',';
		}
	}
	
	// Method 2
	while ((cptr = strchr(str, '\n')) != NULL) *cptr = ',';
	
	// Method 3
	for (int ii = 0; ii < sizeof(str); ii++) {
		if (str[ii] == '\n') str[ii] = ',';
	}
	
	printf("%s\n", str);
	
	return 0;
}