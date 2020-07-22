#include<iostream>
#include<stdio.h>

using namespace std;


int main(){

    int fact(int n);
    int n;
    cout << "Enter the number whose factorial has to be found : ";
    cin >> n;
    cout << fact(n);
}


int fact(int n){
    if(n == 0 || n == 1){
        return 1;
    }
    else if(n > 1){
        return n * fact(n-1);
    }
}
