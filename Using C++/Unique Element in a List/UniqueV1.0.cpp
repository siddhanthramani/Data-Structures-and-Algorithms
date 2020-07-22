#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

char a[100] = {'a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v','a','b','v','c','a','c','s','i','b','v'};

char b[100]; //used to store the values of the unique chars.

int shift = 0; // used to index the unique char array(Array B)
int len = 100;

int main(){

    int breakflag = 0;
    //cout << "Enter any key to start : ";
    //cin >> something;

    for(int i = 0; i < len-1; i++){//the outer loop is used to get the first char of comparison
        for(int j = 1;j < len;j++){// inner loop is used to get the second char of comparison

            for(int k = 0;k < shift; k++){//the unique comp loop is used to check if the value in array A is present in array B
                if(a[j] == b[k]){
                    breakflag = 1;//used to continue from inner loop and NOT this loop
                }
            }
            if(breakflag == 1){
                breakflag = 0;
                continue;
                //we do this as we have to continue to next iteration in inner loop and not the unique comp loop
            }

            if(a[j] != a[i]){
                continue;// if the values are not equal, continue
            }
            else{// if values are not equal and they do not exist in the array B, we have to add it to array B
                b[shift] = a[i];
                shift++;
                break;
            }


        }
    }
    cout<<"The unique values are : \n" ;
    for(int i = 0; i < shift; i++){//to print the unique values out

        cout << b[i];
        cout<<"\n";
    }


}

