# Google-Video-Intelligence-Api
In this lab i will show you how to use Google Video Intelligence Api


## Python Script 

  This script will allow to generate a csv file containing a the name of the video,label (tag) and the segment
  To use this script : 
  ```bash
    - Provide the Name of your video (must be as the video you uploaded in google store bucket) .
    - The name of your bucket in google store .
    - The duration of the video .
    - The label name (tag) .
  ```
  
  ## CSV File
  
    The file have all the information needed about the video label,segments .
    
  ## NOTE :
  
    You must provide a video containing only the label you provided in the script .
    
 # STEPS TO USE GOOGLE VIDEO INTELLIGENCE API 
 
 ## Create a google bucket 
  
  In google cloud platform go to storage and create new bucket .
  
  ```bash
    - Choose regional.
    - us-central .
    - For the class use standard and apply .
  ```
  
 ## ACTIVATE GOOGLE VIDEO INTELLIGENCE API
 
  In the navigation menu,in the bottom you find video intelligence from the go enable your google video intelligence api .
  then create new Dataset name it and choose Video uml Classification .
  Now your data set is created .
  ```bash
    - From the import create new CSV file provided by TRAIN,TEST 
   
        TRAIN,gs://"name of your bucket"/"The csv file you just created with the script".
        TEST,gs://"name of your bucket"/"ANOTHER CSV FILE YOU WILL CREATE WITH THE SCRIPT WITH ANOTHER VIDEO".
    
    - From the video you can add new label or modify your labels segments .
    - Train your model (this could take several hours) .
    - When your model is ready you can test it .
        - Create new prediction csv file provided by the video you want to test .
        - Select the output path to see your prediction .
  ```
  
  ## ENJOY
