#ifndef SENSOR_H
#define SENSOR_H
#include <time.h>
#include <stdio.h>

typedef struct {
    int id;
    char type[16];
    int raw_value;
    float converted;
    time_t timestamp;
} SensorData;

void sensor_init(void);
SensorData sensor_read(int id);
void sensor_print(const SensorData *data);
void sensor_write_csv(FILE *fp, const SensorData *data);

#endif
