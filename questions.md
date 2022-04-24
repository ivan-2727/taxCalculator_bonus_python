1) It's quite tedious to check the correctness of calculations manually, I've done my best but still not sure that there is no bug :) 

2) Why do we need the Vehicle class, why don't use them as strings direcly? - (maybe for future additional properties, but it's not necessary for the particular task)

3) Maybe at some point it is better to implement faster algorithms to compare data with the tax rules (like binary search to find the time zone?), but for now the rate-limiting step is fetching from server. 