#include <stdio.h>
#include <stdlib.h>

int main(){
	system("tcpdump -A -c 100 -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' > m.log");
	return 0;
}
