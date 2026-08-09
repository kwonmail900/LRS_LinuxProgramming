#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include "sensor.h"

void sensor_init(void) {
    srand(time(NULL));
}

SensorData sensor_read(int id) {
    SensorData data;
    data.id = id;
    strcpy(data.type, "CDS");
    data.raw_value = rand() % 4096;
    data.converted = (float)data.raw_value / 4095.0 * 1000.0;
    data.timestamp = time(NULL);
    return data;
}

void sensor_print(const SensorData *data) {
    printf("ID:%d Raw:%d Lux:%.1f\n", data->id, data->raw_value, data->converted);
}

void sensor_write_csv(FILE *fp, const SensorData *data) {
    fprintf(fp, "%d,%s,%d,%.1f,%ld\n", data->id, data->type, data->raw_value, data->converted, data->timestamp);
    fflush(fp);
}
