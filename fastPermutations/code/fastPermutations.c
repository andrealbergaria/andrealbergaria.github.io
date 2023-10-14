#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>


/* Testing function
 * 	printBits...given a size in bytes and a pointer, prints the corresponding bits
 * 	check reference on andrealbergaria.github.io/fastPermutations
 */


void printBits(size_t const size, unsigned char *ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i = size-1; i >= 0; i--) {
        for (j = 7; j >= 0; j--) {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    printf(" (%c) ",*ptr);
}

/* Testing functions
 *
 * Instead of calling many printBits, we have a function for it.
 */

void printArray(u_char *ptr,int len) {
	printf(" \n Result \n");
	for (int i=0; i < len ; i++) {
		printBits(1,ptr+i);
		printf("\n");
	}
	printf("\n");
}

/*
 * Testing
 *
 * To get random number of random character to test...
 */
u_char *getRandomAsciiBytes(int len) {

	srand( (unsigned)time( NULL ) );
   u_char *array = malloc(len);
   char randomLetter;

   for (int i = 0; i < len ; i++) {
	  randomLetter = 'A' + (random() % 26);
      array[i] = randomLetter;

   }

   return array;
}

/*
 *
 * This is the function that we need..check the algorithm in
 * andrealbergaria.github.io/fastPermutations/index.html
 */

u_char *shiftArray(u_char *array,int len) {
	u_char *temp = malloc(len);

	temp = array;
	char byteToRotate = array[0];


	for (int i = 1 ; i < len; i++) {
		array[i-1] = array[i];
		array[i] = 0;
	}
	array[len-1] = byteToRotate;


	return temp;

}



/*
 * Mostly testing function...and C needs a main() :)
 *
 */
int main(int argc, char **argv) {
	int tries = 10;
	int lenRandom = 0;
	int upper=10;
	int lower=1;
	u_char *shiftedArray;
	lenRandom = (rand() %  (upper - lower + 1)) + lower;
	u_char *temp = malloc(lenRandom);

	for (int i=0; i < tries;i++) {
		// Get random length
		// Creates random ascii bytes with random length
	    temp = getRandomAsciiBytes(lenRandom);
	    // Prints all combinations , once a try...
	    // [a,b,c,d,e] , [b,c,d,e,a] [c,d,e,a,b]
	    printf("\nTrying %i \"%s\" LEN %i",i,temp,strlen(temp));

	    // ALL permutations of string
		for (int x=0; x < lenRandom;x++) {

			shiftedArray = shiftArray(temp,lenRandom);
			printArray(shiftedArray,lenRandom);
			temp = shiftedArray;

		}
		lenRandom = (rand() %  (upper - lower + 1)) + lower;
		printf("\n Press key");
		getchar();

	}

}

