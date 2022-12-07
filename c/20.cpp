#include <stdio.h>
#include <malloc.h>
#include <unistd.h>
// #i

int main() {
    printf("閹劌銈絓n");
  printf("娴ｈ法鏁at /proc/%d/maps閺屻儳婀呴崘鍛摠閸掑棝鍘n",getpid());
  
  //閻㈠疇顕?鐎涙濡惃鍕敶鐎?
  void *addr = malloc(1);
  printf("濮?鐎涙濡惃鍕敶鐎涙鎹ｆ慨瀣勾閸р偓:%x\n", addr);
  printf("娴ｈ法鏁at /proc/%d/maps閺屻儳婀呴崘鍛摠閸掑棝鍘n",getpid());
 
  //鐏忓棛鈻兼惔蹇涙▎婵夌儑绱濊ぐ鎾圭翻閸忋儰鎹㈤幇蹇撶摟缁楋附妞傞幍宥呯窔娑撳澧界悰?
  getchar();

  //闁插﹥鏂侀崘鍛摠
  free(addr);
  printf("闁插﹥鏂佹禍?鐎涙濡惃鍕敶鐎?娴ｅ攧eap閸棗鑻熸稉宥勭窗闁插﹥鏂乗n");
  
  getchar();
  return 0;
}