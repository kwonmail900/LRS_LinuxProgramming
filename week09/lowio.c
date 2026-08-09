#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>

int main() {
    int fd = open("output.txt", O_WRONLY|O_CREAT|O_TRUNC, 0644);
    if (fd < 0) { perror("open"); return 1; }
    
    char buf[256];
    int n = snprintf(buf, sizeof(buf), "Hello from PID %d\n", getpid());
    write(fd, buf, n);
    
    close(fd);
    return 0;
}