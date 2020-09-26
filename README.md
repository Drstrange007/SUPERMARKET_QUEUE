# SUPERMARKET_QUEUE

  Run the following commands to run this project . 

      1. git clone  https://github.com/Drstrange007/SUPERMARKET_QUEUE.git . 

      2. cd SUPERMARKET_QUEUE

      3. cd market

      4. python manage.py makemigrations

      5. python manage.py migrate

      6. python manage.py runserver
      
 Use the following Curl to run the rest apis
 
  1. Update queue length api 
        curl --location --request PUT 'http://127.0.0.1:8000/store_queue/Walmart' \
        --header 'Content-Type: application/json' \
        --data-raw '
           {

        "length":12312
            }
         '
  2. Get queue length api 
        curl --location --request GET 'http://127.0.0.1:8000/store_queue/Walmart'
        
  3. Create queue against a store id 
        curl --location --request POST 'http://127.0.0.1:8000/store_queue/' \
        --header 'Content-Type: application/json' \
        --data-raw ' {
           "store_id": "asdaefaesd",
           "length": 1231121
          }
       '
       
  4. Get queue update history 
        curl --location --request GET 'http://127.0.0.1:8000/store_queue/history/Walmart'
         
