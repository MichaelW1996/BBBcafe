# BBB [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

  ## Contents
  -[Credits](#Credits)  
  -[Description](#Description)  
  -[Install](#Install)  
  -[Usage Info](#Usage)  
  -[Questions](#Questions)  
  -[Tests](#Tests)  
  -[License](#License)  

## <span id=Credits>Credits </span>

#### Containerisation & scripting
Michael https://github.com/MichaelW1996  

#### Underlying data pipeline:
Kaelen - https://github.com/kaelan-the-G  
Michael -  https://github.com/MichaelW1996  
Phoenix - https://github.com/PhoenixCaine  
Fruzsi - https://github.com/DebFruzsi



## <span id=Description> Description </span> 

  A Data pipeline to process sales data for a cafe business and produce useful business insights with visualisation, initially hosted on AWS this project now runs locally as a demonstration of skills developed over the duration of a Data engineering bootcamp, skills included in the production of this application include:

    > Data ingestion from CSV
    > Sensitive data removal
    > Data normalisation to 3nf using Python
    > Database design (this project uses PostgreSQL)
    > Unit Testing
    > Containerisation using Docker
    > Visualisations using Grafana - Utilises SQL queries
    > Shell Scripting to deploy/dismantle application
    > Version Control using Git/Github
    > Project management skills including meetings with a faux client
    > Implementation of Agile working methodology with rotating scrum master
    
#### Deprecated Features

    > AWS EC2 instance for visualisation & monitoring hosting
    > AWS Lambda for ETL pipeline
    > AWS S3 Bucket & Redshift for data storage and databasing
    > AWS Cloudformation & Github Actions for CI/CD


  ## Product initiation document
  https://docs.google.com/document/d/1FSQwxu9fgONe1-Cq1r67GGJAH0eON9phLxYBTDiPlAs/edit?usp=sharing

  ## Group board
  https://miro.com/app/board/uXjVK5mj_K8=/

  ## <span id=Install> Install </span>

  > ! Linux users !  
  > Run the StartDB.sh file
  
  > ! Windows users !  
  >Ensure WSL is installed/set up  
  >Run the StartDBWindows.sh file 

  When prompted if the user would like to install packages, type "y".  
  This installs docker, unzip & python packages : dotenv, psycopg2 (for postgreSQL),   
  If user already has these packages feel free to decline packages by typing "n".

  Once packages install the program will start

  ## <span id=Usage> Usage </span>
  > ! Linux users !  
  > Run the StartDB.sh file
  
  > ! Windows users !  
  >Ensure WSL is installed/set up  
  >Run the StartDBWindows.sh file 

  Wait for program to finish processing all records then click on the provided link to grafana & use the login details given in the terminal

  Pressing enter on the terminal will stop and clean up the containers - each time the user launches the app it will process all data again & rebuild dashboards - changes made will not be saved

  ## <span id=Questions> Questions </span>
  For issues or feature requests: https://github.com/MichaelW1996/BBBcafe  
  For other questions, please email me: 
  contact@michaeljohnwalters.co.uk

  ## <span id=Tests> Tests </span>
  Tests may be found in the Tests subfolder, these tests are in development & are still evolving

  ## <span id=License> License </span>
  MIT  
  https://opensource.org/licenses/MIT  
  Copyright BBBgroup
      Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  
      
      The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
      
      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
