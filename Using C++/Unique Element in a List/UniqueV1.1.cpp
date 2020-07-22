#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

char a[100] = {'a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v'};

int len = 100; //length of array A

int main(){

    for(int i = 0; i < (len-1); i++){//the outer loop is used to get the first char of comparison

        for(int j = i+1 ;j < len; j++){// inner loop is used to get the second char of comparison

            if(a[j] != a[i]){
                continue;// if the values are not equal, continue
            }
            else{// if values are not equal and they do not exist in the array B, we have to add it to array B
                for(int d = j; d < (len-1) ; d++){// to delete repeated values from array A so that prog gets faster                        a[d] = a[d+1];
                    a[d] = a[d+1];
                }
                --len;
            }
        }
    }
    cout<<"The unique values are : \n" ;
    for(int i = 0; i < len; i++){//to print the unique values out
        cout << a[i];
        cout<<"\n";
    }


}

