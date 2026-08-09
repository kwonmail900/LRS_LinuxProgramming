// msg_receiver.c (수신기)
#include <stdio.h>
#include <sys/msg.h>

#define MQKEY 51234

struct msgbuf {
  long mtype;
  char mtext[64];
};

int main() {
  int msqid = msgget(MQKEY, 0666);
  struct msgbuf mb;
  int n;

  while((n = msgrcv(msqid, &mb, sizeof(mb.mtext), 0, 0)) > 0){
    printf("[수신] %s\n", mb.mtext);
  }

  msgctl(msqid, IPC_RMID, NULL);
  return 0;
}
