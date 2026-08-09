#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    FILE *fp = fopen("sensor_data.csv", "w");
    if (fp == NULL) { perror("fopen"); return 1; }
    
    fprintf(fp, "id,type,value,timestamp\n");
    srand(time(NULL));
    
    for (int i = 0; i < 10; i++) {
        fprintf(fp, "%d,CDS,%d,%ld\n",
            i+1, rand() % 4096, time(NULL));
    }
    
    fclose(fp);
    printf("sensor_data.csv 생성 완료\n");
    return 0;
}