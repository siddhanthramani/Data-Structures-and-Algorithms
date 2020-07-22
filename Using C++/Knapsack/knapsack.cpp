#include<iostream>
#include<stdio.h>

using namespace std;

int profit[10] = {7, 9, 5, 45,6, 7, 34, 54, 45, 80};//weights of items
int weight[10] = {10,20,30,40,20,30,40, 40,  5, 5};//profits of items
int cap = 100;//the maximum weight allowed in the bag
int p_max = 0;
int p_index = 0;
int p_gain = 0, w_gain = 0;


int main(){

    //using max profit method
    cout << "Using max profit criteria : \n";
    while(1){
        for(int i=0; i<10; i++){//loop to find the maximum value and its index
            if(p_max < profit[i]){
                p_max = profit[i];
                p_index = i;
            }
        }
        w_gain = w_gain + weight[p_index];
        if(w_gain <= cap){//to ensure that the w_gain is not more than cap
            //using here and not in outer while loop as outer loop will execute one more time than needed
            p_gain = p_gain + profit[p_index];
            profit[p_index] = -1; //to ensure that we do not use the same maximum value again
            p_max = 0;//to ensure that we find the next max value
        }
        else{
            w_gain = w_gain - weight[p_index];
            break;
        }
        //displaying outputs
        cout << "The index : ";
        cout << p_index;
        cout << "\tThe total profit : ";
        cout << p_gain;
        cout << "\tThe weight left : ";
        cout << cap - w_gain;
        cout << "\n";
    }

    cout << "Using least weight criteria : \n";

    int profit[10] = {7, 9, 5, 45,6, 7, 34, 54, 45, 80};//weights of items
    int weight[10] = {10,20,30,40,20,30,40, 40,  5, 5};//profits of items
    int cap = 100;//the maximum weight allowed in the bag
    int w_min = 0;
    int w_index = 0;
    int p_gain = 0, w_gain = 0;


    while(1){
        for(int i=0; i<10; i++){
            if(w_min > weight[i]){
                w_min = weight[i];
                w_index = i;
            }

        w_gain = w_gain + weight[w_index];
        if(w_gain <= cap){//to ensure that the w_gain is not more than cap
            //using here and not in outer while loop as outer loop will execute one more time than needed
            p_gain = p_gain + profit[w_index];
            weight[w_index] = 10000; //to ensure that we do not use the same maximum value again
            w_min = 1000;//to ensure that we find the next max value
        }
        else{
            w_gain = w_gain - weight[p_index];
            break;
        }
        //displaying outputs
        cout << "The index : ";
        cout << p_index;
        cout << "\tThe total profit : ";
        cout << p_gain;
        cout << "\tThe weight left : ";
        cout << cap - w_gain;
        cout << "\n";

        }
    }

    return 0;
}
