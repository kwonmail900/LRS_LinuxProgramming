#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include "sensor.h"

#define FIFO_PATH "/tmp/sensor_fifo"

int main() {
    unlink(FIFO_PATH);
    mkfifo(FIFO_PATH, 0666);
    int fd = open(FIFO_PATH, O_RDONLY);
    FILE *csv = fopen("data/sensor_data.csv", "w");
    fprintf(csv, "id,type,raw_value,lux,timestamp\n");

    SensorData data;
    while (read(fd, &data, sizeof(SensorData)) > 0) {
        sensor_print(&data);
        sensor_write_csv(csv, &data);
    }

    fclose(csv);
    close(fd);
    return 0;
}
