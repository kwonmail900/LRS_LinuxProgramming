#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include "sensor.h"

// 센서 초기화 (랜덤 시드)
void sensor_init(void) {
    srand(time(NULL));
    printf("[INFO] Sensor simulator initialized (PID: %d)\n", getpid());
}

// 센서 값 읽기 (CDS 조도 센서 시뮬레이션)
SensorData sensor_read(int id) {
    SensorData data;
    data.id = id;
    strcpy(data.type, "CDS");
    // ESP32 ADC: 0~4095 (12-bit)
    data.raw_value = rand() % 4096;
    // 조도 변환 (간단한 선형 변환)
    data.converted = (float)data.raw_value / 4095.0 * 1000.0;
    data.timestamp = time(NULL);
    return data;
}

// 센서 데이터 화면 출력
void sensor_print(const SensorData *data) {
    char timebuf[20];
    strftime(timebuf, sizeof(timebuf), "%H:%M:%S", localtime(&data->timestamp));
    printf("[%s] ID:%d Type:%s Raw:%d Lux:%.1f\n", timebuf, data->id, data->type, data->raw_value, data->converted);
}

// CSV 형식으로 파일 출력
void sensor_write_csv(FILE *fp, const SensorData *data) {
    fprintf(fp, "%d,%s,%d,%.1f,%ld\n", data->id, data->type, data->raw_value, data->converted, data->timestamp);
    fflush(fp);  // 즉시 파일에 기록
}