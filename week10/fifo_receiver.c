// fifo_receiver.c (서버)
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define FIFO_PATH "/tmp/sensor_fifo"

int main() {
  unlink(FIFO_PATH);
  mkfifo(FIFO_PATH, 0666);
  int fd = open(FIFO_PATH, O_RDONLY);
  int val;
  while(read(fd, &val, sizeof(int))>0)
    printf("[수신] CDS: %d\n", val);
  close(fd);
  return 0;
}
