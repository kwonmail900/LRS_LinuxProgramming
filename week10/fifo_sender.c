// fifo_sender.c (센서)
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

#define FIFO_PATH "/tmp/sensor_fifo"

int main() {
  srand(time(NULL));
  int fd = open(FIFO_PATH, O_WRONLY);
  for (int i = 0; i < 20; i++) {
    int val = rand() % 4096;
    write(fd, &val, sizeof(int));
    usleep(200000);
  }
  close(fd);
  return 0;
}
