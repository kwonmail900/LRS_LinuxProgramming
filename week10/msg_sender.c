// msg_sender.c (센서)
#include <stdio.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MQKEY 51234

struct msgbuf {
  long mtype;
  char mtext[64];
};

int main() {
  int msqid = msgget(MQKEY, IPC_CREAT | 0666);
  srand(time(NULL));
  struct msgbuf mb;
  mb.mtype = 1;

  for(int i=0;i<10;i++){
    snprintf(mb.mtext, 64, "%d,%d", i+1, rand()%4096);
    msgsnd(msqid, &mb, strlen(mb.mtext)+1, 0);
  }
  return 0;
}
