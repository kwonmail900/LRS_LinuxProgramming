#ifndef SENSOR_H
#define SENSOR_H
#include <time.h>

// 센서 데이터 구조체
typedef struct {
    int id;               // 측정 ID (1부터 증가)
    char type[16];        // 센서 타입 ("CDS", "TEMP")
    int raw_value;        // ADC 원시 값 (0~4095)
    float converted;      // 변환 값 (조도 lux, 온도 ℃)
    time_t timestamp;     // 측정 시간
} SensorData;

// 함수 프로토타입
void sensor_init(void);                     // 센서 초기화
SensorData sensor_read(int id);              // 센서 값 읽기
void sensor_print(const SensorData *data);   // 화면 출력
void sensor_write_csv(FILE *fp, const SensorData *data); // CSV 출력
#endif // SENSOR_H