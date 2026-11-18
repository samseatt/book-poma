/* Reproducible illustration, not an empirical model of wealth.
   cc -O3 exchange_simulation.c -o /tmp/poma-exchange
   /tmp/poma-exchange > exchange-simulation.json
   A participation is one trader taking part in a pair exchange.
   Fixed stake: cancel a transfer if its donor has less than one unit.
   Yard-sale stake: 10% of the poorer participant's wealth, fair direction.
   Generator: xorshift64*; rejection sampling avoids modulo bias. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define N 10000
static uint64_t state=17112026;
static uint64_t rng(void){state^=state>>12;state^=state<<25;state^=state>>27;return state*UINT64_C(2685821657736338717);}
static unsigned idx(unsigned n){uint64_t x,t=(-((uint64_t)n))%n;do{x=rng();}while(x<t);return x%n;}
static int cmp(const void*a,const void*b){double x=*(const double*)a,y=*(const double*)b;return (x>y)-(x<y);}
static double top(double*w,int count){double a[N],v=0;for(int i=0;i<N;i++)a[i]=w[i];qsort(a,N,sizeof(double),cmp);for(int i=N-count;i<N;i++)v+=a[i];return v/1000000.;}
int main(void){double w[N],total;unsigned hist[26]={0};for(int i=0;i<N;i++)w[i]=100;
  for(uint64_t t=0;t<UINT64_C(750000000);t++){unsigned a=idx(N),b=idx(N-1);if(b>=a)b++;if(w[a]>=1){w[a]--;w[b]++;}}
  unsigned below=0;total=0;for(int i=0;i<N;i++){total+=w[i];below+=w[i]<100;unsigned b=(unsigned)(w[i]/20);hist[b<25?b:25]++;}
  printf("{\"seed\":17112026,\"traders\":10000,\"initial\":100,\"fixed\":{\"pair_exchanges\":750000000,\"participations_per_person\":150000,\"total\":%.10f,\"below_mean\":%.6f,\"top_tenth_share\":%.6f,\"histogram_counts\":[",total,below/(double)N,top(w,1000));
  for(int i=0;i<26;i++)printf("%s%u",i?",":"",hist[i]);printf("]},\"yard_sale\":{\"stake_fraction\":0.1,\"series\":[");
  state=17112027;for(int i=0;i<N;i++)w[i]=100;
  for(int s=0;s<=60;s++){
    if(s)for(int t=0;t<500000;t++){unsigned a=idx(N),b=idx(N-1);if(b>=a)b++;double v=.1*(w[a]<w[b]?w[a]:w[b]);w[a]-=v;w[b]+=v;}
    printf("%s[%d,%.9f]",s?",":"",s*100,top(w,100));
  }
  total=0;double minimum=w[0];for(int i=0;i<N;i++){total+=w[i];if(w[i]<minimum)minimum=w[i];}
  printf("],\"pair_exchanges\":30000000,\"participations_per_person\":6000,\"total\":%.10f,\"minimum\":%.12g}}\n",total,minimum);
  return 0;
}
