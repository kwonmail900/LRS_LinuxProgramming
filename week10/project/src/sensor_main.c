#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include "sensor.h"

#define FIFO_PATH "/tmp/sensor_fifo"

int main(int argc, char *argv[]) {
    int count = (argc > 1) ? atoi(argv[1]) : 30;
    sensor_init();
    
    int fd = open(FIFO_PATH, O_WRONLY);
    if (fd < 0) { perror("open FIFO"); return 1; }

    for (int i = 1; i <= count; i++) {
        SensorData data = sensor_read(i);
        write(fd, &data, sizeof(SensorData));
        sensor_print(&data);
        usleep(200000);
    }

    close(fd);
    return 0;
}
