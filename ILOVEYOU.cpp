#include<stdio.h>
#include<conio.h>
#include<dos.h>
int main() 
{
    clescr();
    int i;
    textcolor(RED);
    textbackground(WHITE);
    for(i=1; i<120; i++)
    {
        cprintf("I LOVE YOU \3");
        daley(200);
        {
            getch();
        }
    }
}
