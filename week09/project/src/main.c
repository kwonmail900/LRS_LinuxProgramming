#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "sensor.h"

int main(int argc, char *argv[]) {
    int count = 20;               // 기본 측정 횟수
    int interval = 500000;        // 0.5초 (마이크로초)
    if (argc > 1) count = atoi(argv[1]);

    sensor_init();

    // CSV 파일 열기
    FILE *fp = fopen("data/sensor_data.csv", "w");
    if (!fp) { perror("fopen"); return 1; }
    fprintf(fp, "id,type,raw_value,lux,timestamp\n");

    for (int i = 1; i <= count; i++) {
        SensorData data = sensor_read(i);
        sensor_print(&data);         // 화면 출력
        sensor_write_csv(fp, &data); // CSV 저장
        usleep(interval);
    }

    fclose(fp);
    printf("[INFO] %d measurements saved to data/sensor_data.csv\n", count);
    return 0;
}