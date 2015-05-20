#include <stdio.h>

typedef struct _MyStruct{
	int x;
	int y;
}MyStruct;

int hello(MyStruct* s){
//	printf("hello?\n");
	s->x = 100;
	return 10;
}