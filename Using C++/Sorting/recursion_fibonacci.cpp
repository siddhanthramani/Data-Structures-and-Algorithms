#include<iostream>
#include<stdio.h>

using namespace std;


int main(){
    while(1){
        int fib(int n);
        int n;
        cout << "Enter the number whose fibonacci value has to be found : ";
        cin >> n;
        cout << fib(n);
        cout << "\n";
    }

}


int fib(int n){

    if(n == 0){
        return 0;
    }
    else if(n == 1){
        return 1;
    }
    else if(n > 1){
        cout << fib(n-1) + fib(n-2);
        cout << "\t";
        return fib(n-1)+fib(n-2);
    }
}
