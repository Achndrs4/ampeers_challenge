# Python Backend Challenge

Develop the solution yourself. Please note that it is not allowed to post the challenge itself nor the solution on the Internet.

This is a completely made-up challenge designed to find the right person for the right job.

Focus on solving the problem quickly while keeping the code well-structured. Do not optimize for program execution speed.

----------

## Task 1: Vanilla Python (WarmUp)

  * Implement a function which takes a arbitary nested Dict-Object and do the following transformations:
    * add +1 to each Number: `x: 9 ->  x: 10`
    * add 'AE' to each String: `y: 'abc' -> y: 'abc AE'`
    * the object should keep its structure!
    * See a rough example structure below:

    ```js
    // initial dict
    {
      "a": 123,
      "b": "abc"
      "c": [1, 2, 3],
      "d": {
        "e": [4, 5, 6]
      }
    }

    // resulting dict
    {
      "a": 124,
      "b": 'abc AE'
      "c": [2, 3, 4],
      "d": {
        "e": [5, 6, 7]
      }
    }
    ```

Evaluation Criteria:

- Functionality & Correctness
- Traceability of Code

----------

## Heat Loss Analysis

Imagine Ampeers Energy needs to calculate transmission heat loss of every building of every customer and communicate this information to the customers via e-mail.

Transmission heat loss power $P$ is the amount of heat lost through the outer building wall. It is influenced by the insulation standard of the building and is an important metric for estimating how much thermal power is required to keep the building warm.

## 2. Transmission heating loss

To calculate the transmission heat loss we can use the following formula:

$$ P = U \cdot A \cdot \Delta T,$$

where $U$ is the heat transfer coefficient of the outer wall, $A$ is the surface area of the outer wall and $\Delta T$ is the difference between the outside air temperature and room temperature.

Let's assume for simplicity that the buildings in the dataset have no heat loss through the roof and floor and that all buildings are square. Moreover we assume that the room temperature is always 20 °C.

Please calculate for all buildings in the file `building-data-january.csv` the transmission heat loss $P$ for the outside air temperatures of 10 °C, 0 °C and -10 °C and save the results in `results/transmission-heating-loss-results.csv`

Don't forget to write meaningful Python tests for this task. 

Evaluation Criteria:

- Functionality & Correctness
- Traceability of Code
- Quality of Tests

## 3. Text Files

If you could not solve task 2 use the $U$-value instead of the $P$-value for this task. 

We receive the CSV file monthly from our major customer My Real Estate GmbH. Often new property managers get added. We have a local cache to store the calculated transmission heating losses $P$ for each building for each real estate manager. Set up a local JSON file for this. 

For My Real Estate GmbH we want to provide a set of text files with the calculated results per property manager (see `example-text.txt`). These files can be used by My Real Estate Gmbh to inform the property managers about the transmission heating loss $P$ of their buildings. My Real Estate Gmbh would like to receive only the text files for new property managers. 
To be not dependent on correctly storing the csv files each month, create the text files based on our local JSON file.

Create the text files for the text-files for the first three months from the data source
- building-data-january.csv
- building-data-february.csv
- building-data-march.csv

Bear in mind that the code should also work for the following months from when we don't have the data yet.  


Don't forget to write meaningful Python tests for this task. 

Evaluation Criteria:
- Functionality & Correctness
- Traceability of Code
- Quality of Tests
- Clean Architecture

--------

## Some general Hints: 

Reading the csv-file with pandas: 
```Python
import pandas as pd 

filepath = "data/building-data-january.csv"
df = pd.read_csv(filepath, delimiter=";")
```



Reading and writing json data: 
```Python
import json 

data = {"Street": "Bahnhofsstraße"}
json_string = json.dumps(data)

with open('json_data.json', 'w') as outfile:
    json.dump(json_string, outfile, indent=4)

with open('json_data.json', "r") as json_file:
    data = json.load(json_file)
   ```