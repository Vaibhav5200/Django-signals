Question 1 
By default, Django signals execute in a synchronous manner. This simply means the instant the signal is sent, Django waits for every receiver that is connected to return from their execution before continuing with the rest of the code. The whole process, from the time the signal was sent until every receiver returned, happens in the same thread of execution.
