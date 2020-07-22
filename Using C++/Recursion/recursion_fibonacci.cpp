//recursion is used when a function calls itself

#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;


int fib(int n){

    if( n==0 || n ==1)
        return 1;
    else
        return fib(n)*fib(n-1);
}
 //Declare the function fib.

int main(){

    int n;// Input number
    int fibo; // Factorial of input number.

    cout<<"Enter the number: ";
    cin>>n;


    cout<<"The factorial of ";
    cout<<n;
    cout<<" is ";
    cout<<fib(n);

}




