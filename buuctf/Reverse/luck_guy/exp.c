#include <stdio.h>
#include <string.h>

int main() {
	int i;
	char f2[] = "icug`of";
	for (i=0; i <= 7; ++i){
		if ( i % 2 == 1 )
            f2[i] = f2[i] - 2;
        else
            f2[i] = f2[i] - 1;
	}
	printf("GXY{do_not_%s", f2);
	return 0;
}