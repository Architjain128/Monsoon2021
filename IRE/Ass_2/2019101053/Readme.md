# Introduction
+ This code will generate a wikipedia text in `Hindi` language for a `Cricketer` by using their `CricketArchive player ID`.
+ It consits three sections:
    + Personal Life (व्यक्तिगत जीवन)
    + Career (आजीविका)
    + Social Presence (सामाजिक उपस्थिति)
+ Info containss the following:
    + Player Name 
    + Image
    + Citizenship 
    + International 
    + Date of Birth 
    + Place of Birth 
    + Spouse Name
    + Occupation (other than cricket) 
    + Education 
    + Religion 
    + Member of Sports Team 
    + Other Names
    + Awards
    + Social Media Followers 
    + Height
    + Instagram Account 
    + Twitter Account
    + Language Spoken
+ Some examples are :
    | Player Name | Player Id |
    |-------------|------------|
    | MS Dhoni | 7561|
    | Virat Kholi |101095|
    | Anil Kumble| 1972|
# Code
+ `main.ipynb` : contains the main working code 
+ Replace `Player_id` with your player's `CricketArchive player ID` in the code
+ The content for wikipedia page will be generated from the code and will be stored in `output.txt`
+ Copy the content of `output.txt` and paste it to the sandbox page of your player's wikipedia page, publish it and **DONE**🥳 
# Link
https://en.wikipedia.org/wiki/User_talk:Architjain128/sandbox
https://en.wikipedia.org/wiki/User:Architjain128/sandbox
# Wikidata and SPARQL
## Wikidata
Wikidata is a free, collaborative, multilingual, secondary database, collecting structured data to build a world-wide web of structured data, which can be used to understand and interconnect various data sets, which provides a controlled, shared vocabulary for knowledge about entities, their properties, relations, and events, along with software tools to openly edit, review, and refine the data.
## SPARQL
SPARQL is the standard query language and protocol for Linked Open Data and RDF databases. It is very similar to SQL where we can retrieve and modify data in a relational database and by using SPARQL we can do same for NoSQL graph databases which are non-uniform data and stored in various formats and sources. 
# Approach
+ I have used CricketArchive Player Id of the player to find there node and then i have added different properties wrapped arround `OPTIONAL` operator to handle missing values for the properties and if a properties have mulpitple answer i have bunched then together which gives me a dictionary with properties as key and array of values as their dictionary value.
    ```
    SELECT ?item ?itemLabel ?img ?itemDescription ?GenderLabel ?CitizenLabel ?interTeamLabel ?dobLabel ?pbLabel ?spLabel ?ocLabel ?eduLabel ?resLabel ?relLabel ?teamsLabel ?gnLabel ?awLabel ?chLabel ?so ?he ?insta ?twit ?lanLabel
    WHERE
    {
        ?item wdt:P2698 Player_id .
        OPTIONAL{
            ?item wdt:P21 ?Gender .
        }
        OPTIONAL{
            ?item wdt:P18 ?img
        }
        OPTIONAL{
            ?item wdt:P27 ?Citizen .
        }
        OPTIONAL{
            ?item wdt:P1532 ?interTeam .
        }
        OPTIONAL{
            ?item wdt:P569 ?dob .
        }
        OPTIONAL{
            ?item wdt:P19 ?pb .
        }
        OPTIONAL{
            ?item wdt:P26 ?sp .
        }
        OPTIONAL{
            ?item wdt:P106 ?oc .
        }
        OPTIONAL{
            ?item wdt:P69 ?edu .
        }
        OPTIONAL{
            ?item wdt:P551 ?res .
        }
        OPTIONAL{
            ?item wdt:P54 ?teams .
        }
        OPTIONAL{
            ?item wdt:P166 ?aw .
        }
        OPTIONAL{
            ?item wdt:P735 ?gn . 
        }
        OPTIONAL{
            ?item wdt:P40 ?ch .
        }
        OPTIONAL{
            ?item wdt:P140 ?rel .
        }
        OPTIONAL{
            ?item wdt:P8687 ?so .
        }
        OPTIONAL{
            ?item wdt:P2048 ?he .
        }
        OPTIONAL{
            ?item wdt:P2003 ?insta .
        }
        OPTIONAL{
            ?item wdt:P2002 ?twit .
        }
        OPTIONAL{
            ?item wdt:P1412 ?lan .
        }
        SERVICE wikibase:label { bd:serviceParam wikibase:language "hi,en" }
    }
    ```
+ Then i have made a template in hindi language with blanks to be filled with collected values present in dictionary.
+ I have made functions to convert output text to Wikipedia format and saved it in `output.txt`.
+ Then just copied the content from `output.txt` and pasted it to my sandbox and published it.

